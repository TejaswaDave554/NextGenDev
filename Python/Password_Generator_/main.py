import sys
from PyQt5.QtWidgets import QApplication
from password_generator_gui import PasswordGenerator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
