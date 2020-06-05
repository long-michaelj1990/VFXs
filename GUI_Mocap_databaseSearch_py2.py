# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mocap_library_database.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tkinter import *
from PyQt4.phonon import Phonon
from PIL import Image, ImageTk
import tkMessageBox
import os
from os import listdir,environ
from os.path import isfile, join, abspath
import glob
import shutil
import numpy as np
import cv2
import time

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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1900, 1000)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(36, 36, 36);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
#################################################################################################### - Files
        self.file_listwidget = QtGui.QListWidget(self.centralwidget)
        self.file_listwidget.setGeometry(QtCore.QRect(10, 160, 601, 191))
        self.file_listwidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.file_listwidget.setObjectName(_fromUtf8("file_listwidget"))
#################################################################################################### - secondary Files
        self.file_listwidget_sec = QtGui.QListWidget(self.centralwidget)
        self.file_listwidget_sec.setGeometry(QtCore.QRect(10, 410, 601, 181))
        self.file_listwidget_sec.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.file_listwidget_sec.setObjectName(_fromUtf8("file_listwidget_sec"))
#################################################################################################### - fbx button
        self.radioButton_fbx = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_fbx.setGeometry(QtCore.QRect(20, 100, 82, 17))
        self.radioButton_fbx.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.radioButton_fbx.setObjectName(_fromUtf8("radioButton_fbx"))
#################################################################################################### - mov button
        self.radioButton_mov = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_mov.setGeometry(QtCore.QRect(130, 100, 82, 17))
        self.radioButton_mov.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.radioButton_mov.setObjectName(_fromUtf8("radioButton_mov"))
##################################################################################################### - c3d button
        self.radioButton_c3d = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_c3d.setGeometry(QtCore.QRect(240, 100, 82, 17))
        self.radioButton_c3d.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.radioButton_c3d.setObjectName(_fromUtf8("radioButton_c3d"))
##################################################################################################### - x2d button
        self.radioButton_x2d = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_x2d.setGeometry(QtCore.QRect(340, 100, 82, 17))
        self.radioButton_x2d.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.radioButton_x2d.setObjectName(_fromUtf8("radioButton_x2d"))

#################################################################################################### - secondary fbx button
        self.RadioGroup = QtGui.QButtonGroup(self.centralwidget)
        self.Sec_radioButton_fbx = QtGui.QRadioButton(self.centralwidget)
        self.Sec_radioButton_fbx.setGeometry(QtCore.QRect(20, 387, 82, 17))
        self.Sec_radioButton_fbx.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Sec_radioButton_fbx.setObjectName(_fromUtf8("radioButton_fbx"))
        self.Sec_radioButton_fbx.setChecked(False)
        self.Sec_radioButton_fbx.setCheckable(False)

        self.Sec_radioButton_c3d = QtGui.QRadioButton(self.centralwidget)
        self.Sec_radioButton_c3d.setGeometry(QtCore.QRect(130, 387, 82, 17))
        self.Sec_radioButton_c3d.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Sec_radioButton_c3d.setObjectName(_fromUtf8("radioButton_c3d"))
        self.Sec_radioButton_c3d.setChecked(False)
        self.Sec_radioButton_c3d.setCheckable(False)

        self.Sec_radioButton_x2d = QtGui.QRadioButton(self.centralwidget)
        self.Sec_radioButton_x2d.setGeometry(QtCore.QRect(240, 387, 82, 17))
        self.Sec_radioButton_x2d.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Sec_radioButton_x2d.setObjectName(_fromUtf8("radioButton_x2d"))
        self.Sec_radioButton_x2d.setChecked(False)
        self.Sec_radioButton_x2d.setCheckable(False)

        self.RadioGroup.addButton(self.Sec_radioButton_fbx)
        self.RadioGroup.addButton(self.Sec_radioButton_c3d)
        self.RadioGroup.addButton(self.Sec_radioButton_x2d)        
##################################################################################################### - search button
        self.search_btn = QtGui.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(440, 100, 75, 23))
        self.search_btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
"color: rgb(255, 255, 255);"))
        self.search_btn.setObjectName(_fromUtf8("search_btn"))
        self.search_btn.clicked.connect(self.file_search)
