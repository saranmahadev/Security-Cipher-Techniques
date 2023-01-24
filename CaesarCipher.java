import java.util.Scanner;

public class CaesarCipher {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a message: ");
        String message = input.nextLine();
        System.out.print("Enter a key: ");
        int key = input.nextInt();
        String encryptedMessage = encrypt(message, key);
        System.out.println("Encrypted message: " + encryptedMessage);
        String decryptedMessage = decrypt(encryptedMessage, key);
        System.out.println("Decrypted message: " + decryptedMessage);        
        input.close();
    }
    
    public static String encrypt(String message, int key) {
        String encryptedMessage = "";
        for (int i = 0; i < message.length(); i++) {            
            char ch = message.charAt(i);          
            if (ch >= 'A' && ch <= 'Z') {
                ch = (char)(ch + 32);
            }
            if (ch >= 'a' && ch <= 'z') {
                ch = (char)(ch + key);
                if (ch > 'z') {
                    ch = (char)(ch - 'z' + 'a' - 1);
                }
                encryptedMessage += ch;
            } else {
                encryptedMessage += ch;
            }
        }
        return encryptedMessage;
    }
    
    public static String decrypt(String encryptedMessage, int key) {
        String decryptedMessage = "";
        for (int i = 0; i < encryptedMessage.length(); i++) {
            char ch = encryptedMessage.charAt(i);
            if (ch >= 'A' && ch <= 'Z') {
                ch = (char)(ch + 32);                
            }
            if (ch >= 'a' && ch <= 'z') {
                ch = (char)(ch - key);
                if (ch < 'a') {
                    ch = (char)(ch + 'z' - 'a' + 1);
                }
                decryptedMessage += ch;
            } else {
                decryptedMessage += ch;
            }
        }
        return decryptedMessage;
    }
}