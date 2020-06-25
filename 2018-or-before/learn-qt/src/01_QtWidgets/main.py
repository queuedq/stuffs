# https://doc-snapshots.qt.io/qtforpython/tutorials/basictutorial/widgets.html

import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
# Or, if you don't need to pass any arguments:
# app = QApplication([])

# label = QLabel("Hello World!")
# This HTML approach will be valid too!
label = QLabel("<font color=red size=40>Hello World!</font>")

label.show()

app.exec_()
