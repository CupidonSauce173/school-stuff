package com.company.Entities;

import java.util.HashMap;
import java.util.Objects;

public class EntityFactory {
    HashMap<Integer, Entity> entityHashMap = new HashMap<>();

    /**
     * Returns a HashMap containing all the entities in the room
     *
     * @return a HashMap containing all the entities in the room
     */
    public HashMap<Integer, Entity> getEntities() {
        return this.entityHashMap;
    }

    /**
     * Returns the entity with the specified id
     *
     * @param id the unique identifier of the entity
     * @return the entity with the specified id, or null if no entity is found
     */
    public Entity getEntity(int id) {
        return this.entityHashMap.get(id);
    }

    /**
     * Returns the entity with the specified username
     *
     * @param username the username of the entity
     * @return the entity with the specified username, or null if no entity is found
     */
    public Entity getEntity(String username) {
        for (Entity entity : this.entityHashMap.values()) {
            if (Objects.equals(entity.getUsername(), username)) return entity;
        }
        return null;
    }

    /**
     * Registers a new entity in the room
     *
     * @param entity the entity to register
     */
    public void register(Entity entity) {
        this.entityHashMap.put(entity.getId(), entity);
    }

    /**
     * Unregisters an entity from the room
     *
     * @param entity the entity to unregister
     */
    public void unregister(Entity entity) {
        this.entityHashMap.remove(entity.getId());
    }

    /**
     * Unregisters an entity with the specified id from the room
     *
     * @param entityId the id of the entity to unregister
     */
    public void unregister(int entityId) {
        this.entityHashMap.remove(entityId);
    }
}
