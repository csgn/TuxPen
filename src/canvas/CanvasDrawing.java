package canvas;

import javax.swing.*;
import java.awt.*;

import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;

public class CanvasDrawing extends JPanel {
    private int befX, befY, curX, curY;
    public CanvasDrawing() {
        JFrame canvas = new JFrame();
        Dimension screen_resolution = Toolkit.getDefaultToolkit().getScreenSize();

        addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseDragged(MouseEvent event) {
                befX = event.getX();
                befY = event.getY();
                curX = befX;
                curY = befY;
                repaint();
            }
        });

        canvas.setCursor(Toolkit.getDefaultToolkit().createCustomCursor(
                new ImageIcon(this.getClass().getResource(CanvasProperties.pencil_img)).getImage(),
                new Point(0,20),"custom cursor")
        );
        canvas.add(this);
        canvas.setUndecorated(true);
        canvas.setBackground(new Color(0.0f, 0.0f, 0.0f, 0.0f));
        canvas.setSize((int) screen_resolution.getWidth()-100, (int) screen_resolution.getHeight());
        canvas.setVisible(true);
    }

    protected void paintComponent(Graphics graph) {
        Graphics2D graph2d = (Graphics2D) graph;
        graph2d.setColor(new Color(CanvasProperties.color[0], CanvasProperties.color[1], CanvasProperties.color[2]));
        graph2d.setStroke(new BasicStroke(CanvasProperties.pencil_size));
        graph2d.drawLine(curX, curY, befX, befY);
    }
}
