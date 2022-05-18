import os
import shutil
from zipfile import ZipFile

from config import *

ignore=['helpers', 'ex_template']

solution_dir='solution'
sample_solution='my_code.py'

target_dir='../solutions'
if os.path.exists(target_dir):
    shutil.rmtree(target_dir)

os.mkdir(target_dir)

for d in os.listdir(student_source):
    assignment=student_source+'/'+d
    if os.path.isdir(assignment) and d not in ignore:
        print('Enter',assignment)
        solution_path=assignment+'/'+solution_dir+'/'
        solution_file=solution_path+sample_solution
        target=target_dir+'/'+d+'.py'
        if os.path.exists(solution_file):
            print(solution_file, '->', target)
            shutil.copy2(solution_file, target)
        else:
            print('Did not found '+solution_file+'. Assignment skipped!')

shutil.make_archive('../solutions', format='zip', base_dir=target_dir)
