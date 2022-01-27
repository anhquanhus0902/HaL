import java.util.Random;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.io.File;
import java.io.IOException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import exception.*;

/**
 *
 * @author anhquan
 */
public class Main {
    // Please modify this URL.
    private static final String FILE_URL = "\\Employees.txt";
    
    public static void main(String[] args) throws FullNameException, EmailException, PhoneException, BirthdayException, IOException{
        File file = new File(FILE_URL);
        FileReader fr = new FileReader(file);
        BufferedReader br = new BufferedReader(fr);
        Scanner sc = new Scanner(System.in);
        Random rd = new Random();
        
        int act;
        System.out.println("Vui lòng nhập đúng như chỉ dẫn, nếu không chương trình sẽ bị lỗi và bạn sẽ phải khởi động lại");
        System.out.println("Bạn muốn làm gì? (0: Thêm nhân viên | 1: Sửa thông tin | 2: Xóa nhân viên)");
        act = sc.nextInt();
        if (act == 0){
            FileWriter fw = new FileWriter(file, true);
            BufferedWriter bw = new BufferedWriter(fw);
            int count = 0;
            while (true){
                int employeeType;
                System.out.println("0: Nhân viên có kinh nghiệm | 1: Nhân viện mới ra trường | 2: Thực tập sinh | 3: Thoát chương trình");
                employeeType = sc.nextInt();
                sc.nextLine();
                if (employeeType == 3){
                    break;
                }
                else{
                    ++count;
                    String id = String.valueOf(rd.nextInt(9999999));
                    System.out.println("Tên nhân viên");
                    String fullName = sc.nextLine();
                    checkName(fullName);
                    System.out.println("Ngày sinh (Nhập theo định dạng: DD/MM/YYYY)");
                    String birthDay = sc.nextLine();
                    checkBirthday(birthDay);
                    System.out.println("SDT");
                    String phone = sc.nextLine();
                    checkPhone(phone);
                    System.out.println("Email (Đây là email mà công ty đã cấp cho nhân viên, đuôi: @abc.com)");
                    String email = sc.nextLine();
                    checkEmail(email);
                    
                    if (employeeType == 0){
                        System.out.println("Số năm kinh nghiệm");
                        int expInYear = sc.nextInt();
                        sc.nextLine();
                        System.out.println("Kỹ năng chuyên môn");
                        String proSkill = sc.nextLine();
                        Employee exp1 = new Experience(id, fullName, birthDay, phone, email, count, expInYear, proSkill);
                        bw.newLine();
                        bw.write(exp1.toString());
                    }
                    else if (employeeType == 1){
                        System.out.println("Ngày tốt nghiệp");
                        String graduationDate = sc.nextLine();
                        System.out.println("Xếp loại tốt nghiệp");
                        String graduationRank = sc.nextLine();
                        System.out.println("Tên trường");
                        String education = sc.nextLine();
                        Employee frs1 = new Fresher(id, fullName, birthDay, phone, email, count, graduationDate, graduationRank, education);
                        bw.newLine();
                        bw.write(frs1.toString());
                    }
                    else{
                        System.out.println("Chuyên ngành");
                        String major = sc.nextLine();
                        System.out.println("Kỳ học");
                        int semester = sc.nextInt();
                        sc.nextLine();
                        System.out.println("Tên trường");
                        String uniName = sc.nextLine();
                        Employee itn1 = new Intern(id, fullName, birthDay, phone, email, count, major, semester, uniName);
                        bw.newLine();
                        bw.write(itn1.toString());
                    }
                }
            }
            bw.newLine();
            bw.write("Số lượng nhân viên đã nhập: " + count);
            br.close();
            bw.close();
        }
        else{
            List<String> lines = new ArrayList<>();
            System.out.println("Nhập ID của nhân viên");
            int employeeId = sc.nextInt();
            boolean found = false;
            sc.nextLine();
            String line;
            while ((line = br.readLine()) != null){
                if (line.contains(String.valueOf(employeeId))){
                    found = true;
                    if (act == 1){
                        Employee e = getEmployee(line);
                        System.out.println("Tên nhân viên");
                        String newFullName = sc.nextLine();
                        System.out.println("Ngày sinh");
                        String newBirthDay = sc.nextLine();
                        System.out.println("SĐT");
                        String newPhone = sc.nextLine();
                        System.out.println("Email");
                        String newEmail = sc.nextLine();
                        if (!newFullName.isEmpty()){
                            e.setFullName(newFullName);
                        }
                        if (!newBirthDay.isEmpty()){
                            e.setBirthDay(newBirthDay);
                        }
                        if (!newPhone.isEmpty()){
                            e.setPhone(newPhone);
                        }
                        if (!newEmail.isEmpty()){
                            e.setEmail(newEmail);
                        }
                        lines.add(e.toString());
                    }
                    else if (act == 2){
                        lines.add("Đã xóa");
                    }
                    continue;
                }
                lines.add(line);
            }
            FileWriter fw = new FileWriter(file);
            BufferedWriter bw = new BufferedWriter(fw);
            int n = lines.size();
            for (int i = 0; i < n; ++i){
                bw.write(lines.get(i));
                if (i != n-1){
                    bw.newLine();
                }
            }
            System.out.println("Đã cập nhật");
            if (found == false){
                System.out.println("Không tồn tại");
            }
            bw.close();
            br.close();
        }
    }
    
