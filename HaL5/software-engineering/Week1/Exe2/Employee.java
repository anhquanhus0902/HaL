import java.util.List;
import java.util.ArrayList;

/**
 *
 * @author anhquan
 */
public abstract class Employee {
    private String id;
    private String fullName;
    private String birthDay;
    private String phone;
    private String email;
    private int employeeType;
    private int employeeCount;
    private List<Certificate> certiList;

    public Employee(String id, String fullName, String birthDay, String phone, String email, int employeeType, int employeeCount) {
        this.id = id;
        this.fullName = fullName;
        this.birthDay = birthDay;
        this.phone = phone;
        this.email = email;
        this.employeeType = employeeType;
        this.employeeCount = employeeCount;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    public String getBirthDay() {
        return birthDay;
    }

    public void setBirthDay(String birthDay) {
        this.birthDay = birthDay;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getEmployeeType() {
        return employeeType;
    }

    public void setEmployeeType(int employeeType) {
        this.employeeType = employeeType;
    }

    public int getEmployeeCount() {
        return employeeCount;
    }

    public void setEmployeeCount(int employeeCount) {
        this.employeeCount = employeeCount;
    }

    public List<Certificate> getCertiList() {
        return certiList;
    }

    public void setCertiList(List<Certificate> certiList) {
        this.certiList = certiList;
    }

    public String toString() {
        return "Employee:" + "id=" + id + ", fullName=" + fullName + ", birthDay=" + birthDay + ", phone=" + phone + ", email=" + email + ", employeeType=" + employeeType + ", employeeCount=" + employeeCount;
    }
    public void showInfo(){
        System.out.println(toString());
    }
    
    public abstract void showMe();
}
