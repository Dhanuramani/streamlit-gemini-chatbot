import java.io.Serializable;

/**
 * Student class representing a student with basic information
 */
public class Student implements Serializable {
    private static final long serialVersionUID = 1L;
    
    private String name;
    private String id;
    private int age;
    private String grade;
    
    public Student(String name, String id, int age, String grade) {
        this.name = name;
        this.id = id;
        this.age = age;
        this.grade = grade;
    }
    
    // Getters
    public String getName() { return name; }
    public String getId() { return id; }
    public int getAge() { return age; }
    public String getGrade() { return grade; }
    
    // Setters
    public void setName(String name) { this.name = name; }
    public void setId(String id) { this.id = id; }
    public void setAge(int age) { this.age = age; }
    public void setGrade(String grade) { this.grade = grade; }
    
    @Override
    public String toString() {
        return String.format("ID: %-10s | Name: %-20s | Age: %-3d | Grade: %s", 
                           id, name, age, grade);
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Student student = (Student) obj;
        return id.equals(student.id);
    }
    
    @Override
    public int hashCode() {
        return id.hashCode();
    }
}