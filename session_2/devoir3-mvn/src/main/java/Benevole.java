/**
 * Classe utilisée dans une application de gestions d'employés.
 * <p>
 * En plus d'être un employé régulier, un manager est en charge d'un département
 * et reçoit un bonus à chaque semaine.
 *
 * @author Antoine Langevin
 * @date 2023-04-01
 */
public class Benevole extends Employe {

    // ================ Attributs ===============
    private double heuresAccumulees;

    // =========== Constructeur =================
    public Benevole(int unNumero, String unNom) {
        super(unNumero, unNom, 0.0);
        this.heuresAccumulees = 0.0;
    }

    // ======== Accesseurs/Mutateurs =================
    // get : retourne une copies des attributs
    public double getHeuresAccumulees() {
        return this.heuresAccumulees;
    }

    // ========== Autres méthodes ===============
    // Calcule et retourne le salaire de la semaine, et s'occupe de l'accumulation
    // dans les bons atrtibuts
    public double encaisserSalaire(double nombreHeures) {
        this.heuresAccumulees += nombreHeures;
        return 0.0;
    }

    // Réinitialise les variables d'accumulation
    public void reinitialiserPeriodeDeCumul() {
        this.heuresAccumulees = 0.0;
    }

    public String toString() {
        return "Merci " + super.nom + " pour avoir effectué " + this.heuresAccumulees + " heures de bénévolat.";
    }

    // ========== Méthodes redéfinies ===========
}
