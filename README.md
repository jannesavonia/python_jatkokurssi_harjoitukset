# autotest


Automatic grading tool for assignments

- Supports docker to isolate test process on macOS and Linux
- Tested on macOS, Ubuntu, Windows
- Mono for C# support
- Python
- gcc (MinGW on Windows)
---
## Usage:

0) Install required software, see details at [base/README.md](https://github.com/jannesavonia/autotest/blob/main/base/README.md)
1) Create autotest Docker container (optional)
 ```
 cd base/Docker && ./create.sh
```
2) Create assignments with tests
   * exercises folder
   * each assignment is located on separate folder
   * Assignments are tested with tests/tests.sh by student, and tests/realtests.sh by teacher. The latter one is not included in student packet. If no tests/realtests.sh exists, test/tests.sh will be used for teacher tests.
3) Create student template packet 
 ```
 python create_student_pack.py
```
4) Share the template packet to students
5) Student solve assignments
6) Student tests solutions at local computer
7) When all assignments are completed, student packs solutions, and submits the packet to Moodle
8) Download zip containing all submissions from Moodle into root folder, not base, of this project
9) Rename zip file
 ```
 mv FileContainingAllSubmissions.zip submissions.zip
```

10) Grade submissions
 ```
 python test_all_submissions.py
```
11) results.txt contains grades
---
## Student instructions to 
* [install system](https://media.savonia.fi/View.aspx?id=41368~5j~C3GQS3vCws)
* [work with assignments](https://media.savonia.fi/View.aspx?id=41369~5k~cDWsC3GXUu) 
---
## Solutions and templates
* Under each assignment folder create solutions folder
* Copy solution to solution folder under as  
```
my_code.py
```
* Copy template to solution folder under as
 ```
my_code.template.py
```
* You may utilize
 ```
solution2src.py
```
to copy solutions to
 ```
assignment/src/my_code.py
```
* You may utilize
 ```
template2src.py
```
to copy templates to
 ```
assignment/src/my_code.py
```
