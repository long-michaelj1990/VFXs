# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mocap_library_database.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDir, Qt, QUrl,QTimer
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,QListWidget,QRadioButton,QButtonGroup,QPushButton,QComboBox,QLineEdit,QLabel,QCheckBox,QStatusBar,QFileDialog,QMessageBox,
QListWidgetItem,QHBoxLayout,QVBoxLayout,QAction,QMenuBar,QStyle,QSlider,QSizePolicy,QFrame,QTabWidget)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer,QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
#from PIL import Image, ImageTk
import os
import shutil
from shutil import copyfile
import numpy as np
import time
import sys
import subprocess
os.add_dll_directory(r'C:/Program Files/VideoLAN/VLC')
import vlc
from threading import Thread, Lock
import telnetlib
import pygetwindow as gw

sys.path.insert(0, "C:/Program Files/Autodesk/MotionBuilder 2017/bin/x64/python")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        self.secondary_search=0
        self.pause_vid=0
        self.video_playing=0
        self.copy_browse_new=0
        self.mobu_open=0
                     
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1900, 1000)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(36, 36, 36);"))
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
       
        self.tabs = QTabWidget(MainWindow)
        self.tabs.setGeometry(QtCore.QRect(10, 30, 1860, 950))
        self.Tab1widget = QWidget(self.centralwidget)
        self.Tab2widget = QWidget(self.centralwidget)
        self.tabs.addTab(self.Tab1widget,"Library")
        self.tabs.addTab(self.Tab2widget,"Edit")
        
        # Create new action
        self.AboutAction = QAction(QIcon('about.png'), '&About')        
        self.AboutAction.setShortcut('?')
        self.AboutAction.setStatusTip('Library Information')
        self.AboutAction.triggered.connect(self.About_lib)

        # Create exit action
        self.OptionsAction = QAction(QIcon('Options.png'), '&Options')        
        self.OptionsAction.setShortcut('#')
        self.OptionsAction.setStatusTip('Options')
     #   self.exitAction.triggered.connect(self.Close)
        
        # Create exit action
        self.exitAction = QAction(QIcon('exit.png'), '&Exit')        
        self.exitAction.setShortcut('Esc')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(self.Close)

        # Create menu bar and add action
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.fileMenu = self.menuBar.addMenu('&File')
        self.fileMenu.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        #fileMenu.addAction(newAction)
        self.fileMenu.addAction(self.AboutAction)
        self.fileMenu.addAction(self.OptionsAction)
        self.fileMenu.addAction(self.exitAction)

        # Create a basic vlc instance
        self.media = None
        self.is_paused = False
        self.instance = vlc.Instance()
        self.mediaPlayer = self.instance.media_player_new()

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_ui)
        
#################################################################################################### - Files
        self.file_listwidget = QListWidget(self.Tab1widget)
        self.file_listwidget.setGeometry(QtCore.QRect(10, 160, 601, 191))
        self.file_listwidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.file_listwidget.setObjectName(_fromUtf8("file_listwidget"))
#################################################################################################### - secondary Files
        self.file_listwidget_sec = QListWidget(self.Tab1widget)
        self.file_listwidget_sec.setGeometry(QtCore.QRect(10, 410, 601, 181))
        self.file_listwidget_sec.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.file_listwidget_sec.setObjectName(_fromUtf8("file_listwidget_sec"))
#################################################################################################### - fbx button
        self.radioButton_fbx = QRadioButton(self.Tab1widget)
        self.radioButton_fbx.setGeometry(QtCore.QRect(130,100, 82, 17))
        self.radioButton_fbx.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.radioButton_fbx.setObjectName(_fromUtf8("radioButton_fbx"))
#################################################################################################### - mov button
        self.radioButton_mov = QRadioButton(self.Tab1widget)
        self.radioButton_mov.setGeometry(QtCore.QRect(20,100, 82, 17))
        self.radioButton_mov.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.radioButton_mov.setObjectName(_fromUtf8("radioButton_mov"))   
##################################################################################################### - search button
        self.search_btn = QPushButton(self.Tab1widget)
        self.search_btn.setGeometry(QtCore.QRect(440, 100, 75, 23))
        self.search_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.search_btn.setObjectName(_fromUtf8("search_btn"))
        self.search_btn.clicked.connect(self.file_search)
##################################################################################################### - filter button
        self.filter_btn = QPushButton(self.Tab1widget)
        self.filter_btn.setGeometry(QtCore.QRect(440, 130, 75, 23))
        self.filter_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.filter_btn.setObjectName(_fromUtf8("filter_btn"))
        self.filter_btn.clicked.connect(self.Filter_search)
##################################################################################################### - search directory button
        self.Sirch_Dir_Browse_bt = QPushButton(self.Tab1widget)
        self.Sirch_Dir_Browse_bt.setGeometry(QtCore.QRect(440, 40, 75, 23))
        self.Sirch_Dir_Browse_bt.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.Sirch_Dir_Browse_bt.setObjectName(_fromUtf8("Sirch_Dir_Browse_bt"))
        self.Sirch_Dir_Browse_bt.clicked.connect(self.Search_Directory)