##################################################################################################### - filter button
        self.filter_btn = QtGui.QPushButton(self.centralwidget)
        self.filter_btn.setGeometry(QtCore.QRect(440, 130, 75, 23))
        self.filter_btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
"color: rgb(255, 255, 255);"))
        self.filter_btn.setObjectName(_fromUtf8("filter_btn"))
        self.filter_btn.clicked.connect(self.Filter_search)
##################################################################################################### - search directory button
        self.Sirch_Dir_Browse_bt = QtGui.QPushButton(self.centralwidget)
        self.Sirch_Dir_Browse_bt.setGeometry(QtCore.QRect(440, 40, 75, 23))
        self.Sirch_Dir_Browse_bt.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
"color: rgb(255, 255, 255);"))
        self.Sirch_Dir_Browse_bt.setObjectName(_fromUtf8("Sirch_Dir_Browse_bt"))
        self.Sirch_Dir_Browse_bt.clicked.connect(self.Search_Directory)
##################################################################################################### - search directory second button
        self.SecSearch_Dir_Browse_bt = QtGui.QPushButton(self.centralwidget)
        self.SecSearch_Dir_Browse_bt.setGeometry(QtCore.QRect(440, 70, 75, 23))
        self.SecSearch_Dir_Browse_bt.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
"color: rgb(255, 255, 255);"))
        self.SecSearch_Dir_Browse_bt.setObjectName(_fromUtf8("Sirch_Dir_Browse_bt"))
        self.SecSearch_Dir_Browse_bt.clicked.connect(self.Sec_Search_Directory)
##################################################################################################### - search directroy box
        self.Search_Dir_Box = QtGui.QLineEdit(self.centralwidget)
        self.Search_Dir_Box.setGeometry(QtCore.QRect(20, 40, 411, 20))
        self.Search_Dir_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Search_Dir_Box.setObjectName(_fromUtf8("Search_Dir_Box"))
        self.Search_Dir_Box.setText("Primary search..")
##################################################################################################### - search secondary directroy box
        self.SearchSec_Dir_Box = QtGui.QLineEdit(self.centralwidget)
        self.SearchSec_Dir_Box.setGeometry(QtCore.QRect(20, 70, 411, 20))
        self.SearchSec_Dir_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.SearchSec_Dir_Box.setObjectName(_fromUtf8("SearchSec_Dir_Box"))
        self.SearchSec_Dir_Box.setText("Secondary search..")
##################################################################################################### - filter box
       
        self.filter_box = QtGui.QComboBox(self.centralwidget)
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
        self.filter_reset_btn = QtGui.QPushButton(self.centralwidget)
        self.filter_reset_btn.setGeometry(QtCore.QRect(520, 130, 75, 23))
        self.filter_reset_btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
"color: rgb(255, 255, 255);"))
        self.filter_reset_btn.setObjectName(_fromUtf8("filter_reset_btn"))
        self.filter_reset_btn.clicked.connect(self.Reset)
##################################################################################################### - copy directory browse button
        self.Copy_Dir_Browse_Btn = QtGui.QPushButton(self.centralwidget)
        self.Copy_Dir_Browse_Btn.setGeometry(QtCore.QRect(430, 620, 75, 23))
        self.Copy_Dir_Browse_Btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
"color: rgb(255, 255, 255);"))
        self.Copy_Dir_Browse_Btn.setObjectName(_fromUtf8("Copy_Dir_Browse_Btn"))
        self.Copy_Dir_Browse_Btn.clicked.connect(self.Copy_Directory)
##################################################################################################### - copy directory box
        self.Copy_Dir_Box = QtGui.QLineEdit(self.centralwidget)
        self.Copy_Dir_Box.setGeometry(QtCore.QRect(10, 620, 411, 20))
        self.Copy_Dir_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Copy_Dir_Box.setObjectName(_fromUtf8("Copy_Dir_Box"))
##################################################################################################### - copy files button
        self.Copy_Files_Btn = QtGui.QPushButton(self.centralwidget)
        self.Copy_Files_Btn.setGeometry(QtCore.QRect(510, 620, 75, 23))
        self.Copy_Files_Btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
