from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QSpinBox, QTextEdit, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import string
from password_logic import generate_password

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Password Generator")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        
        self.setStyleSheet("background-color: #B0BEC5;")  

        label_chars = QLabel("Chars that will compose the Password:")
        label_chars.setFont(QFont("Arial", 10, QFont.Bold))
        label_chars.setStyleSheet("color: #000000;")  
        layout.addWidget(label_chars)

        self.ptype = QComboBox()
        self.ptype.addItem("Alphanumeric")
        self.ptype.addItem("Numeric")
        self.ptype.addItem("Alpha")
        self.ptype.setStyleSheet("background-color: #FFFFFF; color: #000000 ; font-weight: bold;")  
        layout.addWidget(self.ptype)

        label_num_chars = QLabel("Password Length:")
        label_num_chars.setFont(QFont("Arial", 10, QFont.Bold))
        label_num_chars.setStyleSheet("color: #000000;") 
        layout.addWidget(label_num_chars)

        self.n_chars = QSpinBox()
        self.n_chars.setMinimum(4)
        self.n_chars.setMaximum(15)
        self.n_chars.setStyleSheet("background-color: #FFFFFF; color: #000000; font-weight: bold;")  
        layout.addWidget(self.n_chars)

        label_words = QLabel("Enter words to integrate (separated by commas):")
        label_words.setFont(QFont("Arial", 10, QFont.Bold))
        label_words.setStyleSheet("color: #000000;") 
        layout.addWidget(label_words)

        self.words_input = QLineEdit()
        self.words_input.setStyleSheet("background-color: #FFFFFF; color: #000000; font-weight: bold;")  
        layout.addWidget(self.words_input)

        self.text_password_out = QTextEdit()
        self.text_password_out.setStyleSheet("background-color: #FFFFFF; color: #000000; font-weight: bold;")  
        layout.addWidget(self.text_password_out)

        button_generate = QPushButton("Generate")
        button_generate.setFont(QFont("Arial", 10, QFont.Bold))
        button_generate.setStyleSheet("background-color: #FF5722; color: #FFFFFF;")  
        button_generate.clicked.connect(self.set_password)
        layout.addWidget(button_generate)

        button_close = QPushButton("Close")
        button_close.setFont(QFont("Arial", 10, QFont.Bold))
        button_close.setStyleSheet("background-color: #FF5722; color: #FFFFFF;")  
        button_close.clicked.connect(self.close)
        layout.addWidget(button_close)

        self.setLayout(layout)

    def set_password(self):
        try:
            chars = ''
            ptype = self.ptype.currentText().lower()
            if ptype == 'numeric':
                chars = string.digits
            elif ptype == 'alpha':
                chars = string.ascii_letters
            else:
                chars = string.digits + string.ascii_letters

            words = self.words_input.text().split(',')
            words = [word.strip() for word in words]

            if self.n_chars.value() < sum(len(word) for word in words):
                self.text_password_out.setText("Error: Password length is too short for the provided words.")
                return

            password = generate_password(chars, words, self.n_chars.value())
            self.text_password_out.setText(password)
        except Exception as e:
            self.text_password_out.setText(f"An unexpected error occurred: {str(e)}")