##################################################################################################### - search directory second button
        self.SecSearch_Dir_Browse_bt = QPushButton(self.Tab1widget)
        self.SecSearch_Dir_Browse_bt.setGeometry(QtCore.QRect(440, 70, 75, 23))
        self.SecSearch_Dir_Browse_bt.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.SecSearch_Dir_Browse_bt.setObjectName(_fromUtf8("Sirch_Dir_Browse_bt"))
        self.SecSearch_Dir_Browse_bt.clicked.connect(self.Sec_Search_Directory)
##################################################################################################### - search directroy box
        self.Search_Dir_Box = QLineEdit(self.Tab1widget)
        self.Search_Dir_Box.setGeometry(QtCore.QRect(20, 40, 411, 20))
        self.Search_Dir_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Search_Dir_Box.setObjectName(_fromUtf8("Search_Dir_Box"))
        self.Search_Dir_Box.setText("Primary search..")
##################################################################################################### - search secondary directroy box
        self.SearchSec_Dir_Box = QLineEdit(self.Tab1widget)
        self.SearchSec_Dir_Box.setGeometry(QtCore.QRect(20, 70, 411, 20))
        self.SearchSec_Dir_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.SearchSec_Dir_Box.setObjectName(_fromUtf8("SearchSec_Dir_Box"))
        self.SearchSec_Dir_Box.setText("Secondary search..")
##################################################################################################### - filter box    
        self.filter_box = QComboBox(self.Tab1widget)
        self.filter_box.setGeometry(QtCore.QRect(250, 130, 180, 20))
        self.filter_box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.filter_box.setObjectName(_fromUtf8("filter_box"))
        self.filter_box.addItem("")
        self.filter_box.addItem("Idle")
        self.filter_box.addItem("Walk")
        self.filter_box.addItem("Jog")
        self.filter_box.addItem("Run")
        self.filter_box.addItem("Jump")
        self.filter_box.addItem("Crouch")
        self.filter_box.addItem("Crawl")
        self.filter_box.addItem("Sit")
        self.filter_box.addItem("Climb")
        self.filter_box.addItem("Lye Down")
        self.filter_box.addItem("Spin")
        self.filter_box.addItem("Push")
        self.filter_box.addItem("Pull")
        self.filter_box.addItem("Fall")
        self.filter_box.addItem("Wave")
        self.filter_box.addItem("Cheer")
        self.filter_box.addItem("Fight")
        self.filter_box.addItem("Dance")
        self.filter_box.addItem("Point")
        self.filter_box.addItem("Roll")
        self.filter_box.addItem("Hold")
        self.filter_box.addItem("Throw")
        self.filter_box.addItem("Kick")
        self.filter_box.addItem("Swim")
        self.filter_box.addItem("Acrobatics")
        self.filter_box.addItem("miscellaneous")

        
##################################################################################################### - filter reset button
        self.filter_reset_btn = QPushButton(self.Tab1widget)
        self.filter_reset_btn.setGeometry(QtCore.QRect(520, 130, 75, 23))
        self.filter_reset_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.filter_reset_btn.setObjectName(_fromUtf8("filter_reset_btn"))
        self.filter_reset_btn.clicked.connect(self.Reset)
##################################################################################################### - copy directory browse button
        self.Copy_Dir_Browse_Btn = QPushButton(self.Tab1widget)
        self.Copy_Dir_Browse_Btn.setGeometry(QtCore.QRect(430, 620, 75, 23))
        self.Copy_Dir_Browse_Btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.Copy_Dir_Browse_Btn.setObjectName(_fromUtf8("Copy_Dir_Browse_Btn"))
        self.Copy_Dir_Browse_Btn.clicked.connect(self.Copy_Directory)
##################################################################################################### - copy directory box
        self.Copy_Dir_Box = QLineEdit(self.Tab1widget)
        self.Copy_Dir_Box.setGeometry(QtCore.QRect(10, 620, 411, 20))
        self.Copy_Dir_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Copy_Dir_Box.setObjectName(_fromUtf8("Copy_Dir_Box"))
##################################################################################################### - copy files button
        self.Copy_Files_Btn = QPushButton(self.Tab1widget)
        self.Copy_Files_Btn.setGeometry(QtCore.QRect(510, 620, 75, 23))
        self.Copy_Files_Btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.Copy_Files_Btn.setObjectName(_fromUtf8("Copy_Files_Btn"))
        self.Copy_Files_Btn.clicked.connect(self.Copy_Files_action)
