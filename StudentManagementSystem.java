import java.util.List;
import java.util.Scanner;

/**
 * Main class for the Student Management System
 * Provides a menu-driven console interface for managing students
 */
public class StudentManagementSystem {
    private StudentManager studentManager;
    private InputValidator validator;
    private Scanner scanner;
    
    public StudentManagementSystem() {
        scanner = new Scanner(System.in);
        validator = new InputValidator(scanner);
        studentManager = new StudentManager();
    }
    
    /**
     * Main method to start the application
     */
    public static void main(String[] args) {
        StudentManagementSystem sms = new StudentManagementSystem();
        sms.run();
    }
    
    /**
     * Main application loop
     */
    public void run() {
        System.out.println("=".repeat(60));
        System.out.println("    WELCOME TO STUDENT MANAGEMENT SYSTEM");
        System.out.println("=".repeat(60));
        
        boolean running = true;
        while (running) {
            try {
                displayMenu();
                int choice = validator.getMenuChoice("Enter your choice: ", 1, 8);
                
                switch (choice) {
                    case 1:
                        addStudent();
                        break;
                    case 2:
                        viewAllStudents();
                        break;
                    case 3:
                        updateStudent();
                        break;
                    case 4:
                        deleteStudent();
                        break;
                    case 5:
                        searchStudent();
                        break;
                    case 6:
                        saveData();
                        break;
                    case 7:
                        loadData();
                        break;
                    case 8:
                        running = exitSystem();
                        break;
                }
                
                if (running) {
                    System.out.println("\nPress Enter to continue...");
                    scanner.nextLine();
                }
                
            } catch (Exception e) {
                System.err.println("An unexpected error occurred: " + e.getMessage());
                System.out.println("Please try again.");
            }
        }
    }
    
