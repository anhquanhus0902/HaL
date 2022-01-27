/**
 *
 * @author anhquan
 */
public class Fresher extends Employee{
    private String graduationDate;
    private String graduationRank;
    private String education;
    
    public Fresher(String id, String fullName, String birthDay, String phone, String email, int employeecount, String graduationDate, String graduationRank, String education) {
        super(id, fullName, birthDay, phone, email, 1, employeecount);
        this.graduationDate = graduationDate;
        this.graduationRank = graduationRank;
        this.education = education;
    }

    public String getGraduationDate() {
        return graduationDate;
    }

    public void setGraduationDate(String graduationDate) {
        this.graduationDate = graduationDate;
    }

    public String getGraduationRank() {
        return graduationRank;
    }

    public void setGraduationRank(String graduationRank) {
        this.graduationRank = graduationRank;
    }

    public String getEducation() {
        return education;
    }

    public void setEducation(String education) {
        this.education = education;
    }
    
    public String toString(){
        return super.toString() + ", Graduation Date=" + graduationDate + ", Graduation Rank=" + graduationRank + ", Education=" + education;
    }

    @Override
    public void showMe() {
        System.out.println(super.toString() + ", Graduation Date=" + graduationDate + ", Graduation Rank=" + graduationRank + ", Education=" + education);
    }
}
