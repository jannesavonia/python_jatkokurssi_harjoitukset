import os
import shutil
from zipfile import ZipFile

from config import *

ignore=['helpers', 'ex_template']

solution_dir='solution'
sample_solution='my_code.py'
template='my_code.template.py'

print('WARNING: Overwrites all exercises/ASSIGNMENT/src/mycode.py files!')
cont=input('Type YES to continue. ')
if cont!='YES':
    print('Exit...')
    exit()

for d in os.listdir(student_source):
    assignment=student_source+'/'+d
    if os.path.isdir(assignment) and d not in ignore:
        print('Enter',assignment)
        solution_path=assignment+'/'+solution_dir+'/'
        solution_file=solution_path+sample_solution 
        template_file=solution_path+template
        if os.path.exists(solution_file):
            if os.path.exists(template_file):
                target=assignment+'/src/my_code.py'
                print('Copy',template_file,'->',target)
                shutil.copy2(template_file, target)
            else:
                print('Did not found '+template_file+'. Assignment skipped!')

        else:
            print('Did not found '+solution_file+'. Assignment skipped!')
