import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;

public class NumberGameFrame extends JFrame {
    private JTextField lowerBoundField;
    private JTextField upperBoundField;
    private JTextField guessField;
    private JLabel feedbackLabel;
    private JButton guessButton;
    private int targetNumber;
    private int attemptCount;

    public NumberGameFrame() {
        setTitle("Number Guessing Game");
        setSize(400, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());
        getContentPane().setBackground(new Color(33, 33, 33)); // Dark Gray

        JPanel contentPanel = new JPanel();
        contentPanel.setLayout(new BoxLayout(contentPanel, BoxLayout.Y_AXIS));
        contentPanel.setBackground(new Color(33, 33, 33)); // Dark Gray
        contentPanel.setBorder(new EmptyBorder(20, 20, 20, 20));

        JLabel promptLabel = new JLabel("Enter the lower and upper bounds:");
        promptLabel.setForeground(new Color(176, 190, 197)); // Light Gray
        promptLabel.setFont(new Font("Arial", Font.BOLD, 16));
        promptLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        contentPanel.add(promptLabel);

        lowerBoundField = new JTextField();
        lowerBoundField.setBorder(BorderFactory.createLineBorder(new Color(76, 175, 80), 3)); // Green
        lowerBoundField.setBackground(new Color(50, 50, 50)); // Medium Gray
        lowerBoundField.setForeground(Color.WHITE);
        lowerBoundField.setCaretColor(Color.WHITE);
        lowerBoundField.setMaximumSize(new Dimension(Integer.MAX_VALUE, lowerBoundField.getPreferredSize().height));
        contentPanel.add(Box.createVerticalStrut(10));
        contentPanel.add(lowerBoundField);

        upperBoundField = new JTextField();
        upperBoundField.setBorder(BorderFactory.createLineBorder(new Color(76, 175, 80), 3)); // Green
        upperBoundField.setBackground(new Color(50, 50, 50)); // Medium Gray
        upperBoundField.setForeground(Color.WHITE);
        upperBoundField.setCaretColor(Color.WHITE);
        upperBoundField.setMaximumSize(new Dimension(Integer.MAX_VALUE, upperBoundField.getPreferredSize().height));
        contentPanel.add(Box.createVerticalStrut(10));
        contentPanel.add(upperBoundField);

        JButton startButton = new JButton("Start Game");
        startButton.setBackground(new Color(56, 142, 60)); // Darker Green
        startButton.setForeground(Color.WHITE);
        startButton.setAlignmentX(Component.CENTER_ALIGNMENT);
        startButton.addActionListener(new StartButtonListener(this));
        contentPanel.add(Box.createVerticalStrut(10));
        contentPanel.add(startButton);

        guessField = new JTextField();
        guessField.setBorder(BorderFactory.createLineBorder(new Color(76, 175, 80), 3)); // Green
        guessField.setBackground(new Color(50, 50, 50)); // Medium Gray
        guessField.setForeground(Color.WHITE);
        guessField.setCaretColor(Color.WHITE);
        guessField.setEditable(false);
        guessField.setMaximumSize(new Dimension(Integer.MAX_VALUE, guessField.getPreferredSize().height));
        contentPanel.add(Box.createVerticalStrut(20));
        contentPanel.add(guessField);

        guessButton = new JButton("Submit Guess");
        guessButton.setBackground(new Color(56, 142, 60)); // Darker Green
        guessButton.setForeground(Color.WHITE);
        guessButton.setAlignmentX(Component.CENTER_ALIGNMENT);
        guessButton.addActionListener(new GuessButtonListener(this));
        guessButton.setEnabled(false);
        contentPanel.add(Box.createVerticalStrut(10));
        contentPanel.add(guessButton);

        feedbackLabel = new JLabel("");
        feedbackLabel.setForeground(new Color(176, 190, 197)); // Light Gray
        feedbackLabel.setFont(new Font("Arial", Font.BOLD, 14));
        feedbackLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        contentPanel.add(Box.createVerticalStrut(20));
        contentPanel.add(feedbackLabel);

        add(contentPanel, BorderLayout.CENTER);

        setVisible(true);
    }

    // Getter and Setter methods for fields
    public JTextField getLowerBoundField() {
        return lowerBoundField;
    }

    public JTextField getUpperBoundField() {
        return upperBoundField;
    }

    public JTextField getGuessField() {
        return guessField;
    }

    public JLabel getFeedbackLabel() {
        return feedbackLabel;
    }

    public JButton getGuessButton() {
        return guessButton;
    }

    public int getTargetNumber() {
        return targetNumber;
    }

    public void setTargetNumber(int targetNumber) {
        this.targetNumber = targetNumber;
    }

    public int getAttemptCount() {
        return attemptCount;
    }

    public void setAttemptCount(int attemptCount) {
        this.attemptCount = attemptCount;
    }
}
