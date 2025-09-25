import customtkinter as ctk
import tkinter.messagebox as tkmb
import sqlite3
from datetime import datetime

# --- Model ---
class ComplaintDB:
    def __init__(self, dbname="complaints.db"):
        self.conn = sqlite3.connect(dbname)
        self.init_db()
    def init_db(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS complaints (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        gender TEXT NOT NULL,
                        comment TEXT NOT NULL,
                        submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()
    def add_complaint(self, name, gender, comment):
        c = self.conn.cursor()
        c.execute("INSERT INTO complaints (name, gender, comment) VALUES (?, ?, ?)", (name, gender, comment))
        self.conn.commit()
        return c.lastrowid
    def list_complaints(self, search=None):
        c = self.conn.cursor()
        query = "SELECT id, name, gender, comment, submitted FROM complaints"
        if search:
            query += " WHERE name LIKE ? OR comment LIKE ?"
            c.execute(query, (f'%{search}%', f'%{search}%'))
        else:
            c.execute(query)
        return c.fetchall()
    def delete_complaint(self, cid):
        c = self.conn.cursor()
        c.execute("DELETE FROM complaints WHERE id = ?", (cid,))
        self.conn.commit()

# --- Controller ---
class ComplaintController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)
    def save_complaint(self, name, gender, comment):
        if not name.strip():
            tkmb.showerror("Validation Error", "Name cannot be empty.")
            return False
        if not name.replace(" ", "").isalpha():
            tkmb.showerror("Validation Error", "Name must contain only letters and spaces.")
            return False
        if gender not in ("Male", "Female", "Other"):
            tkmb.showerror("Validation Error", "Choose a valid gender.")
            return False
        if len(comment.strip()) < 10:
            tkmb.showerror("Validation Error", "Comment must be at least 10 characters.")
            return False
        self.model.add_complaint(name, gender, comment.strip())
        tkmb.showinfo("Success", "Complaint submitted successfully!")
        self.view.clear_form()
    def get_complaints(self, search=None):
        rows = self.model.list_complaints(search)
        self.view.populate_list(rows)
    def delete_complaint(self, cid):
        self.model.delete_complaint(cid)
        self.get_complaints()

# --- View ---
class ComplaintView(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.geometry("700x500")
        self.title("Complaint Management (Modern | 2025)")

        # --- Form Frame
        form = ctk.CTkFrame(self)
        form.pack(padx=30, pady=15, fill="x")

        self.entry_name = ctk.CTkEntry(form, placeholder_text="Full Name")
        self.entry_name.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        ctk.CTkLabel(form, text="Full Name:").grid(row=0, column=0, padx=10, pady=10)

        ctk.CTkLabel(form, text="Gender:").grid(row=1, column=0, padx=10, pady=10)
        self.gender_var = ctk.StringVar(value="Male")
        self.r_male = ctk.CTkRadioButton(form, text="Male", variable=self.gender_var, value="Male")
        self.r_female = ctk.CTkRadioButton(form, text="Female", variable=self.gender_var, value="Female")
        self.r_other = ctk.CTkRadioButton(form, text="Other", variable=self.gender_var, value="Other")
        self.r_male.grid(row=1, column=1)
        self.r_female.grid(row=1, column=2)
        self.r_other.grid(row=1, column=3)

        ctk.CTkLabel(form, text="Comment:").grid(row=2, column=0, padx=10, pady=10)
        self.comment_box = ctk.CTkTextbox(form, width=400, height=60)
        self.comment_box.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        self.btn_submit = ctk.CTkButton(form, text="Submit Complaint", command=self._submit)
        self.btn_submit.grid(row=3, column=2, pady=10)
        self.btn_clear = ctk.CTkButton(form, text="Clear", command=self.clear_form)
        self.btn_clear.grid(row=3, column=1, pady=10)
        self.btn_about = ctk.CTkButton(form, text="About", command=self._about)
        self.btn_about.grid(row=3, column=3, pady=10)

        # --- Complaint List Frame
        list_frame = ctk.CTkFrame(self)
        list_frame.pack(padx=30, pady=10, fill="both", expand=True)

        self.search_var = ctk.StringVar()
        self.entry_search = ctk.CTkEntry(list_frame, placeholder_text="Search complaints...", textvariable=self.search_var)
        self.entry_search.grid(row=0, column=1, padx=10, pady=8)
        self.btn_search = ctk.CTkButton(list_frame, text="Search", command=self._search)
        self.btn_search.grid(row=0, column=2, padx=5)
        self.btn_refresh = ctk.CTkButton(list_frame, text="Refresh", command=self._refresh)
        self.btn_refresh.grid(row=0, column=3, padx=5)

        self.complaint_list = ctk.CTkScrollableFrame(list_frame)
        self.complaint_list.grid(row=1, column=0, columnspan=4, sticky="nsew")
        list_frame.rowconfigure(1, weight=1)
        list_frame.columnconfigure(0, weight=1)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
        self._refresh()

    def clear_form(self):
        self.entry_name.delete(0, ctk.END)
        self.gender_var.set("Male")
        self.comment_box.delete("0.0", ctk.END)

    def _submit(self):
        name = self.entry_name.get()
        gender = self.gender_var.get()
        comment = self.comment_box.get("0.0", ctk.END).strip()
        if self.controller:
            self.controller.save_complaint(name, gender, comment)
            self._refresh()

    def _refresh(self):
        if self.controller:
            self.controller.get_complaints()

    def _search(self):
        if self.controller:
            search = self.search_var.get()
            self.controller.get_complaints(search)

    def populate_list(self, rows):
        # Clear previous widgets
        for w in self.complaint_list.winfo_children():
            w.destroy()
        # Header
        ctk.CTkLabel(self.complaint_list, text="ID", width=40, anchor="w", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=5)
        ctk.CTkLabel(self.complaint_list, text="Name", width=90, anchor="w", font=("Helvetica", 12, "bold")).grid(row=0, column=1)
        ctk.CTkLabel(self.complaint_list, text="Gender", width=70, anchor="w", font=("Helvetica", 12, "bold")).grid(row=0, column=2)
        ctk.CTkLabel(self.complaint_list, text="Comment", width=260, anchor="w", font=("Helvetica", 12, "bold")).grid(row=0, column=3)
        ctk.CTkLabel(self.complaint_list, text="Date", width=120, anchor="w", font=("Helvetica", 12, "bold")).grid(row=0, column=4)
        ctk.CTkLabel(self.complaint_list, text="Delete", width=70, anchor="center", font=("Helvetica", 12, "bold")).grid(row=0, column=5)
        for idx, (cid, name, gender, comment, dt) in enumerate(rows, start=1):
            ctk.CTkLabel(self.complaint_list, text=str(cid), width=40, anchor="w").grid(row=idx, column=0, padx=5)
            ctk.CTkLabel(self.complaint_list, text=name, width=90, anchor="w").grid(row=idx, column=1)
            ctk.CTkLabel(self.complaint_list, text=gender, width=70, anchor="w").grid(row=idx, column=2)
            ctk.CTkLabel(self.complaint_list, text=comment, width=260, anchor="w").grid(row=idx, column=3)
            ctk.CTkLabel(self.complaint_list, text=dt[:16], width=120, anchor="w").grid(row=idx, column=4)
            btn = ctk.CTkButton(self.complaint_list, text="Delete", fg_color="red", command=lambda cid=cid: self._delete(cid))
            btn.grid(row=idx, column=5, padx=5)
    def _delete(self, cid):
        if tkmb.askyesno("Delete", "Delete this complaint?"):
            self.controller.delete_complaint(cid)
            self._refresh()

    def _about(self):
        tkmb.showinfo("About", "Modern Complaint Management System\nPowered by CustomTkinter\n2025 Edition\nby Sushant Singh Rathore")

# --- Run Application ---
if __name__ == "__main__":
    model = ComplaintDB()
    view = ComplaintView()
    controller = ComplaintController(model, view)
    view.mainloop()
