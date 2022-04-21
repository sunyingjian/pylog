import os
import shutil
import sys
import SVC_Run
import SVR_Run
import GMM_Run
import KNN_Run
import Tree_Run
import Kmeans_Run
import RF_Run
import RFR_Run
import GBDT_Run
import GBDTR_Run
import MLR_Run
import MLP_Run
import Ridge_Run
import TreeR_Run
import MLPR_Run
import LSTM_Run
import LSTMR_Run
import RTCN_Run
import SAPWFF_Run
import LR_Run
import Lasso_Run
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QAction
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
from PyQt5 import QtWidgets


class Main_Win(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.initUI()



    def initUI(self):
        # 初始窗口最大化
        # self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('自动化测井辅助解释软件 PyLog')
        self.resize(1756, 873)

        #设置绘图背景
        pg.setConfigOption('background','#19232D')
        pg.setConfigOption('foreground','d')
        pg.setConfigOptions(antialias = True)

        #设置透明度
        self.setWindowOpacity(0.8)
        #self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint) #隐藏边框
        self.setAttribute(QtCore.Qt.WA_TintedBackground)

        #主窗口添加菜单部分
        menu = self.menuBar()  # 当前Main_WinM窗体创建menuBar
        file_menu = menu.addMenu('文件')
        edit_menu = menu.addMenu('编辑')
        tool_menu = menu.addMenu('工具')
        window_menu = menu.addMenu('窗口')
        help_menu = menu.addMenu('帮助')

        action_new = QAction('新建',self)
        action_new.setStatusTip('新建项目')  # 状态栏信息
        action_new.setShortcut('Ctrl+N')  # 快捷键设置
        action_new.triggered.connect(self.file_new_action)   #新建项目
        action_open = QAction('打开',self)
        action_open.setStatusTip('打开项目目录')
        action_open.setShortcut('Ctrl+O')
        action_open.triggered.connect(self.file_open_action)
        action_save = QAction('另存为',self)
        action_save.setStatusTip('另存为')
        action_exit = QAction('关闭', self)
        action_exit.setStatusTip('关闭软件')
        action_exit.triggered.connect(self.app.quit)  # 触发事件动作为"关闭窗口"
        action_exit.setShortcut('Ctrl+Q')
        action_maskwin = QAction('任务栏',self)
        action_maskwin.setStatusTip('打开任务栏')
        action_maskwin.triggered.connect(self.mask_win)
        help_about = QAction('关于',self)
        help_about.setStatusTip('关于')


        self.statusBar()  # 状态栏信
        file_menu.addAction(action_new)
        file_menu.addAction(action_open)
        file_menu.addAction(action_save)
        file_menu.addAction(action_exit)
        window_menu.addAction(action_maskwin)
        help_menu.addAction(help_about)


        #最左边任务栏
        # mask_bar = QWidget()
        # mask_bar.setObjectName("mask_bar")
        # mask_bar.setStyleSheet("#mask_bar{background:rgba(255,255,255)}")
        # mask_bar.setStyleSheet("#mask_bar{border:1px solid black}")
        # mask_bar.setFixedWidth(30)
        # mask_btn = QtWidgets.QPushButton(mask_bar)
        # mask_btn.setText("任\n务\n栏")
        # mask_btn.setFixedWidth(30)
        # mask_btn.setFixedHeight(80)
        # mask_btn.clicked.connect(self.mask_visible)


        #主窗口
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        self.main_page = QTabWidget()
        self.main_page.setTabsClosable(True)    #tab中删除图标 可见
        self.main_page.tabCloseRequested.connect(self.tabclose)   #tab关闭的 点击信号
        self.hello_tab = self.hello_page()
        self.setCentralWidget(self.main_page)
        self.main_page.addTab(self.hello_tab, '欢迎页')
        self.exist_maskwin = False  #判断任务栏是否存在
        self.setWindowIcon(QIcon('./image/a.ico'))

    def font_style(self,tabs):
        tabs.setStyleSheet("    color:Block;\n"
                             "    font-family:微软雅黑;\n"
                             "    font-size:8px;\n"
                             )


    #任务栏 （使用停靠窗口）
    def mask_win(self):
        if self.exist_maskwin == False:
            self.maskWin = QDockWidget("任务栏", self)
            self.mask_win = QTabWidget()
            # 选项卡
            self.tab1 = QWidget()  # 分类
            self.tab2 = QWidget()  # 回归
            self.tab3 = QWidget()  # 聚类
            self.tab4 = QWidget()  # 综合分析
            self.tab1UI()
            self.tab2UI()
            self.tab3UI()
            self.tab4UI()

            self.mask_win.addTab(self.tab1, '分类')
            self.mask_win.addTab(self.tab2, '回归')
            self.mask_win.addTab(self.tab3, '聚类')
            self.mask_win.addTab(self.tab4, '综合分析')
            self.mask_win.setTabPosition(QTabWidget.South)
            self.maskWin.setWidget(self.mask_win)
            self.exist_maskwin = True
            #将任务栏加入主窗口
            self.addDockWidget(Qt.LeftDockWidgetArea,self.maskWin)
        else:
            self.maskWin.setVisible(True)


    #tab 删除的实现
    def tabclose(self,index):
        self.main_page.setTabVisible(index,False)
        #self.main_page.tabBar().removeTab(index)

    def file_open_action(self):
        files,_ = QFileDialog.getOpenFileNames(self,"选取文件",os.getcwd())
        print(files)
        for i in range(len(files)):
            _, filename = os.path.split(files[i])
            newfile = '../data/'+ filename
            shutil.copyfile(files[i],newfile)

    def file_new_action(self):
        pass
    
    def fontui(self,btn,size=80):
        btn.setFixedHeight(size)
        btn.setGeometry(QtCore.QRect(310, 330, 81, 25))
        # btn.setFixedHeight(80)
        btn.setStyleSheet("QPushButton{\n"
                             "    color:Block;\n"
                             "    font-family:微软雅黑;\n"
                             "    border: 1px solid DarkGray;\n"
                             "    font-size:24px;\n"
                             "}\n"
                             "QPushButton:hover{\n"
                             "    border: 1px solid Gray;\n"
                             "}\n"
                             "QPushButton:pressed{\n"
                             "    border: 2px solid DarkGray;\n"
                             "}")

    def tab1UI(self):
        layout1 = QGridLayout()
        self.tab1.setLayout(layout1)
        btn_LR = QPushButton('逻辑回归')
        self.fontui(btn_LR)
        btn_LR.clicked.connect(lambda:self.Add_Page(LR_Run.newMainWindow()))

        btn_SVM = QPushButton('支持向量机')
        self.fontui(btn_SVM)
        btn_SVM.clicked.connect(lambda:self.Add_Page(SVC_Run.newMainWindow()))
        
        btn_RF = QPushButton('随机森林')
        self.fontui(btn_RF)
        btn_RF.clicked.connect(lambda :self.Add_Page(RF_Run.newMainWindow()))

        btn_KNN = QPushButton('K近邻')
        self.fontui(btn_KNN)
        btn_KNN.clicked.connect(lambda :self.Add_Page(KNN_Run.newMainWindow()))

        btn_tree = QPushButton('决策树')
        self.fontui(btn_tree)
        btn_tree.clicked.connect(lambda :self.Add_Page(Tree_Run.newMainWindow()))

        btn_gbdt = QPushButton('梯度提升决策树')
        self.fontui(btn_gbdt)
        btn_gbdt.clicked.connect(lambda :self.Add_Page(GBDT_Run.newMainWindow()))

        btn_gmm = QPushButton('高斯混合模型')
        self.fontui(btn_gmm)
        btn_gmm.clicked.connect(lambda :self.Add_Page(GMM_Run.newMainWindow()))


        btn_dnn = QPushButton('全连接神经网络')
        self.fontui(btn_dnn)
        btn_dnn.clicked.connect(lambda :self.Add_Page(MLP_Run.newMainWindow()))

        btn_lstm = QPushButton('LSTM模型')
        self.fontui(btn_lstm)
        btn_lstm.clicked.connect(lambda :self.Add_Page(LSTM_Run.newMainWindow()))

        btn_sapwff = QPushButton('SAPWFF')
        self.fontui(btn_sapwff)
        btn_sapwff.clicked.connect(lambda :self.Add_Page(SAPWFF_Run.newMainWindow()))

        layout1.addWidget(btn_SVM,0,0,1,2,Qt.AlignTop)
        layout1.addWidget(btn_LR,1,0,1,1,Qt.AlignTop)
        layout1.addWidget(btn_RF,3,1,Qt.AlignTop)
        layout1.addWidget(btn_KNN,1,1,Qt.AlignTop)
        layout1.addWidget(btn_tree,3,0,Qt.AlignTop)
        layout1.addWidget(btn_gbdt,4,0,1,2,Qt.AlignTop)
        layout1.addWidget(btn_gmm,2,0,1,2,Qt.AlignTop)
        layout1.addWidget(btn_dnn,6,0,1,2,Qt.AlignTop)
        layout1.addWidget(btn_lstm,5,0,1,1,Qt.AlignTop)
        layout1.addWidget(btn_sapwff,5,1,1,1,Qt.AlignTop)



    def tab2UI(self):
        layout1 = QGridLayout()
        self.tab2.setLayout(layout1)
        btn_MLR = QPushButton('多元线性回归')
        self.fontui(btn_MLR)
        btn_MLR.clicked.connect(lambda:self.Add_Page(MLR_Run.newMainWindow()))

        btn_ridge = QPushButton('岭回归')
        self.fontui(btn_ridge)
        btn_ridge.clicked.connect(lambda: self.Add_Page(Ridge_Run.newMainWindow()))

        btn_lasso = QPushButton('套索回归')
        self.fontui(btn_lasso)
        btn_lasso.clicked.connect(lambda: self.Add_Page(Lasso_Run.newMainWindow()))

        btn_SVR = QPushButton('支持向量回归')
        self.fontui(btn_SVR)
        btn_SVR.clicked.connect(lambda: self.Add_Page(SVR_Run.newMainWindow()))

        btn_tree = QPushButton('决策树')
        self.fontui(btn_tree)
        btn_tree.clicked.connect(lambda: self.Add_Page(TreeR_Run.newMainWindow()))

        btn_rf = QPushButton('随机森林')
        self.fontui(btn_rf)
        btn_rf.clicked.connect(lambda: self.Add_Page(RFR_Run.newMainWindow()))

        btn_gbdt = QPushButton('梯度提升决策树')
        self.fontui(btn_gbdt)
        btn_gbdt.clicked.connect(lambda: self.Add_Page(GBDTR_Run.newMainWindow()))

        btn_dnn = QPushButton('全连接神经网络')
        self.fontui(btn_dnn)
        btn_dnn.clicked.connect(lambda: self.Add_Page(MLPR_Run.newMainWindow()))

        btn_lstm = QPushButton('LSTM模型')
        self.fontui(btn_lstm)
        btn_lstm.clicked.connect(lambda: self.Add_Page(LSTMR_Run.newMainWindow()))

        btn_rtcn = QPushButton('R-TCN模型')
        self.fontui(btn_rtcn)
        btn_rtcn.clicked.connect(lambda: self.Add_Page(RTCN_Run.newMainWindow()))

        layout1.addWidget(btn_MLR, 0, 0, 1, 2, Qt.AlignTop)
        layout1.addWidget(btn_ridge, 1, 0, 1, 1,Qt.AlignTop)
        layout1.addWidget(btn_lasso, 1, 1, 1, 1,Qt.AlignTop)
        layout1.addWidget(btn_SVR,2,0,1,2,Qt.AlignTop)
        layout1.addWidget(btn_tree,3,0,1,1,Qt.AlignTop)
        layout1.addWidget(btn_rf,3,1,1,1,Qt.AlignTop)
        layout1.addWidget(btn_gbdt,4,0,1,2,Qt.AlignTop)
        layout1.addWidget(btn_dnn,5,0,1,2,Qt.AlignTop)
        layout1.addWidget(btn_lstm,6,0,1,1,Qt.AlignTop)
        layout1.addWidget(btn_rtcn,6,1,1,1,Qt.AlignTop)

    def tab3UI(self):
        layout1 = QGridLayout()
        self.tab3.setLayout(layout1)
        btn_kmeans = QPushButton('K聚类')
        self.fontui(btn_kmeans)
        btn_kmeans.clicked.connect(lambda: self.Add_Page(Kmeans_Run.newMainWindow()))

        btn_lda = QPushButton('LDA聚类')
        self.fontui((btn_lda))


        layout1.addWidget(btn_kmeans,0,0,1,1,Qt.AlignTop)
        layout1.addWidget(btn_lda,0,1,1,1,Qt.AlignTop)


    def tab4UI(self):
        layout1 = QGridLayout()
        self.tab4.setLayout(layout1)

        btn_smote = QPushButton('SMOTE')
        self.fontui(btn_smote)

        btn_pca = QPushButton('PCA')
        self.fontui(btn_pca)

        layout1.addWidget(btn_smote, 0, 0, 1, 1, Qt.AlignTop)
        layout1.addWidget(btn_pca, 0, 1, 1, 1, Qt.AlignTop)

    def hello_page(self):
        h = QWidget()
        page_layout = QHBoxLayout()
        h.setLayout(page_layout)
        label = QLabel()
        page_layout.addWidget(label)

        #h.setObjectName("MainWindow")
        #h.setStyleSheet("#MainWindow{border-image:url(./image/a.jpg);}")
        font = QtGui.QFont()
        font.setFamily("默陌信笺手写体")
        font.setPointSize(60)
        label.setFont(font)
        label.setTextFormat(QtCore.Qt.AutoText)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText("石油战线始终是共和国\n"
                      "改革发展的一面旗帜。")
        label.setStyleSheet('color:rgb(0, 0, 0)')
        label.setScaledContents(True)
        return h

    def Add_Page(self,new_page=None):
        page_name = new_page.objectName()
        self.main_page.addTab(new_page, page_name)
        index = self.main_page.indexOf(new_page)
        # print(index)
        self.main_page.setCurrentIndex(index)
        #print(self.main_page.currentWidget())



if __name__=='__main__':
    Main_Win = Main_Win()
    Main_Win.show()
    sys.exit(Main_Win.app.exec())