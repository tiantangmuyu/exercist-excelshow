#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:40:45 2021

@author: mutt
"""
import sys
import pandas as pd


from PyQt5.QtWidgets import QApplication, QMainWindow,QFileSystemModel,QHeaderView
from PyQt5 import QtCore


from excel_show_ui import Ui_MainWindow
from PandasModel import PandasModel

import os
basic_path      =  os.path.abspath(os.path.dirname(__file__))



class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.datadf = pd.DataFrame()
        self.setupUi(self)
        self.init_fil_show_treeview()    
        self.search_btn.clicked.connect(self.search_keyword)
        self.search_box.currentIndexChanged.connect(self.selectionchange)
        
        
        

    def init_fil_show_treeview(self):
        self.fil_show_treeview
        self.model = QFileSystemModel()
        self.model.setRootPath(basic_path) 
        #self.model.setFilter(QtCore.QDir.Dirs|QtCore.QDir.NoDotAndDotDot)
        self.model.setNameFilterDisables(False)
        self.model.setNameFilters(['*.xls','*.xlsx'])
        self.fil_show_treeview.doubleClicked.connect(self.show_excel_with_double_clicked)
        self.fil_show_treeview.setModel(self.model)
        self.fil_show_treeview.setRootIndex(self.model.index(basic_path))
        self.fil_show_treeview.setAnimated(False)
        self.fil_show_treeview.setIndentation(40)
        self.fil_show_treeview.setSortingEnabled(True)
        self.fil_show_treeview.setWindowTitle("Dir View")
        self.fil_show_treeview.resize(640, 480)
        self.fil_show_treeview.setColumnWidth(0, 300)
        
        
        
        #自适应列宽度
        #self.excel_show_tabelview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    
    def show_excel_with_double_clicked(self, Qmodelidx):
    
        #获取双击后的指定路径
        filePath = self.model.filePath(Qmodelidx)
        kind = self.model.fileInfo(Qmodelidx).isFile()
        
        if kind:
            self.datadf = load_data(filePath,[0]) 
            if len(self.datadf.columns) <= 15:
                self.excel_show_tabelview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            else:
                self.excel_show_tabelview.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
                
            
        else:
            #合并文件操作
            PathDataSet = os.listdir(filePath) 
            full_path = [filePath + "/" + i for i in PathDataSet if ".xls" in i  ]
            self.datadf = pd.DataFrame()
            for path in full_path :
                self.datadf = self.datadf.append(load_data(path,[0]),ignore_index=True)
            
            
            if len(self.datadf.columns) <= 15:
                self.excel_show_tabelview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            else:
                self.excel_show_tabelview.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
                
        self.excel_show_tabelview.setModel(PandasModel(self.datadf))
        self.show_QComboBox()
        
    def show_QComboBox(self):
        self.search_box.clear()
        #self.search_box.addItem("全选")
        self.search_box.addItems(self.datadf.columns)
        print(self.search_box.currentText())
            
    #combobox 
    def selectionchange(self):
        print(self.search_box.currentText())
            
        
        
        

        
    #search btn   
    def search_keyword(self):
        print("搜索按钮点击")
    
        
    
def load_data(data_path,drop_list=[] ,healder_int=1):  
    
    try:
        
        df = pd.read_excel(data_path,header=healder_int,sheet_name = 0)
        df.fillna("",inplace=True)
        df.index=df.index+1
        if len(drop_list) != 0 :
            df.drop(df.columns[drop_list],axis=1,inplace=True)
        
        
        return df
    except BaseException as e:
        print("error:", e)
        return pd.DataFrame.empty()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.setWindowTitle("数据查询系统 Beta 0.1")
    myWin.show()
    sys.exit(app.exec_())






















'''
from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd

from PandasModel import PandasModel

from dqpy import Ui_Form












class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        
        vLayout = QtWidgets.QVBoxLayout(self)
        hLayout = QtWidgets.QHBoxLayout()
        
        self.pathLE = QtWidgets.QLineEdit(self)
        hLayout.addWidget(self.pathLE)
        
        self.loadBtn = QtWidgets.QPushButton("Select File", self)
        hLayout.addWidget(self.loadBtn)
        vLayout.addLayout(hLayout)
        
        self.pandasTv = QtWidgets.QTableView(self)
        vLayout.addWidget(self.pandasTv)
        
        self.loadBtn.clicked.connect(self.loadFile)
        
        self.pandasTv.setSortingEnabled(True)

    def loadFile(self):
        
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开文件", "", "excel(*.xlsx *.xls)");
        self.pathLE.setText(fileName)
        df = pd.read_excel(fileName,header = 1)
        model = PandasModel(df)
        self.pandasTv.setModel(model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
'''