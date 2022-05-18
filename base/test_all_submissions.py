from zipfile import ZipFile
from config import *
import shutil
import os
import subprocess
import sys
import pathlib

def getName(path):
    s=path.split('_')[0]
    names=s.split(' ')
    return names

def unpack(stdentzip):
    unzip_target=tmp_dir+'/unzip'
    if os.path.exists(unzip_target):
        try:
            os.remove(unzip_target)
        except:
            pass
    os.mkdir(unzip_target)
    print()
    with ZipFile(studentzip, 'r') as myzip:
        myzip.extractall(path=unzip_target)

    extrapath=''
    if os.path.exists(unzip_target+'/assignments'):
        print('WARNING: found extra path from', unzip_target)
        extrapath='assignments/'
    
    #Copy src directories, nothing else
    #Delete ex_template directories
    assignment_list=os.listdir(test_target)
    for assignment in assignment_list:
        src=unzip_target+'/'+extrapath+assignment+'/src'
        tgt=test_target+'/'+assignment+'/src'
        if assignment=='ex_template':
            if os.path.exists(test_target+'/'+assignment):
                shutil.rmtree(test_target+'/'+assignment)
            continue
        if assignment=='helpers':
            continue
        if not os.path.exists('exercises/'+assignment+'/tests'):
            print(assignment)
            continue
        print(src, '->', tgt)
        if os.path.exists(tgt+'/my_code.py'):
            os.remove(tgt+'/my_code.py')
        #if os.path.exists(tgt):
        #    shutil.rmtree(tgt)
        try:
            #print(32*'-')
            for fn in os.listdir(src+'/'):
                if os.path.isfile(src+'/'+fn):
                    print(src+'/'+fn, '->', tgt+'/'+fn)
                    shutil.copyfile(src+'/'+fn, tgt+'/'+fn)
            #shutil.copytree(src, tgt, ignore=ignore)
            #shutil.copytree(src, tgt)
            #print(32*'*')
        except:
            pass


def createTestTree():
    # copy exercises
    shutil.copytree(student_source, test_target, ignore=ignore)
    #shutil.copy2('unpack.py', test_target)

    # Overwrite student tests
    for file in os.listdir(test_target):
        ex_path = test_target + '/' + file
        if os.path.isdir(ex_path):
            realtest_path = ex_path + '/tests/realtests.py'
            test_path = ex_path + '/tests/tests.py'
            if os.path.exists(realtest_path):
                try:
                    os.remove(test_path)
                except:
                    pass
                os.rename(realtest_path, test_path)

            src_path = ex_path + '/src/my_code.py'
            if os.path.exists(src_path):
                try:
                    os.remove(src_path)
                except:
                    pass

        result_path = ex_path + '/tests/result.txt'
        if os.path.exists(result_path):
            try:
                os.remove(result_path)
            except:
                pass

    if os.path.exists(allresults_path):
        try:
            os.remove(allresults_path)
        except:
            pass

def readPoints():
    total=0
    resfile=open(allresults_path, 'rt')
    lines=resfile.readlines()
    resfile.close()

    for l in lines:
        ll=l.split('\t')
        total=total+int(ll[1])

    return total

#Directory to create test environment for "manual test"
unpacked_dir='../unpacked'
if os.path.exists(unpacked_dir):
    shutil.rmtree(unpacked_dir)


resfile=open(resultfile, 'wt')
with ZipFile('../submissions.zip', 'r') as rootzip:
    for name in rootzip.namelist():
        print('\n\n-----------------------------------\n')
        shutil.rmtree(tmp_dir, ignore_errors=True)
        os.mkdir(tmp_dir)
        shutil.rmtree(test_target, ignore_errors=True)
        firstname, lastname=getName(name)
        print(firstname, lastname)
        rootzip.extract(name, path=tmp_dir)
        studentzip=tmp_dir+'/'+name

        createTestTree()
        
        
        print(studentzip)
        unpack(studentzip)
        
        shutil.copytree(test_target, unpacked_dir+'/'+firstname+'_'+lastname, ignore=ignore)
        shutil.copy2('./exercises/testall.py', test_target)


        #test all submissions of a student
        if not use_docker:
            if os.path.exists(allresults_path):
                os.remove(allresults_path)
            cmdline=sys.executable+' testall.py'
            print(cmdline)
            rc = subprocess.call(cmdline, shell=True, cwd=test_target)
            print(rc)
        else:                
            abs_test_path='"'+str(pathlib.Path(test_target).absolute())+'"'
            #cmdline = 'docker container run -w/test --rm --name unittest -v ' + abs_test_path + ':/test python:latest python3 /test/testall.py'
            cmdline = 'docker container run -w/test --rm --name unittest -v ' + abs_test_path + ':/test autotest python3 /test/testall.py'
            print(cmdline)
            rc = subprocess.call(cmdline, shell=True, cwd=test_target)
            print(rc)

        points=readPoints()
        resfile.write(lastname+','+firstname+','+str(points)+'\n')
        print('-----------------------------------')
resfile.close()
