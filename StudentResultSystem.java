import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Main Driver Class for the Student Result Analysis System.
 *
 * Responsibilities:
 * - Dynamically parses 'RAnalysis.csv' using BufferedReader.
 * - Safely handles non-numeric, null, empty, "#NUM!", and "AB" values.
 * - Instantiates Student and CourseScore objects utilizing OOP design.
 * - Displays a formatted tabular report and comprehensive class analytics.
 */
public class StudentResultSystem {

    /**
     * Internal specification class for course metadata in the dataset.
     */
    private static class CourseConfig {
        final String courseName;
        final int columnIndex;
        final double maxMarks;

        CourseConfig(String courseName, int columnIndex, double maxMarks) {
            this.courseName = courseName;
            this.columnIndex = columnIndex;
            this.maxMarks = maxMarks;
        }
    }

    // 8 Course Blocks as specified in requirements
    private static final List<CourseConfig> COURSE_CONFIGS = List.of(
            new CourseConfig("IOS", 8, 50.0),
            new CourseConfig("DA", 14, 50.0),
            new CourseConfig("P&S", 20, 50.0),
            new CourseConfig("BA&TMM", 26, 50.0),
            new CourseConfig("M&A", 32, 50.0),
            new CourseConfig("MARATHI", 39, 50.0),
            new CourseConfig("COI", 45, 100.0),
            new CourseConfig("LBRDBA", 51, 50.0)
    );

    /**
     * Safely parses numeric marks from a CSV token.
     * Handles empty tokens, whitespace, "AB" (absent), "#NUM!", "NA", etc.
     *
     * @param tokens array of row values
     * @param index  column index to extract
     * @return parsed double or 0.0 if invalid/empty
     */
    public static double parseMarks(String[] tokens, int index) {
        if (tokens == null || index < 0 || index >= tokens.length) {
            return 0.0;
        }
        String val = tokens[index].trim();
        if (val.isEmpty() || val.equalsIgnoreCase("AB")
                || val.equalsIgnoreCase("#NUM!")
                || val.equalsIgnoreCase("NA")
                || val.equalsIgnoreCase("ABSENT")
                || val.equalsIgnoreCase("-")) {
            return 0.0;
        }
        try {
            return Double.parseDouble(val);
        } catch (NumberFormatException e) {
            return 0.0;
        }
    }

