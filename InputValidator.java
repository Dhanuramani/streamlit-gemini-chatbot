import java.util.Scanner;

/**
 * InputValidator class handles input validation and user input operations
 */
public class InputValidator {
    private Scanner scanner;
    
    public InputValidator(Scanner scanner) {
        this.scanner = scanner;
    }
    
    /**
     * Validate and get student name
     */
    public String getValidName(String prompt) {
        String name;
        do {
            System.out.print(prompt);
            name = scanner.nextLine().trim();
            
            if (name.isEmpty()) {
                System.out.println("Error: Name cannot be empty. Please try again.");
                continue;
            }
            
            if (name.length() < 2) {
                System.out.println("Error: Name must be at least 2 characters long. Please try again.");
                continue;
            }
            
            if (!name.matches("[a-zA-Z\\s]+")) {
                System.out.println("Error: Name can only contain letters and spaces. Please try again.");
                continue;
            }
            
            break;
        } while (true);
        
        return name;
    }
    
    /**
     * Validate and get student ID
     */
    public String getValidId(String prompt) {
        String id;
        do {
            System.out.print(prompt);
            id = scanner.nextLine().trim();
            
            if (id.isEmpty()) {
                System.out.println("Error: ID cannot be empty. Please try again.");
                continue;
            }
            
            if (id.length() < 3) {
                System.out.println("Error: ID must be at least 3 characters long. Please try again.");
                continue;
            }
            
            if (!id.matches("[a-zA-Z0-9]+")) {
                System.out.println("Error: ID can only contain letters and numbers. Please try again.");
                continue;
            }
            
            break;
        } while (true);
        
        return id.toUpperCase();
    }
    
    /**
     * Validate and get student age
     */
    public int getValidAge(String prompt) {
        int age;
        do {
            System.out.print(prompt);
            try {
                String input = scanner.nextLine().trim();
                age = Integer.parseInt(input);
                
                if (age < 5 || age > 100) {
                    System.out.println("Error: Age must be between 5 and 100. Please try again.");
                    continue;
                }
                
                break;
            } catch (NumberFormatException e) {
                System.out.println("Error: Please enter a valid number for age.");
            }
        } while (true);
        
        return age;
    }
    
    /**
     * Validate and get student grade
     */
    public String getValidGrade(String prompt) {
        String grade;
        do {
            System.out.print(prompt);
            grade = scanner.nextLine().trim().toUpperCase();
            
            if (grade.isEmpty()) {
                System.out.println("Error: Grade cannot be empty. Please try again.");
                continue;
            }
            
            // Accept grades like A, B, C, D, F or A+, B-, etc.
            if (!grade.matches("[A-F][+-]?|PASS|FAIL")) {
                System.out.println("Error: Grade must be A-F (with optional + or -) or PASS/FAIL. Please try again.");
                continue;
            }
            
            break;
        } while (true);
        
        return grade;
    }
    
    /**
     * Get menu choice with validation
     */
    public int getMenuChoice(String prompt, int min, int max) {
        int choice;
        do {
            System.out.print(prompt);
            try {
                String input = scanner.nextLine().trim();
                choice = Integer.parseInt(input);
                
                if (choice < min || choice > max) {
                    System.out.printf("Error: Please enter a number between %d and %d.%n", min, max);
                    continue;
                }
                
                break;
            } catch (NumberFormatException e) {
                System.out.println("Error: Please enter a valid number.");
            }
        } while (true);
        
        return choice;
    }
    
    /**
     * Get confirmation (Y/N)
     */
    public boolean getConfirmation(String prompt) {
        String input;
        do {
            System.out.print(prompt + " (Y/N): ");
            input = scanner.nextLine().trim().toLowerCase();
            
            if (input.equals("y") || input.equals("yes")) {
                return true;
            } else if (input.equals("n") || input.equals("no")) {
                return false;
            } else {
                System.out.println("Error: Please enter Y or N.");
            }
        } while (true);
    }
    
    /**
     * Get non-empty string input
     */
    public String getNonEmptyString(String prompt) {
        String input;
        do {
            System.out.print(prompt);
            input = scanner.nextLine().trim();
            
            if (input.isEmpty()) {
                System.out.println("Error: Input cannot be empty. Please try again.");
                continue;
            }
            
            break;
        } while (true);
        
        return input;
    }
}