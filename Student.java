import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Student class extending Person and implementing Gradable.
 * Demonstrates Inheritance (from Person), Interface Implementation / Polymorphism (Gradable),
 * and Composition (maintaining a List of CourseScore objects).
 */
public class Student extends Person implements Gradable {

    private String rollNo;
    private String prn;
    private final List<CourseScore> courseScores;

    /**
     * Default constructor.
     */
    public Student() {
        super();
        this.rollNo = "";
        this.prn = "";
        this.courseScores = new ArrayList<>();
    }

    /**
     * Parameterized constructor.
     *
     * @param rollNo student roll number
     * @param prn    student Permanent Registration Number (PRN)
     * @param name   student full name
     */
    public Student(String rollNo, String prn, String name) {
        super(name);
        this.rollNo = (rollNo != null) ? rollNo.trim() : "";
        this.prn = (prn != null) ? prn.trim() : "";
        this.courseScores = new ArrayList<>();
    }

    public String getRollNo() {
        return rollNo;
    }

    public void setRollNo(String rollNo) {
        this.rollNo = (rollNo != null) ? rollNo.trim() : "";
    }

    public String getPrn() {
        return prn;
    }

    public void setPrn(String prn) {
        this.prn = (prn != null) ? prn.trim() : "";
    }

    /**
     * Adds a course score to the student's academic record.
     * Demonstrates Composition.
     *
     * @param score CourseScore object
     */
    public void addCourseScore(CourseScore score) {
        if (score != null) {
            this.courseScores.add(score);
        }
    }

    /**
     * Returns an unmodifiable view of the course scores list.
     *
     * @return unmodifiable list of CourseScore
     */
    public List<CourseScore> getCourseScores() {
        return Collections.unmodifiableList(courseScores);
    }

    /**
     * Calculates total marks obtained across all courses.
     *
     * @return aggregate obtained marks
     */
    public double getTotalObtainedMarks() {
        double sum = 0.0;
        for (CourseScore score : courseScores) {
            sum += score.getObtainedMarks();
        }
        return sum;
    }

    /**
     * Calculates total maximum marks possible across all courses.
     *
     * @return aggregate maximum marks
     */
    public double getTotalMaxMarks() {
        double sum = 0.0;
        for (CourseScore score : courseScores) {
            sum += score.getMaxMarks();
        }
        return sum;
    }

    /**
     * Calculates aggregate percentage across all courses.
     *
     * @return percentage as a double
     */
    @Override
    public double calculatePercentage() {
        double maxTotal = getTotalMaxMarks();
        if (maxTotal <= 0.0) {
            return 0.0;
        }
        return (getTotalObtainedMarks() / maxTotal) * 100.0;
    }

    /**
     * Gets final overall grade based on aggregate percentage.
     *
     * @return grade string
     */
    @Override
    public String getGrade() {
        return Gradable.determineGrade(calculatePercentage());
    }

    /**
     * Determines whether the student passed the overall threshold (>= 40.0%).
     *
     * @return true if passed, false otherwise
     */
    public boolean isPassed() {
        return calculatePercentage() >= 40.0;
    }

    @Override
    public String toString() {
        return String.format("Student[Roll=%s, PRN=%s, Name=%s, Marks=%.2f/%.2f, Pct=%.2f%%, Grade=%s]",
                rollNo, prn, getName(), getTotalObtainedMarks(), getTotalMaxMarks(),
                calculatePercentage(), getGrade());
    }
}
