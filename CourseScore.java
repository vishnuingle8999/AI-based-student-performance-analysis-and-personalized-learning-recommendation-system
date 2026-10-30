/**
 * CourseScore class representing the score obtained by a student in a specific course.
 * Implements Gradable to demonstrate interface realization and polymorphism.
 */
public class CourseScore implements Gradable {

    private String courseName;
    private double obtainedMarks;
    private double maxMarks;

    /**
     * Default constructor.
     */
    public CourseScore() {
        this("", 0.0, 0.0);
    }

    /**
     * Parameterized constructor.
     *
     * @param courseName    the name or code of the course
     * @param obtainedMarks marks scored by the student
     * @param maxMarks      maximum allowable marks for the course
     */
    public CourseScore(String courseName, double obtainedMarks, double maxMarks) {
        this.courseName = (courseName != null) ? courseName.trim() : "";
        this.obtainedMarks = Math.max(0.0, obtainedMarks);
        this.maxMarks = Math.max(0.0, maxMarks);
    }

    public String getCourseName() {
        return courseName;
    }

    public void setCourseName(String courseName) {
        this.courseName = (courseName != null) ? courseName.trim() : "";
    }

    public double getObtainedMarks() {
        return obtainedMarks;
    }

    public void setObtainedMarks(double obtainedMarks) {
        this.obtainedMarks = Math.max(0.0, obtainedMarks);
    }

    public double getMaxMarks() {
        return maxMarks;
    }

    public void setMaxMarks(double maxMarks) {
        this.maxMarks = Math.max(0.0, maxMarks);
    }

    @Override
    public double calculatePercentage() {
        if (maxMarks <= 0.0) {
            return 0.0;
        }
        return (obtainedMarks / maxMarks) * 100.0;
    }

    @Override
    public String getGrade() {
        return Gradable.determineGrade(calculatePercentage());
    }

    @Override
    public String toString() {
        return String.format("%s: %.2f / %.2f (%.2f%% - %s)",
                courseName, obtainedMarks, maxMarks, calculatePercentage(), getGrade());
    }
}
