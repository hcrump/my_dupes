"""
My attempt at learning how to use files and directories.
I want to create a program to find duplicate files on my pc and do
something with them.
"""
import os
import filecmp
import pprint
import itertools
import hashlib
from collections import OrderedDict

#use raw text or python thinks the \U in \Users is a unicode ref
HOME = r'C:\Users\horace\Desktop\python\temp\my_dupes'
TEST = True # turn on test creation
testdirs = ['testdir'+str(i) for i in range(1,4)]
testfiles1 = ['files'+str(i) for i in range(1,4)]
testfiles2 = ['aa','bb','cc']
all_files = set()
cmp_groups = {}
dict_size = {}
dict_hash = {}

def create_test_tree_single():
    '''Creates 1 directory tree of folders to test'''    
    npath = HOME
    print('-'*40)
    print('Creating test directories-single tree')
    
    for i in testdirs:
        npath = os.path.join(npath,i)
        if not os.path.exists(npath):
            print('...created',npath)
            os.mkdir(npath)
        else:
            print('...already exists',npath)
         

def create_test_files():
    '''Creates files in test dirs, some same, some not'''   
    npath = HOME
    created = False
    print('-'*40)
    print ('Creating test files')

    for dirs,subdirs,files in os.walk(npath):
        npath = os.path.join(npath,dirs)
        for t in testfiles1:
            fullpath = os.path.join(npath,t)
            if not os.path.isfile(fullpath):
                fp=open(fullpath,'a')
                print('a',file=fp)
                fp.close()
                print('...Created file:',fullpath)
                created = True
        if not npath.endswith('2'): #need files to be absent from 1 dir       
            for t in testfiles2:
                fullpath = os.path.join(npath,t)
                if not os.path.isfile(fullpath):
                    fp=open(fullpath,'a')
                    fp.close()
                    print('...Created file:',fullpath)
                    created = True
    if not created:
        print('...nothing created')
                  
          
def list_tree():
    '''Creates files in test dirs, some same, some not'''
    npath = HOME
    print('-'*40)
    print ('Showing Directory contents')
    
    for dirs,subdirs,files in os.walk(npath):
        npath = os.path.join(npath,dirs)
        print(dirs)
        for name in files:
            print('Files:',name)
    
    
def get_all_files():
    '''compares files'''   
    npath = HOME
    file_list = set()
    
    print('-'*40)
    print('Getting Files')
    
    for dirs,_,files in os.walk(npath):
        npath = os.path.join(npath,dirs)
        for name in files:
            file_list.add(os.path.join(npath,name))
    pprint.pprint(file_list)
    return file_list    
  
    
def compare_by_filecmp(mylist):
    '''Comparing files in list, actually a set'''    
    print('-'*40)
    print('Compare by filecmp')
    
    for a,b in itertools.combinations(mylist,2):
        if filecmp.cmp(a,b):
            pass
        
        
def compare_by_size(mylist):
    '''Comparing files in list by size, actually a set'''    
    print('-'*40)
    print('Compare by size')
    adict = {}
    for i in mylist:
        statinfo = os.stat(i)
        adict.setdefault(statinfo.st_size,[]).append(i)
    return adict


def compare_by_hash(mylist):
    '''Comparing files in list by hash, actually a set'''    
    print('-'*40)
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
        
def pretty_sort(adict):
    '''print dict sorted by key, then values'''
    print('-'*40)
    print("Pretty Sort")
    for key,values in sorted(adict.items()):
        print (key)
        for value in sorted(values):
            print ("   ",value)
            

def list_dupes(adict):
    '''Show duplicatesk'''
    print('-'*40)
    print("Show Duplicates")
    for key,values in sorted(adict.items()):
        if len(values) > 1:
            print (key)
            for value in sorted(values):
                print("   ",value)
#----MAIN
    
print ('Current directory:\n',os.getcwd())

if os.getcwd != HOME:
    os.chdir(HOME)

print('Contents:\n',os.listdir(HOME))

if TEST:
    create_test_tree_single()
    create_test_files()
    list_tree()
    
all_files = get_all_files()
dict_size = compare_by_size(all_files)
pprint.pprint (dict_size)
dict_hash = compare_by_hash(all_files)
pretty_sort(dict_hash)
list_dupes(dict_hash)
print("==================Complete================")
print('Current Dir:',os.getcwd())

  
            