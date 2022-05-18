import os
import shutil
from zipfile import ZipFile

from config import *

#copy exercises
if os.path.exists(student_target):
    shutil.rmtree(student_target)
shutil.copytree(student_source, student_target, ignore=ignore)

"""
#remove real (teacher) tests
for file in os.listdir(student_target):
    ex_path=student_target+'/'+file
    if os.path.isdir(ex_path):
        realtest_path=ex_path+'/tests/realtests.py'
        if os.path.exists(realtest_path):
            os.remove(realtest_path)
        solution_path=ex_path+'/solution'
        if os.path.exists(solution_path):
            shutil.rmtree(solution_path)
        results_path=ex_path+'/tests/result.txt'
        if os.path.exists(results_path):
            os.remove(results_path)

#remove main result file
results_path=student_target+'/results.txt'
if os.path.exists(results_path):
    os.remove(results_path)
"""


#if os.path.exists(student_zip):
#    os.remove(student_zip)

shutil.make_archive(os.path.splitext(student_zip)[0], format='zip', base_dir=student_target_dir, root_dir=student_root)






