package com.company.Furnitures;

import com.company.Items.Item;

import java.util.HashMap;

public class Furniture implements Cloneable {
    int id;
    String name;
    int size;
    HashMap<Integer, Item> itemHashMap = new HashMap<>();
    boolean breakable;
    String description;
    int randomId;

    /**
     * Creates a new Furniture object.
     *
     * @param id          The ID of the Furniture object.
     * @param name        The name of the Furniture object.
     * @param size        The size of the Furniture object.
     * @param breakable   The breakable state of the Furniture object.
     * @param description The description of the Furniture object.
     */
    public Furniture(int id, String name, int size, boolean breakable, String description) {
        this.id = id;
        this.name = name;
        this.size = size;
        this.breakable = breakable;
        this.description = description;
    }

    private Furniture() {}

    /**
     * Returns the ID of the furniture.
     *
     * @return The ID of the furniture.
     */
    public int getId() {
        return this.id;
    }

    /**
     * Returns a random ID for the furniture.
     *
     * @return A random ID for the furniture.
     */
    public int getRandomId() {
        return this.randomId;
    }


    /**
     * Sets a random ID for the furniture.
     *
     * @param randomId The random ID to set for the furniture.
     */
    public void setRandomId(int randomId) {
        this.randomId = randomId;
    }

    /**
     * Returns the name of the furniture.
     *
     * @return The name of the furniture.
     */
    public String getName() {
        return this.name;
    }

    /**
     * Returns the size of the furniture.
     *
     * @return The size of the furniture.
     */
    public int getSize() {
        return this.size;
    }

    /**
     * Returns the description of the furniture.
     *
     * @return The description of the furniture.
     */
    public String getDescription() {
        return this.description;
    }

    /**
     * Returns whether the furniture can be broken or not.
     *
     * @return True if the furniture can be broken, false otherwise.
     */
    public boolean isBreakable() {
        return this.breakable;
    }

    /**
     * Sets whether the furniture can be broken or not.
     *
     * @param value True if the furniture can be broken, false otherwise.
     */
    public void setBreakable(boolean value) {
        this.breakable = value;
    }

    /**
     * Returns a HashMap of the items contained in the furniture.
     *
     * @return A HashMap of the items contained in the furniture.
     */
    public HashMap<Integer, Item> getItems() {
        return this.itemHashMap;
    }

    /**
     * Adds an item to the furniture.
     *
     * @param item The item to add to the furniture.
     */
    public void add(Item item) {
        this.itemHashMap.put(item.getRandomId(), item);
    }

    /**
     * Removes an item from the furniture.
     *
     * @param item The item to remove from the furniture.
     */
    public void remove(Item item) {
        this.itemHashMap.remove(item.hashCode(), item);
    }

    /**
     * Clones the furniture.
     *
     * @return A clone of the furniture.
     */
    @Override
    public Furniture clone() {
        try {
            Furniture furniture = (Furniture) super.clone();
            furniture.itemHashMap = new HashMap<>();
            return furniture;

        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}
