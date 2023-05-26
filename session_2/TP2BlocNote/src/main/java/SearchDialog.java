import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SearchDialog extends JDialog implements ActionListener{

    private JLabel label;
    private JButton nextButton;
    private JButton cancelButton;
    private JTextField textField;

    /**
     * Antoine Langevin
     */
    public SearchDialog(DocumentContainer documentContainer) {
        this.createItems();
        this.registerButtonAction();

        this.setTitle("Rechercher");

        JPanel panel = new JPanel(new BorderLayout(30, 30));

        this.nextButton.setPreferredSize(textField.getPreferredSize());
        this.cancelButton.setPreferredSize(textField.getPreferredSize());

        JPanel buttonPanel = new JPanel(new GridLayout(1, 2, 0, 0));
        buttonPanel.add(this.nextButton);
        buttonPanel.add(this.cancelButton);

        JPanel searchPanel = new JPanel(new BorderLayout(5, 0));
        searchPanel.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        searchPanel.add(textField, BorderLayout.NORTH);
        searchPanel.add(buttonPanel, BorderLayout.CENTER);

        panel.add(this.label, BorderLayout.WEST);
        panel.add(searchPanel, BorderLayout.CENTER);
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        getContentPane().add(panel);
        pack();
        setLocationRelativeTo(documentContainer);
        this.setVisible(true);
    }

    /**
     * Antoine Langevin
     */
    private void createItems() {
        this.label = new JLabel("Rechercher:");
        this.textField = new JTextField(20);
        this.nextButton = new JButton("Suivant");
        this.cancelButton = new JButton("Annuler");
        this.label = new JLabel("Rechercher:");
        this.textField = new JTextField(10);
    }

    /**
     * Antoine Langevin
     */
    private void registerButtonAction() {
        TextEditorApp.buttonActions.put(this.nextButton, () -> {
            
        });
        TextEditorApp.buttonActions.put(this.cancelButton, this::dispose);
    }

    /**
     * Antoine Langevin & Ismail
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        JMenuItem item = (JMenuItem) e.getSource();
        if (TextEditorApp.menuActions.containsKey(item)) {
            Runnable action = TextEditorApp.menuActions.get(item);
            action.run();
        } else {
            // needs to throw an exception.
        }
    }
}
