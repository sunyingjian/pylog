import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import init_ui
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import sklearn.metrics as metrics
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def data_process(train_path,validation_path,select_features,pre_feature):
    train_data = pd.read_csv(train_path)
    valid_data = pd.read_csv(validation_path)
    train_data_x = train_data.loc[:,select_features]
    train_data_y = train_data[pre_feature]
    valid_data_x = valid_data.loc[:,select_features]
    valid_data_y = valid_data[pre_feature]
    data = {'X_train':train_data_x,'y_train':train_data_y,'X_valid':valid_data_x,'y_valid':valid_data_y}
    return data

def train_useGBDTR(data,options):
    model = make_pipeline(StandardScaler(),GradientBoostingRegressor(n_estimators=int(options['n_estimators']),
                criterion=options['criterion'],
                loss=options['loss']))
    model.fit(data['X_train'],data['y_train'])
    y_pred = model.predict(data['X_valid'])
    mae = metrics.median_absolute_error(data['y_valid'],y_pred)
    mse = metrics.mean_squared_error(data['y_valid'],y_pred)
    r2 = metrics.r2_score(data['y_valid'],y_pred)
    res = {'MAE':mae,
           'MSE':mse,
           'R2':r2,
           'data':y_pred}
    return res

class Downleft(init_ui.downleft):
    def __init__(self):
        super().__init__()
    def tab3UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.label_criterion = QLabel("切分标准")
        self.label_criterion.setEnabled(True)
        self.combox_criterion = QComboBox()
        self.combox_criterion.setEnabled(True)
        self.combox_criterion.addItem("")
        self.combox_criterion.addItem("")
        self.combox_criterion.addItem("")
        self.combox_criterion.setCurrentText("friedman_mse")
        self.combox_criterion.setItemText(0, "friedman_mse")
        self.combox_criterion.setItemText(1, "mse")
        self.combox_criterion.setItemText(2, "mae")
        self.label_loss = QLabel("loss")
        self.label_loss.setEnabled(True)
        self.combox_loss = QComboBox()
        self.combox_loss.setEnabled(True)
        self.combox_loss.addItem("")
        self.combox_loss.addItem("")
        self.combox_loss.addItem("")
        self.combox_loss.addItem("")
        self.combox_loss.setCurrentText("ls")
        self.combox_loss.setItemText(0, "ls")
        self.combox_loss.setItemText(1, "lad")
        self.combox_loss.setItemText(2, "huber")
        self.combox_loss.setItemText(3, "quantile")
        self.label_n_estimators = QLabel("n_estimators")
        self.label_n_estimators.setEnabled(True)
        self.spinBox_n_estimators = QSpinBox()
        self.spinBox_n_estimators.setEnabled(True)
        self.spinBox_n_estimators.setPrefix('')
        self.spinBox_n_estimators.setMinimum(5)
        self.spinBox_n_estimators.setMaximum(1000)
        self.spinBox_n_estimators.setSingleStep(1)
        self.spinBox_n_estimators.setProperty("value", 100)
        self.spinBox_n_estimators.setObjectName("n_estimators")
        formLayout = QFormLayout()
        formLayout.addRow(self.label_criterion, self.combox_criterion)
        formLayout.addRow(self.label_loss, self.combox_loss)
        formLayout.addRow(self.label_n_estimators, self.spinBox_n_estimators)
        hbox.addLayout(formLayout)
        vbox.addLayout(hbox)
        self.tab3.setLayout(vbox)


