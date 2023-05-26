package com.company.Entities;

import com.company.Items.Durable;
import com.company.Items.Item;
import com.company.Room;
import com.company.Utils;

public class Entity {
    int id;
    int health;
    Item rightHandItem;
    Item leftHandItem;
    String username;
    Room room;

    /**
     * Constructor for Entity class.
     *
     * @param id          The ID of the Entity.
     * @param health      The health of the Entity.
     * @param username    The username of the Entity.
     * @param room        The room the Entity is currently in.
     */
    public Entity(int id, int health, String username, Room room) {
        this.id = id;
        this.health = health;
        this.username = username;
        this.room = room;
    }

    /**
     * Get the ID of the Entity.
     *
     * @return The ID of the Entity.
     */
    public int getId() {
        return this.id;
    }

    /**
     * Get the health of the Entity.
     *
     * @return The health of the Entity.
     */
    public int getHealth() {
        return this.health;
    }

    /**
     * Set the health of the Entity.
     *
     * @param health The health to set for the Entity.
     */
    public void setHealth(int health) {
        this.health = health;
    }

    /**
     * Get the username of the Entity.
     *
     * @return The username of the Entity.
     */
    public String getUsername() {
        return this.username;
    }

    /**
     * Get the Item in the Entity's right hand.
     *
     * @return The Item in the Entity's right hand.
     */
    public Item getRightHandItem() {return this.rightHandItem;}

    /**
     * Set the Item in the Entity's right hand.
     *
     * @param rightHandItem The Item to set in the Entity's right hand.
     */
    public void setRightHandItem(Item rightHandItem) {
        this.rightHandItem = rightHandItem;
    }

    /**
     * Get the Item in the Entity's left hand.
     *
     * @return The Item in the Entity's left hand.
     */
    public Item getLeftHandItem() {
        return this.leftHandItem;
    }

    /**
     * Set the Item in the Entity's left hand.
     *
     * @param leftHandItem The Item to set in the Entity's left hand.
     */
    public void setLeftHandItem(Item leftHandItem) {
        this.leftHandItem = leftHandItem;
    }

    /**
     * Get the Room where the Entity is currently located.
     *
     * @return The Room where the Entity is currently located.
     */
    public Room getRoom() {
        return this.room;
    }

    /**
     * Set the Room where the Entity is currently located.
     *
     * @param room The Room to set as the Entity's current location.
     */
    public void setRoom(Room room) {
        this.room = room;
    }

    /**
     * Increase the health of the Entity.
     *
     * @param health The amount to increase the health of the Entity by.
     */
    public void addHealth(int health) {
        this.health += health;
    }


    /**
     * Attack another Entity.
     *
     * @param entity The Entity to attack.
     */
    public void attack(Entity entity) {
        if (this.rightHandItem instanceof Durable) {
            entity.applyDamage(((Durable) this.rightHandItem).getDamage());
            ((Durable) this.rightHandItem).addDamage(1);
        } else if (this.leftHandItem instanceof Durable) {
            entity.applyDamage(((Durable) this.leftHandItem).getDamage());
            ((Durable) this.leftHandItem).addDamage(1);
        } else {
            Utils.writeSlowMessage("Attaquer avec quoi...?");
        }
    }

    /**
     * Apply damage to the Entity.
     *
     * @param damageCount The amount of damage to apply to the Entity.
     */
    public void applyDamage(int damageCount) {
        if (damageCount >= health) {
            this.kill();
        } else this.health -= damageCount;
    }


    /**
     * Kill the Entity.
     */
    public void kill() {

    }
}
