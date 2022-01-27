/**
 *
 * @author anhquan
 */
public class Intern extends Employee{
    private String major;
    private int semester;
    private String uniName;

    public Intern(String id, String fullName, String birthDay, String phone, String email, int employeecount, String major, int semester, String uniName) {
        super(id, fullName, birthDay, phone, email, 2, employeecount);
        this.major = major;
        this.semester = semester;
        this.uniName = uniName;
    }

    public String getMajor() {
        return major;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public int getSemester() {
        return semester;
    }

    public void setSemester(int semester) {
        this.semester = semester;
    }

    public String getUniName() {
        return uniName;
    }

    public void setUniName(String uniName) {
        this.uniName = uniName;
    }
    
    public String toString(){
        return super.toString() + ", Major=" + major + ", Semester=" + semester + ", University Name=" + uniName;
    }

    @Override
    public void showMe() {
        System.out.println(super.toString() + ", Major=" + major + ", Semester=" + semester + ", University Name=" + uniName);
    }
}
