package com.company;

import com.company.Entities.Entity;
import com.company.Entities.EntityFactory;
import com.company.Entities.Player;
import com.company.Furnitures.Furniture;
import com.company.Furnitures.FurnitureFactory;
import com.company.Items.Durable;
import com.company.Items.Item;
import com.company.Items.ItemFactory;

import java.util.HashMap;
import java.util.Random;
import java.util.Scanner;

public class Loader {

    public static void main(String[] args) {
        System.out.println("-- PROBLÈMES CONNUS --");
        System.out.println("- Trop d'items spawn dans les meubles.");
        System.out.println("- Problème d'affichage de la vie quand un monstre attaque.\n\n\n");

        Random random = new Random();

        ItemFactory itemFactory = new ItemFactory();
        EntityFactory entityFactory = new EntityFactory();
        FurnitureFactory furnitureFactory = new FurnitureFactory();

        itemFactory.registerDefaults();
        furnitureFactory.registerDefaults();

        HashMap<Integer, Room> roomHashMap = Utils.generateRooms(itemFactory, furnitureFactory);

        Scanner scanner = new Scanner(System.in);
        String userInput = "";

        Player player = new Player(1, 100, "Joueur", roomHashMap.get(0));
        Entity gardien_du_donjon_1 = new Entity(2, 50, "Gardien du donjon", roomHashMap.get(4));
        Entity gardien_du_donjon_2 = new Entity(3, 50, "Gardien du donjon", roomHashMap.get(6));
        Entity boss = new Entity(4, 100, "Gardien Sacré", roomHashMap.get(roomHashMap.size() - 1));

        // equip the monsters
        gardien_du_donjon_1.setLeftHandItem(itemFactory.getItem(1007)); // lance
        gardien_du_donjon_2.setLeftHandItem(itemFactory.getItem(1007)); // lance
        boss.setLeftHandItem(itemFactory.getItem(1008)); // épée en fer

        // spawn them in random rooms
        gardien_du_donjon_1.setRoom(roomHashMap.get(random.nextInt(0, roomHashMap.size() - 1)));
        gardien_du_donjon_2.setRoom(roomHashMap.get(random.nextInt(0, roomHashMap.size() - 1)));
        boss.setRoom(roomHashMap.get(random.nextInt(0, roomHashMap.size() - 1)));

        // register them in the entityFactory
        entityFactory.register(gardien_du_donjon_1);
        entityFactory.register(gardien_du_donjon_2);
        entityFactory.register(boss);
        entityFactory.register(player);

        player.setRoom(roomHashMap.get(0));
        Utils.writeSlowMessage(
                """
                        Bienvenue, aventuriers intrépides, dans un monde de magie et de ténèbres.\s
                        Vous avez été appelés dans mon château pour une mission périlleuse :
                        survivre aussi longtemps que possible dans des salles magiques remplies de
                        monstres terrifiants. Votre objectif est simple : éliminer les ennemis un par 
                        un jusqu'à ce qu'il n'en reste plus.

                        Cependant, cela ne sera pas facile. Les monstres sont vicieux, rusés et dangereux.
                        Vous devrez utiliser toutes vos compétences, votre équipement et votre intelligence
                        pour les vaincre. Explorez chaque salle avec soin, car vous ne savez jamais où se cachent
                        les ennemis.

                        Le temps est votre ennemi, car plus vous passez de temps dans le château, plus les monstres
                        deviendront forts et agressifs. Soyez prêts à affronter des défis de plus en plus difficiles
                        à mesure que vous progressez.

                        Soyez courageux et rusé, et montrez que vous êtes le héros de cette aventure. Survivez aussi
                        longtemps que possible dans ces salles magiques remplies de monstres terrifiants, jusqu'à ce que
                        vous éliminiez le dernier ennemi. Alors, êtes-vous prêt à relever le défi et à devenir le héros
                        de cette aventure fantastique ?
                        
                        Vous vous réveillez.....
                        
                        """);
        Utils.writeSlowMessage(roomHashMap.get(0).getDescription() + "\n");
        Furniture lastFurnitureChecked = null;
        while (!userInput.equals("/stop")) {
            // ENTITY CHECK
            for (Entity entity : entityFactory.getEntities().values()) {
                if (entity.getHealth() <= 0) {
                    entityFactory.unregister(entity);
                    continue;
                }
                if (entity instanceof Player) continue;
                if (entity.getRoom() == player.getRoom())
                    Utils.writeSlowMessage("ALERT - Un monstre est dans la même salle que vous!\n");
            }

            // PLAYER TURN
            System.out.print("Joueur:> ");
            userInput = scanner.nextLine().toLowerCase();
            Room room = player.getRoom();
            int roomVisibility = room.getVisibility();
            if ((player.getLeftHandItem() != null && player.getLeftHandItem().getName().contains("lanterne")) ||
                    (player.getRightHandItem() != null && player.getRightHandItem().getName().contains("lanterne"))) {
                roomVisibility += 5;
            } else {
                if ((player.getLeftHandItem() != null && player.getLeftHandItem().getName().contains("lumineuse")) ||
                        (player.getRightHandItem() != null && player.getRightHandItem().getName().contains("lumineuse"))) {
                    roomVisibility += 2;
                }
            }

            if (userInput.contains("aide")) {
                Utils.writeSlowMessage("Vous pouvez utiliser quelques mots pour faire des actions. \n");
                Utils.writeSlowMessage("lire, déposer <droite, gauche>, prend, prendre\n");
                Utils.writeSlowMessage("attaque, attaquer, boire, examine, examiner\n");
                Utils.writeSlowMessage("ouvrire, ouvre\n");
                Utils.writeSlowMessage("Note importante, pour intéragir avec des items, vous devez spécifier\n sont numéro afficher avant.\n");
            } else if (userInput.contains("lire")) {
                if(player.getRightHandItem() != null) {
                    if (player.getRightHandItem().getName().contains("livre")) {
                        Utils.writeSlowMessage(player.getRightHandItem().getDescription() + "\n");
                    }
                }
                if(player.getLeftHandItem() != null) {
                    if (player.getLeftHandItem().getName().contains("livre")) {
                        Utils.writeSlowMessage(player.getLeftHandItem().getDescription() + "\n");
                    }
                }
            } else if (userInput.contains("déposer")) {
                if (userInput.contains("droite")) {
                    room.getItems().put(player.getRightHandItem().getId(), player.getRightHandItem());
                    player.drop("right");
                } else if (userInput.contains("gauche")) {
                    room.getItems().put(player.getLeftHandItem().getId(), player.getLeftHandItem());
                    player.drop("left");
                } else {
                    Utils.writeSlowMessage("Déposer l'item de quelle main?.. \n");
                }
            } else if (userInput.contains("prend") || userInput.contains("prendre")) {
                for (Item item : room.getItems().values()) {
                    if (userInput.contains(String.valueOf(item.getRandomId()))) {
                        player.pick(item);
                        room.getFurnitures().remove(item.getRandomId());
                    }
                }
                if (lastFurnitureChecked == null) continue;
                for (Item item : lastFurnitureChecked.getItems().values()) {
                    if (userInput.contains(String.valueOf(item.getRandomId()))) {
                        player.pick(item);
                        lastFurnitureChecked.getItems().remove(item.getRandomId());
                    }
                }
            } else if (userInput.contains("attaque") || userInput.contains("attaquer")) {
                Utils.writeSlowMessage("Entitées dans la salle: \n");
                for (Entity entity : entityFactory.getEntities().values()) {
                    if (entity.getRoom() == player.getRoom()) {
                        Utils.writeSlowMessage(entity.getId() + " - " + entity.getUsername() + "\n");
                    }
                }
                Utils.writeSlowMessage("Quelle entitée voulez-vous attaquer?\n");
                String target = scanner.nextLine().toLowerCase();
                for (Entity entity : entityFactory.getEntities().values()) {
                    if (entity.getRoom() == player.getRoom() && target.contains(String.valueOf(entity.getId()))) {
                        Utils.writeSlowMessage("ALERT - Vous attaquez " + entity.getUsername() + "\n");
                        player.attack(entity);
                    }
                }
            } else if (userInput.contains("boire")) {
                if (player.getLeftHandItem().getName().contains("potion")) {
                    if (player.getLeftHandItem().getName().contains("vie")) {
                        String hp = player.getLeftHandItem().getDescription().replaceAll("\\D+", "");
                        player.addHealth(Integer.parseInt(hp));
                        player.setLeftHandItem(null);
                        Utils.writeSlowMessage("Miam.. +" + hp + "/hp");
                    } else if (player.getRightHandItem().getName().contains("vie")) {
                        String hp = player.getRightHandItem().getDescription().replaceAll("\\D+", "");
                        player.addHealth(Integer.parseInt(hp));
                        player.setLeftHandItem(null);
                        Utils.writeSlowMessage("Miam.. +" + hp + "/hp");
                    } else {
                        Utils.writeSlowMessage("Boire quoi?..\n");
                    }
                }
            } else if (userInput.contains("examine") || userInput.contains("chercher") || userInput.contains("examiner")) {
                if (userInput.contains("pièce") || userInput.contains("salle")) {
                    if (roomVisibility < 2) {
                        Utils.writeSlowMessage("Agh.. Je ne peux pas voir grand chose.. \n");
                    } else if (roomVisibility > 2) {
                        Utils.writeSlowMessage("Je vois... \n");
                        for (Furniture furniture : room.getFurnitures().values()) {
                            Utils.writeSlowMessage(furniture.getRandomId() + " - " + furniture.getName() + "\n");
                        }
                        for (Item item : room.getItems().values()) {
                            Utils.writeSlowMessage(item.getRandomId() + " - " + item.getName() + "\n");
                        }
                    }
                } else {
                    for (Furniture furniture : room.getFurnitures().values()) {
                        if (userInput.contains(furniture.getName())) {
                            Utils.writeSlowMessage(furniture.getDescription() + "\n");
                        }
                    }
                }
                Utils.writeSlowMessage("Je vois " + room.getDoorTargets().size() + " portes, elles vont vers les salles\n");
                for (Room nextRoom : room.getDoorTargets().values()) {
                    Utils.writeSlowMessage(" " + nextRoom.getId());
                }
                System.out.println(".");
            } else if (userInput.contains("ouvrir") || userInput.contains("ouvre")) {
                for (Furniture furniture : room.furnitureHashMap.values()) {
                    if (userInput.contains(String.valueOf(furniture.getRandomId()))) {
                        for (Item item : furniture.getItems().values()) {
                            Utils.writeSlowMessage(item.getRandomId() + " - " + item.getName() + "\n");
                        }
                        lastFurnitureChecked = furniture;
                    } else if (userInput.contains("porte")) {
                        for (Room nextRoom : room.getDoorTargets().values()) {
                            if (userInput.contains(String.valueOf(nextRoom.getId()))) {
                                Utils.writeSlowMessage("Je rentre dans la salle " + nextRoom.getId() + "\n");
                                player.setRoom(roomHashMap.get(nextRoom.getId()));
                                Utils.writeSlowMessage(player.getRoom().getDescription() + "\n");
                                break;
                            }
                        }
                        break;
                    }
                }
            }

            // MONSTER TURN
            HashMap<Integer, Entity> entities = entityFactory.getEntities();
            for (Entity entity : entities.values()) {
                if (entity instanceof Player) continue;
                if (entity.getRoom() == player.getRoom()) {
                    // will attack
                    Durable weapon = (Durable) entity.getLeftHandItem();
                    Utils.writeSlowMessage("ALERT - L'entité " + entity.getUsername() + " vous a attaqué! \n");
                    Utils.writeSlowMessage("ALERT - Vous avez perdu " + weapon.getDamage() + "\n");
                    Utils.writeSlowMessage("ALERT - Il vous reste " + player.getHealth() + " \n");
                    entity.attack(player);
                } else {
                    // will go in another room
                    entity.setRoom(entity.getRoom().getDoorTargets().get(random.nextInt(0, entity.getRoom().getDoorTargets().size())));
                }
            }
        }
    }
}