    /**
     * Display the main menu
     */
    private void displayMenu() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("                    MAIN MENU");
        System.out.println("=".repeat(60));
        System.out.println("1. Add Student");
        System.out.println("2. View All Students");
        System.out.println("3. Update Student");
        System.out.println("4. Delete Student");
        System.out.println("5. Search Student");
        System.out.println("6. Save Data");
        System.out.println("7. Load Data");
        System.out.println("8. Exit");
        System.out.println("=".repeat(60));
        System.out.println("Total Students: " + studentManager.getStudentCount());
        System.out.println("=".repeat(60));
    }
    
    /**
     * Add a new student
     */
    private void addStudent() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println("                ADD NEW STUDENT");
        System.out.println("=".repeat(50));
        
        try {
            String name = validator.getValidName("Enter student name: ");
            String id = validator.getValidId("Enter student ID: ");
            int age = validator.getValidAge("Enter student age: ");
            String grade = validator.getValidGrade("Enter student grade: ");
            
            if (studentManager.addStudent(name, id, age, grade)) {
                System.out.println("\n✓ Student added successfully!");
                System.out.println("Student Details:");
                System.out.println("Name: " + name);
                System.out.println("ID: " + id);
                System.out.println("Age: " + age);
                System.out.println("Grade: " + grade);
            } else {
                System.out.println("\n✗ Error: A student with ID '" + id + "' already exists!");
            }
            
        } catch (Exception e) {
            System.err.println("Error adding student: " + e.getMessage());
        }
    }
    
    /**
     * View all students
     */
    private void viewAllStudents() {
        try {
            studentManager.viewAllStudents();
        } catch (Exception e) {
            System.err.println("Error viewing students: " + e.getMessage());
        }
    }
    
    /**
     * Update an existing student
     */
    private void updateStudent() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println("                UPDATE STUDENT");
        System.out.println("=".repeat(50));
        
        try {
            String id = validator.getValidId("Enter student ID to update: ");
            Student student = studentManager.findStudentById(id);
            
            if (student == null) {
                System.out.println("\n✗ Student with ID '" + id + "' not found!");
                return;
            }
            
            System.out.println("\nCurrent student details:");
            System.out.println(student);
            System.out.println();
            
            String newName = validator.getValidName("Enter new name: ");
            int newAge = validator.getValidAge("Enter new age: ");
            String newGrade = validator.getValidGrade("Enter new grade: ");
            
            if (validator.getConfirmation("Are you sure you want to update this student?")) {
                if (studentManager.updateStudent(id, newName, newAge, newGrade)) {
                    System.out.println("\n✓ Student updated successfully!");
                    System.out.println("Updated Details:");
                    System.out.println(studentManager.findStudentById(id));
                } else {
                    System.out.println("\n✗ Error updating student!");
                }
            } else {
                System.out.println("Update cancelled.");
            }
            
        } catch (Exception e) {
            System.err.println("Error updating student: " + e.getMessage());
        }
    }
    
    /**
     * Delete a student
     */
    private void deleteStudent() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println("                DELETE STUDENT");
        System.out.println("=".repeat(50));
        
        try {
            String id = validator.getValidId("Enter student ID to delete: ");
            Student student = studentManager.findStudentById(id);
            
            if (student == null) {
                System.out.println("\n✗ Student with ID '" + id + "' not found!");
                return;
            }
            
            System.out.println("\nStudent to be deleted:");
            System.out.println(student);
            
            if (validator.getConfirmation("\nAre you sure you want to delete this student?")) {
                if (studentManager.deleteStudent(id)) {
                    System.out.println("\n✓ Student deleted successfully!");
                } else {
                    System.out.println("\n✗ Error deleting student!");
                }
            } else {
                System.out.println("Deletion cancelled.");
            }
            
        } catch (Exception e) {
            System.err.println("Error deleting student: " + e.getMessage());
        }
    }
    
    /**
     * Search for students
     */
    private void searchStudent() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println("                SEARCH STUDENT");
        System.out.println("=".repeat(50));
        System.out.println("1. Search by Name");
        System.out.println("2. Search by ID");
        System.out.println("=".repeat(50));
        
        try {
            int choice = validator.getMenuChoice("Enter search type: ", 1, 2);
            
            if (choice == 1) {
                searchByName();
            } else {
                searchById();
            }
            
        } catch (Exception e) {
            System.err.println("Error during search: " + e.getMessage());
        }
    }
    
    /**
     * Search students by name
     */
    private void searchByName() {
        String name = validator.getNonEmptyString("Enter name to search: ");
        List<Student> results = studentManager.searchByName(name);
        studentManager.displaySearchResults(results, name);
    }
    
    /**
     * Search student by ID
     */
    private void searchById() {
        String id = validator.getValidId("Enter ID to search: ");
        Student student = studentManager.findStudentById(id);
        
        if (student != null) {
            System.out.println("\n" + "=".repeat(70));
            System.out.println("         SEARCH RESULT FOR ID: " + id);
            System.out.println("=".repeat(70));
            System.out.println("  1. " + student);
            System.out.println("=".repeat(70));
        } else {
            System.out.println("\n✗ No student found with ID: " + id);
        }
    }
    
    /**
     * Save data to file
     */
    private void saveData() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println("                SAVE DATA");
        System.out.println("=".repeat(50));
        
        try {
            if (studentManager.saveToFile()) {
                System.out.println("✓ Data saved successfully to file!");
                System.out.println("Total students saved: " + studentManager.getStudentCount());
            } else {
                System.out.println("✗ Error saving data to file!");
            }
        } catch (Exception e) {
            System.err.println("Error saving data: " + e.getMessage());
        }
    }
    
    /**
     * Load data from file
     */
    private void loadData() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println("                LOAD DATA");
        System.out.println("=".repeat(50));
        
        try {
            if (validator.getConfirmation("This will replace current data. Continue?")) {
                if (studentManager.loadFromFile()) {
                    System.out.println("✓ Data loaded successfully from file!");
                    System.out.println("Total students loaded: " + studentManager.getStudentCount());
                } else {
                    System.out.println("✗ Error loading data from file!");
                }
            } else {
                System.out.println("Load operation cancelled.");
            }
        } catch (Exception e) {
            System.err.println("Error loading data: " + e.getMessage());
        }
    }
    
    /**
     * Exit the system
     */
    private boolean exitSystem() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println("                EXIT SYSTEM");
        System.out.println("=".repeat(50));
        
        try {
            if (validator.getConfirmation("Do you want to save data before exiting?")) {
                saveData();
            }
            
            System.out.println("\n" + "=".repeat(60));
            System.out.println("    THANK YOU FOR USING STUDENT MANAGEMENT SYSTEM");
            System.out.println("                    GOODBYE!");
            System.out.println("=".repeat(60));
            
            scanner.close();
            return false; // Exit the main loop
            
        } catch (Exception e) {
            System.err.println("Error during exit: " + e.getMessage());
            return true; // Continue running if there's an error
        }
    }
}