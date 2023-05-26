package com.company.Items;

import com.company.Utils;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Random;
import java.util.Scanner;

public class ItemFactory {
    private final HashMap<Integer, Item> itemHashMap = new HashMap<>();
    private final Random random = new Random();

    public Item getRandomItem() {
        Item randomItem = this.getItem(
                this.random.nextInt(1000, 1000 + (this.getItems().size() - 1)));
        if(randomItem == null) {
            return null;
        }
        return randomItem.clone();
    }

    /**
     * Get an item by its ID.
     *
     * @param itemId The ID of the item.
     * @return The item object with the specified ID, or null if it does not exist.
     */
    public Item getItem(int itemId) {
        return this.itemHashMap.get(itemId);
    }

    /**
     * Get all registered items.
     *
     * @return A HashMap of all registered items, where the keys are item IDs and the values are item objects.
     */
    public HashMap<Integer, Item> getItems() {
        return this.itemHashMap;
    }

    /**
     * Register default items from a JSON file.
     */
    public void registerDefaults() {
        try {
            InputStream inputStream = ItemFactory.class.getResourceAsStream("/items.json");
            if (inputStream == null) throw new Exception("Problem while registering the default items.");
            Scanner scanner = new Scanner(inputStream, StandardCharsets.UTF_8);
            String json = scanner.useDelimiter("\\A").next();
            JSONArray itemsArray = new JSONArray(json);

            // Iterate over the elements in the array
            for (int i = 0; i < itemsArray.length(); i++) {
                JSONObject item = itemsArray.getJSONObject(i);
                int id = item.getInt("id");
                String name = item.getString("name");
                String description = item.getString("description");
                if (item.has("durable")) {
                    Durable itemToRegister = new Durable(id, name, description, Utils.getNextRandomId(), item.getInt("baseActions"));
                    if (item.has("damage")) {
                        itemToRegister.setDamage(item.getInt("damage"));
                    }
                    this.register(itemToRegister);
                } else {
                    Item itemToRegister = new Item(id, name, description, Utils.getNextRandomId());
                    this.register(itemToRegister);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Register an item.
     *
     * @param item The item to register.
     */
    public void register(Item item) {
        this.itemHashMap.put(item.getId(), item);
    }

    /**
     * Register a durable item.
     *
     * @param item The durable item to register.
     */
    public void register(Durable item) {
        this.itemHashMap.put(item.getId(), item);
    }

    /**
     * Unregister an item.
     *
     * @param item The item to unregister.
     */
    public void unregister(Item item) {
        this.itemHashMap.remove(item.getId());
    }

    /**
     * Unregister a durable item.
     *
     * @param item The durable item to unregister.
     */
    public void unregister(Durable item) {
        this.itemHashMap.remove(item.getId());
    }
}
