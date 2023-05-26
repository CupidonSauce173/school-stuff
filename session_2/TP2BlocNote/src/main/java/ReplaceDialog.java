import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ReplaceDialog extends JDialog implements ActionListener{

    private JLabel searchLabel;
    private JLabel replaceLabel;
    private JTextField searchTextField;
    private JTextField replaceTextField;
    private JButton nextButton;
    private JButton replaceButton;
    private JButton replaceAllButton;
    private JButton cancelButton;

    /**
     * Antoine Langevin
     */
    public ReplaceDialog(DocumentContainer documentContainer) {
        this.createComponents();
        this.registerButtonActions();

        JPanel panel = new JPanel(new BorderLayout(10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        JPanel searchPanel = new JPanel(new BorderLayout(5, 5));
        searchPanel.add(this.searchTextField, BorderLayout.CENTER);
        searchPanel.add(this.nextButton, BorderLayout.EAST);

        JPanel replacePanel = new JPanel(new BorderLayout(5, 5));
        replacePanel.add(this.replaceTextField, BorderLayout.CENTER);
        replacePanel.add(this.replaceButton, BorderLayout.EAST);

        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT, 5, 5));
        buttonPanel.add(this.nextButton);
        buttonPanel.add(this.replaceButton);
        buttonPanel.add(this.replaceAllButton);
        buttonPanel.add(this.cancelButton);

        JPanel labelPanel = new JPanel(new GridLayout(2, 1, 5, 5));
        labelPanel.add(this.searchLabel);
        labelPanel.add(this.replaceLabel);

        JPanel inputPanel = new JPanel(new GridLayout(2, 1, 10, 10));
        inputPanel.add(searchPanel);
        inputPanel.add(replacePanel);
        panel.add(labelPanel, BorderLayout.WEST);
        panel.add(inputPanel, BorderLayout.CENTER);
        panel.add(buttonPanel, BorderLayout.SOUTH);

        getContentPane().add(panel);
        pack();
        setLocationRelativeTo(documentContainer);
        setVisible(true);
    }

    /**
     * Antoine Langevin
     */
    private void createComponents() {
        this.searchLabel = new JLabel("Rechercher :");
        this.replaceLabel = new JLabel("Replacer Par :");
        this.searchTextField = new JTextField(20);
        this.replaceTextField = new JTextField(20);
        this.nextButton = new JButton("Suivant");
        this.replaceButton = new JButton("Remplacer");
        this.replaceAllButton = new JButton("Remplacer tout");
        this.cancelButton = new JButton("Annuler");
    }

    /**
     * Antoine Langevin & Ismail
     */
    private void registerButtonActions() {
        TextEditorApp.buttonActions.put(this.nextButton, () -> {
            // Tu peux faire les actions là, so dans nextButton, tu vas remplacer la prochaine apparition du mot par exemple.
        });
        TextEditorApp.buttonActions.put(this.replaceButton, () -> {

        });
        TextEditorApp.buttonActions.put(this.replaceAllButton, () -> {

        });
        TextEditorApp.buttonActions.put(this.cancelButton, this::dispose);
    }

    /**
     * Antoine Langevin & Ismail
     */
    @Override
    public void actionPerformed(ActionEvent e) {

    }
}




