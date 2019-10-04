# https://doc-snapshots.qt.io/qtforpython/tutorials/basictutorial/qml.html

from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl
from os import path

app = QApplication([])
view = QQuickView()

dir = path.dirname(__file__)
url = QUrl(path.join(dir, "view.qml"))

view.setSource(url)
view.show()
app.exec_()
