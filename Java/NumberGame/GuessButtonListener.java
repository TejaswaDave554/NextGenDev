import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GuessButtonListener implements ActionListener {
    private final NumberGameFrame gameFrame;

    public GuessButtonListener(NumberGameFrame gameFrame) {
        this.gameFrame = gameFrame;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        try {
            int guess = Integer.parseInt(gameFrame.getGuessField().getText());
            int target = gameFrame.getTargetNumber();
            int attemptCount = gameFrame.getAttemptCount() + 1;
            gameFrame.setAttemptCount(attemptCount);

            int difference = Math.abs(guess - target);
            
            if (difference == 0) {
                gameFrame.getFeedbackLabel().setText("Correct! Attempts: " + attemptCount);
                gameFrame.getFeedbackLabel().setForeground(new Color(0, 230, 118)); // Bright Green
                gameFrame.getGuessField().setEditable(false);
                gameFrame.getGuessButton().setEnabled(false);
            } else if (difference <= 5) {
                gameFrame.getFeedbackLabel().setText("Very close!");
                gameFrame.getFeedbackLabel().setForeground(new Color(255, 235, 59)); // Yellow
            } else if (difference <= 10) {
                gameFrame.getFeedbackLabel().setText(guess < target ? "Little close (Low)" : "Little close (High)");
                gameFrame.getFeedbackLabel().setForeground(new Color(255, 152, 0)); // Orange
            } else if (difference <= 20) {
                gameFrame.getFeedbackLabel().setText(guess < target ? "Near Too Low" : "Near Too High");
                gameFrame.getFeedbackLabel().setForeground(new Color(244, 67, 54)); // Red
            } else {
                gameFrame.getFeedbackLabel().setText(guess < target ? "Too Low" : "Too High");
                gameFrame.getFeedbackLabel().setForeground(new Color(233, 30, 99)); // Deep Pink
            }
        } catch (NumberFormatException ex) {
            gameFrame.getFeedbackLabel().setText("Please enter a valid number.");
            gameFrame.getFeedbackLabel().setForeground(new Color(255, 61, 0)); // Bright Red
        }
    }
}