##################################################################################################### - movie preview box       
        self.Mov_preview_Box =  QFrame(self.Tab1widget)
        self.Mov_preview_Box.setGeometry(QtCore.QRect(820, 60, 1011, 751))
        self.Mov_preview_Box.setStyleSheet(_fromUtf8("background-color: rgb(10, 10, 10);"))
        self.Mov_preview_Box.setObjectName(_fromUtf8("Mov_preview_Box"))

        self.controlLayout = QVBoxLayout()
        self.controlLayout.setContentsMargins(0, 0, 0, 0)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.Mov_preview_Box)
        
       
        self.playButton = QPushButton(self.Tab1widget)
        self.playButton.setGeometry(QtCore.QRect(920, 820, 30, 30))
        self.playButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.playButton.setIcon(self.playButton.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.stopbutton = QPushButton(self.Tab1widget)
        self.stopbutton.setGeometry(QtCore.QRect(960, 820, 30, 30))
        self.stopbutton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.stopbutton.setIcon(self.stopbutton.style().standardIcon(QStyle.SP_MediaStop))
        self.stopbutton.clicked.connect(self.stop)

        self.positionSlider = QSlider(QtCore.Qt.Horizontal,self.Tab1widget)
        self.positionSlider.setMaximum(1000)
        self.positionSlider.setGeometry(QtCore.QRect(1000, 820, 751, 30))
        self.positionSlider.sliderMoved.connect(self.set_position)
        self.positionSlider.sliderPressed.connect(self.set_position)

##################################################################################################### - Time box
        self.Time_update = QLineEdit(self.Tab1widget)
        self.Time_update.setGeometry(QtCore.QRect(1760, 820, 70, 20))
        self.Time_update.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n""background-color: rgb(80, 80, 80);"))
        self.Time_update.setObjectName(_fromUtf8("time_box"))
        self.Time_update.setText("0:00:000")
       
####################################################################################### - select all
        self.Select_all_bt = QCheckBox(self.Tab1widget)
        self.Select_all_bt.setGeometry(QtCore.QRect(10, 130, 120, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Select_all_bt.setFont(font)
        self.Select_all_bt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Select_all_bt.setObjectName(_fromUtf8("Auto_Transfer_bt"))
        self.Select_all_bt.stateChanged.connect(self.Select_all_bt_func)
####################################################################################### - secondary search
        self.Second_search_bt = QCheckBox(self.Tab1widget)
        self.Second_search_bt.setGeometry(QtCore.QRect(250,98, 155, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Second_search_bt.setFont(font)
        self.Second_search_bt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Second_search_bt.setObjectName(_fromUtf8("Auto_Transfer_bt"))
        self.Second_search_bt.stateChanged.connect(self.S_Search)
##################################################################################################### - Static texts
        self.Mocap_Lib_Text = QLabel(self.centralwidget)
        self.Mocap_Lib_Text.setGeometry(QtCore.QRect(900, 10, 201, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Mocap_Lib_Text.setFont(font)
        self.Mocap_Lib_Text.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Mocap_Lib_Text.setObjectName(_fromUtf8("Mocap_Lib_Text"))
#####################################################################################################
        self.Take_Preview_Txt = QLabel(self.Tab1widget)
        self.Take_Preview_Txt.setGeometry(QtCore.QRect(1300, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.Take_Preview_Txt.setFont(font)
        self.Take_Preview_Txt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Take_Preview_Txt.setObjectName(_fromUtf8("Take_Preview_Txt"))
#####################################################################################################
        self.Search_Dir_Text = QLabel(self.Tab1widget)
        self.Search_Dir_Text.setGeometry(QtCore.QRect(200, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.Search_Dir_Text.setFont(font)
        self.Search_Dir_Text.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Search_Dir_Text.setObjectName(_fromUtf8("Search_Dir_Text"))
#####################################################################################################        
        self.copy_Dir_Txt = QLabel(self.Tab1widget)
        self.copy_Dir_Txt.setGeometry(QtCore.QRect(190, 600, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.copy_Dir_Txt.setFont(font)
        self.copy_Dir_Txt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.copy_Dir_Txt.setObjectName(_fromUtf8("copy_Dir_Txt"))
#####################################################################################################
        self.keyword_filter_txt = QLabel(self.Tab1widget)
        self.keyword_filter_txt.setGeometry(QtCore.QRect(150, 130, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.keyword_filter_txt.setFont(font)
        self.keyword_filter_txt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.keyword_filter_txt.setObjectName(_fromUtf8("keyword_filter_txt"))
        self.keyword_filter_txt.raise_()
#####################################################################################################
        self.file_listwidget.raise_()
        self.radioButton_fbx.raise_()
        self.radioButton_mov.raise_()
        self.search_btn.raise_()
        self.filter_btn.raise_()
        self.Sirch_Dir_Browse_bt.raise_()
        self.Search_Dir_Box.raise_()
        self.filter_box.raise_()
        self.filter_reset_btn.raise_()
        self.Copy_Dir_Browse_Btn.raise_()
        self.Copy_Dir_Box.raise_()
        self.Copy_Files_Btn.raise_()
        self.Mov_preview_Box.raise_()
        self.Mocap_Lib_Text.raise_()
        self.Take_Preview_Txt.raise_()
        self.Search_Dir_Text.raise_()
        self.copy_Dir_Txt.raise_()
        self.Mov_preview_Box.raise_()
        self.playButton.raise_()
        self.positionSlider.raise_()
#####################################################################################################################################################################
#####################################################################################################################################################################
        
        ##################################################################################################### - open mobu
        
        self.Mobu_O = QPushButton(self.Tab2widget)
        self.Mobu_O.setGeometry(QtCore.QRect(465, 110, 105, 23))
        self.Mobu_O.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.Mobu_O.setObjectName(_fromUtf8("filter_reset_btn"))
        self.Mobu_O.clicked.connect(self.Open_mobu)

        ##################################################################################################### - Close mobu
        
        self.Mobu_C = QPushButton(self.Tab2widget)
        self.Mobu_C.setGeometry(QtCore.QRect(465, 240, 105, 23))
        self.Mobu_C.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.Mobu_C.setObjectName(_fromUtf8("filter_reset_btn"))
        self.Mobu_C.clicked.connect(self.Close_mobu)
        
        ##################################################################################################### - search directroy box
        self.copy_listwidget_sec = QListWidget(self.Tab2widget)
        self.copy_listwidget_sec.setGeometry(QtCore.QRect(10, 80, 401, 181))
        self.copy_listwidget_sec.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.copy_listwidget_sec.setObjectName(_fromUtf8("file_listwidget_sec"))
        ##################################################################################################### - Get files button
        self.Copy_search_btn = QPushButton(self.Tab2widget)
        self.Copy_search_btn.setGeometry(QtCore.QRect(530, 40, 75, 23))
        self.Copy_search_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.Copy_search_btn.setObjectName(_fromUtf8("search_btn"))
        self.Copy_search_btn.clicked.connect(self.file_search_Copy)
        ##################################################################################################### - Browse button
        self.Copy_browse_btn = QPushButton(self.Tab2widget)
        self.Copy_browse_btn.setGeometry(QtCore.QRect(440, 40, 75, 23))
        self.Copy_browse_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.Copy_browse_btn.setObjectName(_fromUtf8("search_btn"))
        self.Copy_browse_btn.clicked.connect(self.Copy_Directory_secWidg)
        ##################################################################################################### - primary file
        self.Set_Master_btn = QPushButton(self.Tab2widget)
        self.Set_Master_btn.setGeometry(QtCore.QRect(470, 80, 90, 23))
        self.Set_Master_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.Set_Master_btn.setObjectName(_fromUtf8("Set_Master_btn"))
        self.Set_Master_btn.clicked.connect(self.Primary_file)
        ##################################################################################################### - Merge file
        self.Set_Merge_btn = QPushButton(self.Tab2widget)
        self.Set_Merge_btn.setGeometry(QtCore.QRect(470, 140, 90, 23))
        self.Set_Merge_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.Set_Merge_btn.setObjectName(_fromUtf8("Set_Master_btn"))
       # self.Set_Merge_btn.clicked.connect(self.Merge_Mobu)
        ##################################################################################################### - copy directory box
        self.Copy_Dir_Box_New = QLineEdit(self.Tab2widget)
        self.Copy_Dir_Box_New.setGeometry(QtCore.QRect(10, 40, 401, 20))
        self.Copy_Dir_Box_New.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Copy_Dir_Box_New.setObjectName(_fromUtf8("Copy_Dir_Box"))
        
        #####################################################################################################        
        self.copy_Dir_Txt_new = QLabel(self.Tab2widget)
        self.copy_Dir_Txt_new.setGeometry(QtCore.QRect(150, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.copy_Dir_Txt_new.setFont(font)
        self.copy_Dir_Txt_new.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.copy_Dir_Txt_new.setObjectName(_fromUtf8("copy_Dir_Txt_new"))
        
        #####################################################################################################    
        self.Mobu_Box =  QFrame(self.Tab2widget)
        self.Mobu_Box.setGeometry(QtCore.QRect(620, 20, 1200, 751))
        self.Mobu_Box.setStyleSheet(_fromUtf8("background-color: rgb(10,10,10);"))
        self.Mobu_Box.setObjectName(_fromUtf8("Mobu_Box"))
        
        self.layout2 = QVBoxLayout(self.Mobu_Box)
        self.layout2.setContentsMargins(0, 0, 0, 0)    
        
        self.TR_Box =  QFrame(self.Tab2widget)
        self.TR_Box.setGeometry(QtCore.QRect(620, 810,1200, 80))
        self.TR_Box.setStyleSheet(_fromUtf8("background-color: rgb(10,10,10);"))
        self.TR_Box.setObjectName(_fromUtf8("TR_Box"))
        
        self.layout3 = QVBoxLayout(self.TR_Box)
        self.layout3.setContentsMargins(0, 0, 0, 0)  
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        self.radioButton_fbx.setText("Fbx")
        self.radioButton_mov.setText("mov")
        self.search_btn.setText("Search")
        self.filter_btn.setText("Filter")
        self.Sirch_Dir_Browse_bt.setText("Browse..")
        self.filter_reset_btn.setText("Reset")
        self.Copy_Dir_Browse_Btn.setText("Browse..")
        self.Copy_Files_Btn.setText("Copy files")
        self.Mocap_Lib_Text.setText("Mocap Library Database")
        self.Take_Preview_Txt.setText("Take Preview")
        self.Search_Dir_Text.setText("Search Directory")
        self.copy_Dir_Txt.setText("Copy Directory")
        self.keyword_filter_txt.setText( "Keyword Filter")
        self.Select_all_bt.setText("Select/unselect all")
        self.Second_search_bt.setText("Activate secondary search")
        self.SecSearch_Dir_Browse_bt.setText("Browse..")
        self.Copy_browse_btn.setText("Browse..")
        self.Copy_search_btn.setText("Get files")
        self.Mobu_O.setText("Run Motion Builder")
        self.copy_Dir_Txt_new.setText("Copy Directory")
        self.Set_Master_btn.setText("Set Primary File")
        self.Mobu_C.setText("Close Motion Builder")
        self.Set_Merge_btn.setText("Merge Files")

        
    def Search_Directory(self):
        self.Master_Directory = str(QFileDialog.getExistingDirectory())
        self.Search_Dir_Box.setText(self.Master_Directory)            

    def Sec_Search_Directory(self):
        self.Sec_Master_Directory = str(QFileDialog.getExistingDirectory())
        self.SearchSec_Dir_Box.setText(self.Sec_Master_Directory)

        

    def file_search(self):

        self.files=0
        
        if self.radioButton_fbx.isChecked()==True:
            self.file_ext=(".fbx")
        elif self.radioButton_mov.isChecked()==True:
            self.file_ext=(".mov")
        else:
            self.mssgebox=QMessageBox()
            self.mssgebox.setIcon(QMessageBox.Information)
            self.mssgebox.setWindowTitle("Error")
            self.mssgebox.setDetailedText("Please choose a file type")
            self.mssgebox.setStandardButtons(QMessageBox.Ok)
            returnValue = self.mssgebox.exec()
            if returnValue == QMessageBox.Ok:
                self.mssgebox.close()
            self.files=1
            
        if self.secondary_search==1:
                self.file_ext_Sec=".fbx"
           
        self.file_directory=[]
        self.file_directory_filt=[]

        self.file_directory_Sec=[]
        self.file_directory_filt_Sec=[]
        self.Select_all_bt.setCheckState(QtCore.Qt.Unchecked)

        if self.files==0:  
            try:
                self.file_listwidget.clear()
                for root,dirs,files in os.walk(self.Master_Directory):    
                    for fi in files:                      
                        files_str=str(files)
                        if fi.endswith(self.file_ext):
                           self.item=QListWidgetItem()
                           self.item.setText(fi)
                           self.item.setFlags(self.item.flags()|QtCore.Qt.ItemIsUserCheckable)
                           self.item.setCheckState(QtCore.Qt.Unchecked)
                           self.file_listwidget.addItem(self.item)
                           for i in range(len(files)):
                               self.file_directory.append(root +'\\'+ files[i])
                for i in range(len(self.file_directory)):
                    if self.file_directory[i].endswith(self.file_ext):
                        self.file_directory_filt.append(self.file_directory[i])

            except WindowsError as e:
                        e = str(e)
            if self.secondary_search==1:
                try:
                    self.file_listwidget_sec.clear()
                    for root,dirs,files in os.walk(self.Sec_Master_Directory):    
                        for fi in files:
                            self.files_str_sec=str(files)
                            if fi.endswith(self.file_ext_Sec): #change this
                               self.item=QListWidgetItem()
                               self.item.setText(fi)
                               self.item.setFlags(self.item.flags()|QtCore.Qt.ItemIsUserCheckable)
                               self.item.setCheckState(QtCore.Qt.Unchecked)
                               self.file_listwidget_sec.addItem(self.item)
                               for i in range(len(files)):
                                   self.file_directory_Sec.append(root +'\\'+ files[i]) # change this
                    for i in range(len(self.file_directory_Sec)): # cahnge this
                        if self.file_directory_Sec[i].endswith(self.file_ext_Sec): #change this
                            self.file_directory_filt_Sec.append(self.file_directory_Sec[i])     #change this   
                except WindowsError as e:
                            e = str(e)

    def Filter_search(self):
        self.Reset()
        self.file_directory_filt=[]
        self.keyword=str(self.filter_box.currentText())
        if "Idle" in self.keyword:
            self.keyword="Idl_"
        if "Walk" in self.keyword:
            self.keyword="Wlk_"
        if "Run" in self.keyword:
            self.keyword="Rn_"
        if "Jump" in self.keyword:
            self.keyword="Jmp_"
        if "Crouch" in self.keyword:
            self.keyword="Crch_"
        if "Crawl" in self.keyword:
            self.keyword="Crwl_"
        if "Sit" in self.keyword:
            self.keyword="St_"
        if "Climb" in self.keyword:
            self.keyword="Clmb_"
        if "Lye Down" in self.keyword:
            self.keyword="LD_"
        if "Spin" in self.keyword:
            self.keyword="Spn_"
        if "Push" in self.keyword:
            self.keyword="Psh_"
        if "Pull" in self.keyword:
            self.keyword="Pll_"
        if "Fall" in self.keyword:
            self.keyword="Fll_"
        if "Wave" in self.keyword:
            self.keyword="Wv_"
        if "Cheer" in self.keyword:
            self.keyword="Chr_"

        if "Fight" in self.keyword:
            self.keyword="Fght_"
        if "Dance" in self.keyword:
            self.keyword="Dnc_"
        if "Point" in self.keyword:
            self.keyword="Pnt_"
        if "Roll" in self.keyword:
            self.keyword="Rll_"
        if "Hold" in self.keyword:
            self.keyword="Hld_"
        if "Throw" in self.keyword:
            self.keyword="Thrw_"
        if "Kick" in self.keyword:
            self.keyword="Kck_"
        if "Swim" in self.keyword:
            self.keyword="Swm_"
        if "Acrobatics" in self.keyword:
            self.keyword="Acr_"
        if "miscellaneous" in self.keyword:
            self.keyword="Msc_"
        
        self.Select_all_bt.setCheckState(QtCore.Qt.Unchecked)
        try:
            self.itemsTextList =  [str(self.file_listwidget.item(i).text()) for i in range(self.file_listwidget.count())]
            self.file_listwidget.clear()
            for fi in self.itemsTextList:
                    if self.keyword in fi:
                           item_filt=QListWidgetItem()
                           item_filt.setText(fi)
                           item_filt.setFlags(item_filt.flags()|QtCore.Qt.ItemIsUserCheckable)
                           item_filt.setCheckState(QtCore.Qt.Unchecked)
                           self.file_listwidget.addItem(item_filt)
            for i in range(len(self.file_directory)):
                if self.keyword in self.file_directory[i]:
                    self.file_directory_filt.append(self.file_directory[i])
        except NameError as e:
                e = str(e)
                
        if self.secondary_search ==1:
            self.file_directory_filt_Sec=[]
            try:
                self.itemsTextList =  [str(self.file_listwidget_sec.item(i).text()) for i in range(self.file_listwidget_sec.count())]
                self.file_listwidget_sec.clear()
                for fi in self.itemsTextList:
                        if self.keyword in fi:     
                               item_filt=QListWidgetItem()
                               item_filt.setText(fi)
                               item_filt.setFlags(item_filt.flags()|QtCore.Qt.ItemIsUserCheckable)
                               item_filt.setCheckState(QtCore.Qt.Unchecked)
                               self.file_listwidget_sec.addItem(item_filt)
                for i in range(len(self.file_directory_Sec)): 
                    if self.keyword in self.file_directory_Sec[i]:
                        self.file_directory_filt_Sec.append(self.file_directory_Sec[i]) 
            except NameError as e:
                    e = str(e)
                                    
                            
    def Reset(self):
        self.file_directory=[]
        self.file_directory_filt=[]
        self.Select_all_bt.setCheckState(QtCore.Qt.Unchecked)
        try:
                self.file_listwidget.clear()
                for root,dirs,files in os.walk(self.Master_Directory):
                    for fi in files:
                        self.files_str=str(files)
                        if fi.endswith(self.file_ext):
                           self.item=QListWidgetItem()
                           self.item.setText(fi)
                           self.item.setFlags(self.item.flags()|QtCore.Qt.ItemIsUserCheckable)
                           self.item.setCheckState(QtCore.Qt.Unchecked)
                           self.file_listwidget.addItem(self.item)
                           for i in range(len(files)):
                               self.file_directory.append(root +'\\'+ files[i])
                for i in range(len(self.file_directory)):
                        if self.file_directory[i].endswith(self.file_ext):
                            self.file_directory_filt.append(self.file_directory[i])
        except WindowsError as e:
                        e = str(e)
        except NameError as e:
                e = str(e)
        if self.secondary_search==1:
            self.file_directory_Sec=[]
            self.file_directory_filt_Sec=[]
            try:
                    self.file_listwidget_sec.clear()
                    for root,dirs,files in os.walk(self.Sec_Master_Directory):
                        for fi in files:
                            self.files_str=str(files)
                            if fi.endswith(self.file_ext_Sec): #change that part
                               self.item=QListWidgetItem()
                               self.item.setText(fi)
                               self.item.setFlags(self.item.flags()|QtCore.Qt.ItemIsUserCheckable)
                               self.item.setCheckState(QtCore.Qt.Unchecked)
                               self.file_listwidget_sec.addItem(self.item)
                               for i in range(len(files)):
                                   self.file_directory_Sec.append(root +'\\'+ files[i])
                    for i in range(len(self.file_directory_Sec)): #change that part
                            if self.file_directory_Sec[i].endswith(self.file_ext): #change that part
                                self.file_directory_filt_Sec.append(self.file_directory_Sec[i]) #change that part
            except WindowsError as e:
                            e = str(e)
            except NameError as e:
                    e = str(e)

        
    def Copy_Directory(self):
        self.Copy_Directory_str = str(QFileDialog.getExistingDirectory())
        self.Copy_Dir_Box.setText(self.Copy_Directory_str)
        self.Copy_Dir_Box_New.setText(self.Copy_Directory_str)
        
    def Copy_Files_action(self):
        self.copy_files=[]
        
        for i in range(self.file_listwidget.count()):
                if self.file_listwidget.item(i).checkState()==Qt.Checked:
                    self.copy_files.append(self.file_directory_filt[i])
                else:
                    pass
                
        if self.secondary_search==1:
            for i in range(self.file_listwidget_sec.count()):
                if self.file_listwidget_sec.item(i).checkState()==Qt.Checked:
                    self.copy_files.append(self.file_directory_filt_Sec[i])
                    time.sleep(0.01)
                else:
                    pass

        try:
            if len(self.copy_files)>0:
                try:                
                    for f in self.copy_files:
                        shutil.copy(f, self.Copy_Directory_str)
                    self.mssgebox=QMessageBox()
                    self.mssgebox.setIcon(QMessageBox.Information)
                    self.mssgebox.setWindowTitle("Success")
                    self.mssgebox.setDetailedText("Files copied")
                    self.mssgebox.setStandardButtons(QMessageBox.Ok)
                    returnValue = self.mssgebox.exec()
                    if returnValue == QMessageBox.Ok:
                        self.mssgebox.close()
                except:
                    self.mssgebox=QMessageBox()
                    self.mssgebox.setIcon(QMessageBox.Information)
                    self.mssgebox.setWindowTitle("Error")
                    self.mssgebox.setDetailedText("Please choose copy location")
                    self.mssgebox.setStandardButtons(QMessageBox.Ok)
                    returnValue = self.mssgebox.exec()
                    if returnValue == QMessageBox.Ok:
                        self.mssgebox.close()
                    
            else:
                self.mssgebox=QMessageBox()
                self.mssgebox.setIcon(QMessageBox.Information)
                self.mssgebox.setWindowTitle("Error")
                self.mssgebox.setDetailedText("Please choose copy files")
                self.mssgebox.setStandardButtons(QMessageBox.Ok)
                returnValue = self.mssgebox.exec()
                if returnValue == QMessageBox.Ok:
                    self.mssgebox.close()
                    
        except NameError as e:
                e = str(e)
                
    def Select_all_bt_func(self):
       
        for i in range(self.file_listwidget.count()):
            if self.file_listwidget.item(i).checkState()==Qt.Checked:
                self.file_listwidget.item(i).setCheckState(QtCore.Qt.Unchecked)
            elif self.file_listwidget.item(i).checkState()==Qt.Unchecked:
                self.file_listwidget.item(i).setCheckState(QtCore.Qt.Checked)
        if self.secondary_search==1:
            for i in range(self.file_listwidget_sec.count()):
                if self.file_listwidget_sec.item(i).checkState()==Qt.Checked:
                    self.file_listwidget_sec.item(i).setCheckState(QtCore.Qt.Unchecked)
                elif self.file_listwidget_sec.item(i).checkState()==Qt.Unchecked:
                    self.file_listwidget_sec.item(i).setCheckState(QtCore.Qt.Checked)
            

    def S_Search(self):        
        if self.Second_search_bt.isChecked()==True:
            self.secondary_search=1
        if self.Second_search_bt.isChecked()==False:
            self.secondary_search=0
                
    def play(self):

        self.video_preview_file=[]
        try:
            if self.file_ext==".mov":

                self.Selected_file=self.file_listwidget.selectedIndexes()[0]
                self.Selected_file=self.Selected_file.data()
                self.Selected_file_str=str(self.Selected_file)

                for i in range(len(self.file_directory_filt)):
                    if self.Selected_file_str in self.file_directory_filt[i]:
                        self.video_preview_file.append(self.file_directory_filt[i])

                if self.video_playing==0:
                    self.media = self.instance.media_new(self.video_preview_file[0])
                    self.mediaPlayer.set_media(self.media)
                    # Parse the metadata of the file
                    self.media.parse()
                    self.mediaPlayer.set_hwnd(int(self.Mov_preview_Box.winId()))

                
                if self.pause_vid==0:
                    if self.mediaPlayer.play() == -1:
                        return
                    self.playButton.setIcon(self.playButton.style().standardIcon(QStyle.SP_MediaPause))
                    self.mediaPlayer.play()
                    self.timer.start()
                    self.is_paused = False
                    self.pause_vid=1
                    self.video_playing=1
                else:
                    self.pause()
        except:
            pass

    def stop(self):
        """Stop player
        """
        self.video_playing=0
        self.mediaPlayer.stop()
        self.playButton.setIcon(self.playButton.style().standardIcon(QStyle.SP_MediaPlay))
     
    def pause(self):
        self.mediaPlayer.pause()
        self.is_paused = True
        self.timer.stop()
        self.playButton.setIcon(self.playButton.style().standardIcon(QStyle.SP_MediaPlay))
        self.pause_vid=0


        
    def set_position(self):
        """Set the movie position according to the position slider.
        """

        # The vlc MediaPlayer needs a float value between 0 and 1, Qt uses
        # integer variables, so you need a factor; the higher the factor, the
        # more precise are the results (1000 should suffice).

        # Set the media position to where the slider was dragged
        self.timer.stop()
        pos = self.positionSlider.value()
        self.mediaPlayer.set_position(pos / 1000.0)
        self.timer.start()

    def update_ui(self):
        """Updates the user interface"""

        # Set the slider's position to its corresponding media position
        # Note that the setValue function only takes values of type int,
        # so we must first convert the corresponding media position.
        media_pos = int(self.mediaPlayer.get_position() * 1000)
        self.video_time=self.mediaPlayer.get_position()*100
        self.video_time_ROUND=np.around((self.video_time),decimals=3)
        self.Time_update.setText(str(self.video_time_ROUND))

        


        #formatted_time = self.video_time.strftime('%M:%S.%f')

     #   print(formatted_time)
        self.positionSlider.setValue(media_pos)

        # No need to call this function if nothing is played
        if not self.mediaPlayer.is_playing():
            self.timer.stop()

            # After the video finished, the play button stills shows "Pause",
            # which is not the desired behavior of a media player.
            # This fixes that "bug".
            if not self.is_paused:
                self.stop()
                
#####################################################################################################################################################################
#####################################################################################################################################################################
                                                              #  2nd widget Functions
#####################################################################################################################################################################
#####################################################################################################################################################################

    def Copy_Directory_secWidg(self):
        self.Copy_Directory_str_new = str(QFileDialog.getExistingDirectory())
        self.Copy_Dir_Box_New.setText(self.Copy_Directory_str_new)
        self.copy_browse_new=1
        
    def Open_mobu(self):
        self.mobu_open=1
        host = "localhost"
        port = 4242
        self.mobu=subprocess.Popen(["C:\\Program Files\\Autodesk\\MotionBuilder 2017\\bin\\x64\\motionbuilder.exe","-verbosePython","-suspendMessages",self.mobu_primary])
        time.sleep(6)

        gw.getAllTitles()
        self.Mobu_win=gw.getWindowsWithTitle('MotionBuilder')[0]
        self.Mobu_hwnd=self.Mobu_win._hWnd
        self.window = QWindow.fromWinId(self.Mobu_hwnd)  
                
        self.Mobu_view=QWidget.createWindowContainer(self.window)
        self.Mobu_view.setGeometry(QtCore.QRect(620, 20, 1200, 751))
        self.layout2.addWidget(self.Mobu_view)
        self.Mobu_Box.update()
        
        self.Mobu_TR=gw.getWindowsWithTitle('Transport')[0]
        self.MobuTR_hwnd=self.Mobu_TR._hWnd
        self.window_TR = QWindow.fromWinId(self.MobuTR_hwnd)  
                
        self.Mobu_TRview=QWidget.createWindowContainer(self.window_TR)
     #   print(dir(self.Mobu_Pyview))
        self.Mobu_TRview.setGeometry(QtCore.QRect(620, 790,1200, 60))
        self.layout3.addWidget(self.Mobu_TRview)
        self.Mobu_Box.update()
        self.TR_Box.update()
        
        
        
        self.t1=Thread(target=self.MobuThread)
        self.t1.setDaemon(True)
        self.t1.start()

        
    def Close_mobu(self):
        #self.mobu.kill()
        self.mobu_open=0
        subprocess.call(['taskkill', '/F', '/T', '/PID', str(self.mobu.pid)])
        try:
            self.layout2.removeWidget(self.Mobu_view)
            self.layout2.removeWidget(self.Mobu_view_transport)
        except:
                pass
        self.Mobu_win=[]
        self.Mobu_hwnd=[]
        self.Mobu_view=[]
        
        self.Mobu_TR=[]
        self.MobuTR_hwnd=[]
        self.Mobu_TRview=[]
   
    def file_search_Copy(self):
        self.files=0
        self.Copy_file_ext=".fbx"
               
        self.file_directory_Widgesec=[]
        self.file_directory_filt_widgesec=[]

        self.Select_all_bt.setCheckState(QtCore.Qt.Unchecked)

        if self.files==0:  
            try:
                self.copy_listwidget_sec.clear()
                try:
                    if self.copy_browse_new==0:
                        self.Copy_Directory_str_new=self.Copy_Directory_str
                    else:
                        pass
                    for root,dirs,files in os.walk(self.Copy_Directory_str_new):    
                        for fi in files:                      
                            files_str=str(files)
                            if fi.endswith(self.Copy_file_ext):
                               self.item=QListWidgetItem()
                               self.item.setText(fi)
                               self.item.setFlags(self.item.flags()|QtCore.Qt.ItemIsUserCheckable)
                               self.item.setCheckState(QtCore.Qt.Unchecked)
                               self.copy_listwidget_sec.addItem(self.item)
                               for i in range(len(files)):
                                   self.file_directory_Widgesec.append(root +'\\'+ files[i])
                    for i in range(len(self.file_directory_Widgesec)):
                        if self.file_directory_Widgesec[i].endswith(self.Copy_file_ext):
                            self.file_directory_filt_widgesec.append(self.file_directory_Widgesec[i])
                except:
                    self.mssgebox=QMessageBox()
                    self.mssgebox.setIcon(QMessageBox.Information)
                    self.mssgebox.setWindowTitle("Error")
                    self.mssgebox.setDetailedText("Choose copy directory")
                    self.mssgebox.setStandardButtons(QMessageBox.Ok)
                    returnValue = self.mssgebox.exec()
                    if returnValue == QMessageBox.Ok:
                        self.mssgebox.close()
                    

            except WindowsError as e:
                        e = str(e)
    def Primary_file(self):

        self.copy_files_widge=[]
        try:
            for i in range(self.copy_listwidget_sec.count()):
                    if self.copy_listwidget_sec.item(i).checkState()==Qt.Checked:
                        self.copy_files_widge.append(self.file_directory_filt_widgesec[i])
                    else:
                        pass
            self.mobu_primary=self.copy_files_widge[0]
        except:
            pass
    
    def MobuThread(self):
        while self.mobu_open==1:
            self.Mobu_Box.update()
            self.TR_Box.update()
            time.sleep(0.01)
            break
            
#####################################################################################################################################################################
#####################################################################################################################################################################        
    def About_lib(self):
        self.mssgebox=QMessageBox()
        self.mssgebox.setIcon(QMessageBox.Information)
        self.mssgebox.setWindowTitle("About")
        self.mssgebox.setDetailedText("Mocap Database Version 1.0")
        self.mssgebox.setStandardButtons(QMessageBox.Ok)
        returnValue = self.mssgebox.exec()
        if returnValue == QMessageBox.Ok:
            self.mssgebox.close()

    def Close(self):

        MainWindow.close()
        MainWindow.destroy()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

