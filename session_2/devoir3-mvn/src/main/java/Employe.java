/**
 * Classe utilisée dans une application de gestions d'employés.
 * <p>
 * Cette classe permet de calculer le salaire pour une semaine pour un
 * employé, ansi que d'accumuler ses revenus sur une longue période
 * (typiquement une année)
 *
 * @author Pierre Coutu
 * @date 2019-02-10
 */
public class Employe {

    // ================ Attributs ===============
    protected int numero;
    protected String nom;
    protected double tauxHoraire;
    protected double salaireAccumule = 0.0; // valeur par défaut

    // =========== Constructeur =================

    /**
     * Ce constructeur initialise 3 de ses attributs avec
     * les 3 paramètres qu'il reçoit. Le salaireAccumule
     * conserve sa valeur par défaut, soit 0.0
     *
     * @param unNumero      (int) numéro d'identification de l'employé
     * @param unNom         (String) nom de l'employé
     * @param unTauxHoraire (double) montant versé pour chaque heure travaillée
     */
    public Employe(int unNumero, String unNom, double unTauxHoraire) {
        this.numero = unNumero;
        this.nom = unNom;
        this.tauxHoraire = unTauxHoraire;
    }

    // ======== Accesseurs/Mutateurs =================
    // retourne une copies des attributs
    public int getNumero() {
        return this.numero;
    }

    public String getNom() {
        return this.nom;
    }

    public double getTauxHoraire() {
        return this.tauxHoraire;
    }

    // permet de modifier les attributs
    public void setTauxHoraire(double nouveauTaux) {
        this.tauxHoraire = nouveauTaux;
    }

    // ========== Autres méthodes ===============

    /**
     * Calcule et retourne le salaire d'un employé selon le nombre d'heures reçu
     * en paramètre. De plus, le salaire de la semaine est ajouté à l'attribut
     * salaireAccumule. Le calcul du salaire inclus la prime de surtemps pour les heures
     * qui dépasse 40 (50% de plus).
     *
     * @param nombreHeures (double) nombre d'heures travaillées dans la semaine
     * @return (double) le montant d'argent gagné par le travailler pour sa semaine de travail
     */
    public double encaisserSalaire(double nombreHeures) {
        double salaireSemaine = 0.0;
        if (nombreHeures < 40.0) {
            salaireSemaine = nombreHeures * this.tauxHoraire;
        } else {
            salaireSemaine = (40.0 + 1.5 * (nombreHeures - 40.0)) * this.tauxHoraire;
        }
        this.salaireAccumule += salaireSemaine;
        return salaireSemaine;
    }

    /**
     * Calcule et retourne les revenus accumulés par l'employé.
     * Pour l'instant ses seuls revenus sont son salaire.
     * Plus d'option à venir vers la fin de la session ...
     *
     * @return (double) revenus accumulés par l'employé (Ici, même chose que salaire accumulé)
     */
    public double calculerRevenuAccumule() {
        return this.salaireAccumule;
    }

    /**
     * Réinitialise tous les attributs qui accumulent des quantités (ici seulement salaireAccumules)
     */
    public void reinitialiserPeriodeDeCumul() {
        this.salaireAccumule = 0.0;
    }

    // ========== Méthodes redéfinies ===========

    /**
     * Formate la représentation en chaine de caractère
     *
     * @return format  : NOM [#NUMERO] @TAUX_HORAIRE $/heure (revenu accumulé : REVENU_ACCUMULE $)
     */
    public String toString() {
        String message;
        message = this.nom + " [#" + this.numero + "] : @" + this.tauxHoraire + " $/heure (revenu accumulé : " + this.calculerRevenuAccumule() + " $)";
        return message;
    }
}
