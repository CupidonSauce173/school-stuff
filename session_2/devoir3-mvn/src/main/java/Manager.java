/**
 * Classe utilisée dans une application de gestions d'employés.
 * <p>
 * En plus d'être un employé régulier, un manager est en charge d'un département
 * et reçoit un bonus à chaque semaine.
 *
 * @author Antoine Langevin
 * @date 2023-04-01
 */
public class Manager extends Employe {

    // ================ Attributs ===============
    private String departement;
    private double bonusSemaine, bonusAccumules;

    // =========== Constructeur =================
    public Manager(int unNumero, String unNom, double unTaux, String unDepartement, double unBonusSemaine) {
        super(unNumero, unNom, unTaux);
        departement = unDepartement;
        bonusSemaine = unBonusSemaine;
        bonusAccumules = 0.0;
    }

    // ======== Accesseurs/Mutateurs =================
    // get : retourne une copies des attributs
    public String getDepartement() {
        return departement;
    }

    public double getBonusSemaine() {
        return bonusSemaine;
    }

    // set : permet de modifier les attributs

    // ========== Autres méthodes ===============

    // ========== Méthodes redéfinies ===========
    // Calcule et retourne le salaire de la semaine, et s'occupe de l'accumulation
    // dans les bons atrtibuts
    public double encaisserSalaire(double nombreHeures) {
        // variables locales
        double salaire = 0.0;
        // Le parent s'occupe de la partie du salaire dues aux heures travaillées
        salaire = super.encaisserSalaire(nombreHeures);
        // traiter les bonus
        this.bonusAccumules += this.bonusSemaine;
        salaire += this.bonusSemaine;
        // retourner le salaire de la semaine, avec les bonus
        return salaire;
    }

    // Calcule et retourne les revenus accumulés (salaire+commissions)
    public double calculerRevenuAccumule() {
        // parties du parent (salaireAccumule dues aux heures) + commissions Accumles
        return super.calculerRevenuAccumule() + this.bonusAccumules;
    }

    // Réinitialise les variables d'accumulation
    public void reinitialiserPeriodeDeCumul() {
        super.reinitialiserPeriodeDeCumul();
        this.bonusAccumules = 0.0;
    }

    public String toString() {
        return super.toString() + " (incluant les bonus)";
    }
}
