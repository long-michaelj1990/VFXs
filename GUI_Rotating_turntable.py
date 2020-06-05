# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rotating_turntable.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import Arduino
from Arduino import arduino
import serial
from Tkinter import *
import tkMessageBox
import time
import zmq
from threading import Thread,Lock
from decimal import *
import json

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
        self.ardOpen=0
        self.autostart=0
        self.image_count=0
        self.pause_scan=0
        self.resume_scan=0
        self.stop_scan=0
        self.poleriseShot=0
        self.CamA="A"
        self.CamB="B"
        self.CamC="C"
        self.Diffused="Diff"
        self.crosspolar="XP"
        self.lookDev="LD"
        self.QC="No"
        self.photos_taken=[]
        self.QC_photo=[]
        self.Diff_count=0
        self.XP_count=0
        self.LD_count=0
        self.next_move=0
        self.prev_move=0
        self.rotations=0
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(452, 670)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(36,36,36);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# title text
        self.Title = QtGui.QLineEdit(self.centralwidget)
        self.Title.setEnabled(True)
        self.Title.setGeometry(QtCore.QRect(135, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.Title.setFrame(False)
        self.Title.setReadOnly(True)
        self.Title.setObjectName(_fromUtf8("Title"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# save location box
        self.save_box = QtGui.QLineEdit(self.centralwidget)
        self.save_box.setEnabled(True)
        self.save_box.setGeometry(QtCore.QRect(10, 80, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.save_box.setFont(font)
        self.save_box.setAutoFillBackground(False)
        self.save_box.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.save_box.setFrame(False)
        self.save_box.setReadOnly(False)
        self.save_box.setObjectName(_fromUtf8("save_box"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# prop name box
        self.filename_box = QtGui.QLineEdit(self.centralwidget)
        self.filename_box.setEnabled(True)
        self.filename_box.setGeometry(QtCore.QRect(120, 140, 140, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.filename_box.setFont(font)
        self.filename_box.setAutoFillBackground(False)
        self.filename_box.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.filename_box.setFrame(False)
        self.filename_box.setReadOnly(False)
        self.filename_box.setObjectName(_fromUtf8("filename_box"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# prop number box
        self.filenumber_box = QtGui.QLineEdit(self.centralwidget)
        self.filenumber_box.setEnabled(True)
        self.filenumber_box.setGeometry(QtCore.QRect(270, 140, 90, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.filenumber_box.setFont(font)
        self.filenumber_box.setAutoFillBackground(False)
        self.filenumber_box.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.filenumber_box.setFrame(False)
        self.filenumber_box.setReadOnly(False)
        self.filenumber_box.setObjectName(_fromUtf8("filenumber_box"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   polerise check box     
        self.polorise_bt = QtGui.QCheckBox(self.centralwidget)
        self.polorise_bt.setGeometry(QtCore.QRect(30, 280, 150, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.polorise_bt.setFont(font)
        self.polorise_bt.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"background-color: rgb(36,36,36);"))
        self.polorise_bt.setObjectName(_fromUtf8("polorise_bt"))
        self.polorise_bt.setCheckable(True)
        self.polorise_bt.toggle()
        self.polorise_bt.setEnabled(True)
        self.polorise_bt.clicked.connect(self.polar)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# diffused manual  
        self.Diff_bt = QtGui.QCheckBox(self.centralwidget)
        self.Diff_bt.setGeometry(QtCore.QRect(110, 550, 150, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Diff_bt.setFont(font)
        self.Diff_bt.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"background-color: rgb(36,36,36);"))
        self.Diff_bt.setObjectName(_fromUtf8("Diff_bt"))
        self.Diff_bt.setCheckable(True)
        self.Diff_bt.setEnabled(True)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# cross polar manual
        self.CP_bt = QtGui.QCheckBox(self.centralwidget)
        self.CP_bt.setGeometry(QtCore.QRect(180, 550, 150, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.CP_bt.setFont(font)
        self.CP_bt.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"background-color: rgb(36,36,36);"))
        self.CP_bt.setObjectName(_fromUtf8("CP_bt"))
        self.CP_bt.setCheckable(True)
        self.CP_bt.setEnabled(True)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# look deve manual
        self.LD_bt = QtGui.QCheckBox(self.centralwidget)
        self.LD_bt.setGeometry(QtCore.QRect(260, 550, 150, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.LD_bt.setFont(font)
        self.LD_bt.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"background-color: rgb(36,36,36);"))
        self.LD_bt.setObjectName(_fromUtf8("LD_bt"))
        self.LD_bt.setCheckable(True)
        self.LD_bt.setEnabled(True)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# show name box
        self.Show_Name = QtGui.QLineEdit(self.centralwidget)
        self.Show_Name.setEnabled(True)
        self.Show_Name.setGeometry(QtCore.QRect(10, 140, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Show_Name.setFont(font)
        self.Show_Name.setAutoFillBackground(False)
        self.Show_Name.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.Show_Name.setFrame(False)
        self.Show_Name.setReadOnly(False)
        self.Show_Name.setObjectName(_fromUtf8("Show_Name"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# wait interval box
        self.wait_box = QtGui.QLineEdit(self.centralwidget)
        self.wait_box.setEnabled(True)
        self.wait_box.setGeometry(QtCore.QRect(230, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.wait_box.setFont(font)
        self.wait_box.setAutoFillBackground(False)
        self.wait_box.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.wait_box.setFrame(False)
        self.wait_box.setReadOnly(False)
        self.wait_box.setObjectName(_fromUtf8("wait_box"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# degree per rotation box
        self.degree_box = QtGui.QLineEdit(self.centralwidget)
        self.degree_box.setEnabled(True)
        self.degree_box.setGeometry(QtCore.QRect(30, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.degree_box.setFont(font)
        self.degree_box.setAutoFillBackground(False)
        self.degree_box.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.degree_box.setFrame(False)
        self.degree_box.setReadOnly(False)
        self.degree_box.setObjectName(_fromUtf8("degree_box"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# photo number box
        self.number_text_boc = QtGui.QLineEdit(self.centralwidget)
        self.number_text_boc.setEnabled(True)
        self.number_text_boc.setGeometry(QtCore.QRect(340, 445, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.number_text_boc.setFont(font)
        self.number_text_boc.setAutoFillBackground(False)
        self.number_text_boc.setStyleSheet(_fromUtf8("background-color: rgb(36,36,36)\n;color: rgb(255, 255, 255);"))
        self.number_text_boc.setFrame(False)
        self.number_text_boc.setReadOnly(True)
        self.number_text_boc.setObjectName(_fromUtf8("number_text_boc"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# degree text
        self.degrees_text = QtGui.QLineEdit(self.centralwidget)
        self.degrees_text.setEnabled(True)
        self.degrees_text.setGeometry(QtCore.QRect(100, 230, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.degrees_text.setFont(font)
        self.degrees_text.setAutoFillBackground(False)
        self.degrees_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.degrees_text.setFrame(False)
        self.degrees_text.setReadOnly(True)
        self.degrees_text.setObjectName(_fromUtf8("degrees_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# filename text
        self.filename_text = QtGui.QLineEdit(self.centralwidget)
        self.filename_text.setEnabled(True)
        self.filename_text.setGeometry(QtCore.QRect(160, 115, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.filename_text.setFont(font)
        self.filename_text.setAutoFillBackground(False)
        self.filename_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.filename_text.setFrame(False)
        self.filename_text.setReadOnly(True)
        self.filename_text.setObjectName(_fromUtf8("filename_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# file number text
        self.filenumb_text = QtGui.QLineEdit(self.centralwidget)
        self.filenumb_text.setEnabled(True)
        self.filenumb_text.setGeometry(QtCore.QRect(280, 115, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.filenumb_text.setFont(font)
        self.filenumb_text.setAutoFillBackground(False)
        self.filenumb_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.filenumb_text.setFrame(False)
        self.filenumb_text.setReadOnly(True)
        self.filenumb_text.setObjectName(_fromUtf8("filenumb_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# show name text
        self.showname_text = QtGui.QLineEdit(self.centralwidget)
        self.showname_text.setEnabled(True)
        self.showname_text.setGeometry(QtCore.QRect(30, 115, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.showname_text.setFont(font)
        self.showname_text.setAutoFillBackground(False)
        self.showname_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.showname_text.setFrame(False)
        self.showname_text.setReadOnly(True)
        self.showname_text.setObjectName(_fromUtf8("showname_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# setup text
        self.setup_text = QtGui.QLineEdit(self.centralwidget)
        self.setup_text.setEnabled(True)
        self.setup_text.setGeometry(QtCore.QRect(190, 180, 50, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.setup_text.setFont(font)
        self.setup_text.setAutoFillBackground(False)
        self.setup_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.setup_text.setFrame(False)
        self.setup_text.setReadOnly(True)
        self.setup_text.setObjectName(_fromUtf8("setup_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arduino text
        self.arduino_text = QtGui.QLineEdit(self.centralwidget)
        self.arduino_text.setEnabled(True)
        self.arduino_text.setGeometry(QtCore.QRect(380, 115, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.arduino_text.setFont(font)
        self.arduino_text.setAutoFillBackground(False)
        self.arduino_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.arduino_text.setFrame(False)
        self.arduino_text.setReadOnly(True)
        self.arduino_text.setObjectName(_fromUtf8("arduino_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# values set text
        self.set_text = QtGui.QLineEdit(self.centralwidget)
        self.set_text.setEnabled(True)
        self.set_text.setGeometry(QtCore.QRect(310, 325, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.set_text.setFont(font)
        self.set_text.setAutoFillBackground(False)
        self.set_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.set_text.setFrame(False)
        self.set_text.setReadOnly(True)
        self.set_text.setObjectName(_fromUtf8("set_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#      wait interval text  
        self.wait_text = QtGui.QLineEdit(self.centralwidget)
        self.wait_text.setEnabled(True)
        self.wait_text.setGeometry(QtCore.QRect(300, 230, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.wait_text.setFont(font)
        self.wait_text.setAutoFillBackground(False)
        self.wait_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.wait_text.setFrame(False)
        self.wait_text.setReadOnly(True)
        self.wait_text.setObjectName(_fromUtf8("wait_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# browse file button
        self.Browse_btn = QtGui.QPushButton(self.centralwidget)
        self.Browse_btn.setGeometry(QtCore.QRect(320, 90, 75, 23))
        self.Browse_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.Browse_btn.setObjectName(_fromUtf8("Browse_btn"))
        self.Browse_btn.clicked.connect(self.set_save_loction)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# set values button  
        self.setVals_btn = QtGui.QPushButton(self.centralwidget)
        self.setVals_btn.setGeometry(QtCore.QRect(130, 320, 75, 23))
        self.setVals_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.setVals_btn.setObjectName(_fromUtf8("setVals_btn"))
        self.setVals_btn.clicked.connect(self.set_Vals)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# reset values button
        self.reset_btn = QtGui.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(220, 320, 81, 23))
        self.reset_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.reset_btn.setObjectName(_fromUtf8("reset_btn"))
        self.reset_btn.clicked.connect(self.Reset_vals)
        self.reset_btn.setEnabled(False)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# start scan button
        self.start_btn = QtGui.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(150, 360, 111, 41))
        self.start_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.start_btn.setObjectName(_fromUtf8("start_btn"))
        self.start_btn.clicked.connect(self.Start_scan_thread)
        self.start_btn.setEnabled(False)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# pause button
        self.pause_btn = QtGui.QPushButton(self.centralwidget)
        self.pause_btn.setGeometry(QtCore.QRect(170, 410, 75, 23))
        self.pause_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.pause_btn.setObjectName(_fromUtf8("pause_btn"))
        self.pause_btn.clicked.connect(self.Pause_scan)
        self.pause_btn.setEnabled(False)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# resume button 
        self.resume_btn = QtGui.QPushButton(self.centralwidget)
        self.resume_btn.setGeometry(QtCore.QRect(170, 440, 75, 23))
        self.resume_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.resume_btn.setObjectName(_fromUtf8("resume_btn"))
        self.resume_btn.clicked.connect(self.Resume_scan_thread)
        self.resume_btn.setEnabled(False)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# stop button
        self.stop_btn = QtGui.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(170, 470, 75, 23))
        self.stop_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.stop_btn.setObjectName(_fromUtf8("stop_btn"))
        self.stop_btn.clicked.connect(self.Stop_scan)
        self.stop_btn.setEnabled(False)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# previous scan buttn
        self.prev_btn = QtGui.QPushButton(self.centralwidget)
        self.prev_btn.setGeometry(QtCore.QRect(90, 520, 101, 23))
        self.prev_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.prev_btn.setObjectName(_fromUtf8("prev_btn"))
        self.prev_btn.clicked.connect(self.Prev_scan)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# next scan button
        self.next_btn = QtGui.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(220, 520, 101, 23))
        self.next_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.next_btn.setObjectName(_fromUtf8("next_btn"))
        self.next_btn.clicked.connect(self.Next_scan)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# manual scan button
        self.manual_btn = QtGui.QPushButton(self.centralwidget)
        self.manual_btn.setGeometry(QtCore.QRect(150, 570, 111, 41))
        self.manual_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.manual_btn.setObjectName(_fromUtf8("manual_btn"))
        self.manual_btn.clicked.connect(self.Manual_scan)
        self.manual_btn.setEnabled(False)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# close gui btton
        self.close_btn = QtGui.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(160, 620, 90, 23))
        self.close_btn.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);"))
        self.close_btn.setObjectName(_fromUtf8("next_btn"))
        self.close_btn.clicked.connect(self.close)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# lcd number box  
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 445, 61, 31))
        self.lcdNumber.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# com port drop down
        self.COMport_Dropdown= QtGui.QComboBox(self.centralwidget)
        self.COMport_Dropdown.setGeometry(QtCore.QRect(370, 150, 67, 20))
        self.COMport_Dropdown.addItem("COM1")
        self.COMport_Dropdown.addItem("COM2")
        self.COMport_Dropdown.addItem("COM3")
        self.COMport_Dropdown.addItem("COM4")
        self.COMport_Dropdown.addItem("COM5")
        self.COMport_Dropdown.addItem("COM6")
        self.COMport_Dropdown.addItem("COM7")
        self.COMport_Dropdown.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# photo captured text   
        self.captured_text = QtGui.QLineEdit(self.centralwidget)
        self.captured_text.setEnabled(True)
        self.captured_text.setGeometry(QtCore.QRect(280, 495, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.captured_text.setFont(font)
        self.captured_text.setAutoFillBackground(False)
        self.captured_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255)\n;""background-color: rgb(36,36,36);"))
        self.captured_text.setFrame(False)
        self.captured_text.setReadOnly(True)
        self.captured_text.setObjectName(_fromUtf8("captured_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# photo progree text
        self.status_text = QtGui.QLineEdit(self.centralwidget)
        self.status_text.setEnabled(True)
        self.status_text.setGeometry(QtCore.QRect(280, 385, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.status_text.setFont(font)
        self.status_text.setAutoFillBackground(False)
        self.status_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255)\n;""background-color: rgb(36,36,36);"))
        self.status_text.setFrame(False)
        self.status_text.setReadOnly(True)
        self.status_text.setObjectName(_fromUtf8("status_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# manual capture text
        self.manualstatus_text = QtGui.QLineEdit(self.centralwidget)
        self.manualstatus_text.setEnabled(True)
        self.manualstatus_text.setGeometry(QtCore.QRect(280, 575, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.manualstatus_text.setFont(font)
        self.manualstatus_text.setAutoFillBackground(False)
        self.manualstatus_text.setStyleSheet(_fromUtf8("color: rgb(255,255,255)\n;""background-color: rgb(36,36,36);"))
        self.manualstatus_text.setFrame(False)
        self.manualstatus_text.setReadOnly(True)
        self.manualstatus_text.setObjectName(_fromUtf8("manualstatus_text"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.seq_num = 0
        self.context = zmq.Context()
        self.sub_address = "tcp://127.0.0.1:54544" #end address of camera
        self.sub_socket = self.context.socket(zmq.REQ) # bidirectional socket
        self.sub_socket.connect(self.sub_address)

        self.seq_num = 0
        self.context_test = zmq.Context()
        self.sub_address_test = "tcp://127.0.0.1:54543" #end address of camera
        self.sub_socket_test = self.context_test.socket(zmq.SUB) # bidirectional socket
        self.sub_socket_test.setsockopt(zmq.SUBSCRIBE, b"")
        self.sub_socket_test.connect(self.sub_address_test)
        
        print("Opened listener to: {0}".format(self.sub_address))
        t1=Thread(target=self.SmartShooter_Listener)
        t1.setDaemon(True)
        t1.start()
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Title.setText(_translate("MainWindow", "Turntable Control", None))
        self.save_box.setText(_translate("MainWindow", "Save location...", None))
        self.Browse_btn.setText(_translate("MainWindow", "Browse", None))
        self.filename_box.setText(_translate("MainWindow", "Prop name..", None))
        self.filenumber_box.setText(_translate("MainWindow", "1001", None))
        self.Show_Name.setText(_translate("MainWindow", "Show name..", None))
        self.wait_box.setText(_translate("MainWindow", "3", None))
        self.degree_box.setText(_translate("MainWindow", "10", None))
        self.setVals_btn.setText(_translate("MainWindow", "Set values", None))
        self.reset_btn.setText(_translate("MainWindow", "Reset Default", None))
        self.degrees_text.setText(_translate("MainWindow", "Degrees per rotation ", None))
        self.wait_text.setText(_translate("MainWindow", "Wait Interval (s)", None))
        self.start_btn.setText(_translate("MainWindow", "Start", None))
        self.pause_btn.setText(_translate("MainWindow", "Pause", None))
        self.resume_btn.setText(_translate("MainWindow", "Resume", None))
        self.stop_btn.setText(_translate("MainWindow", "Stop", None))
        self.prev_btn.setText(_translate("MainWindow", "Previous position ", None))
        self.next_btn.setText(_translate("MainWindow", "Next Position", None))
        self.manual_btn.setText(_translate("MainWindow", "Manual Capture", None))
        self.number_text_boc.setText(_translate("MainWindow", "/72", None))
        self.captured_text.setText(_translate("MainWindow", "Captured Images", None))
        self.set_text.setText(_translate("MainWindow", "", None))
        self.close_btn.setText(_translate("MainWindow", "Close", None))
        self.polorise_bt.setText(_translate("MainWindow", "Cross polerization active", None))
        self.status_text.setText(_translate("MainWindow", "", None))
        self.manualstatus_text.setText(_translate("MainWindow", "", None))
        self.filename_text.setText(_translate("MainWindow", "Prop name", None))
        self.filenumb_text.setText(_translate("MainWindow", "File number", None))
        self.showname_text.setText(_translate("MainWindow", "Show name", None))
        self.arduino_text.setText(_translate("MainWindow", "Arduino", None))
        self.setup_text.setText(_translate("MainWindow", "Setup", None))
        self.Diff_bt.setText(_translate("MainWindow", "Diffuse", None))
        self.CP_bt.setText(_translate("MainWindow", "X Polar", None))
        self.LD_bt.setText(_translate("MainWindow", "LookDev", None))

    def set_save_loction(self):
        Save_location = str(QFileDialog.getExistingDirectory())
        self.save_box.setText(Save_location)

        self.photolocation = {}
        self.photolocation["msg_type"] = "Request"
        self.photolocation["msg_id"] = "SetOptionsMsg"
        self.photolocation["msg_ref_num"] = 12
        self.photolocation['GridPhotoPath'] = Save_location
        self.sub_socket.send_string(json.dumps(self.photolocation))
        rep = self.sub_socket.recv()
        str_msg_location = rep.decode("utf-8-sig")
        json_msg_photlocation = json.loads(str_msg_location)


    def set_Vals(self):        
        self.autostart=0
        self.image_count=0
        self.pause_scan=0
        self.resume_scan=0
        self.stop_scan=0
        self.poleriseShot=0
        self.photos_taken=[]
        self.QC_photo=[]
        self.Diff_count=0
        self.XP_count=0
        self.LD_count=0
        
        self.con = {}
        self.con["msg_type"] = "Request"
        self.con["msg_id"] = "ConnectMsg"
        self.con["msg_ref_num"] = 0
        self.con["CameraSelection"] = "All"
        self.sub_socket.send_string(json.dumps(self.con))
        self.rep_con = self.sub_socket.recv()
        self.str_msg_con = self.rep_con.decode("utf-8-sig")
        self.json_msg_con = json.loads(self.str_msg_con)
        

        PORT=str(self.COMport_Dropdown.currentText())
        try:
            if self.ardOpen==0:
                self.ard = serial.Serial(PORT, 9600,timeout=.1)
                self.Show_Name_text=self.Show_Name.text()
                self.wait_box_int= int(self.wait_box.text())
                self.degree_box_int= int(self.degree_box.text())
                self.number_text_boc_int=str(self.number_text_boc.text())
                self.splittext=self.number_text_boc_int.split("/")
                self.Total_image_number=int(self.splittext[1])

                if self.polorise_bt.isChecked()==True:
                    self.image_total=360/self.degree_box_int*2
                    self.number_text_boc.setText(_translate("MainWindow", "/"+str(self.image_total), None))

                    self.lcdNumber.display(self.image_count)
                    
                if self.polorise_bt.isChecked()==False:
                    self.image_total=360/self.degree_box_int
                    self.number_text_boc.setText(_translate("MainWindow", "/"+str(self.image_total), None))

                    self.lcdNumber.display(self.image_count)
                    
                Tk().withdraw()
                tkMessageBox.showinfo('Success','Arduino connected')
                self.set_text.setText(_translate("MainWindow", "Values Set", None))
                self.ardOpen=1

                self.save_file=self.save_box.text()+"\\"+self.Show_Name_text+"_Log.csv"
                with open(self.save_file,'w+') as f:
                    f.write("Prop Name,Diff Total,XP Total,LD Total, Manual QC\n")
                    f.close()
                
            else:
                self.wait_box_int= int(self.wait_box.text())
                self.degree_box_int= int(self.degree_box.text())
                self.number_text_boc_int=str(self.number_text_boc.text())
                self.splittext=self.number_text_boc_int.split("/")
                self.Total_image_number=int(self.splittext[1])

                if self.polorise_bt.isChecked()==True:
                    self.image_total=360/self.degree_box_int*2
                    self.number_text_boc.setText(_translate("MainWindow", "/"+str(self.image_total), None))
                    self.lcdNumber.display(self.image_count)
                    
                if self.polorise_bt.isChecked()==False:
                    self.image_total=360/self.degree_box_int
                    self.number_text_boc.setText(_translate("MainWindow", "/"+str(self.image_total), None))
                    self.lcdNumber.display(self.image_count)
                    
                self.set_text.setText(_translate("MainWindow", "Values updated", None))
            
            self.manual_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)
            self.resume_btn.setEnabled(True)
            self.pause_btn.setEnabled(True)
            self.start_btn.setEnabled(True)
            self.reset_btn.setEnabled(True)    
        except:
                Tk().withdraw()
                tkMessageBox.showinfo('Error','Port error')
        
    def Reset_vals(self):
        self.autostart=0
        self.image_count=0
        self.pause_scan=0
        self.resume_scan=0
        self.stop_scan=0
        self.poleriseShot=0
        self.photos_taken=[]

        self.next_move=0
        self.prev_move=0
    
        for i in range(0,self.rotations):
            self.ard.write("b_"+str(self.degree_box_int)+",\n")
            self.data = self.ard.readline()
        self.rotations=0
        self.set_text.setText(_translate("MainWindow", "Values Reset", None))
        self.wait_box.setText(_translate("MainWindow", "3", None))
        self.degree_box.setText(_translate("MainWindow", "10", None))
        self.lcdNumber.display(self.image_count)
        self.filenumber_box.setText(_translate("MainWindow", "1001", None))
        
    def polar(self):
        if self.polorise_bt.isChecked()==True:
                self.wait_box_int= int(self.wait_box.text())
                self.degree_box_int= int(self.degree_box.text())
                self.number_text_boc_int=str(self.number_text_boc.text())

                self.image_total=360/self.degree_box_int*2
                self.number_text_boc.setText(_translate("MainWindow", "/"+str(self.image_total), None))
                self.image_count=0
                self.lcdNumber.display(self.image_count)

        if self.polorise_bt.isChecked()==False:
                self.wait_box_int= int(self.wait_box.text())
                self.degree_box_int= int(self.degree_box.text())
                self.number_text_boc_int=str(self.number_text_boc.text())

                self.image_total=360/self.degree_box_int
                self.number_text_boc.setText(_translate("MainWindow", "/"+str(self.image_total), None))
                self.image_count=0
                self.lcdNumber.display(self.image_count)
        


##############################################################################################################################

    def Start_scan_thread(self):                
        t2=Thread(target=self.Start_scan)
        t2.setDaemon(True)
        t2.start()
        
    def Start_scan(self):
        try:
            self.status_text.setText(_translate("MainWindow", "Scan Started..", None))
            self.filenumb_text_int=int(self.filenumber_box.text())
            if self.pause_scan==0:
                self.image_count=0
            else:
                self.image_count=self.image_count
                
            while self.pause_scan==0 and self.stop_scan==0:
                    
                for i in range(self.image_total+1):
                    if self.image_count==self.image_total+1:
                        self.image_count=self.image_count-1
                        self.lcdNumber.display(0)
                        self.status_text.setText(_translate("MainWindow", "", None))
                        self.newfilenumber=self.filenumb_text_int-1
                        self.filenumber_box.setText(_translate("MainWindow", "1001", None))
                        self.status_text.setText(_translate("MainWindow", "Capture Complete", None))
                        self.unique_QC_photo=set(self.QC_photo)
                        self.unique_QC_list=list(self.unique_QC_photo)
                        with open(self.save_file,'a+') as f:
                            f.write(str(self.filename_box.text())+","+str(self.Diff_count)+","+str(self.XP_count)+","+str(self.LD_count)+","+str(self.unique_QC_list)+"\n")
                            f.close()
                            
                        app.processEvents()
                        self.stop_scan=1
                        break
                    
                    if self.stop_scan==1:
                        self.lcdNumber.display(0)
                        self.filenumber_box.setText(_translate("MainWindow", "1001", None))
                        self.status_text.setText(_translate("MainWindow", "Capture Stopped", None))
                        time.sleep(0.01)
                        for i in range(0,self.rotations):
                            self.ard.write("b_"+str(self.degree_box_int)+",\n")
                            self.data = self.ard.readline()
                            #time.sleep(0.2)
                        self.rotations=0
                        break
                    
                    if self.pause_scan==0 and self.stop_scan==0:
                        self.autostart=1
                        if self.polorise_bt.isChecked()==False:
                            if self.image_count>0:
                                self.status_text.setText(_translate("MainWindow", "Taking Diff photo", None))
                                app.processEvents()
                            
                        if self.polorise_bt.isChecked()==True:
                            if self.poleriseShot==0:
                                if self.image_count>0:
                                    self.status_text.setText(_translate("MainWindow", "Taking Diff photo", None))
                                    app.processEvents()
                            elif self.poleriseShot==1:
                                if self.image_count>0:
                                    self.status_text.setText(_translate("MainWindow", "Taking XP photo", None))
                                    app.processEvents()
                                    
                        self.pause_btn.setEnabled(False)    
                        time.sleep(self.wait_box_int)
                        
                        if self.image_count>0:
                            self.pause_btn.setEnabled(False)
                            if self.polorise_bt.isChecked()==False:                 
                                self.trigger()
                                time.sleep(1)
                                self.ard.write("a_"+str(self.degree_box_int)+",\n")
                                self.data = self.ard.readline()
                                self.rotations=self.rotations+1
                                
                            if self.polorise_bt.isChecked()==True:
                                if self.poleriseShot==0:
                                    self.trigger()
                                    time.sleep(1)
                                    self.poleriseShot=1
                                elif self.poleriseShot==1:
                                    self.trigger()
                                    time.sleep(1)
                                    self.ard.write("a_"+str(self.degree_box_int)+",\n")
                                    self.data = self.ard.readline()
                                    self.poleriseShot=0
                                    self.rotations=self.rotations+1
                                
                        self.image_count=self.image_count+1
                        self.lcdNumber.display(self.image_count)
                        self.status_text.setText(_translate("MainWindow", "Photo saved", None))
                            
                        self.newfilenumber=self.filenumb_text_int+i
                        self.filenumber_box.setText(_translate("MainWindow", str(self.newfilenumber), None))
                        app.processEvents()
                        time.sleep(1)

                    elif self.pause_scan==1:
                        self.lcdNumber.display(self.image_count)
                        self.filenumber_box.setText(_translate("MainWindow", str(self.newfilenumber), None))
                        self.filenumb_text_int=int(self.filenumber_box.text())
                        self.status_text.setText(_translate("MainWindow", "Paused..", None))
                        time.sleep(0.01)
                        break
                             
        except:
            pass

    def Resume_scan_thread(self):
        t3=Thread(target=self.Resume_scan)
        t3.setDaemon(True)
        t3.start()
        
    def Resume_scan(self):
        try:
            self.autostart=1
            self.pause_scan=2
            self.QC="No"
            self.resume_image=self.image_total-self.image_count
            
            if self.Pause_polerise==0:
                self.poleriseShot=0
            elif self.Pause_polerise==1:
                self.poleriseShot=1                
                
            while self.pause_scan==2 and self.stop_scan==0:                    
                for i in range (self.resume_image+1):
                    if self.image_count==self.image_total+1:
                        self.image_count=self.image_count-1
                        self.lcdNumber.display(0)
                        self.status_text.setText(_translate("MainWindow", "", None))
                        self.newfilenumber=self.filenumb_text_int-1
                        self.filenumber_box.setText(_translate("MainWindow", "1001", None))
                        self.status_text.setText(_translate("MainWindow", "Capture Complete", None))
                        self.unique_QC_photo=set(self.QC_photo)
                        self.unique_QC_list=list(self.unique_QC_photo)
                        with open(self.save_file,'a+') as f:
                            f.write(str(self.filename_box.text())+","+str(self.Diff_count)+","+str(self.XP_count)+","+str(self.LD_count)+","+str(self.unique_QC_list)+"\n")
                            f.close()
                        app.processEvents()
                        self.stop_scan=1
                        break
                    
                    if self.stop_scan==1:
                        self.lcdNumber.display(0)
                        self.filenumber_box.setText(_translate("MainWindow", "1001", None))
                        self.status_text.setText(_translate("MainWindow", "Capture Stopped", None))
                        time.sleep(0.01)
                        for i in range(0,self.rotations):
                            self.ard.write("b_"+str(self.degree_box_int)+",\n")
                            self.data = self.ard.readline()
                            #time.sleep(0.2)
                        self.rotations=0
                        break
        
                    if self.pause_scan==2:
                        if self.polorise_bt.isChecked()==False: 
                            self.status_text.setText(_translate("MainWindow", "Taking Diff photo", None))
                            app.processEvents()
                            
                        if self.polorise_bt.isChecked()==True:
                            if self.poleriseShot==0:
                                self.status_text.setText(_translate("MainWindow", "Taking Diff photo", None))
                                app.processEvents()
                            elif self.poleriseShot==1:
                                self.status_text.setText(_translate("MainWindow", "Taking XP photo", None))
                                app.processEvents()

                        self.pause_btn.setEnabled(False)
                        self.autostart=1
                        self.image_count=self.image_count+1
                        time.sleep(self.wait_box_int)
                        
                        
                        if self.polorise_bt.isChecked()==False:
                            self.trigger()
                            time.sleep(1)
                            self.ard.write("a_"+str(self.degree_box_int)+",\n")
                            self.data = self.ard.readline()
                            self.rotations=self.rotations+1

                        if self.polorise_bt.isChecked()==True:
                            if self.poleriseShot==0:
                                self.trigger()
                                time.sleep(1)
                            elif self.poleriseShot==1:
                                self.trigger()
                                time.sleep(1)
                                self.ard.write("a_"+str(self.degree_box_int)+",\n")
                                self.data = self.ard.readline()
                                self.rotations=self.rotations+1
                        
                        self.lcdNumber.display(self.image_count)
                        self.newfilenumber=self.filenumb_text_int+i+1
                        self.status_text.setText(_translate("MainWindow", "Photo saved", None))

                        self.filenumber_box.setText(_translate("MainWindow", str(self.newfilenumber), None))
                        app.processEvents()
                        time.sleep(1)

                    elif self.pause_scan==1:
                        self.lcdNumber.display(self.image_count)
                        self.filenumber_box.setText(_translate("MainWindow", str(self.newfilenumber), None))
                        self.status_text.setText(_translate("MainWindow", "Paused..", None))
                        self.filenumb_text_int=int(self.filenumber_box.text())
                        time.sleep(0.01)
                        break
                    
        except:
            pass
        
##############################################################################################################################         

    def Manual_scan(self):
        try:
            if self.autostart==0:
                if self.polorise_bt.isChecked()==False:                 
                    self.trigger()
                    time.sleep(1)
                    self.ard.write("a_"+str(self.degree_box_int)+",\n")
                    self.data = self.ard.readline()
                    self.rotations=self.rotations+1
                if self.polorise_bt.isChecked()==True:
                    if self.poleriseShot==0:
                        self.trigger()
                        time.sleep(1)
                    elif self.poleriseShot==1:
                        self.trigger()
                        time.sleep(1)
                        self.ard.write("a_"+str(self.degree_box_int)+",\n")
                        self.data = self.ard.readline()
                        self.rotations=self.rotations+1
                        
                self.filenumb_text_int=int(self.filenumber_box.text())         
                self.manualstatus_text.setText(_translate("MainWindow", "Photo saved", None))
        except:
            pass
        
    def Prev_scan(self):
        try:
            self.next_move=0
            self.rounded_lCD=int((round(self.lcdNumber.value())))
            self.manualstatus_text.setText(_translate("MainWindow", "", None))
            if self.rounded_lCD>0:
                self.image_count=self.image_count-1
                self.lcdNumber.display(self.image_count)
                self.rounded_lCD=int((round(self.lcdNumber.value())))
                self.LED_Length=len(str(self.rounded_lCD))
                if self.LED_Length==1:
                    self.filestnumberstring="100"+str(self.rounded_lCD)
                elif self.LED_Length==2:
                    self.filestnumberstring="10"+str(self.rounded_lCD)
                    
                self.filenumber_box.setText(_translate("MainWindow", str(self.filestnumberstring), None))
            if self.rounded_lCD==0:
                self.lcdNumber.display(0)
                self.image_count=self.image_total
                self.rounded_lCD=int((round(self.lcdNumber.value())))
##                self.LED_Length=len(str(self.rounded_lCD))
##                if self.LED_Length==1:
##                    self.filestnumberstring="100"+str(self.rounded_lCD)
##                elif self.LED_Length==2:
##                    self.filestnumberstring="10"+str(self.rounded_lCD)
                self.filenumber_box.setText(_translate("MainWindow", "1001", None))

            self.filenumb_text_int=int(self.filenumber_box.text())   
            self.prev_move=self.prev_move+1
            ##################################
            if self.polorise_bt.isChecked()==False:
                self.ard.write("b_"+str(self.degree_box_int)+",\n")
                self.data = self.ard.readline()
                self.rotations=self.rotations-1
            if self.polorise_bt.isChecked()==True:
                if self.poleriseShot==0:
                    self.poleriseShot=1
                    self.next_btn.setEnabled(False)
                    pass
                if self.poleriseShot==1:
                    self.poleriseShot=0
                    
                    pass
                if self.prev_move==2:
                    self.ard.write("b_"+str(self.degree_box_int)+",\n")
                    self.data = self.ard.readline()
                    self.rotations=self.rotations-1
                    self.poleriseShot=0
                    self.next_btn.setEnabled(True)
                    self.prev_move=0  
            ##################################
                
        except:
            pass
        
    def Next_scan(self):
        try:
            self.prev_move=0
            self.manualstatus_text.setText(_translate("MainWindow", "", None))
            self.rounded_lCD=int((round(self.lcdNumber.value())))
            self.image_count=self.image_count+1
            self.lcdNumber.display(self.image_count)
            self.rounded_lCD=int((round(self.lcdNumber.value())))
            self.LED_Length=len(str(self.rounded_lCD))
            if self.LED_Length==1:
                self.filestnumberstring="100"+str(self.rounded_lCD)
            elif self.LED_Length==2:
                self.filestnumberstring="10"+str(self.rounded_lCD)
            self.filenumber_box.setText(_translate("MainWindow", str(self.filestnumberstring), None))
            
            if  self.image_count==self.image_total+1:
                self.image_count=0
                self.lcdNumber.display(0)
##                self.rounded_lCD=int((round(self.lcdNumber.value())))
##                self.LED_Length=len(str(self.rounded_lCD))
##                if self.LED_Length==1:
##                    self.filestnumberstring="100"+str(self.rounded_lCD)
##                elif self.LED_Length==2:
##                    self.filestnumberstring="10"+str(self.rounded_lCD)
                self.filenumber_box.setText(_translate("MainWindow", "1001", None))

            self.filenumb_text_int=int(self.filenumber_box.text())
            self.next_move= self.next_move+1
            ##################################

            if self.polorise_bt.isChecked()==False:
                self.ard.write("a_"+str(self.degree_box_int)+",\n")
                self.data = self.ard.readline()
                self.rotations=self.rotations+1
            if self.polorise_bt.isChecked()==True:
                if self.poleriseShot==0:
                    self.poleriseShot=1
                    self.prev_btn.setEnabled(False)
                    pass
                if self.poleriseShot==1:
                    self.poleriseShot=0
                    pass
                if  self.next_move==2:
                    self.ard.write("a_"+str(self.degree_box_int)+",\n")
                    self.data = self.ard.readline()
                    self.rotations=self.rotations+1
                    self.prev_btn.setEnabled(True)
                    self.poleriseShot=0
                    self.next_move=0
            ##################################
    
        except:
            pass
        

##############################################################################################################################        
    def Pause_scan(self):
        try:
            self.pause_scan=1
            self.autostart=0
            self.Pause_polerise=self.poleriseShot
        except:
            pass
        
    def Stop_scan(self):
        try:
            self.stop_scan=1
            self.autostart=0
            self.ard.write("c_\n")
            self.data = self.ard.readline()
        except:
            pass
        
    def close(self):
        try:
            self.ard.close()
        except:
            pass
        MainWindow.close()
##############################################################################################################################
        
        ##############################################################################################################################
                                                    #Smart Shooter
        ##############################################################################################################################
        
    def SmartShooter_Listener(self):
        while (True):
            pass
            
    def trigger(self):
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                                            # take photo command
        self.req = {}
        self.req["msg_type"] = "Request"
        self.req["msg_id"] = "ShootMsg"
        self.req["msg_ref_num"] = 0
        self.req["CameraSelection"] = "All"
        self.sub_socket.send_string(json.dumps(self.req))
        self.rep = self.sub_socket.recv()
        self.str_msg = self.rep.decode("utf-8-sig")
        self.json_msg = json.loads(self.str_msg)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                                # check photo existance whilst  paused for QC
        if self.autostart==0:
             if self.pause_scan==1:
                 for photo in self.photos_taken:
                    if  str(self.filenumber_box.text()) == photo:
             
                            self.QC="Yes"
                            if self.Diff_bt.isChecked()==True:
                                self.LD_bt.setEnabled(False)
                                self.CP_bt.setEnabled(False)
                                self.shot_type_man="Diff"
                                self.poleriseShot=0
                                self.QC_photo.append(str(self.shot_type_man)+"_"+str(self.filenumber_box.text()))
                            elif self.LD_bt.isChecked()==True:
                                self.Diff_bt.setEnabled(False)
                                self.CP_bt.setEnabled(False)
                                self.shot_type_man="LD"
                                self.QC_photo.append(str(self.shot_type_man)+"_"+str(self.filenumber_box.text()))
                            elif self.CP_bt.isChecked()==True:
                                self.LD_bt.setEnabled(False)
                                self.CP_bt.setEnabled(False)
                                self.shot_type_man="XP"
                                self.QC_photo.append(str(self.shot_type_man)+"_"+str(self.filenumber_box.text()))
                                self.poleriseShot=1
                            else:
                                self.shot_type_man="error"
                    elif str(self.newfilenumber) == photo:
                 
                            self.QC="Yes"
                            if self.Diff_bt.isChecked()==True:
                                self.LD_bt.setEnabled(False)
                                self.CP_bt.setEnabled(False)
                                self.shot_type_man="Diff"
                                self.poleriseShot=0
                                self.QC_photo.append(str(self.shot_type_man)+"_"+str(self.filenumber_box.text()))
                            elif self.LD_bt.isChecked()==True:
                                self.Diff_bt.setEnabled(False)
                                self.CP_bt.setEnabled(False)
                                self.shot_type_man="LD"
                                self.QC_photo.append(str(self.shot_type_man)+"_"+str(self.filenumber_box.text()))
                            elif self.CP_bt.isChecked()==True:
                                self.LD_bt.setEnabled(False)
                                self.CP_bt.setEnabled(False)
                                self.shot_type_man="XP"
                                self.QC_photo.append(str(self.shot_type_man)+"_"+str(self.filenumber_box.text()))
                                self.poleriseShot=1
                            else:
                                self.shot_type_man="error"
                    else:
                            self.QC="No"
                            
        if self.pause_scan==1:
            self.photos_taken.append(str(self.newfilenumber))
        else:
            self.photos_taken.append(str(self.filenumber_box.text()))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        if self.polorise_bt.isChecked()==False:
            self.req_rename = {}
            self.req_rename["msg_type"] = "Request"
            self.req_rename["msg_id"] = "SetOptionsMsg"
            self.req_rename["msg_ref_num"] = 2
            self.req_rename["GridUniqueTag"] = str(self.Show_Name_text)+"_"+str(self.filename_box.text())+"_"+str(self.Diffused)+"_"+str(self.CamA)
            self.sub_socket.send_string(json.dumps(self.req_rename))
            self.rep_rename = self.sub_socket.recv()
            self.str_msg_rename = self.rep_rename.decode("utf-8-sig")
            self.json_msg_rename = json.loads(self.str_msg_rename)
            self.Diff_count=self.Diff_count+1
            self.poleriseShot=0

        if self.polorise_bt.isChecked()==True:    
            if self.poleriseShot==0:
                self.req_rename = {}
                self.req_rename["msg_type"] = "Request"
                self.req_rename["msg_id"] = "SetOptionsMsg"
                self.req_rename["msg_ref_num"] = 2
                if self.autostart==1:
                    self.req_rename["GridUniqueTag"] = str(self.Show_Name_text)+"_"+str(self.filename_box.text())+"_"+str(self.Diffused)+"_"+str(self.CamA)
                elif self.autostart==0: #manual capture whilst paused 
                    self.req_rename["GridUniqueTag"] = str(self.Show_Name_text)+"_"+str(self.filename_box.text())+"_"+str(self.shot_type_man)+"_"+str(self.CamA)
                    
                self.sub_socket.send_string(json.dumps(self.req_rename))
                self.rep_rename = self.sub_socket.recv()
                self.str_msg_rename = self.rep_rename.decode("utf-8-sig")
                self.json_msg_rename = json.loads(self.str_msg_rename)
                self.Diff_count=self.Diff_count+1
                self.poleriseShot=1
                
            elif self.poleriseShot==1:
                self.req_rename = {}
                self.req_rename["msg_type"] = "Request"
                self.req_rename["msg_id"] = "SetOptionsMsg"
                self.req_rename["msg_ref_num"] = 2
                if self.autostart==1: 
                    self.req_rename["GridUniqueTag"] = str(self.Show_Name_text)+"_"+str(self.filename_box.text())+"_"+str(self.crosspolar)+"_"+str(self.CamA)
                elif self.autostart==0: #manual capture whilst paused 
                    self.req_rename["GridUniqueTag"] = str(self.Show_Name_text)+"_"+str(self.filename_box.text())+"_"+str(self.shot_type_man)+"_"+str(self.CamA)
                    
                self.sub_socket.send_string(json.dumps(self.req_rename))
                self.rep_rename = self.sub_socket.recv()
                self.str_msg_rename = self.rep_rename.decode("utf-8-sig")
                self.json_msg_rename = json.loads(self.str_msg_rename)
                self.XP_count=self.XP_count+1
                self.poleriseShot=0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

                        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                    # set photo number
        self.req_renum = {}
        self.req_renum["msg_type"] = "Request"
        self.req_renum["msg_id"] = "SetSequenceNumMsg"
        self.req_renum["GridSequenceNum"] = int(self.filenumber_box.text())
        self.sub_socket.send_string(json.dumps(self.req_renum))
        self.rep_renum = self.sub_socket.recv()
        self.str_msg_renum = self.rep_renum.decode("utf-8-sig")
        self.json_msg_renum = json.loads(self.str_msg_renum)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        self.Diff_bt.setEnabled(True)
        self.LD_bt.setEnabled(True)
        self.CP_bt.setEnabled(True)
        self.pause_btn.setEnabled(True)

            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

