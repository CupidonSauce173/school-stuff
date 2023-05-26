import javax.swing.*;
import java.awt.*;
import java.io.File;

public class DocumentContainer extends JTabbedPane {
    Component rootPane;
    JFileChooser fileChooser;

    /**
     * Constructeur de base de la classe DocumentContainer.
     * Antoine Langevin
     */
    public DocumentContainer(Component rootPane) {
        this.rootPane = rootPane;
        this.fileChooser = new JFileChooser(String.valueOf(this.rootPane));
        this.createNewDocument();
        this.createNewDocument();
    }

    /**
     * Crée un nouvel onglet contenant un nouveau document vide.
     * Antoine Langevin
     */
    public void createNewDocument() {
        TextDocument newDoc = new TextDocument();
        this.addTab("*Nouveau document", newDoc);
    }

    /**
     * Crée un nouvel onglet contenant le contenu d'un document
     * existant sur le disque dur. Une fenêtre de type JFileChooser
     * s'execute pour choisir le fichier.
     * Antoine Langevin
     */
    public void openDocument() {
        var result = this.fileChooser.showOpenDialog(this.rootPane);
        if(result == JFileChooser.APPROVE_OPTION){
            File selectedFile = this.fileChooser.getSelectedFile();
            // opens and moves the user to the new tab.
            this.setSelectedComponent(
                    this.add(selectedFile.getName(), new TextDocument(selectedFile))
            );
        } else {
            // handle the error.
        }
    }

    /**
     * Appel la méthode save du TextDocument de l'onglet sélectionné.
     */
    public void saveCurrentDocument() {

    }

    /**
     * Appelle la méthode saveAs du TextDocument de l'onglet
     * sélectionné.
     */
    public void saveAsCurrentDocument() {}

    /**
     * Appelle la méthode close du TextDocument de l'onglet
     * sélectionné.
     * @return boolean
     */
    public boolean closeCurrentDocument() {
        if(this.getSelectedComponent() instanceof TextDocument) {
            ((TextDocument) this.getSelectedComponent()).close();
        }
        return true;
    }

    /**
     *
     * @return boolean
     */
    public boolean closeAllDocument() {
        return true;
    }

    /**
     * Antoine Langevin
     */
    public void undoCurrentDocument() {
        if(this.getSelectedComponent() instanceof TextDocument) {
            ((TextDocument) this.getSelectedComponent()).undo();
        }
    }

    /**
     * Antoine Langevin
     */
    public void redoCurrentDocument() {
        if(this.getSelectedComponent() instanceof TextDocument) {
            ((TextDocument) this.getSelectedComponent()).redo();
        }
    }

    /**
     * Antoine Langevin
     */
    public void copyInCurrentDocument() {
        if(this.getSelectedComponent() instanceof TextDocument) {
            ((TextDocument) this.getSelectedComponent()).copy();
        }
    }

    /**
     * Antoine Langevin
     */
    public void cutInCurrentDocument() {
        if(this.getSelectedComponent() instanceof TextDocument) {
            ((TextDocument) this.getSelectedComponent()).cut();
        }
    }

    /**
     * Antoine Langevin
     */
    public void pasteInCurrentDocument() {
        if(this.getSelectedComponent() instanceof TextDocument) {
            ((TextDocument) this.getSelectedComponent()).paste();
        }
    }

    public void selectNext(String toSearch) {}

    public void replaceNext(String toSearch, String toReplace) {}

    public void replaceAll(String toSearch, String toReplace) {}

    public boolean closeDocumentAt(int index) { return true; }
}
