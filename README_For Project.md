# Modern Complaint Management System 🎯

**A sophisticated Python GUI application built with CustomTkinter, featuring modern design, MVC architecture, and robust data management.**

---

## 📋 Overview

This is a completely modernized complaint management system that replaces traditional Tkinter with CustomTkinter for a sleek, professional interface. Built following industry best practices with MVC architecture, input validation, and integrated SQLite database management.

## ✨ Features

### 🎨 Modern User Interface
- **CustomTkinter Integration**: Beautiful, responsive UI that works seamlessly across platforms
- **Dark/Light/System Theme Support**: Automatic theme detection with user preference options
- **Professional Layout**: Clean, intuitive design with proper spacing and typography
- **Responsive Design**: Adapts to different screen sizes and resolutions

### 🔧 Advanced Functionality
- **Real-time Input Validation**: Comprehensive validation for names, gender selection, and comment length
- **Integrated Search & Filter**: Find complaints quickly with text-based search functionality
- **CRUD Operations**: Create, Read, Update, and Delete complaints with ease
- **Data Export Ready**: Structured data format ready for future export features

### 🏗️ Technical Excellence
- **MVC Architecture**: Clean separation of Model, View, and Controller for maintainability
- **SQLite Integration**: Built-in database with automatic table creation and management
- **Error Handling**: Robust error handling with user-friendly messages
- **Memory Efficient**: Optimized database connections and resource management

### 🚀 User Experience
- **Instant Feedback**: Real-time validation messages and success notifications
- **Bulk Operations**: Refresh and delete multiple records efficiently
- **About Dialog**: Built-in information and help system
- **Clear Form Function**: Quick reset for new complaint entries

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Install Dependencies
```bash
pip install customtkinter
```

### Step 2: Download and Run
1. Download the `complaint_management.py` file
2. Run the application:
```bash
python complaint_management.py
```

### Alternative Installation Methods

#### Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv complaint_app
source complaint_app/bin/activate  # On Windows: complaint_app\Scripts\activate

# Install dependencies
pip install customtkinter

# Run application
python complaint_management.py
```

#### For Development
```bash
git clone [repository-url]
cd complaint-management-system
pip install -r requirements.txt  # If requirements.txt is available
python complaint_management.py
```

## 🚀 Quick Start

1. **Launch the Application**
   ```bash
   python complaint_management.py
   ```

2. **Submit a Complaint**
   - Enter your full name
   - Select gender (Male/Female/Other)
   - Write your complaint (minimum 10 characters)
   - Click "Submit Complaint"

3. **Manage Complaints**
   - View all complaints in the scrollable list
   - Use the search box to filter complaints
   - Click "Delete" to remove specific complaints
   - Use "Refresh" to update the list

## 📁 Project Structure

```
complaint-management-system/
│
├── complaint_management.py    # Main application file
├── complaints.db             # SQLite database (auto-created)
├── README.md                 # This file
└── requirements.txt          # Dependencies (optional)
```

## 🔧 Technical Details

### Architecture Pattern
- **Model**: `ComplaintDB` class handles all database operations
- **View**: `ComplaintView` class manages the user interface
- **Controller**: `ComplaintController` class coordinates between Model and View

### Database Schema
```sql
CREATE TABLE complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    gender TEXT NOT NULL,
    comment TEXT NOT NULL,
    submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Key Components
- **Input Validation**: Ensures data integrity and user experience
- **Search Functionality**: Real-time filtering of complaint records
- **Theme Support**: Automatic system theme detection
- **Error Handling**: Comprehensive error messages and recovery

## 🎯 Usage Examples

### Basic Complaint Submission
1. Open the application
2. Fill in the required fields
3. Click "Submit Complaint"
4. Receive confirmation message

### Searching Complaints
1. Use the search box in the complaints list section
2. Enter keywords from name or comment
3. Click "Search" to filter results
4. Click "Refresh" to show all complaints

### Managing Records
1. View all complaints in the scrollable list
2. Click "Delete" next to any complaint to remove it
3. Confirm deletion in the popup dialog
4. List automatically refreshes

## 🔍 Features in Detail

### Input Validation Rules
- **Name**: Must contain only letters and spaces, cannot be empty
- **Gender**: Must select one of the three available options
- **Comment**: Minimum 10 characters required

### Search Capabilities
- Search by complainant name
- Search by comment content
- Case-insensitive matching
- Partial word matching

### Data Management
- Automatic database creation on first run
- Persistent data storage
- Safe deletion with confirmation
- Timestamp tracking for all complaints

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'customtkinter'`
**Solution**: 
```bash
pip install customtkinter
```

**Issue**: Application doesn't start
**Solution**: 
- Ensure Python 3.8+ is installed
- Try running with: `python3 complaint_management.py`

**Issue**: Database permission errors
**Solution**: 
- Ensure write permissions in the application directory
- Run application with appropriate user privileges

### Getting Help
- Check the "About" dialog in the application
- Verify all dependencies are installed correctly
- Ensure Python version compatibility

## 🚧 Future Enhancements

- [ ] Data export functionality (CSV, PDF)
- [ ] User authentication system
- [ ] Advanced reporting and analytics
- [ ] Email notification system
- [ ] Backup and restore functionality
- [ ] Multi-language support
- [ ] Mobile-responsive web version

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex functionality
- Include docstrings for all methods
- Test thoroughly before submitting

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Sushant Singh Rathore**

- 🌟 Passionate Python Developer
- 🎯 Specialist in Modern GUI Applications
- 🚀 Advocate for Clean Code and Best Practices

---

## 🙏 Acknowledgments

- CustomTkinter team for the amazing modern UI framework
- Python community for continuous support and inspiration
- SQLite for providing a robust, lightweight database solution

## 📊 Project Stats

- **Language**: Python 3.8+
- **GUI Framework**: CustomTkinter
- **Database**: SQLite3
- **Architecture**: MVC Pattern
- **License**: MIT
- **Version**: 1.0.0 (2025 Edition)

---

**⭐ If you find this project helpful, please consider giving it a star!**

*Built with ❤️ by Sushant Singh Rathore - Modern Python GUI Development*