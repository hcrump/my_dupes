import os.path
import hashlib
import subprocess
import sys
import re
from PyQt5.QtWidgets import (QApplication,  QMainWindow, QFileSystemModel,
                             QTreeView,QListView,QTreeWidgetItem,QMessageBox)
from PyQt5 import QtGui
from PyQt5.QtCore import QModelIndex
from my_filelist import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.title = "Hdog's duplicate file finder!"
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
           
        #setup filetree
        self.model = QFileSystemModel()
        self.model.setRootPath('C:\\')
        self.filetree.setModel(self.model)        
        self.filetree.setSortingEnabled(True)        
        self.filetree.setWindowTitle('Dir View')
        self.filetree.setMinimumSize(600,300)
        #self.filetree.setMaximumHeight(300)
        self.filetree.setColumnWidth(0,350)
        self.filetree.setColumnWidth(1,75)
        self.filetree.setColumnWidth(2,50)
        self.filetree.my_filepath = 'C:/Users/horace/Desktop'
        self.model.directoryLoaded.connect(self.expand_initial_dir)
        
        #setup shortlist
        self.shortlist.setWindowTitle('Selected Paths')
        
        #setup filelist
        self.filelist.setMinimumSize(600,300)
        self.filelist.my_filepath = ""
        
        #setup my_console
        self.my_console.appendPlainText('Console Started...')
               
        #setup signals
        self.filetree.doubleClicked.connect(self.select_from_filetree)
        self.filelist.doubleClicked.connect(self.select_from_filelist)
        self.btn1.clicked.connect(self.add_to_shortlist)
        self.btn2.clicked.connect(self.delete_from_shortlist)
        self.btn3.clicked.connect(self.start_scan)
        self.shortlist.itemClicked.connect(self.get_selection_index)   
        self.searchbar.returnPressed.connect(self.start_scan)
        #checkbox_single

        #self.checkbox_single.stateChanged.connect(self.box_changed)
        #spinbox
        #self.spinBox.valueChanged.connect(self.spin_changed)
        
        
        #menu bar        
        self.actionAbout.setShortcut("Ctrl+Alt+A")
        self.actionAbout.setStatusTip("How about that!")
        self.actionAbout.triggered.connect(self.msg_about)
        self.actionGo_Away.setStatusTip("Don't push this button!")
        self.actionGo_Away.triggered.connect(self.close)
        self.actionDON_T_DO_IT.setStatusTip("Seriously? You know what's about to happen.")
        self.actionDON_T_DO_IT.triggered.connect(self.close)
        
        #colors
        palette = QtGui.QPalette()
        #palette.setColor(self.backgroundRole(), QtGui.QColor("#99ccff"))
        palette.setColor(self.backgroundRole(), QtGui.QColor("#74b9ff"))
        self.setPalette(palette)
        #self.searchbar.setPalette(palette)               
        self.searchbar.setStyleSheet('background-color: #dfe6e9;color: red;')      
        self.filetree.setStyleSheet('background-color: #dfe6e9')
        self.filelist.setStyleSheet('background-color: #dfe6e9')
        self.shortlist.setStyleSheet('background-color: #dfe6e9')
        #self.filelist.headerItem().setBackground(0, QtGui.QColor(234, 236, 238))
        self.menubar.setStyleSheet('background-color:#dfe6e9')
        self.my_console.setStyleSheet('background-color:#dfe6e9')
    
        #setup ToolTips
        self.checkbox_single.setToolTip(
                'Changes behavior. Use this to find only files that are\n'
                'only in one directory tree, but not another. Only works\n'
                'with 2 directory trees. Otherwise it gives error msg.')
        self.searchbar.setToolTip(
                'You can filter the search by any string.\n\n'
                '    example: "desktop" will display only paths that have\n'
                '              the string "desktop" anywhere in it.\n\n'
                'You can filter by extension as well\n'
                '     example: ".jpg" will display only files with ".jpg" extension\n\n'
                'Multiple strings are treated as an "OR" search')    
        self.shortlist.setToolTip(
                'To add search directories, double click any folder from the left\n'
                'directory tree, then hit the Select button\n\n'
                'To remove paths from the right search window, select the path and\n'
                'click the Delete button')
        self.btn3.setToolTip(
                'Hit this button to start a scan. You can also just hit <enter>\n'
                'from the search pattern bar to the right')
        self.spinBox.setToolTip(
                'Set the minimum number of duplicate files to be displayed\n\n'
                '    Example: \n'
                '            1 would display all files.\n'
                '            2 would display all files that have at least 2 or more\n'
                '            duplicates.')
        self.filelist.setToolTip(
                'Double Click on any full filepath to open that files folder location\n')
                
        
        
    def expand_initial_dir(self, root_dir):
        '''expands each dir from top to end, can't do all at once'''
        self.my_print('Expanding ' + root_dir)
        path = os.path.normpath(self.filetree.my_filepath)
        path = path.split(os.sep)
        part = ""
        for i in path:
            part = part + i + os.sep
            self.filetree.expand(self.model.index(part))

      
    def spin_changed(self):
        self.my_print(self.spinBox.cleanText())
        
    def box_changed(self):
        if self.checkbox_single.isChecked():
            self.my_print('checkbox is checked.')
            
        else:
            self.my_print('checkbox is unchecked.')
            
            
    def get_checkbox_status(self):
        return self.checkbox_single.isChecked()
            
            
    def my_print(self, msg):
        '''Prints to both stdout and self.my_console'''
        self.my_console.appendPlainText(str(msg))
        
    def msg_about(self):
        print('About')
        title = 'About Hdogs Duplicate File Finder'
        message = ("---------------------------------------------------\n"
                   "Hdogs Duplicate File Finder v1.0\n"
                   "\n"
                   "By: Horace Crump\n"
                   "V1.0 1/29/18\n"
                   "\n"
                   "Tools:\nPyQt5\nQT Designer v5.6.2\nPython v3.6\nSpyder v3.2.6\n"
                   "\n"
                   "Why?\n"
                   "Mainly wanted to learn python. But, I had a ton of duplicate\n"
                   "files from making backups over the years and I was moving.\n"
                   "I decided that I wanted to find and consolidate all of those\n"
                   "files. Sounded like a fun project.\n"
                   "\n"
                   "-cheers!\n"
                   "---------------------------------------------------")
        QMessageBox.about(self,title, message)
       
        
    def get_pattern(self):
        '''Gets search pattern from user search bar, creates regex list'''
        print('get_pattern')
        temp= []
        search_list = []
        temp = self.searchbar.text().split()
        #[search_list.append(x) for x in temp if x not in search_list]        
        for x in temp:
            if x not in search_list:
                if x.startswith('*'): #remove leading asterix, which break it
                    x = re.sub('(^[\*]+)',r'\\*',x)
                    print ('x:',x)
                if x.startswith('.'):
                    x = re.sub(r'(^[.]+)',r'\\.',x)
                    print('xx:',x)
                
                search_list.append(x)
                
        print(search_list)
        combined = '(' + ')|('.join(search_list) + ')'
        print('comb:',combined)
        return combined
        
    def start_scan(self):
        '''gets paths from shortlist and scans them all'''
        print('start_scan -start')
        big_list = set([])
        my_dict = {}
        size = 0
        self.filelist.clear()
        if self.shortlist.count() > 0: 
            new_pattern = self.get_pattern()
            for i in range(self.shortlist.count()):
                next_dir = self.shortlist.item(i).text()
                big_list.update(get_all_files(next_dir,new_pattern))
                print('...scanning',next_dir)
                size = len(big_list)
                print(size,'files to scan')
            if self.radiobyname.isChecked():
                print ('byname is checked')
                my_dict = compare_by_name(big_list)
            elif self.radiobysize.isChecked():
                print ('bysize is checked')
                my_dict = compare_by_size(big_list)
            elif self.radiobyhash.isChecked():
                print ('hash is checked')
                if size > 1000:
                    msg = ("Over " + str(size) + " files not allowed with hash"
                        " method, try smaller folders")
                    QMessageBox.about(self, "Sorry",msg)                       
                    print('Hash intensive, try smaller folder size')
                else:
                    my_dict = compare_by_hash(big_list)
            else:
                self.my_print('Nothing checked, bugged?')
            duplicate_min = self.spinBox.cleanText()
            self.my_print('-'*60)
            self.my_print('Minimum duplicate size: '+ duplicate_min)
            self.my_print('Pattern filter: ' + new_pattern)
            final_dict = get_dupes(my_dict, duplicate_min)
            fill_widget(self.filelist, final_dict)
            self.my_print(str(len(final_dict))+' keys out of '+str(len(big_list))+
                          ' files matched!')
         
            
    def select_from_filetree(self,signal):
        print('select -start')
        self.filetree.my_filepath =self.filetree.model().filePath(signal)
        print(self.filetree.my_filepath)
        print('select -end')
        
        
    def select_from_filelist(self,signal):
        print('select -start')
        item = self.filelist.currentItem()
        fullpath = item.text(0)
        self.filelist.my_filepath = os.path.dirname(os.path.abspath(fullpath))
        print(self.filelist.my_filepath)
        subprocess.Popen('explorer ' +self.filelist.my_filepath)
        print('select -end')        
        
        
    def add_to_shortlist(self):
        '''update shortlist with dir only and block duplicates'''
        print('add_to_shortlist -start')
        set1 = set([])
        if len(self.filetree.my_filepath) > 0 and is_dir(self.filetree.my_filepath):           
            set1.update([str(self.shortlist.item(i).text()) for i in range(self.shortlist.count())] )
            set1.add(self.filetree.my_filepath)         
            self.shortlist.clear()
            self.shortlist.addItems(set1)                 
        print(set1)
        print('add_to_shortlist - end')
    
    
    def get_selection_index(self,item):
        print ('get_selection_index -start')
        #print (self.shortlist.selectedItems())          
        print (item.text())
        print('get_selection_index -end')
    
    
    def delete_from_shortlist(self):
        '''remove selected entries from shortlist'''
        print ('delete_from_shortlist -start')
        full_lst = [str(self.shortlist.item(i).text()) for i in range(self.shortlist.count())]
        lst = [item.text() for item in self.shortlist.selectedItems()]
        if len(lst) > 0:
            for i in list(lst):
                full_lst.remove(i)
            self.shortlist.clear()
            self.shortlist.addItems(full_lst)


