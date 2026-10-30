/**
 * Gradable interface defining the contract for entities that can be graded.
 * Demonstrates the Abstraction and Polymorphism principles in OOP.
 */
public interface Gradable {

    /**
     * Calculates and returns the percentage obtained.
     *
     * @return percentage as a double
     */
    double calculatePercentage();

    /**
     * Determines and returns the grade based on standard criteria.
     *
     * @return grade string (e.g., "O (Outstanding)", "A+ (Excellent)", etc.)
     */
    String getGrade();

    /**
     * Utility method to map a percentage value to its corresponding grade category.
     *
     * Grading Criteria:
     * - Percentage >= 85.0%: "O (Outstanding)"
     * - Percentage >= 75.0%: "A+ (Excellent)"
     * - Percentage >= 65.0%: "A (Very Good)"
     * - Percentage >= 55.0%: "B+ (Good)"
     * - Percentage >= 50.0%: "B (Above Average)"
     * - Percentage >= 40.0%: "C (Pass)"
     * - Percentage <  40.0%: "F (Fail)"
     *
     * @param percentage the percentage score
     * @return the grade description string
     */
    static String determineGrade(double percentage) {
        if (percentage >= 85.0) {
            return "O (Outstanding)";
        } else if (percentage >= 75.0) {
            return "A+ (Excellent)";
        } else if (percentage >= 65.0) {
            return "A (Very Good)";
        } else if (percentage >= 55.0) {
            return "B+ (Good)";
        } else if (percentage >= 50.0) {
            return "B (Above Average)";
        } else if (percentage >= 40.0) {
            return "C (Pass)";
        } else {
            return "F (Fail)";
        }
    }
}
