import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

/**
 * Fichier sur le polymorphisme pour la gestion d'employés.
 */
public class ExerciceChap9C01 {

    public static void main(String[] args) throws IOException {
        ArrayList<Employe> liste = new ArrayList<>();
        Random generateur = new Random();
        DecimalFormat df = new DecimalFormat("#.##");
        lireEmployes(liste, "compagnieABC.txt");

        liste.add(new Employe(123, "Zach", 15.5));
        liste.add(new Employe(124, "Yurrik", 14.5));
        liste.add(new Manager(125, "Xavier", 20, "Info", 100));
        liste.add(new Vendeur(126, "William", 13, 2));
        liste.add(new Benevole(127, "Vicky"));
        liste.add(new Vendeur(128, "Ulf", 17.5, 1));
        liste.add(new Benevole(129, "Théo"));

        for (Employe emp : liste) {
            for (int i = 0; i < 52; i++) {
                double workedHours = Double.parseDouble(df.format(generateur.nextDouble(30, 50)));
                if (emp instanceof Vendeur) {
                    ((Vendeur) emp).setVentesSemaine(Double.parseDouble(df.format(generateur.nextDouble(100, 300))));
                }
                emp.encaisserSalaire(workedHours);
            }
        }

        double totalGivenSalary = 0.0d;
        for (Employe emp : liste) {
            System.out.println(emp);
            totalGivenSalary += emp.salaireAccumule;
            if (emp instanceof Benevole) sauvegarderBenevole((Benevole) emp);
        }
        System.out.printf("Salaire total versé: %,.2f ", totalGivenSalary );
    }

    /**
     * Fonction pour lire et rajouter des employés d'un fichier source.
     *
     * @param uneListe d'employés.
     * @param nomFichier de la source des employés à rajouter.
     */
    public static void lireEmployes(ArrayList<Employe> uneListe, String nomFichier) {
        InputStream inputStream = ExerciceChap9C01.class.getClassLoader().getResourceAsStream(nomFichier);
        assert inputStream != null;
        Scanner scanner = new Scanner(inputStream);
        while (scanner.hasNextLine()) {
            String[] empData = scanner.nextLine().split(":");
            switch (empData[0]) {
                case "Vendeur" -> uneListe.add(new Vendeur(
                        Integer.parseInt(empData[1]),
                        empData[2],
                        Double.parseDouble(empData[3]),
                        Double.parseDouble(empData[4]))
                );
                case "Manager" -> uneListe.add(new Manager(
                        Integer.parseInt(empData[1]),
                        empData[2],
                        Double.parseDouble(empData[3]),
                        empData[4],
                        Double.parseDouble(empData[5])
                ));
                case "Benevole" -> uneListe.add(new Benevole(
                        Integer.parseInt(empData[1]),
                        empData[2]
                ));
                default -> uneListe.add(new Employe(
                        Integer.parseInt(empData[1]),
                        empData[2],
                        Double.parseDouble(empData[3])
                ));
            }
        }
    }

    /**
     * Fonction qui créer un fichier txt de certificat de remerciement
     * des heures données.
     *
     * @param unBenevole qui a besoin d'un certificat.
     * @throws IOException s'il y a un problème avec la sauvegarde ou l'écriture du fichier.
     */
    public static void sauvegarderBenevole(Benevole unBenevole) throws IOException {
        PrintWriter writer = new PrintWriter("certs/" + unBenevole.getNom() + ".txt", StandardCharsets.UTF_8);
        writer.println(unBenevole);
        writer.close();
    }
}
