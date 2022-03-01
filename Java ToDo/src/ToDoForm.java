import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ToDoForm extends JFrame {
    private JTextField textField1;
    private JButton addTaskButton;
    private JList list1;
    private JButton deleteTaskButton;
    private JPanel panelMain;
    DefaultListModel listModel = new DefaultListModel();

    public ToDoForm() {
        addTaskButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String task = textField1.getText();
                listModel.addElement(task);
                list1.setModel(listModel);

                textField1.setText("");
                
            }
        });
        deleteTaskButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                //remove selected item from list
                int selectedIndex = list1.getSelectedIndex();
                if (selectedIndex != -1) {
                    listModel.remove(selectedIndex);
                }
                list1.setModel(listModel);
            }
        });
    }
    public static void main(String[] args) {
        ToDoForm form = new ToDoForm();
        form.setContentPane(form.panelMain);
        form.setSize(400, 400);
        form.setVisible(true);
        form.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
