/**
 * Person base class representing an individual person.
 * Demonstrates the Encapsulation principle of Object-Oriented Programming.
 */
public class Person {

    private String name;

    /**
     * Default constructor.
     */
    public Person() {
        this.name = "";
    }

    /**
     * Parameterized constructor.
     *
     * @param name the full name of the person
     */
    public Person(String name) {
        this.name = (name != null) ? name.trim() : "";
    }

    /**
     * Gets the person's name.
     *
     * @return name of the person
     */
    public String getName() {
        return name;
    }

    /**
     * Sets the person's name.
     *
     * @param name new name to set
     */
    public void setName(String name) {
        this.name = (name != null) ? name.trim() : "";
    }

    @Override
    public String toString() {
        return "Person{name='" + name + "'}";
    }
}
