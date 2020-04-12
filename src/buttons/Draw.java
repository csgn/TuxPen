package buttons;

import buttons.colors.ColorProperties;
import canvas.CanvasDrawing;
import canvas.CanvasProperties;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Draw extends JLabel {
    private Boolean active_canvas = false;

    public Draw(JFrame main_frame) {
        Draw label = this;
        label.setIcon(new ImageIcon(this.getClass().getResource("/img/content/defdraw.png")));
        label.setBorder(BorderFactory.createLineBorder(new Color(24, 24, 24), 12));

        this.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                if (!active_canvas) {
                    new CanvasDrawing();
                    active_canvas = true;
                } else {
                    CanvasProperties.color = ColorProperties.DEFAULT_COLOR;
                }
            }

            @Override
            public void mouseEntered(MouseEvent e) {
                label.setIcon(new ImageIcon(this.getClass().getResource("/img/content/hovdraw.png")));
                main_frame.setCursor(Cursor.HAND_CURSOR);
            }

            @Override
            public void mouseExited(MouseEvent e) {
                label.setIcon(new ImageIcon(this.getClass().getResource("/img/content/defdraw.png")));
                main_frame.setCursor(Cursor.DEFAULT_CURSOR);
            }
        });
    }
}
