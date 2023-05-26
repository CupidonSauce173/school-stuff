import java.util.Scanner;

/**
 * Fichier : ES.java
 * Descr.  : Librairies pour les lectures au clavier et l'affichage à l'écran.
 * Auteur  : Pierre Coutu
 */
public class ES {
    // ================== attribut statique ======================
    private static Scanner entree = null;
    // ================== méthodes statiques ======================

    /**
     * Méthode qui permet d'afficher un message à l'écran
     */
    public static void afficher(String message) {
        System.out.println(message);
    }

    /**
     * Méthode qui permet de lire un nombre entier au clavier.
     */
    public static int lireEntier(String message) {
        int valeurSaisie = 0;
        if (entree == null) {
            entree = new Scanner(System.in);
        }
        afficher(message);
        valeurSaisie = Integer.parseInt(entree.nextLine());
        return valeurSaisie;
    }

    /**
     * Méthode qui permet de lire un nombre réel au clavier.
     */
    public static double lireReel(String message) {
        double valeurSaisie = 0.0;
        if (entree == null) {
            entree = new Scanner(System.in);
        }
        afficher(message);
        valeurSaisie = Double.parseDouble(entree.nextLine());
        return valeurSaisie;
    }

    /**
     * Méthode qui permet de lire une ligne de texte au clavier.
     */
    public static String lireChaine(String message) {
        String valeurSaisie = "";
        if (entree == null) {
            entree = new Scanner(System.in);
        }
        afficher(message);
        valeurSaisie = entree.nextLine();
        return valeurSaisie;
    }

    /**
     * Méthode qui permet de lire un caractère au clavier.
     */
    public static char lireCaractere(String message) {
        char valeurSaisie = ' ';
        if (entree == null) {
            entree = new Scanner(System.in);
        }
        afficher(message);
        valeurSaisie = entree.nextLine().charAt(0);
        return valeurSaisie;
    }


}
