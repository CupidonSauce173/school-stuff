package com.company.Items;

public class Durable extends Item {

    protected int actions;
    protected int damage = 0;
    private boolean breakable = true;

    /**
     * Create a new Durable object with the specified parameters.
     *
     * @param id          The ID of the Durable.
     * @param name        The name of the Durable.
     * @param description The description of the Durable.
     * @param randomId    The randomly generated ID of the Durable.
     * @param baseActions The base number of actions of the Durable.
     */
    public Durable(int id, String name, String description, int randomId, int baseActions) {
        super(id, name, description, randomId);
        this.actions = baseActions;
    }

    /**
     * Get the amount of damage the durable item has taken.
     *
     * @return The amount of damage the durable item has taken.
     */
    public int getDamage() {
        return this.damage;
    }

    /**
     * Set the amount of damage the durable item has taken.
     *
     * @param damage The amount of damage to set.
     */
    public void setDamage(int damage) {
        this.damage = damage;
    }

    /**
     * Get the remaining number of actions the durable item can take.
     *
     * @return The remaining number of actions.
     */
    public int getRemainingActions() {
        return this.actions;
    }

    /**
     * Check if the durable item can be broken.
     *
     * @return true if the item can be broken, false otherwise.
     */
    public boolean isBreakable() {
        return this.breakable;
    }

    /**
     * Set the breakable state of the durable item.
     *
     * @param value The new breakable state.
     */
    public void setBreakable(boolean value) {
        this.breakable = value;
    }

    /**
     * Set the number of actions the durable item can take.
     *
     * @param actions The number of actions to set.
     */
    public void setActions(int actions) {
        this.actions = actions;
    }

    /**
     * Add damage to the durable item.
     *
     * @param value The amount of damage to add.
     */
    public void addDamage(int value) {
        if (value > this.actions || value >= (this.actions - this.damage)) {
            this.destroy();
        } else {
            this.damage += value;
            this.actions -= value;
        }
    }

    /**
     * Remove damage to the durable item.
     *
     * @param value The amount of damage to add.
     */
    public void removeDamage(int value) {
        if (value >= this.damage) this.damage = 0;
        else {
            this.damage -= value;
        }
    }

    /**
     * Destroys the item
     * <p>
     * NOT IMPLEMENTED YET
     */
    public void destroy() {

    }
}
