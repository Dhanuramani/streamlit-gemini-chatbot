import java.io.*;
import java.util.ArrayList;
import java.util.List;

/**
 * StudentManager class handles all student operations and file I/O
 */
public class StudentManager {
    private ArrayList<Student> students;
    private static final String DATA_FILE = "students.dat";
    
    public StudentManager() {
        students = new ArrayList<>();
        loadFromFile();
    }
    
    /**
     * Add a new student to the system
     */
    public boolean addStudent(String name, String id, int age, String grade) {
        // Check if student ID already exists
        if (findStudentById(id) != null) {
            return false; // Student with this ID already exists
        }
        
        Student student = new Student(name, id, age, grade);
        students.add(student);
        return true;
    }
    
    /**
     * View all students
     */
    public void viewAllStudents() {
        if (students.isEmpty()) {
            System.out.println("No students found in the system.");
            return;
        }
        
        System.out.println("\n" + "=".repeat(70));
        System.out.println("                        ALL STUDENTS");
        System.out.println("=".repeat(70));
        
        for (int i = 0; i < students.size(); i++) {
            System.out.printf("%3d. %s%n", (i + 1), students.get(i));
        }
        System.out.println("=".repeat(70));
        System.out.println("Total students: " + students.size());
    }
    
    /**
     * Update student by ID
     */
    public boolean updateStudent(String id, String newName, int newAge, String newGrade) {
        Student student = findStudentById(id);
        if (student != null) {
            student.setName(newName);
            student.setAge(newAge);
            student.setGrade(newGrade);
            return true;
        }
        return false;
    }
    
    /**
     * Delete student by ID
     */
    public boolean deleteStudent(String id) {
        Student student = findStudentById(id);
        if (student != null) {
            students.remove(student);
            return true;
        }
        return false;
    }
    
    /**
     * Search students by name (partial match, case-insensitive)
     */
    public List<Student> searchByName(String name) {
        List<Student> results = new ArrayList<>();
        String searchName = name.toLowerCase().trim();
        
        for (Student student : students) {
            if (student.getName().toLowerCase().contains(searchName)) {
                results.add(student);
            }
        }
        return results;
    }
    
    /**
     * Find student by exact ID match
     */
    public Student findStudentById(String id) {
        for (Student student : students) {
            if (student.getId().equalsIgnoreCase(id.trim())) {
                return student;
            }
        }
        return null;
    }
    
    /**
     * Save students to file
     */
    public boolean saveToFile() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(DATA_FILE))) {
            oos.writeObject(students);
            return true;
        } catch (IOException e) {
            System.err.println("Error saving to file: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * Load students from file
     */
    @SuppressWarnings("unchecked")
    public boolean loadFromFile() {
        File file = new File(DATA_FILE);
        if (!file.exists()) {
            return true; // No file exists yet, start with empty list
        }
        
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(DATA_FILE))) {
            students = (ArrayList<Student>) ois.readObject();
            return true;
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Error loading from file: " + e.getMessage());
            students = new ArrayList<>(); // Start with empty list if loading fails
            return false;
        }
    }
    
    /**
     * Get total number of students
     */
    public int getStudentCount() {
        return students.size();
    }
    
    /**
     * Display search results
     */
    public void displaySearchResults(List<Student> results, String searchTerm) {
        if (results.isEmpty()) {
            System.out.println("No students found matching: " + searchTerm);
            return;
        }
        
        System.out.println("\n" + "=".repeat(70));
        System.out.println("         SEARCH RESULTS FOR: " + searchTerm.toUpperCase());
        System.out.println("=".repeat(70));
        
        for (int i = 0; i < results.size(); i++) {
            System.out.printf("%3d. %s%n", (i + 1), results.get(i));
        }
        System.out.println("=".repeat(70));
        System.out.println("Found " + results.size() + " student(s)");
    }
}