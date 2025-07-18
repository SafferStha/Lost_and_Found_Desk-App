# Lost & Found Desk App

A modern Lost & Found management system built with Python Tkinter and SQLite3. This application provides an intuitive interface for managing lost and found items with search functionality and a clean tabular display. It is designed for use by administrators and instructors to efficiently report and search for lost and found items.

## Features

### Admin Interface

- **Modern Dashboard**: Clean, professional interface with blue color scheme
- **Item Management**: Report lost and found items with detailed information
- **Search Functionality**: Search items by name, category, or location
- **Table View**: Comprehensive table displaying all items with sortable columns
- **Real-time Updates**: Automatically refresh table when new items are added

### Database Features

- **SQLite3 Database**: Lightweight and efficient database for storing item data
- **Reliable Storage**: SQLite3 database for reliable data storage
- **Separate Tables**: Distinct tables for lost and found items to maintain organization
- **User Management**: User management system with admin authentication
- **Data Integrity**: Ensures data integrity with proper validation and error handling

### User Experience

- **Responsive Design**: Modern GUI that matches professional standards
- **Color-coded Buttons**:
  - Red for "Reporting Lost Item"
  - Green for "Reporting Found Item"
  - Blue for "Searching Items"
- **Easy Navigation**: Intuitive button layout and search controls
- **Data Validation**: Error handling for database operations
- **User-friendly Forms**: Simple forms for reporting items with clear instructions

### Default Credentials

- **User Name**: admin
- **Password**: admin123

### Application Interface

The admin interface includes:

1. **Header**: "Lost & Found Desk - Welcome Admin"
2. **Action Buttons**:
   - Reporting Lost Item (Red)
   - Reporting Found Item (Green)
   - Searching Items (Blue)
3. **Search Bar**: With "Search" and "Show All" buttons
4. **Data Table**: Displays all items with columns:
   - ID
   - Item Name
   - Category
   - Type (Lost/Found)
   - Date
   - Location
   - Status

### Adding Items

1. Click "Report Lost Item" or "Report Found Item"
2. Fill in the form with:
   - Item Name
   - Item Category
   - Date (Lost/Found)
   - Location (Lost/Found)
   - Description
3. Click "Submit" to add the item

### Searching Items

1. Enter search terms in the search box
2. Click "Search" to filter results
3. Click "Show All" to display all items

## Requirements

- Python 3
- Tkinter
- SQLite3

### Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Lost-and-Found_desk_App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Lost-and-Found_desk_App
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Access the application through the provided GUI.
5. Use the default credentials to log in:
   - Username: `admin`
   - Password: `admin123`
6. Explore the features as an Admin or Instructor.

---
