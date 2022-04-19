from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import log_plot
import ShowImage_TopRight

class topleft(QWidget):
    def __init__(self):
        super(topleft, self).__init__()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.tabWidget = QTabWidget()
        self.btu1 = QPushButton('增加')
        self.btu2 = QPushButton('删除')
        self.tab1 = QWidget()
        self.tab1.setObjectName('训练数据')
        self.tab2 = QWidget()
        self.tab2.setObjectName('验证数据')
        self.tab3 = QWidget()
        self.tab3.setObjectName('测试数据')
        self.tabWidget.addTab(self.tab1,'训练数据')
        self.tabWidget.addTab(self.tab2,'验证数据')
        self.tabWidget.addTab(self.tab3,'测试数据')
        self.hbox1.addStretch(0)
        self.hbox1.addWidget(self.btu1)
        self.hbox1.addWidget(self.btu2)
        self.hbox1.addStretch(1)
        self.hbox.addWidget(self.tabWidget)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.setLayout(self.vbox)
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.setPalette(palette1)
        self.btu1.clicked.connect(self.clicked_btu1)
        self.btu2.clicked.connect(self.clicked_btu2)
        self.setAutoFillBackground(True)
    def clicked_btu1(self):
        self.Treeviewwidget = QWidget()
        self.Treeviewwidget.resize(500,500)
        self.Treeviewwidget.setWindowTitle('数据资源')
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()
        self.model = QDirModel()
        self.tree = QTreeView()
        self.btu = QPushButton('确定')
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index('./data'))
        hbox1.addWidget(self.tree)
        hbox2.addStretch(0)
        hbox2.addWidget(self.btu)
        hbox2.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.tree.clicked.connect(self.tree_clicked)
        self.btu.clicked.connect(self.clicked_btn)
        self.Treeviewwidget.setLayout(vbox)
        self.Treeviewwidget.show()
    def clicked_btu2(self):
        if self.tabWidget.currentWidget().objectName() == '训练数据':
            row = self.listwidget_train.currentRow()
            self.listwidget_train.takeItem(row)
        if self.tabWidget.currentWidget().objectName() == '验证数据':
            row = self.listwidget_val.currentRow()
            self.listwidget_val.takeItem(row)
        if self.tabWidget.currentWidget().objectName() == '测试数据':
            row = self.listwidget_test.currentRow()
            self.listwidget_test.takeItem(row)
        QApplication.processEvents()
    def tree_clicked(self,Qmodelidx):
        self.filePath = self.model.filePath(Qmodelidx)
        self.fileName = self.model.fileName(Qmodelidx)
        self.fileInfo = self.model.fileInfo(Qmodelidx)
    def clicked_btn(self):
        if self.tabWidget.currentWidget().objectName() == '训练数据':
            self.listwidget_train.addItem(self.fileName)
        if self.tabWidget.currentWidget().objectName() == '验证数据':
            self.listwidget_val.addItem(self.fileName)
        if self.tabWidget.currentWidget().objectName() == '测试数据':
            self.listwidget_test.addItem(self.fileName)
        QApplication.processEvents()
    def tab1UI(self):
        layout = QHBoxLayout()
        self.listwidget_train = QListWidget()
        layout.addWidget(self.listwidget_train)
        self.tab1.setLayout(layout)
    def tab2UI(self):
        layout = QHBoxLayout()
        self.listwidget_val = QListWidget()
        layout.addWidget(self.listwidget_val)
        self.tab2.setLayout(layout)
    def tab3UI(self):
        layout = QHBoxLayout()
        self.listwidget_test = QListWidget()
        layout.addWidget(self.listwidget_test)
        self.tab3.setLayout(layout)

