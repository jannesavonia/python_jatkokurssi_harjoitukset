import shutil

student_root='../'
student_target_dir='assignments'
student_target=student_root+student_target_dir
student_zip=student_target+'.zip'
student_source='./exercises'
test_target='../test'
ignore=shutil.ignore_patterns('*.*~', '__pycache__', 'realtests.py', 'solution', 'result.txt', 'results.txt', '.DS_Store', 'ex_template', 'allsrc.zip')
tmp_dir='../tmp'
submission_path='../submissions.zip'
resultfile='../results.txt'

allresults_path = test_target + '/results.txt'

use_docker=False
#if you use docker, fetch python image
# docker pull python