    public static boolean checkName(String name) throws FullNameException{
        for (int i = 0; i < name.length(); ++i){
            char c  = name.charAt(i);
            if (c < 'A' || (c > 'Z' && c < 'a') || c > 'z'){
                if (c != ' '){
                    throw new FullNameException("Tên chứa ký tự không hợp lệ");
                }
            }
        }
        return true;
    }
    
    public static boolean checkBirthday(String birthday) throws BirthdayException{
        String[] a = birthday.split("/");
        if (a.length == 3){
            for (int i = 0; i < 3; ++i){
                for (int j = 0; j < a[i].length(); ++j){
                    if (a[i].charAt(j) < '0' || a[i].charAt(j) > '9'){
                        throw new BirthdayException("Ngày sinh không hợp lệ");
                    }
                }
            }
            if (a[2].length() == 4 && Integer.parseInt(a[2]) < 9999){
                if (Integer.parseInt(a[1]) > 0 && Integer.parseInt(a[1]) <= 12){
                    if (Integer.parseInt(a[0]) > 0 && Integer.parseInt(a[0]) <= 31){
                        return true;
                    }
                }
            }
        }
        throw new BirthdayException("Ngày sinh không hợp lệ");
    }
    
    public static boolean checkPhone(String phone) throws PhoneException{
        for (int i = 0; i < phone.length(); ++i){
            char c = phone.charAt(i);
            if (c < '0' || c > '9'){
                throw new PhoneException("SĐT không hợp lệ");
            }
        }
        return true;
    }
    
    public static boolean checkEmail(String email) throws EmailException{
        if (!email.endsWith("@abc.com")){
            throw new EmailException("Email không hợp lệ");
        }
        return true;
    }
    
    public static Employee getEmployee(String line){
        String[] features = line.split(", ");
        String[] values = new String[features.length];
        for (int i = 0; i < features.length; ++i){
            values[i] = features[i].split("=")[1];
        }
        Employee e;
        if (Integer.parseInt(values[5]) == 0){
            e = new Experience(values[0], values[1], values[2], values[3], values[4], Integer.parseInt(values[6]), Integer.parseInt(values[7]), values[8]);
            return e;
        }
        else if (Integer.parseInt(values[5]) == 1){
            e = new Fresher(values[0], values[1], values[2], values[3], values[4], Integer.parseInt(values[6]), values[7], values[8], values[9]);
            return e;
        }
        else{
            e = new Intern(values[0], values[1], values[2], values[3], values[4], Integer.valueOf(values[6]), values[7], Integer.valueOf(values[8]), values[9]);
            return e;
        }
    }
}
