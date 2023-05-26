import javax.swing.*;
import java.awt.event.*;
import java.util.HashMap;
import java.util.Map;

public class TextEditorApp extends JFrame implements ActionListener {

    DocumentContainer documentContainer;
    JMenuBar menuBar;
    JMenu fileMenu, editMenu, toolsMenu, helpMenu;
    JMenuItem newItem, openItem, saveItem, saveUnderItem, closeItem, closeAllItem, quitItem; // File menu
    JMenuItem undoItem, redoItem, copyItem, cutItem, pasteItem; // Edit menu
    JMenuItem findItem, replaceItem; // Tools menu
    JMenuItem aboutItem; // Help bar

    public static final Map<JMenuItem, Runnable> menuActions = new HashMap<>();
    public static final Map<JButton, Runnable> buttonActions = new HashMap<>();

    /**
     * Antoine Langevin
     */
    public TextEditorApp() {
        this.setTitle("Éditeur de texte");
        this.setSize(800, 600);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLocationRelativeTo(null);

        addComponents();
        createItems();
        addMenus();
        addListeners();

        this.setVisible(true);
    }

    /**
     * Ajout du composant de DocumentContainer.
     * Antoine Langevin
     */
    private void addComponents() {
        this.documentContainer = new DocumentContainer(this.rootPane);
        this.add(this.documentContainer);
    }

    private void createItems() {
        this.menuBar = new JMenuBar();
        // menu bars
        this.fileMenu = new JMenu("Fichier");
        this.editMenu = new JMenu("Editer");
        this.toolsMenu = new JMenu("Outils");
        this.helpMenu = new JMenu("Help");
        // files bar items
        this.newItem = new JMenuItem("Nouveau");
        this.openItem = new JMenuItem("Ouvrir");
        this.saveItem = new JMenuItem("Sauvegarder");
        this.saveUnderItem = new JMenuItem("Sauvegarder sous...");
        this.closeItem = new JMenuItem("Fermer");
        this.closeAllItem = new JMenuItem("Fermer tout");
        this.quitItem = new JMenuItem("Quitter");
        // Edit bar items
        this.redoItem = new JMenuItem("Redo");
        this.undoItem = new JMenuItem("Undo");
        this.copyItem = new JMenuItem("Copy");
        this.cutItem = new JMenuItem("Cut");
        this.pasteItem = new JMenuItem("Paste");
        // Tools bar items
        this.findItem = new JMenuItem("Chercher");
        this.replaceItem = new JMenuItem("Remplacer");
        // Help bar items
        this.aboutItem = new JMenuItem("À propos");

        this.createKeyStrokes();
        this.registerButtonAction();
    }

    /**
     * Antoine Langevin
     */
    private void registerButtonAction() {
        /*
        J'utilise un HashMap pour stocker une action à un bouton, la raison pour cela est
        que si nous voulons rajouter des sous-menus et avec des boutons, l'itération va devenir
        longue et pénible tandis que le HashMap va accéder directement à l'action si l'instance
        du bouton est stocké dans le map.
         */
        TextEditorApp.menuActions.put(this.newItem, this.documentContainer::createNewDocument);
        TextEditorApp.menuActions.put(this.openItem, this.documentContainer::openDocument);
        TextEditorApp.menuActions.put(this.saveItem, this.documentContainer::saveCurrentDocument);
        TextEditorApp.menuActions.put(this.saveUnderItem, this.documentContainer::saveAsCurrentDocument);
        TextEditorApp.menuActions.put(this.closeItem, this.documentContainer::closeCurrentDocument);
        TextEditorApp.menuActions.put(this.closeAllItem, this.documentContainer::closeAllDocument);
        TextEditorApp.menuActions.put(this.quitItem, this::removeAll);
        TextEditorApp.menuActions.put(this.undoItem, this.documentContainer::undoCurrentDocument);
        TextEditorApp.menuActions.put(this.redoItem, this.documentContainer::redoCurrentDocument);
        TextEditorApp.menuActions.put(this.copyItem, this.documentContainer::copyInCurrentDocument);
        TextEditorApp.menuActions.put(this.cutItem, this.documentContainer::cutInCurrentDocument);
        TextEditorApp.menuActions.put(this.pasteItem, this.documentContainer::pasteInCurrentDocument);
        TextEditorApp.menuActions.put(this.findItem, () -> {
            /* get string for searchNext() */
            SearchDialog searchDialog = new SearchDialog(this.documentContainer);
        });
        TextEditorApp.menuActions.put(this.replaceItem, () -> {
            /* get string for replaceNext() */
            ReplaceDialog replaceDialog = new ReplaceDialog(this.documentContainer);
        });
        TextEditorApp.menuActions.put(this.aboutItem, () -> {
            /* create the about dialog box. */
        });

        for (JMenuItem button : TextEditorApp.menuActions.keySet()) {
            button.addActionListener(this);
        }
    }

