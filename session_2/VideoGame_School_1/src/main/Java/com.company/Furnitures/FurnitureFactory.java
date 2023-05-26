package com.company.Furnitures;

import com.company.Items.ItemFactory;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Random;
import java.util.Scanner;

public class FurnitureFactory {

    HashMap<Integer, Furniture> furnitureHashMap = new HashMap<>();
    private final Random random = new Random();

    public Furniture getRandomFurniture() {
        Furniture randomFurniture = this.getFurnitures().get(
                this.random.nextInt(2000, 2000 + (this.getFurnitures().size() - 1)));
        return randomFurniture.clone();
    }

    /**
     * Get furniture by its ID.
     *
     * @param furnitureId The ID of the furniture.
     * @return The furniture object with the specified ID, or null if it does not exist.
     */
    public Furniture getFurniture(int furnitureId) {
        return this.furnitureHashMap.get(furnitureId).clone();
    }

    /**
     * Get all furniture in the world.
     *
     * @return A HashMap containing all furniture objects in the world.
     */
    public HashMap<Integer, Furniture> getFurnitures() {
        return this.furnitureHashMap;
    }

    /**
     * Register the default furniture objects.
     */
    public void registerDefaults() {
        try {
            InputStream inputStream = ItemFactory.class.getResourceAsStream("/furnitures.json");
            if (inputStream == null) throw new Exception("Problem while registering the default furnitures.");
            Scanner scanner = new Scanner(inputStream, StandardCharsets.UTF_8.name());
            String json = scanner.useDelimiter("\\A").next();
            JSONArray furnitureArray = new JSONArray(json);

            // Iterate over the elements in the array
            for (int i = 0; i < furnitureArray.length(); i++) {
                JSONObject furniture = furnitureArray.getJSONObject(i);
                Furniture furnitureToRegister = new Furniture(
                        furniture.getInt("id"),
                        furniture.getString("name"),
                        furniture.getInt("size"),
                        furniture.getBoolean("breakable"),
                        furniture.getString("description")
                );
                this.register(furnitureToRegister);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Register a furniture object.
     *
     * @param furniture The furniture object to register.
     */
    public void register(Furniture furniture) {
        this.furnitureHashMap.put(furniture.getId(), furniture);
    }
}
