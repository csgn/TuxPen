package pane;

import buttons.Clear;
import buttons.Close;
import buttons.Draw;
import buttons.colors.*;
import canvas.CanvasProperties;

import javax.swing.*;
import java.awt.*;

public class ContentPane extends JPanel {
    public ContentPane(JFrame main_frame) {
        JPanel contentPane = new JPanel(new FlowLayout());
        contentPane.setBackground(new Color(24, 24, 24));

        contentPane.add(new Draw(main_frame));
        contentPane.add(new ColorButton(main_frame, ColorProperties.default_red, ColorProperties.hoverable_red, ColorProperties.red));
        contentPane.add(new ColorButton(main_frame, ColorProperties.default_green, ColorProperties.hoverable_green, ColorProperties.green));
        contentPane.add(new ColorButton(main_frame, ColorProperties.default_blue, ColorProperties.hoverable_blue, ColorProperties.blue));
        contentPane.add(new ColorButton(main_frame, ColorProperties.default_orange, ColorProperties.hoverable_orange, ColorProperties.orange));
        contentPane.add(new ColorButton(main_frame, ColorProperties.default_pink, ColorProperties.hoverable_pink, ColorProperties.pink));
        contentPane.add(new ColorButton(main_frame, ColorProperties.default_yellow, ColorProperties.hoverable_yellow, ColorProperties.yellow));
        contentPane.add(new Clear(main_frame));
        contentPane.add(new Close(main_frame));

        JLabel tux = new JLabel(new ImageIcon(this.getClass().getResource("/img/linux.png")));
        tux.setBorder(BorderFactory.createLineBorder(new Color(24, 24, 24), 30));
        contentPane.add(tux);

        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        this.add(contentPane);
    }
}