    /**
     * Antoine Langevin
     */
    private void createKeyStrokes() {
        // Files bar shortcuts.
        this.openItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_O, InputEvent.CTRL_DOWN_MASK));
        this.saveItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, InputEvent.CTRL_DOWN_MASK));
        this.saveUnderItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, InputEvent.CTRL_DOWN_MASK | InputEvent.SHIFT_DOWN_MASK));
        this.newItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_N, InputEvent.CTRL_DOWN_MASK));
        this.closeItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_W, InputEvent.CTRL_DOWN_MASK));
        this.closeAllItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_W, InputEvent.CTRL_DOWN_MASK | InputEvent.SHIFT_DOWN_MASK));
        this.quitItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_F4, InputEvent.CTRL_DOWN_MASK));
        // Edit bar shortcuts.
        this.undoItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Z, InputEvent.CTRL_DOWN_MASK));
        this.redoItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Y, InputEvent.CTRL_DOWN_MASK));
        this.copyItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_C, InputEvent.CTRL_DOWN_MASK));
        this.cutItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_X, InputEvent.CTRL_DOWN_MASK));
        this.pasteItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_V, InputEvent.CTRL_DOWN_MASK));
        // Tools bar shortcuts
        this.findItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_F, InputEvent.CTRL_DOWN_MASK));
        this.replaceItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_F, InputEvent.CTRL_DOWN_MASK | InputEvent.SHIFT_DOWN_MASK));
        // Help bar shortcuts
        this.aboutItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_F1, 0));
    }

    /**
     * Antoine Langevin
     */
    private void addMenus() {
        // Files menu items
        this.fileMenu.add(this.newItem);
        this.fileMenu.addSeparator();
        this.fileMenu.add(this.openItem);
        this.fileMenu.addSeparator();
        this.fileMenu.add(this.saveItem);
        this.fileMenu.addSeparator();
        this.fileMenu.add(this.saveUnderItem);
        this.fileMenu.addSeparator();
        this.fileMenu.add(this.closeItem);
        this.fileMenu.addSeparator();
        this.fileMenu.add(this.closeAllItem);
        this.fileMenu.addSeparator();
        this.fileMenu.add(this.quitItem);
        // Edit menu items
        this.editMenu.add(this.undoItem);
        this.editMenu.addSeparator();
        this.editMenu.add(this.redoItem);
        this.editMenu.addSeparator();
        this.editMenu.add(this.copyItem);
        this.editMenu.addSeparator();
        this.editMenu.add(this.cutItem);
        this.editMenu.addSeparator();
        this.editMenu.add(this.pasteItem);
        // Help bar items
        this.toolsMenu.addSeparator();
        this.toolsMenu.add(this.findItem);
        this.toolsMenu.addSeparator();
        this.toolsMenu.add(this.replaceItem);
        // Tools menu items
        this.helpMenu.add(this.aboutItem);

        this.menuBar.add(this.fileMenu);
        this.menuBar.add(this.editMenu);
        this.menuBar.add(this.toolsMenu);
        this.menuBar.add(this.helpMenu);

        this.setJMenuBar(this.menuBar);
    }

    /**
     * Antoine Langevin & Ismail
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        JMenuItem item = (JMenuItem) e.getSource();
        if (menuActions.containsKey(item)) {
            Runnable action = menuActions.get(item);
            action.run();
        } else {
            // needs to throw an exception.
        }
    }

    /**
     * Ajoute les Listeners aux différentes menuActions des menus
     * et ajoute un WindowListener à la fenêtre pour détecter
     * losque l'utilisateur clique sur le X pour fermer la fenêtre.
     * S'occupe de la fermeture adéquate des documents à ce moment-là.
     *
     * Antoine Langevin & Ismail
     */
    private void addListeners() {
        this.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                e.getWindow().dispose();
            }

            @Override
            public void windowClosed(WindowEvent e) {
                System.out.println("MyApp is closed");
            }
        });
    }
}
