import sys
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)  # We want the axes cleared every time plot() is called

        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):

    def compute_initial_figure(self):
        seabed = np.load('data/Penobscot_Seabed.npy')
        self.axes.imshow(seabed, aspect=0.5, cmap="viridis_r", origin='lower')


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QWidget(self)

        l = QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=8, height=6, dpi=200)
        l.addWidget(sc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About",
                          """embedding_in_qt5.py example
Copyright 2015 BoxControL
This program is a simple example of a Qt5 application embedding matplotlib
canvases. It is base on example from matplolib documentation, and initially was
developed from Florent Rougon and Darren Dale.
http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html
It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation."""
                          )


if __name__ == '__main__':
    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("PyQt5 Matplot Example")
    aw.show()
    # sys.exit(qApp.exec_())
    app.exec_()
