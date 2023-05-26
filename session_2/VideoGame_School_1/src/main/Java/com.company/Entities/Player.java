package com.company.Entities;

import com.company.Items.Item;
import com.company.Room;
import com.company.Utils;

public class Player extends Entity {

    /**
     * Constructor for Player class
     *
     * @param id          unique identifier for player
     * @param health      player's initial health value
     * @param username    player's username
     * @param room        the room where the player is located
     */
    public Player(int id, int health, String username, Room room) {
        super(id, health, username, room);
    }

    /**
     * Allows the player to pick up an item
     *
     * @param item the item that the player wants to pick up
     */
    public void pick(Item item) {
        Utils.writeSlowMessage("Okay, je vais prendre " + item.getName() + "\n");
        if (this.leftHandItem != null && this.rightHandItem != null) {
            Utils.writeSlowMessage("Oh non, mes mains sont pleines.. \n");
        } else {
            if (this.rightHandItem == null) {
                this.rightHandItem = item;
            } else {
                this.leftHandItem = item;
            }
        }
    }

    /**
     * Allows the player to drop an item
     *
     * @param hand the hand from which the player wants to drop the item ("left" or "right")
     */
    public void drop(String hand) {
        Item dropped;
        if (hand.equals("left")) {
            dropped = this.leftHandItem;
            this.leftHandItem = null;
        } else {
            dropped = this.rightHandItem;
            this.rightHandItem = null;
        }
        Utils.writeSlowMessage("Okay, j'ai déposé " + dropped.getName() + "\n");
    }

    /**
     * Causes the player to die and terminates the program
     */

    public void kill() {
        Utils.writeSlowMessage("Vous êtes mort.. Il restait tellement de chose à découvrire. Dommage.");
        System.exit(0);
    } // overwrite of the Entity method.

}
