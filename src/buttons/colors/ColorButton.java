package buttons.colors;

import canvas.CanvasProperties;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class ColorButton extends JLabel {
    public ColorButton(JFrame main_frame, String default_img, String hoverable_img, int[] pencil_color) {
        ColorButton label = this;
        label.setIcon(new ImageIcon(this.getClass().getResource(default_img)));

        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                label.setIcon(new ImageIcon(this.getClass().getResource(hoverable_img)));
                main_frame.setCursor(Cursor.HAND_CURSOR);
            }

            @Override
            public void mousePressed(MouseEvent e) {
                CanvasProperties.color = pencil_color;
            }

            @Override
            public void mouseExited(MouseEvent e) {
                label.setIcon(new ImageIcon(this.getClass().getResource(default_img)));
                main_frame.setCursor(Cursor.DEFAULT_CURSOR);
            }
        });
    }
}
