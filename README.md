# Lost & Found Desk App

A modern Lost & Found management system built with Python Tkinter. This application provides an intuitive interface for managing lost and found items with advanced search functionality, dark/light mode support, and a clean tabular display.

## Features

### User Interface

- **Dark/Light Mode Toggle**: Switch between dark and light themes for better user experience
- **Modern Dashboard**: Clean, professional interface with customizable color schemes
- **Responsive Design**: Modern GUI that adapts to different themes
- **User-friendly Forms**: Simple forms for reporting items with clear instructions

### Admin Interface

- **Tabbed Interface**: Clean, organized admin panel with multiple tabs
- **Item Management**: Report lost and found items with detailed information
- **User Management**: Admin authentication and user management system
- **Dark Mode Support**: Toggle between light and dark themes in admin panel

### Search and Navigation

- **Advanced Search**: Detailed search functionality with multiple criteria (item type, category, keywords)
- **Quick Search**: Fast search from main interface
- **Modal Windows**: Professional popup windows for forms and searches
- **Intuitive Navigation**: Easy-to-use interface with clear button layouts

### Database Features

- **SQLite3 Database**: Lightweight and efficient database for storing item data (planned feature)
- **Data Validation**: Form validation and error handling
- **Modal Forms**: Professional form interfaces for data entry

### Application Components

1. **Login System** (`login.py`):
   - User authentication interface
   - Animated text effects
   - Registration functionality
   - Admin panel access

2. **User Interface** (`user_page_prototype.py`):
   - Report lost/found items
   - Advanced search functionality
   - Dark/light mode toggle
   - Clean table display

3. **Admin Panel** (`admin_control_panel.py`):
   - Administrative controls
   - Item management
   - User management
   - Dark mode support

### User Experience

- **Theme Switching**: Dark and light mode support across all interfaces
- **Color-coded Buttons**:
  - Red for "Report Lost Item"
  - Green for "Report Found Item"
  - Blue for "Search Items"
- **Animated Effects**: Text animations and visual feedback
- **Modal Dialogs**: Professional popup windows for forms
- **Form Validation**: Input validation with error messages

### Getting Started

**Prerequisites:**

- Python 3.x
- Tkinter (usually included with Python)

**Running the Application:**

1. Navigate to the project directory
2. Run the main login interface:

   ```bash
   python login.py
   ```

3. Or run the user interface directly:

   ```bash
   python user_page_prototype.py
   ```

4. Or access the admin panel:

   ```bash
   python admin_control_panel.py
   ```

### Application Flow

1. **Start with Login** (`login.py`) - Main entry point with authentication
2. **User Interface** - Report items, search, and manage findings
3. **Admin Panel** - Administrative controls and user management

---
