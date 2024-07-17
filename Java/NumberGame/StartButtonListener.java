import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class StartButtonListener implements ActionListener {
    private final NumberGameFrame gameFrame;

    public StartButtonListener(NumberGameFrame gameFrame) {
        this.gameFrame = gameFrame;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        try {
            int lowerBound = Integer.parseInt(gameFrame.getLowerBoundField().getText());
            int upperBound = Integer.parseInt(gameFrame.getUpperBoundField().getText());
            if (lowerBound >= upperBound) {
                gameFrame.getFeedbackLabel().setText("Upper bound must be greater than lower bound.");
                gameFrame.getFeedbackLabel().setForeground(new Color(255, 61, 0)); // Bright Red
                return;
            }
            int targetNumber = new Random().nextInt(upperBound - lowerBound + 1) + lowerBound;
            gameFrame.setTargetNumber(targetNumber);
            gameFrame.setAttemptCount(0);
            gameFrame.getFeedbackLabel().setText("Game started! Enter your guess.");
            gameFrame.getFeedbackLabel().setForeground(new Color(0, 230, 118)); // Bright Green
            gameFrame.getGuessField().setEditable(true);
            gameFrame.getGuessField().setText(""); // Clear previous guess
            gameFrame.getGuessButton().setEnabled(true);
        } catch (NumberFormatException ex) {
            gameFrame.getFeedbackLabel().setText("Please enter valid numbers.");
            gameFrame.getFeedbackLabel().setForeground(new Color(255, 61, 0)); // Bright Red
        }
    }
}