"color: rgb(255, 255, 255);"))
        self.Copy_Files_Btn.setObjectName(_fromUtf8("Copy_Files_Btn"))
        self.Copy_Files_Btn.clicked.connect(self.Copy_Files_action)
##################################################################################################### - movie preview box
        self.Mov_preview_Box =  QtGui.QLabel(self.centralwidget)
        self.Mov_preview_Box.setGeometry(QtCore.QRect(820, 110, 1011, 751))
        self.Mov_preview_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Mov_preview_Box.setObjectName(_fromUtf8("Mov_preview_Box"))
##################################################################################################### - movie preview button
        self.Mov_Preview_Btn = QtGui.QPushButton(self.centralwidget)
        self.Mov_Preview_Btn.setGeometry(QtCore.QRect(1300, 870, 75, 23))
        self.Mov_Preview_Btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
"color: rgb(255, 255, 255);"))
        self.Mov_Preview_Btn.setObjectName(_fromUtf8("Mov_Preview_Btn"))
        self.Mov_Preview_Btn.clicked.connect(self.preview)
##################################################################################################### - close button
        self.Close_Btn = QtGui.QPushButton(self.centralwidget)
        self.Close_Btn.setGeometry(QtCore.QRect(1800, 960, 75, 23))
        self.Close_Btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
"color: rgb(255, 255, 255);"))
        self.Close_Btn.setObjectName(_fromUtf8("Close_Btn"))
        self.Close_Btn.clicked.connect(self.Close)
##################################################################################################### - About btn
        self.About_Btn = QtGui.QPushButton(self.centralwidget)
        self.About_Btn.setGeometry(QtCore.QRect(1850, 30, 31, 23))
        icon  = QtGui.QPixmap('FStore.png')
        self.About_Btn.setIcon(QtGui.QIcon(icon))
        self.About_Btn.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);"))
        self.About_Btn.setText(_fromUtf8(""))
        self.About_Btn.setObjectName(_fromUtf8("About_Btn"))
        self.About_Btn.clicked.connect(self.About_lib)
