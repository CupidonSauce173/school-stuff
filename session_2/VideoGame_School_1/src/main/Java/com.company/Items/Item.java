package com.company.Items;

public class Item implements Cloneable{
    int id;
    String name;
    String description;
    int randomId;

    /**
     * Constructor for an Item object.
     *
     * @param id          The ID of the item.
     * @param name        The name of the item.
     * @param description The description of the item.
     * @param randomId    The random ID of the item.
     */
    public Item(int id, String name, String description, int randomId) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.randomId = randomId;
    }

    /**
     * Get the ID of the item.
     * <p>
     * * @return The ID of the item.
     */
    public int getId() {
        return this.id;
    }

    /**
     * Get the random ID of the item.
     *
     * @return The random ID of the item.
     */
    public int getRandomId() {
        return this.randomId;
    }

    /**
     * Get the name of the item.
     *
     * @return The name of the item.
     */
    public String getName() {
        return this.name;
    }

    /**
     * Set the name of the item.
     *
     * @param name The new name of the item.
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Get the description of the item.
     *
     * @return The description of the item.
     */
    public String getDescription() {
        return this.description;
    }

    /**
     * Set the description of the item.
     *
     * @param description The new description of the item.
     */
    public void setDescription(String description) {
        this.description = description;
    }

    @Override
    public Item clone() {
        try {
            return (Item) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}
