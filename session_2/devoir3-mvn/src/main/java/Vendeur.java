/**
 * Classe utilisée dans une application de gestions d'employés.
 * <p>
 * En plus d'être un employé régulier, un vendeur reçoit une commssion selon le nombre
 * de vente qu'il a effectué dans la semaine.
 *
 * @author Pierre Coutu
 * @date 2019-05-06
 */
public class Vendeur extends Employe {

    // ================ Attributs ===============
    private double ventesSemaine = 0.0;
    private double tauxCommission = 0.0;   // en pourcentage
    private double commissionsAccumulees = 0.0;

    // =========== Constructeur =================
    public Vendeur(int unNumero, String unNom, double unTauxHoraire, double unTauxCommission) {
        // initialise les attributs parent
        super(unNumero, unNom, unTauxHoraire);
        // initialise les attributs enfant
        tauxCommission = unTauxCommission;
    }

    // ======== Accesseurs/Mutateurs =================
    // get : retourne une copies des attributs
    public double getTauxCommission() {
        return tauxCommission;
    }

    // set : permet de modifier les attributs
    public void setVentesSemaine(double lesVentes) {
        ventesSemaine = lesVentes;
    }

    // ========== Autres méthodes ===============
    // ========== Méthodes redéfinies ===========
    // Calcule et retourne le salaire de la semaine, et s'occupe de la'accumulation
    // dans les bons atrtibuts
    public double encaisserSalaire(double nombreHeures) {
        // variables locales
        double salaire = 0.0, commissions = 0.0;
        // Le parent s'occupe de la partie du salaire dues aux heures travaillées
        salaire = super.encaisserSalaire(nombreHeures);
        // traiter les commissions
        commissions = ventesSemaine * tauxCommission / 100.0;
        commissionsAccumulees += commissions;
        salaire += commissions;
        // réinitialiser les ventes pour la prochaine semaine
        ventesSemaine = 0.0;
        // retourner le salaire de la semaine, avec les commissions
        return salaire;
    }

    // Calcule et retourne les revenus accumulés (salaire+commissions)
    public double calculerRevenuAccumule() {
        // parties du parent (salaireAccumule dues aux heures) + commissions Accumles
        return super.calculerRevenuAccumule() + commissionsAccumulees;
    }

    // Réinitialise les variables d'accumulation
    public void reinitialiserPeriodeDeCumul() {
        super.reinitialiserPeriodeDeCumul();
        commissionsAccumulees = 0.0;
    }

    public String toString() {
        return super.toString() + " (incluant les commissions)";
    }
}
