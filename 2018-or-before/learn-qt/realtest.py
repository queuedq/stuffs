from PySide2 import QtCore, QtWidgets
import sys

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, parent=None):
    QtWidgets.QMainWindow.__init__(self)
    self.resize(400, 280)

    self.centralWidget = QtWidgets.QWidget(self)
    self.setCentralWidget(self.centralWidget)

    self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
    self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 360, 240))

    self.gridLayout = QtWidgets.QHBoxLayout(self.gridLayoutWidget)


    self.searchInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
    self.gridLayout.addWidget(self.searchInput)

    self.searchButton = QtWidgets.QPushButton(self.gridLayoutWidget)
    self.gridLayout.addWidget(self.searchButton)

    self.downloadButton = QtWidgets.QPushButton(self.gridLayoutWidget)
    self.gridLayout.addWidget(self.downloadButton)


    self.statusDisplay = QtWidgets.QLabel(self.gridLayoutWidget)
    self.gridLayout.addWidget(self.statusDisplay)


    self.setWindowTitle('map crawler')
    self.searchButton.setText('search')
    self.downloadButton.setText('download')
    # QtCore.QMetaObject.connectSlotsByName(self)

    self.searchButton.clicked.connect(self.search)

    self.config = ''
    # self.config.load()
    self.data = []

    # self.configDialog = ConfigDialog(self)
    # self.infoDialog = InfoDialog(self)

  @QtCore.Slot()
  def search(self):
    query = self.searchInput.text()
    self.statusDisplay.setText('Current entry: ' + query)


if __name__ == '__main__':
  app = QtWidgets.QApplication([])

  window = MainWindow()
  window.show()

  app.exec_()
