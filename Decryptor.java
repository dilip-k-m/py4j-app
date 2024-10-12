import com.google.gson.Gson;
import java.util.HashMap;
import java.util.Map;

public class Decryptor {
    public static void main(String[] args) {
        String encryptedPayload = args[0];
        String decryptedData = decryptPayload(encryptedPayload);
        System.out.println(new Gson().toJson(decryptedData));
    }

    private static Map<String, Object> decryptPayload(String encryptedPayload) {
        // Decryption logic here
        Map<String, Object> decryptedData = new HashMap<>();
        decryptedData.put("key", "decrypted_value"); // Sample data
        return decryptedData;
    }
}
