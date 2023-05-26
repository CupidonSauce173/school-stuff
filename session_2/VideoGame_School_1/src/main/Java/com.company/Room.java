package com.company;

import com.company.Furnitures.Furniture;
import com.company.Items.Item;

import java.util.HashMap;

public class Room {
    int id;
    int visibility;
    int size;
    String description;

    HashMap<Integer, Room> doors = new HashMap<>();
    HashMap<Integer, Item> itemHashMap = new HashMap<>();
    HashMap<Integer, Furniture> furnitureHashMap = new HashMap<>();

    /**
     * Constructor method for the Room object.
     *
     * @param id   of the room
     * @param size of the room
     */
    public Room(int id, int size) {
        this.id = id;
        this.size = size;
    }

    public HashMap<Integer, Item> getItems() {
        return this.itemHashMap;
    }

    public HashMap<Integer, Furniture> getFurnitures() {
        return this.furnitureHashMap;
    }

    /**
     * Get the ID of the room.
     * <p>
     * * @return The ID of the room.
     */
    public int getId() {
        return this.id;
    }

    /**
     * Get the size of the room.
     * <p>
     * * @return The size of the room.
     */
    public int getSize() {
        return this.size;
    }

    /**
     * Get the visibility of the room.
     * <p>
     * * @return The visibility of the room.
     */
    public int getVisibility() {
        return this.visibility;
    }

    /**
     * Set the visibility of the room.
     *
     * @param visibility The new visibility of the room.
     */
    public void setVisibility(int visibility) {
        this.visibility = visibility;
    }

    /**
     * Get the description of the room.
     * <p>
     * * @return The description of the room.
     */
    public String getDescription() {
        return this.description;
    }

    /**
     * Set the description of the room.
     *
     * @param description The new description of the room.
     */
    public void setDescription(String description) {
        this.description = description;
    }

    /**
     * Set the door of the room with the specified ID to lead to the specified room.
     *
     * @param id   The ID of the door.
     * @param room The room that the door leads to.
     */
    public void setDoor(int id, Room room) {
        doors.put(id, room);
    }

    /**
     * Get the room that the door with the specified ID leads to.
     *
     * @param index The ID of the door.
     * @return The room that the door leads to.
     */
    public Room getDoorTarget(int index) {
        return this.doors.get(index);
    }

    /**
     * Get a HashMap of all the doors in the room and the rooms they lead to.
     *
     * @return A HashMap of all the doors in the room and the rooms they lead to.
     */
    public HashMap<Integer, Room> getDoorTargets() {
        return this.doors;
    }
}