def is_dir(path):
    '''verify if path is a directory or file '''
    if os.path.isdir(path):
        return True
    
    
def get_all_files(rootdirs,combined):
    '''compares files'''
    print('Get_all_files -start')   
    npath=rootdirs
    file_list = set()     
    for dirs,_,files in os.walk(npath):
        for name in files:
            full_name = os.path.join(dirs,name)
            if re.search(combined, full_name, re.IGNORECASE):
                file_list.add(full_name)
    return file_list        
 

def compare_by_name(mylist):
    '''Comparing files in list by size, actually a set'''    
    print('Compare by size')
    adict = {}
    for i in mylist:
        filename = os.path.basename(i)
        adict.setdefault(filename,[]).append(i)
    return adict

    
def compare_by_size(mylist):
    '''Comparing files in list by size, actually a set'''    
    print('Compare by size')
    adict = {}
    for i in mylist:
        statinfo = os.stat(i)
        adict.setdefault(statinfo.st_size,[]).append(i)
    return adict


def compare_by_hash(mylist):
    '''Comparing files in list by hash, actually a set'''    
    print('Compare by hash')
    adict = {}
    for i in mylist:
        myhash = get_hash_md5(i)
        adict.setdefault(myhash,[]).append(i)
    return adict

               
def get_hash_md5(filename):
    '''use md5 hash method on each file'''
    myhash = hashlib.md5()
    with open(filename,"rb") as f:
        for b in iter(lambda : f.read(2**20), b""):
            myhash.update(b)
    return myhash.hexdigest()