class newMainWindow(QWidget):
    def __init__(self):
        super(newMainWindow, self).__init__()
        self.initUI()
        self.setObjectName('GBDT')

    def initUI(self):
        # self.widget = QWidget()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.setWindowTitle('CIFLOg')
        self.setWindowState(Qt.WindowMaximized)
        self.topleft = init_ui.topleft()
        palette1 = QPalette()
        palette1.setColor(self.topleft.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.topleft.setPalette(palette1)
        self.topleft.setAutoFillBackground(True)

        self.downleft = Downleft()
        palette2 = QPalette()
        palette2.setColor(self.downleft.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.downleft.setPalette(palette2)
        self.downleft.setAutoFillBackground(True)

        self.topright = init_ui.topright()
        palette3 = QPalette()
        palette3.setColor(self.topright.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.topright.setPalette(palette3)
        self.topright.setAutoFillBackground(True)

        self.downright = init_ui.downright_r()
        palette4 = QPalette()
        palette4.setColor(self.downright.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.downright.setPalette(palette4)
        self.downright.setAutoFillBackground(True)

        self.splitter1 = QSplitter(Qt.Vertical)
        self.splitter1.addWidget(self.topleft)
        self.splitter1.addWidget(self.downleft)
        self.splitter1.setSizes([100, 200])
        self.vbox1.addWidget(self.splitter1)
        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.addWidget(self.topright)
        self.splitter2.addWidget(self.downright)
        self.splitter2.setSizes([100,100])
        self.splitter3 = QSplitter(Qt.Horizontal)
        self.splitter3.addWidget(self.splitter1)
        self.splitter3.addWidget(self.splitter2)
        self.splitter3.setSizes([100,500])
        self.vbox2.addWidget(self.splitter2)
        self.hbox.addWidget(self.splitter3)
        self.setLayout(self.hbox)
        self.topleft.listwidget_train.clicked.connect(self.downleft_fea)
        self.topleft.listwidget_val.clicked.connect(self.downleft_fea)
        self.topleft.listwidget_test.clicked.connect(self.downleft_fea)
        self.downleft.button_Run.clicked.connect(self.fun_Run)

    def downleft_fea(self):
        if self.topleft.tabWidget.currentWidget().objectName() == '训练数据':
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().deleteLater()
            datafile = pd.read_csv('./data/' + self.topleft.listwidget_train.currentItem().text())
            self.downleft.data_train = self.topleft.listwidget_train.currentItem().text()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab1_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().deleteLater()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab2_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show2)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.showimage_topright)
        if self.topleft.tabWidget.currentWidget().objectName() == '验证数据':
            datafile = pd.read_csv('./data/' + self.topleft.listwidget_val.currentItem().text())
            self.downleft.data_val = self.topleft.listwidget_val.currentItem().text()
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().deleteLater()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab1_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().deleteLater()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab2_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show2)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.showimage_topright)
        if self.topleft.tabWidget.currentWidget().objectName() == '测试数据':
            datafile = pd.read_csv('./data/' + self.topleft.listwidget_test.currentItem().text())
            self.downleft.data_test = self.topleft.listwidget_test.currentItem().text()
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().deleteLater()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab1_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().deleteLater()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab2_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show2)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.showimage_topright)
        QApplication.processEvents()

    def fun_Run(self):
        print('进入fun_Run函数')
        if (self.downleft.data_train != None) and (self.downleft.data_val != None) and (len(self.downleft.feature_selected) != 0) and (
                self.downleft.feature_pre != None):
            datafile_train = './data/' + self.downleft.data_train
            datafile_test = './data/' + self.downleft.data_val
            data_test = pd.read_csv(datafile_train)
            criterion = self.downleft.combox_criterion.currentText()
            loss = self.downleft.combox_loss.currentText()
            n_estimators = self.downleft.spinBox_n_estimators.value()
            options = {'criterion': criterion,
                       'loss': loss, 'n_estimators': n_estimators,
                       }
            data = data_process(datafile_train, datafile_test, self.downleft.feature_selected, self.downleft.feature_pre)
            res = train_useGBDTR(data, options)
            self.downright.textLine_acc.setText(str(res['acc']))
            self.downright.textLine_recall.setText(str(res['recall_score']))
            self.downright.textLine_f1.setText(str(res['f1_score']))
            print(str(res['confusion_matrix']))
            self.downright.showWidget.setText(str(res['confusion_matrix']))
        print('退出fun_run函数')
    def showimage_topright(self):
            for i in range(self.downleft.layout_tab1_grid.count()):
                if self.downleft.layout_tab1_grid.itemAt(i).widget().isChecked() == True:
                    # print(self.layout_tab1_grid.itemAt(i).widget().text())
                    self.topright.stack1.features_show.append(self.downleft.layout_tab1_grid.itemAt(i).widget().text())
            self.topright.stack1.initUI()
    #如果关闭了主窗体，则所有窗体都关闭
    def closeEvent(self, event):
        sys.exit(0)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    newmainwindow = newMainWindow()
    newmainwindow.show()
    sys.exit(app.exec_())
