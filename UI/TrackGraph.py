'''

使用PyQtGraph绘图

pip Install pyqtgraph
'''


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
import pyqtgraph as pg
from myMainWindow import MainWindow
import numpy as np



class GraphWindow(QMainWindow, MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        pg.setConfigOption('background', '#f0f0f0')
        pg.setConfigOption('foreground', 'd')
        self.myPlt = self.mainGraph.addPlot(title="场景绘制")

    def graph_paint(self, x_list, y_list, symbol="o"):

        self.myPlt.plot(x_list, y_list, pen=None,
                  name="Red curve", symbol=symbol)






if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    myPaint = GraphWindow()
    myPaint.graph_paint([1,2], [3, 4])
    sys.exit(app.exec_())
