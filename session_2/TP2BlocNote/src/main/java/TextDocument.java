import javax.swing.*;
import javax.swing.event.UndoableEditListener;
import javax.swing.undo.UndoManager;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class TextDocument extends JEditorPane {
    UndoManager undoManager = new UndoManager();

    /**
     * Antoine Langevin
     */
    public TextDocument() {
        this.registerEditListener(undoManager);
    }

    /**
     * Antoine Langevin
     * @param file
     */
    public TextDocument(File file) {
        this.registerEditListener(undoManager);
        StringBuilder fileContent = new StringBuilder();
        try {
            FileReader reader = new FileReader(file);
            int charCount;
            while((charCount = reader.read()) != -1) {
                fileContent.append((char) charCount);
            }
            reader.close();
        } catch (IOException e) {
            // handle exception, will open a confirmation pane to
            // tell the user that there was a problem while opening their file.
        }

        this.setText(fileContent.toString());
    }

    /**
     * Antoine Langevin
     * @param undoableEditListener
     */
    public void registerEditListener(UndoableEditListener undoableEditListener) {
        this.getDocument().addUndoableEditListener(undoableEditListener);

    }

    public boolean getHasChanged() {
        return false;
    }

    public String getFileName() { return null; }

    public boolean save() {
        this.getHasChanged();
        return true;
    }

    public boolean saveAs() { return true; }

    public boolean close() { return true; }

    /**
     * Antoine Langevin
     */
    public void undo() {
        if (this.undoManager.canUndo()) {
            this.undoManager.undo();
        }
    }

    /**
     * Antoine Langevin
     */
    public void redo() {
        if (this.undoManager.canRedo()) {
            this.undoManager.redo();
        }
    }

    public boolean selectNext(String toSearch) {
        return true;
    }

    public boolean replaceNext(String toSearch, String toReplace) { return true; }

    public boolean replaceAll(String toSearch, String toReplace) { return true; }

    public File openDialog() { return null; }

    public void load() {}

    public void addComponents() {}

    public void addListeners() {}

    public File saveDialog() { return null; }
}
