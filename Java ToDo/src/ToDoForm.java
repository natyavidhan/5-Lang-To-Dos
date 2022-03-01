import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ToDoForm {
    private JTextField textField1;
    private JButton addTaskButton;
    private JList list1;
    private JButton deleteTaskButton;

    public ToDoForm() {
        addTaskButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                //add the text in the text field to the list
                String task = textField1.getText();
                DefaultListModel model = (DefaultListModel) list1.getModel();
                model.addElement(task);
                textField1.setText("");
                
            }
        });
    }
}
