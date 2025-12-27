# Student Management System

A comprehensive console-based student management system built in Java with full CRUD operations, file persistence, and input validation.

## Features

- **Add Student**: Add new students with name, ID, age, and grade
- **View All Students**: Display all students in a formatted table
- **Update Student**: Modify existing student information by ID
- **Delete Student**: Remove students from the system by ID
- **Search Students**: Search by name (partial match) or exact ID match
- **File Operations**: Save/load student data to/from file for persistence
- **Input Validation**: Comprehensive validation for all user inputs
- **Exception Handling**: Robust error handling throughout the application

## Technical Implementation

- **ArrayList**: Used for dynamic student storage
- **Serialization**: File persistence using Java object serialization
- **Input Validation**: Custom validator class with comprehensive checks
- **Exception Handling**: Try-catch blocks for all critical operations
- **Menu-Driven Interface**: User-friendly console navigation

## File Structure

```
├── Student.java                    # Student model class
├── StudentManager.java             # Core business logic and file operations
├── InputValidator.java             # Input validation utilities
├── StudentManagementSystem.java    # Main application with menu interface
└── students.dat                    # Data file (created automatically)
```

## Compilation and Execution

### Compile the program:
```bash
javac *.java
```

### Run the program:
```bash
java StudentManagementSystem
```

## Usage Guide

### Main Menu Options:
1. **Add Student** - Enter student details with validation
2. **View All Students** - Display formatted list of all students
3. **Update Student** - Modify existing student by ID
4. **Delete Student** - Remove student by ID with confirmation
5. **Search Student** - Search by name or ID
6. **Save Data** - Manually save data to file
7. **Load Data** - Load data from file (replaces current data)
8. **Exit** - Exit with optional save prompt

### Input Validation Rules:
- **Name**: 2+ characters, letters and spaces only
- **ID**: 3+ characters, alphanumeric, automatically converted to uppercase
- **Age**: Integer between 5-100
- **Grade**: A-F (with optional +/-) or PASS/FAIL

## Data Persistence

- Student data is automatically saved to `students.dat` using Java serialization
- Data persists between program sessions
- Manual save/load options available in the menu
- Automatic data loading on program startup

## Error Handling

- Input validation with user-friendly error messages
- File I/O exception handling
- Duplicate ID prevention
- Confirmation prompts for destructive operations

## Sample Usage

```
=============================================================
                    MAIN MENU
=============================================================
1. Add Student
2. View All Students
3. Update Student
4. Delete Student
5. Search Student
6. Save Data
7. Load Data
8. Exit
=============================================================
Total Students: 0
=============================================================
Enter your choice: 1

==================================================
                ADD NEW STUDENT
==================================================
Enter student name: John Doe
Enter student ID: ST001
Enter student age: 20
Enter student grade: A

✓ Student added successfully!
Student Details:
Name: John Doe
ID: ST001
Age: 20
Grade: A
```

## System Requirements

- Java 8 or higher
- Console/Terminal environment
- Write permissions for data file creation

## Notes

- Student IDs are case-insensitive and automatically converted to uppercase
- The system prevents duplicate student IDs
- All data is stored locally in the `students.dat` file
- Search by name supports partial matching and is case-insensitive