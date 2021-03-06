import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Test Form")
        self.edit = QLineEdit("Write name here")
        self.button = QPushButton("Show Greets")
        self.button.clicked.connect(self.greetings)

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        
        self.setLayout(layout)

    def greetings(self):
        print ("Hello {}".format(self.edit.text()))

if __name__ == '__main__':
    app = QApplication([])
    form = Form()
    form.show()
    sys.exit(app.exec_())
