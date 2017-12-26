import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont

import numpy as np
import matplotlib.pyplot as plt


# Comment
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()






if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



seabed = np.load('data/Penobscot_Seabed.npy')
fig = plt.figure(figsize=(15,6))
ax = fig.add_subplot(111)
plt.imshow(seabed, aspect=0.5, cmap="viridis_r", origin='lower')
cbar = plt.colorbar(label="Two-way time")
cbar.ax.invert_yaxis()
ax.set_xlabel("Inline")
ax.set_ylabel("Xline")
ax.grid(color='w', alpha=0.2)
plt.show()