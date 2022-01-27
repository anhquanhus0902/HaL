/**
 *
 * @author anhquan
 */
public class Experience extends Employee{
    private int expInYear;
    private String proSkill;

    public Experience(String id, String fullName, String birthDay, String phone, String email, int employeeCount, int expInYear, String proSkill) {
        super(id, fullName, birthDay, phone, email, 0, employeeCount);
        this.expInYear = expInYear;
        this.proSkill = proSkill;
    }

    public int getExpInYear() {
        return expInYear;
    }

    public void setExpInYear(int expInYear) {
        this.expInYear = expInYear;
    }

    public String getProSkill() {
        return proSkill;
    }

    public void setProSkill(String proSkill) {
        this.proSkill = proSkill;
    }
    
    public String toString(){
        return super.toString() + ", ExpInYear=" + expInYear + ", Proskill=" + proSkill;
    }
    
    @Override
    public void showMe() {
        System.out.println(super.toString() + ", ExpInYear=" + expInYear + ", Proskill=" + proSkill);
    }
}
