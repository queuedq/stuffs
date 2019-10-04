import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import *


class Greeter(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.setWindowTitle('Dynamic Greeter')
    self.resize(400, 280)

    self.centralWidget = QWidget(self)
    self.setCentralWidget(self.centralWidget)

    # Create the QVBoxLayout that lays out the whole form
    self.layout = QVBoxLayout()
    self.layout.addStretch(1)
    self.centralWidget.setLayout(self.layout)

    # Create the form layout that manages the labeled controls
    self.form_layout = QFormLayout()
    self.layout.addLayout(self.form_layout)

    # Create the entry control to specify a
    # recipient and set its placeholder text
    self.recipient = QLineEdit(self)
    self.recipient.setPlaceholderText("e.g. 'world' or 'Matey'")
    self.form_layout.addRow('Recipient', self.recipient)

    # Create and add the label to show the greeting text
    self.greeting = QLabel('', self)
    self.form_layout.addRow('Greeting', self.greeting)


    # Create a horizontal box layout to hold the button
    self.button_box = QHBoxLayout()
    self.button_box.addStretch(1)

    # Create the build button with its caption
    self.build_button = QPushButton('Build Greeting', self)
    self.build_button.clicked.connect(self.show_greeting)
    self.button_box.addWidget(self.build_button)
    self.layout.addLayout(self.button_box)

  @Slot()
  def show_greeting(self):
    self.greeting.setText(
      'Hello, {}!'.format(self.recipient.text())
    )


class Main(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.setWindowTitle('Main')
    self.setMinimumWidth(400)

    self.centralWidget = QWidget(self)
    self.setCentralWidget(self.centralWidget)

    self.layout = QVBoxLayout()
    self.layout.addStretch(1)
    self.centralWidget.setLayout(self.layout)

    self.showButton = QPushButton('Show dialog', self)
    self.showButton.clicked.connect(self.show_greeter)
    self.layout.addWidget(self.showButton)


    self.greeter = Greeter()

  @Slot()
  def show_greeter(self):
    self.greeter.show()


# Create an instance of the application window and run it

# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)

# app = Main()
app = Greeter()
app.show()

qt_app.exec_()
