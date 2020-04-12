package buttons;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Clear extends JLabel {
    public Clear(JFrame main_frame) {
        Clear label = this;
        label.setIcon(new ImageIcon(this.getClass().getResource("/img/content/defclear.png")));
        label.setBorder(BorderFactory.createLineBorder(new Color(24, 24, 24), 12));

        this.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {

            }

            @Override
            public void mouseEntered(MouseEvent e) {
                label.setIcon(new ImageIcon(this.getClass().getResource("/img/content/hovclear.png")));
                main_frame.setCursor(Cursor.HAND_CURSOR);
            }

            @Override
            public void mouseExited(MouseEvent e) {
                label.setIcon(new ImageIcon(this.getClass().getResource("/img/content/defclear.png")));
                main_frame.setCursor(Cursor.DEFAULT_CURSOR);
            }
        });
    }
}