    /**
     * Reads and parses student records from the CSV file.
     *
     * @param filePath path to RAnalysis.csv
     * @return list of parsed Student objects
     */
    public static List<Student> loadStudentsFromCsv(String filePath) {
        List<Student> students = new ArrayList<>();
        File file = new File(filePath);

        if (!file.exists()) {
            System.err.println("[ERROR] CSV file not found at: " + file.getAbsolutePath());
            return students;
        }

        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(new FileInputStream(file), StandardCharsets.UTF_8))) {

            String line;
            int rowIndex = 0;

            while ((line = reader.readLine()) != null) {
                // Header metadata is in Rows 0-2 (0-indexed)
                if (rowIndex < 3) {
                    rowIndex++;
                    continue;
                }
                rowIndex++;

                String trimmedLine = line.trim();
                if (trimmedLine.isEmpty()) {
                    continue;
                }

                // Preserve trailing empty tokens using limit -1
                String[] tokens = line.split(",", -1);

                // Need at least Roll No (0), PRN (1), Name (2)
                if (tokens.length < 3) {
                    continue;
                }

                String rollNo = tokens[0].trim();
                String prn = tokens[1].trim();
                String name = tokens[2].trim();

                // Skip blank entries
                if (rollNo.isEmpty() && prn.isEmpty() && name.isEmpty()) {
                    continue;
                }

                Student student = new Student(rollNo, prn, name);

                // Add scores for each of the 8 Course Blocks
                for (CourseConfig config : COURSE_CONFIGS) {
                    double marks = parseMarks(tokens, config.columnIndex);
                    student.addCourseScore(new CourseScore(config.courseName, marks, config.maxMarks));
                }

                students.add(student);
            }
        } catch (Exception e) {
            System.err.println("[ERROR] Exception occurred while reading CSV: " + e.getMessage());
            e.printStackTrace();
        }

        return students;
    }

    /**
     * Displays a formatted tabular report of all processed students.
     *
     * @param students list of students to display
     */
    public static void displayStudentReport(List<Student> students) {
        String separator = "+--------+------------------+-----------------------------------+--------------+------------+--------------------+";
        System.out.println("\n" + separator);
        System.out.printf("| %-6s | %-16s | %-33s | %-12s | %-10s | %-18s |\n",
                "Roll", "PRN", "Student Name", "Marks (450)", "Percentage", "Grade");
        System.out.println(separator);

        for (Student s : students) {
            System.out.printf("| %-6s | %-16s | %-33s | %6.2f / 450 | %9.2f%% | %-18s |\n",
                    s.getRollNo(),
                    s.getPrn(),
                    s.getName(),
                    s.getTotalObtainedMarks(),
                    s.calculatePercentage(),
                    s.getGrade());
        }
        System.out.println(separator);
    }

    /**
     * Calculates and displays summary analytics for the class.
     *
     * @param students list of students
     */
    public static void displaySummaryAnalytics(List<Student> students) {
        if (students.isEmpty()) {
            System.out.println("\n[INFO] No student records available for analytics.");
            return;
        }

        int totalStudents = students.size();
        int passedCount = 0;
        int failedCount = 0;
        double totalPercentageSum = 0.0;
        double totalMarksSum = 0.0;

        Student topStudent = students.get(0);
        Student lowestStudent = students.get(0);

        Map<String, Integer> gradeDistribution = new LinkedHashMap<>();
        gradeDistribution.put("O (Outstanding)", 0);
        gradeDistribution.put("A+ (Excellent)", 0);
        gradeDistribution.put("A (Very Good)", 0);
        gradeDistribution.put("B+ (Good)", 0);
        gradeDistribution.put("B (Above Average)", 0);
        gradeDistribution.put("C (Pass)", 0);
        gradeDistribution.put("F (Fail)", 0);

        for (Student s : students) {
            double pct = s.calculatePercentage();
            totalPercentageSum += pct;
            totalMarksSum += s.getTotalObtainedMarks();

            if (s.isPassed()) {
                passedCount++;
            } else {
                failedCount++;
            }

            String grade = s.getGrade();
            gradeDistribution.put(grade, gradeDistribution.getOrDefault(grade, 0) + 1);

            if (pct > topStudent.calculatePercentage()) {
                topStudent = s;
            }
            if (pct < lowestStudent.calculatePercentage()) {
                lowestStudent = s;
            }
        }

        double classAveragePct = totalPercentageSum / totalStudents;
        double classAverageMarks = totalMarksSum / totalStudents;
        double passPct = (passedCount * 100.0) / totalStudents;
        double failPct = (failedCount * 100.0) / totalStudents;

        System.out.println("\n========================================================");
        System.out.println("               CLASS SUMMARY ANALYTICS                  ");
        System.out.println("========================================================");
        System.out.printf(" Total Students Evaluated : %d\n", totalStudents);
        System.out.printf(" Class Average Marks      : %.2f / 450.00\n", classAverageMarks);
        System.out.printf(" Class Average Percentage : %.2f%%\n", classAveragePct);
        System.out.printf(" Passed Students          : %d (%.2f%%)\n", passedCount, passPct);
        System.out.printf(" Failed Students          : %d (%.2f%%)\n", failedCount, failPct);
        System.out.println("--------------------------------------------------------");
        System.out.println(" Performance Extremes:");
        System.out.printf("  - Top Performer   : %s (%s) - %.2f Marks (%.2f%%, %s)\n",
                topStudent.getName(), topStudent.getRollNo(),
                topStudent.getTotalObtainedMarks(), topStudent.calculatePercentage(), topStudent.getGrade());
        System.out.printf("  - Lowest Performer: %s (%s) - %.2f Marks (%.2f%%, %s)\n",
                lowestStudent.getName(), lowestStudent.getRollNo(),
                lowestStudent.getTotalObtainedMarks(), lowestStudent.calculatePercentage(), lowestStudent.getGrade());

        System.out.println("--------------------------------------------------------");
        System.out.println(" Grade Distribution:");
        for (Map.Entry<String, Integer> entry : gradeDistribution.entrySet()) {
            double share = (entry.getValue() * 100.0) / totalStudents;
            int barLength = (int) Math.round(share / 4.0); // ASCII bar chart
            String bar = "#".repeat(Math.max(0, barLength));
            System.out.printf("  %-18s : %2d students (%5.1f%%)  [%s]\n",
                    entry.getKey(), entry.getValue(), share, bar);
        }

        // Course-wise breakdown
        System.out.println("--------------------------------------------------------");
        System.out.println(" Course-wise Performance Average:");
        for (int i = 0; i < COURSE_CONFIGS.size(); i++) {
            CourseConfig cfg = COURSE_CONFIGS.get(i);
            double courseTotal = 0.0;
            for (Student s : students) {
                if (i < s.getCourseScores().size()) {
                    courseTotal += s.getCourseScores().get(i).getObtainedMarks();
                }
            }
            double courseAvg = courseTotal / totalStudents;
            double coursePct = (courseAvg / cfg.maxMarks) * 100.0;
            System.out.printf("  %-8s (Max: %3.0f) : Avg: %5.2f  (%.2f%%)\n",
                    cfg.courseName, cfg.maxMarks, courseAvg, coursePct);
        }
        System.out.println("========================================================\n");
    }

    /**
     * Main entry point for the application.
     *
     * @param args optional command line arguments (args[0] = path to csv)
     */
    public static void main(String[] args) {
        System.out.println("========================================================");
        System.out.println("   STUDENT RESULT ANALYSIS & RECOMMENDATION SYSTEM      ");
        System.out.println("========================================================");

        String filePath = (args.length > 0) ? args[0] : "RAnalysis.csv";
        System.out.println("[INFO] Reading dataset from: " + filePath);

        List<Student> students = loadStudentsFromCsv(filePath);
        System.out.println("[SUCCESS] Successfully loaded and parsed " + students.size() + " student records.");

        // Display individual student results table
        displayStudentReport(students);

        // Display class summary analytics
        displaySummaryAnalytics(students);
    }
}
