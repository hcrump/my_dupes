# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_filelist.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 765)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filetree = QtWidgets.QTreeView(self.centralwidget)
        self.filetree.setObjectName("filetree")
        self.horizontalLayout.addWidget(self.filetree)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setObjectName("btn1")
        self.verticalLayout_2.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setObjectName("btn2")
        self.verticalLayout_2.addWidget(self.btn2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setObjectName("btn3")
        self.verticalLayout_2.addWidget(self.btn3)
        self.radiobysize = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobysize.setChecked(True)
        self.radiobysize.setObjectName("radiobysize")
        self.verticalLayout_2.addWidget(self.radiobysize)
        self.radiobyname = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobyname.setObjectName("radiobyname")
        self.verticalLayout_2.addWidget(self.radiobyname)
        self.radiobyhash = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobyhash.setChecked(False)
        self.radiobyhash.setObjectName("radiobyhash")
        self.verticalLayout_2.addWidget(self.radiobyhash)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.shortlist = QtWidgets.QListWidget(self.centralwidget)
        self.shortlist.setObjectName("shortlist")
        self.horizontalLayout.addWidget(self.shortlist)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.filelist = QtWidgets.QTreeWidget(self.centralwidget)
        self.filelist.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.filelist.setAutoFillBackground(True)
        self.filelist.setAlternatingRowColors(True)
        self.filelist.setAnimated(True)
        self.filelist.setObjectName("filelist")
        self.filelist.headerItem().setTextAlignment(0, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.filelist.headerItem().setFont(0, font)
        self.verticalLayout.addWidget(self.filelist)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDON_T_DO_IT = QtWidgets.QAction(MainWindow)
        self.actionDON_T_DO_IT.setObjectName("actionDON_T_DO_IT")
        self.menuMenu.addAction(self.actionDON_T_DO_IT)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "Select ->"))
        self.btn2.setText(_translate("MainWindow", "Delete"))
        self.btn3.setText(_translate("MainWindow", "Scan"))
        self.radiobysize.setText(_translate("MainWindow", "By Size"))
        self.radiobyname.setText(_translate("MainWindow", "By Name"))
        self.radiobyhash.setText(_translate("MainWindow", "By Hash"))
        self.filelist.setWhatsThis(_translate("MainWindow", "wtf"))
        self.filelist.setSortingEnabled(True)
        self.filelist.headerItem().setText(0, _translate("MainWindow", " Key                    Value"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionDON_T_DO_IT.setText(_translate("MainWindow", "DON\"T DO IT!!!"))

