package com.company;

import com.company.Furnitures.Furniture;
import com.company.Furnitures.FurnitureFactory;
import com.company.Items.Item;
import com.company.Items.ItemFactory;

import java.util.HashMap;
import java.util.Random;

public class Utils {

    static Random random = new Random();

    public static int getNextRandomId() {
        return random.nextInt(0, 99999);
    }

    /**
     * Will write a message by stopping the thread for between 0 and 50 miliseconds.
     *
     * @param message to display.
     */
    public static void writeSlowMessage(String message) {
        Random random = new Random();
        for (int i = 0; i < message.length(); i++) {
            System.out.print(message.charAt(i));
            try {
                Thread.sleep(random.nextInt(0, 50));
            } catch (InterruptedException e) {
                System.out.println("InterruptedException: " + e.getMessage());
            }
        }
    }

    /**
     * Will generate a set of rooms and populate them with furniture's and items.
     *
     * @param itemFactory      of the application.
     * @param furnitureFactory of the application.
     * @return the HashMap of the rooms.
     */
    public static HashMap<Integer, Room> generateRooms(ItemFactory itemFactory, FurnitureFactory furnitureFactory) {
        HashMap<Integer, Room> roomHashMap = new HashMap<>();
        Random random = new Random();
        int roomsToGenerate = random.nextInt(10, 30);

        // generating the room objects
        for (int i = 0; i < roomsToGenerate; i++) {
            Room room = new Room(i, random.nextInt(5, 30));
            roomHashMap.put(room.getId(), room);
        }

        // generating the doors
        for (int i = 0; i < roomsToGenerate; i++) {
            Room room = roomHashMap.get(i);
            room.setVisibility(random.nextInt(1, 5));
            int doorsToGenerate = random.nextInt(1, 3);
            for (int k = 0; k < doorsToGenerate; k++) {
                Room target = roomHashMap.get(random.nextInt(0, roomsToGenerate - 1));
                while (target.getId() == room.getId()) {
                    target = roomHashMap.get(random.nextInt(0, roomsToGenerate - 1));
                }
                room.setDoor(k, target);
            }
        }

        // generating the furniture's
        for (int i = 0; i < roomsToGenerate; i++) {
            Room room = roomHashMap.get(i);
            int remainingSize = room.getSize();
            while (remainingSize > 0) {
                Furniture randomFurniture = furnitureFactory.getRandomFurniture();
                if (randomFurniture != null) {
                    randomFurniture.setRandomId(Utils.getNextRandomId());
                    room.getFurnitures().put(randomFurniture.getId(), randomFurniture);
                    remainingSize -= randomFurniture.getSize();
                }
            }
        }

        // generating the items
        for (int i = 0; i < roomsToGenerate; i++) {
            Room room = roomHashMap.get(i);
            int size = room.getSize();
            int toGen;
            if (size > 29) { // 10 - 12 items to spawn
                toGen = random.nextInt(10, 12);
            } else if (size > 20) { // 7 - 9 items to spawn
                toGen = random.nextInt(7, 9);
            } else if (size > 10) { // 4 - 6 items to spawn
                toGen = random.nextInt(4, 6);
            } else { // 0 - 3 items to spawn
                toGen = random.nextInt(0, 3);
            }
            for (int k = 0; k < toGen; k++) {
                Item item = itemFactory.getRandomItem();
                if (item != null) {
                    room.getItems().put(item.getId(), item);
                } else k--;
            }
            // generating items in furniture's
            for (Furniture furniture : room.getFurnitures().values()) {
                for (int k = 0; k < furniture.getSize(); k++) {
                    Item item = itemFactory.getRandomItem();
                    if (item != null) {
                        furniture.add(item);
                    }
                }
            }
        }

        // generating a description for each room
        for (int i = 0; i < roomsToGenerate; i++) {
            StringBuilder description = new StringBuilder();
            Room room = roomHashMap.get(i);
            switch (room.getVisibility()) {
                case 0 -> description.append("Je ne vois rien... ");
                case 1 -> description.append("Je vois presque rien! ");
                case 2 -> description.append("Enfin, un peu de lumière.. ");
                case 3 -> description.append("C'est un peu sombre, ");
                case 4 -> description.append("Bon, une nouvelle salle.. ");
                case 5 -> description.append("Une salle bien éclairé! ");
            }
            int size = room.getSize();
            if (room.getVisibility() < 3) {
                description.append("Agh.. Je ne pourrais dire à quel point cette salle est grande. ");
            } else {
                if (size > 29) description.append("Wow... Quelle grande salle! ");
                else if (size > 20) description.append("Beaucoup d'exploration à faire ici.. ");
                else if (size > 10)
                    description.append("Agh.. J'espère qu'il n'y aura pas d'ennemie, c'est un peu petit ici. ");
                else description.append("C'est vraiment petit ici. ");
            }
            room.setDescription(description.toString());
        }
        return roomHashMap;
    }
}
