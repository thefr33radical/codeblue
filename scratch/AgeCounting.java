import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.net.HttpURLConnection;
import java.net.URL;


public class AgeCounting {
    public static void main(String[] args) {
        try {
            // Step 1: Send GET request to the API
            String apiUrl = "https://coderbyte.com/api/challenges/json/age-counting";
            HttpURLConnection connection = (HttpURLConnection) new URL(apiUrl).openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Content-Type", "application/json");

            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
            
            // Step 2: Parse the JSON response
            
            String data = response.toString();
            

            // Step 3: Count items with age >= 50
            String[] items = data.split(", ");
            int count = 0;

            for (String item : items) {
                
                String[] parts = item.split(" ");
                // String keyPart = parts[0]; // key=STRING
                // String agePart = parts[1]; // age=INTEGER

                if(item.startsWith("ag"))
                {
                    try{

                    
                int age = Integer.parseInt(item.split("=")[1].trim());
    
                if (age >= 50) {
                    count++;
                }
            }
                
                catch (Exception e)
                {
                
                }

               
            }
            }

        

            // Step 4: Combine result with challenge token and reverse it
            String challengeToken = "ej71vsoi"; // Use your challenge token here
            String output = count + ":" + challengeToken;
            String reversedOutput = new StringBuilder(output).reverse().toString();

            // Print the final reversed output
            System.out.println(reversedOutput);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
