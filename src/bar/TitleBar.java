package bar;

import javax.swing.*;

import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;

public class TitleBar extends JPanel {
    private int px, py;

    public TitleBar(JFrame main_frame) {
        JLabel header = new JLabel("TuxPen");
        header.setForeground(new Color(255, 255, 255));

        this.setBackground(new Color(21, 21, 21));
        this.add(header);
        this.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent event) {
                px = event.getX();
                py = event.getY();
                main_frame.setCursor(Cursor.MOVE_CURSOR);
            }

            @Override
            public void mouseDragged(MouseEvent event) {
                int x = main_frame.getLocation().x + event.getX() - px;
                int y = main_frame.getLocation().y + event.getY() - py;
                main_frame.setLocation(x, y);
            }

            @Override
            public void mouseExited(MouseEvent e) {
                main_frame.setCursor(Cursor.DEFAULT_CURSOR);
            }
        });

        this.addMouseMotionListener(new MouseMotionAdapter() {
            @Override
            public void mouseDragged(MouseEvent event) {
                int x = main_frame.getLocation().x + event.getX() - px;
                int y = main_frame.getLocation().y + event.getY() - py;
                main_frame.setLocation(x, y);
            }
        });
    }
}