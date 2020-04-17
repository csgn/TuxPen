import bar.TitleBar;
import pane.ContentPane;

import javax.swing.*;
import java.awt.*;

public class TuxPen  {
    public static void init() {
        JFrame main_frame = new JFrame();
        Dimension screen_resolution = Toolkit.getDefaultToolkit().getScreenSize();

        main_frame.add(new TitleBar(main_frame), BorderLayout.PAGE_START);
        main_frame.add(new ContentPane(main_frame));

        main_frame.setUndecorated(true);

        if (System.getProperty("os.name").startsWith("Windows")) {
            main_frame.setLocation((int) screen_resolution.getWidth() - 55, ((int) screen_resolution.getHeight() - 345) / 2);
        } else {
            main_frame.setLocation((int) screen_resolution.getWidth(), ((int) screen_resolution.getHeight() - 345) / 2);
        }

        main_frame.setBackground(new Color(0.0f, 0.0f, 0.0f, 0.0f));
        main_frame.setSize(55, 345);
        main_frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                init();
            }
        });
    }
}
