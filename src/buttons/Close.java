package buttons;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Close extends JLabel {
    public Close(JFrame main_frame) {
        Close label = this;
        label.setIcon(new ImageIcon(this.getClass().getResource("/img/content/defcross.png")));
        label.setBorder(BorderFactory.createLineBorder(new Color(24, 24, 24), 12));

        this.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                System.exit(0);
            }

            @Override
            public void mouseEntered(MouseEvent e) {
                label.setIcon(new ImageIcon(this.getClass().getResource("/img/content/hovcross.png")));
                main_frame.setCursor(Cursor.HAND_CURSOR);
            }

            @Override
            public void mouseExited(MouseEvent e) {
                label.setIcon(new ImageIcon(this.getClass().getResource("/img/content/defcross.png")));
                main_frame.setCursor(Cursor.DEFAULT_CURSOR);
            }
        });
    }
}
