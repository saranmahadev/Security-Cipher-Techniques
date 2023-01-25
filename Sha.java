import java.security.MessageDigest;
import java.util.Scanner;

public class Sha {
    public static void main(String[] args) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA1");
            System.out.println("Algorithm: " + md.getAlgorithm());
            System.out.println("Provider: " + md.getProvider());
            
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter a string: ");
            String input = sc.nextLine();            
            md.update(input.getBytes());
            byte[] output = md.digest();
            System.out.println("SHA1 of \"" + input + "\": " + bytesToHex(output));
            sc.close();
            
        } catch (Exception e) {
            System.out.println("Exception: " + e);
        }
    }
    
    private static String bytesToHex(byte[] b) {
        StringBuffer result = new StringBuffer();
        for (int i = 0; i < b.length; i++) {
            result.append(Integer.toString((b[i] & 0xff) + 0x100, 16).substring(1));
        }
        return result.toString();
    }
}