####################################################################################### - select all
        self.Select_all_bt = QtGui.QCheckBox(self.centralwidget)
        self.Select_all_bt.setGeometry(QtCore.QRect(10, 130, 120, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Select_all_bt.setFont(font)
        self.Select_all_bt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Select_all_bt.setObjectName(_fromUtf8("Auto_Transfer_bt"))
        self.Select_all_bt.stateChanged.connect(self.Select_all_bt_func)
####################################################################################### - secondary search
        self.Second_search_bt = QtGui.QCheckBox(self.centralwidget)
        self.Second_search_bt.setGeometry(QtCore.QRect(10, 355, 155, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Second_search_bt.setFont(font)
        self.Second_search_bt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Second_search_bt.setObjectName(_fromUtf8("Auto_Transfer_bt"))
        self.Second_search_bt.stateChanged.connect(self.S_Search)
##################################################################################################### - Static texts
        self.Mocap_Lib_Text = QtGui.QLabel(self.centralwidget)
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
        self.Take_Preview_Txt = QtGui.QLabel(self.centralwidget)
        self.Take_Preview_Txt.setGeometry(QtCore.QRect(1300, 90, 111, 16))
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
        self.About_Txt = QtGui.QLabel(self.centralwidget)
        self.About_Txt.setGeometry(QtCore.QRect(1850, 10, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.About_Txt.setFont(font)
        self.About_Txt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.About_Txt.setObjectName(_fromUtf8("About_Txt"))
#####################################################################################################
        self.Search_Dir_Text = QtGui.QLabel(self.centralwidget)
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
        self.copy_Dir_Txt = QtGui.QLabel(self.centralwidget)
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
        self.keyword_filter_txt = QtGui.QLabel(self.centralwidget)
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
        self.radioButton_c3d.raise_()
        self.radioButton_x2d.raise_()
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
        self.Mov_Preview_Btn.raise_()
        self.Close_Btn.raise_()
        self.Mocap_Lib_Text.raise_()
        self.Take_Preview_Txt.raise_()
        self.About_Btn.raise_()
        self.About_Txt.raise_()
        self.Search_Dir_Text.raise_()
        self.copy_Dir_Txt.raise_()
#####################################################################################################################################################################
#####################################################################################################################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.radioButton_fbx.setText(_translate("MainWindow", "Fbx", None))
        self.radioButton_mov.setText(_translate("MainWindow", "mov", None))
        self.radioButton_c3d.setText(_translate("MainWindow", "C3D", None))
        self.radioButton_x2d.setText(_translate("MainWindow", "x2d", None))
        self.search_btn.setText(_translate("MainWindow", "Search", None))
        self.filter_btn.setText(_translate("MainWindow", "Filter", None))
        self.Sirch_Dir_Browse_bt.setText(_translate("MainWindow", "Browse..", None))
        self.filter_reset_btn.setText(_translate("MainWindow", "Reset", None))
        self.Copy_Dir_Browse_Btn.setText(_translate("MainWindow", "Browse..", None))
        self.Copy_Files_Btn.setText(_translate("MainWindow", "Copy files", None))
        self.Mov_Preview_Btn.setText(_translate("MainWindow", "Preview", None))
        self.Close_Btn.setText(_translate("MainWindow", "Close", None))
        self.Mocap_Lib_Text.setText(_translate("MainWindow", "Mocap Library Database", None))
        self.Take_Preview_Txt.setText(_translate("MainWindow", "Take Preview", None))
        self.About_Txt.setText(_translate("MainWindow", "About", None))
        self.Search_Dir_Text.setText(_translate("MainWindow", "Search Directory", None))
        self.copy_Dir_Txt.setText(_translate("MainWindow", "Copy Directory", None))
        self.keyword_filter_txt.setText(_translate("MainWindow", "Keyword Filter", None))
        self.Select_all_bt.setText(_translate("MainWindow", "Select/unselect all", None))
        self.Second_search_bt.setText(_translate("MainWindow", "Activate secondary search", None))
        self.Sec_radioButton_fbx.setText(_translate("MainWindow", "Fbx", None))
        self.Sec_radioButton_c3d.setText(_translate("MainWindow", "C3D", None))
        self.Sec_radioButton_x2d.setText(_translate("MainWindow", "x2d", None))
        self.SecSearch_Dir_Browse_bt.setText(_translate("MainWindow", "Browse..", None))
        
    def Search_Directory(self):
        self.Master_Directory = str(QFileDialog.getExistingDirectory())
        self.Search_Dir_Box.setText(self.Master_Directory)

    def Sec_Search_Directory(self):
        
        self.Sec_Master_Directory = str(QFileDialog.getExistingDirectory())
        self.SearchSec_Dir_Box.setText(self.Sec_Master_Directory)

    def file_search (self):

        self.files=0
        if self.radioButton_fbx.isChecked()==True:
            self.file_ext=(".fbx")
        elif self.radioButton_mov.isChecked()==True:
            self.file_ext=(".mov")
        elif self.radioButton_c3d.isChecked()==True:
            self.file_ext=(".c3d")
        elif self.radioButton_x2d.isChecked()==True:
            self.file_ext=(".x2d")
        else:
            Tk().withdraw()
            tkMessageBox.showinfo('Error', 'Please choose file type')
            self.files=1
        if self.secondary_search==1:
            if self.Sec_radioButton_fbx.isChecked()==True:
                self.file_ext_Sec=(".fbx")
            elif self.Sec_radioButton_c3d.isChecked()==True:
                self.file_ext_Sec=(".c3d")
            elif self.Sec_radioButton_x2d.isChecked()==True:
                self.file_ext_Sec=(".x2d")
            else:
                Tk().withdraw()
                tkMessageBox.showinfo('Error', 'Please choose file type')
                self.files=1
        
            
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
                           self.item=QtGui.QListWidgetItem()
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
                               self.item=QtGui.QListWidgetItem()
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
            self.keyword="Misc_"
        
        self.Select_all_bt.setCheckState(QtCore.Qt.Unchecked)
        try:
            self.itemsTextList =  [str(self.file_listwidget.item(i).text()) for i in range(self.file_listwidget.count())]
            self.file_listwidget.clear()
            for fi in self.itemsTextList:
                    if self.keyword in fi:
                           item_filt=QtGui.QListWidgetItem()
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
                               item_filt=QtGui.QListWidgetItem()
                               item_filt.setText(fi)
                               item_filt.setFlags(item_filt.flags()|QtCore.Qt.ItemIsUserCheckable)
                               item_filt.setCheckState(QtCore.Qt.Unchecked)
                               self.file_listwidget_sec.addItem(item_filt)
                for i in range(len(self.file_directory_Sec)): #change this
                    if self.keyword in self.file_directory_Sec[i]:#change this
                        self.file_directory_filt_Sec.append(self.file_directory_Sec[i]) #change this
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
                           self.item=QtGui.QListWidgetItem()
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
                               self.item=QtGui.QListWidgetItem()
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
            for f in self.copy_files:
                shutil.copy(f, self.Copy_Directory_str)
            Tk().withdraw()
            tkMessageBox.showinfo('Success', 'Files copied')
        except NameError as e:
                e = str(e)
                Tk().withdraw()
                tkMessageBox.showinfo('Error', 'Choose Copy location')
                
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
            self.Sec_radioButton_fbx.setCheckable(True)
            self.Sec_radioButton_fbx.setEnabled(True)
            self.Sec_radioButton_c3d.setCheckable(True)
            self.Sec_radioButton_c3d.setEnabled(True)            
            self.Sec_radioButton_x2d.setCheckable(True)
            self.Sec_radioButton_x2d.setEnabled(True)
            
            self.secondary_search=1
        if self.Second_search_bt.isChecked()==False:
            self.Sec_radioButton_fbx.setEnabled(False)
            self.Sec_radioButton_fbx.toggle()
            self.Sec_radioButton_fbx.setCheckable(False)

            self.Sec_radioButton_c3d.setEnabled(False)
            self.Sec_radioButton_c3d.toggle()
            self.Sec_radioButton_c3d.setCheckable(False)

            self.Sec_radioButton_x2d.setEnabled(False)
            self.Sec_radioButton_x2d.toggle()
            self.Sec_radioButton_x2d.setCheckable(False)
            self.secondary_search=0
                
    def preview(self):
        self.video_preview_file=[]
        self.scale_percent=100

        if self.file_ext==".mov": 
            self.Selected_file=self.file_listwidget.selectedIndexes()[0]
            self.Selected_file=self.Selected_file.data().toString()
            self.Selected_file_str=str(self.Selected_file)
            
            for i in range(len(self.file_directory_filt)):
                if self.Selected_file_str in self.file_directory_filt[i]:
                    self.video_preview_file.append(self.file_directory_filt[i])
            self.cap=cv2.VideoCapture(self.video_preview_file[0])
            if(self.cap.isOpened())==False:
               print("error")
            while(self.cap.isOpened()):
                ret, frame = self.cap.read()
                try:
                    width2=int(frame.shape[1]*self.scale_percent/100)
                    height2=int(frame.shape[0]*self.scale_percent/100)
                    dim=(width2,height2)
                    img=cv2.resize(frame, dim, interpolation = cv2.INTER_AREA) 
                    if ret ==True:
                        self.displayImage(img,1)
                        if cv2.waitKey(25) &0xFF == ord('q'):
                            break
                    else:
                       break
                except AttributeError as e:
                    e=str(e)
                    break
                
            self.cap.release()
            cv2.destroyAllWindows()
            
    def displayImage(self,img,window=1):                                            # conversion of cam 1 into pyqt widget 
        qformat=QImage.Format_Indexed8
        if (len(img.shape))==3: #[0]=rows,[1]=cols,[2]=channels
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        Out_img=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)  
        Out_Img=Out_img.rgbSwapped() #BGR>>RGB
        
        if window==1:
             self.Mov_preview_Box.setPixmap(QPixmap.fromImage(Out_Img))
             self.Mov_preview_Box.setScaledContents(True)
            # counter1 +=1           
        
    def About_lib(self):

        Tk().withdraw()
        tkMessageBox.showinfo('About', 'Mocap Database Version 1.0')

    def Close(self):

        MainWindow.close()
        MainWindow.destroy()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