class topright(QWidget):
    def __init__(self):
        super(topright, self).__init__()
        self.initUI()

    def initUI(self):
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.label1 = QLabel('测井曲线数据可视化')
        self.hbox1.addStretch(0)
        self.hbox1.addWidget(self.label1)
        self.hbox1.addStretch(1)
        self.btuWidget = QWidget()
        self.button1 = QPushButton('训练数据')
        self.button2 = QPushButton('验证数据')
        self.button3 = QPushButton('测试数据')
        self.butVbox = QVBoxLayout()
        self.butVbox.addStretch(0)
        self.butVbox.addWidget(self.button1)
        self.butVbox.addWidget(self.button2)
        self.butVbox.addWidget(self.button3)
        self.butVbox.addStretch(1)
        self.btuWidget.setLayout(self.butVbox)

        self.stack = QStackedWidget()
        self.stack1 = ShowImage_TopRight.ApplicationWindow()
        self.stack2 = ShowImage_TopRight.ApplicationWindow()
        self.stack3 = ShowImage_TopRight.ApplicationWindow()
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.hbox2.addWidget(self.btuWidget)
        self.hbox2.addWidget(self.stack)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        palette = QPalette()
        palette.setColor(self.btuWidget.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.btuWidget.setPalette(palette)
        self.btuWidget.setAutoFillBackground(True)
        palette1 = QPalette()
        palette.setColor(self.stack1.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.stack1.setPalette(palette)
        self.stack1.setAutoFillBackground(True)
        palette2 = QPalette()
        palette.setColor(self.stack2.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.stack2.setPalette(palette)
        self.stack2.setAutoFillBackground(True)
        palette3 = QPalette()
        palette.setColor(self.stack3.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.stack3.setPalette(palette)
        self.stack3.setAutoFillBackground(True)

    def tab1UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.stack1.label = QLabel('训练数据')
        hbox.addWidget(self.stack1.label)

        vbox.addLayout(hbox)
        self.stack1.setLayout(vbox)
    def tab2UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.stack2.label = QLabel('验证数据')
        hbox.addWidget(self.stack2.label)

        vbox.addLayout(hbox)
        self.stack2.setLayout(vbox)
    def tab3UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.stack3.label = QLabel('测试数据')
        hbox.addWidget(self.stack3.label)

        vbox.addLayout(hbox)
        self.stack3.setLayout(vbox)

    # def display(self,index):
    #     self.stack.setCurrentIndex(index)

class downleft(QWidget):
    def __init__(self):
        super(downleft, self).__init__()
        self.initUI()
        self.data_train = None
        self.data_val = None
        self.data_test = None
        self.feature_pre = None
        self.feature_selected = []

    def initUI(self):

        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox = QHBoxLayout()
        self.button_Run = QPushButton()
        self.button_Run.setText('运行')
        self.tabWidget = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabWidget.addTab(self.tab1, '输入特征')
        self.tabWidget.addTab(self.tab2, '预测目标')
        self.tabWidget.addTab(self.tab3, '模型参数')
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.button_Run)
        self.hbox1.addWidget(self.tabWidget)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def feaChecked_show(self):
        self.feature_selected = []
        for i in range(self.layout_tab1_grid.count()):
            if self.layout_tab1_grid.itemAt(i).widget().isChecked() == True:
                print(self.layout_tab1_grid.itemAt(i).widget().text())
                self.feature_selected.append(self.layout_tab1_grid.itemAt(i).widget().text())
        print('输入特征-------------------------------------------------------------')
    def feaChecked_show2(self):
        self.feature_pre = None
        for i in range(self.layout_tab2_grid.count()):
            if self.layout_tab2_grid.itemAt(i).widget().isChecked() == True:
                print(self.layout_tab2_grid.itemAt(i).widget().text())
                self.feature_pre = self.layout_tab2_grid.itemAt(i).widget().text()
        print('预测目标-------------------------------------------------------------')
    def tab1UI(self):
        self.layout_tab1 = QVBoxLayout()
        self.layout_tab1_grid = QGridLayout()
        self.layout_tab1.addStretch(0)
        self.layout_tab1.addLayout(self.layout_tab1_grid)
        self.layout_tab1.addStretch(1)
        self.tab1.setLayout(self.layout_tab1)
    def tab2UI(self):
        self.layout_tab2 = QVBoxLayout()
        self.layout_tab2_grid = QGridLayout()
        self.layout_tab2.addStretch(0)
        self.layout_tab2.addLayout(self.layout_tab2_grid)
        self.layout_tab2.addStretch(1)
        self.tab2.setLayout(self.layout_tab2)


class downright_c(QWidget):
    def __init__(self):
        super(downright_c, self).__init__()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.label_acc = QLabel('准确率:')
        self.textLine_acc = QLineEdit()
        self.label_f1 = QLabel('F1得分:')
        self.textLine_f1 = QLineEdit()
        self.label_recall = QLabel('召回率:')
        self.textLine_recall = QLineEdit()
        self.btu = QLabel('算法运行结果')
        self.hbox.addStretch(0)
        self.hbox.addWidget(self.btu)
        self.hbox.addStretch(1)

        self.showWidget = QTextBrowser()
        qfont = QFont()
        qfont.setPointSize(23)
        self.showWidget.setFont(qfont)
        self.showWidget.setEnabled(True)
        self.hbox1.addWidget(self.showWidget)
        self.hbox2.addStretch(0)
        self.hbox2.addWidget(self.label_acc)
        self.hbox2.addWidget(self.textLine_acc)
        self.hbox2.addWidget(self.label_recall)
        self.hbox2.addWidget(self.textLine_recall)
        self.hbox2.addWidget(self.label_f1)
        self.hbox2.addWidget(self.textLine_f1)
        self.hbox2.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)
        palette = QPalette()
        palette.setColor(self.showWidget.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.showWidget.setPalette(palette)
        self.showWidget.setAutoFillBackground(True)


class downright_r(QWidget):
    def __init__(self):
        super(downright_r, self).__init__()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.label_mae = QLabel('MAE:')
        self.textLine_mae = QLineEdit()
        self.label_mse = QLabel('MSE:')
        self.textLine_mse = QLineEdit()
        self.label_r2 = QLabel('R2')
        self.textLine_r2 = QLineEdit()
        self.btu = QLabel('算法运行结果')
        self.hbox.addStretch(0)
        self.hbox.addWidget(self.btu)
        self.hbox.addStretch(1)

        self.showWidget = QTextBrowser()
        qfont = QFont()
        qfont.setPointSize(23)
        self.showWidget.setFont(qfont)
        self.showWidget.setEnabled(True)
        self.hbox1.addWidget(self.showWidget)
        self.hbox2.addStretch(0)
        self.hbox2.addWidget(self.label_mae)
        self.hbox2.addWidget(self.textLine_mae)
        self.hbox2.addWidget(self.label_mse)
        self.hbox2.addWidget(self.textLine_mse)
        self.hbox2.addWidget(self.label_r2)
        self.hbox2.addWidget(self.textLine_r2)
        self.hbox2.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)
        palette = QPalette()
        palette.setColor(self.showWidget.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.showWidget.setPalette(palette)
        self.showWidget.setAutoFillBackground(True)

class downright_cl(downright_r):
    def __init__(self):
        super().__init__()
    def initUI(self):
        self.hbox = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.showWidget = QTextBrowser()
        qfont = QFont()
        qfont.setPointSize(23)
        self.showWidget.setFont(qfont)
        self.showWidget.setEnabled(True)
        self.hbox1.addWidget(self.showWidget)
        self.hbox2.addStretch(0)
        self.hbox2.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)
        palette = QPalette()
        palette.setColor(self.showWidget.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.showWidget.setPalette(palette)
        self.showWidget.setAutoFillBackground(True)