def get_dupes(adict, min_duplicates):
    '''
    Only keep entries that have more than one value entry
    The point is to find dupes unless checkbox is set, then
    i'm just listing every file with or without a pattern match
    '''
    print("Get Duplicates")
    d1 = {}    
    min_duplicates = int(min_duplicates)
    #only print keys with > values
    d1 = {k:v for k,v in adict.items() if len(v) >= min_duplicates}
    return d1

def fill_item(item, value):
  item.setExpanded(True)
  if type(value) is dict:
    for key, val in sorted(value.items()):
      child = QTreeWidgetItem()
      child.setText(0, str(key))
      item.addChild(child)
      fill_item(child, val)
  elif type(value) is list:
    for val in value:
      child = QTreeWidgetItem()
      item.addChild(child)
      if type(val) is dict:      
        child.setText(0, '[dict]')
        fill_item(child, val)
      elif type(val) is list:
        child.setText(0, '[list]')
        fill_item(child, val)
      else:
        child.setText(0, str(val))              
      child.setExpanded(True)
  else:
    child = QTreeWidgetItem()
    child.setText(0, str(value))
    item.addChild(child)

def fill_widget(widget, value):
  widget.clear()
  fill_item(widget.invisibleRootItem(), value)
    
 

def main():
    #this is needed for Spyder IDE
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()      
    ui = MainWindow()
    #-----------------------------------
     
    
    ui.show()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()    
