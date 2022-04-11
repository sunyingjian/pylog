import sys
import pandas as pd
from PyQt5 import QtCore, QtWidgets
if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.features_show = []
        self.initUI()
        self.figure = None
    def initUI(self):
        self.train_data = pd.read_csv('./data/train_data.csv')
        self.train_data = self.train_data[self.train_data['Well Name'] == 'SHRIMPLIN']
        self.train_data = self.train_data.sort_values(by='Depth')
        self.ztop = self.train_data.Depth.min()
        self.zbot = self.train_data.Depth.max()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        self.colors = 'bgrcmykwbgrcmykw'
        layout = QtWidgets.QVBoxLayout(self._main)
        print(len(self.features_show))
        if len(self.features_show) != 0:
            if len(self.features_show) == 1:
                plt.cla()
                f,ax = plt.subplots()
                c = self.features_show[0]
                ax.plot(list(self.train_data.Depth),list(self.train_data[c]),color = self.colors[0])
                ax.grid()
                ax.set_ylabel(c)
                # self.static_canvas = FigureCanvas(f)
                # layout.addWidget(self.static_canvas)
                # self.addToolBar(NavigationToolbar(self.static_canvas, self))
                self.features_show=[]
            else:
                plt.cla()
                f, ax = plt.subplots(int(len(self.features_show)),1)
                indexs = 0
                for c in self.features_show:
                    print('c:',c)
                    if c == 'Depth' or c=='Formation'or c == 'Facies':
                        continue
                    ax[indexs].plot(list(self.train_data.Depth),list(self.train_data[c]),color = self.colors[indexs])
                    ax[indexs].set_ylabel(c)
                    ax[indexs].grid()
                    indexs += 1
                # for i in range(len(self.features_show) - 1):
                #     ax[i].set_ylim(self.ztop, self.zbot)
                #     ax[i].invert_yaxis()
                #     ax[i].grid()
                #     ax[i].locator_params(axis='x', nbins=3)
                self.features_show=[]
            self.static_canvas = FigureCanvas(f)
            layout.addWidget(self.static_canvas)

            # self.addToolBar(NavigationToolbar(self.static_canvas, self))
        # self.static_canvas = FigureCanvas(f)
        # layout.addWidget(self.static_canvas)
        # self.addToolBar(NavigationToolbar(self.static_canvas, self))
            # plt.show()
        # self._static_ax = static_canvas.figure.subplots()
        # self._static_ax.set_xlim([self.ztop,self.zbot])
        # self._static_ax.plot(self.train_data.Depth,self.train_data['GR'])
        # self._static_ax.grid()




if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()