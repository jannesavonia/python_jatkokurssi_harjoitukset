exercises - Contains exercises, each exercise in an individual folder

exercises/ex_template
  * src/my_code.py - solution template
  * src/my_code.cs - solution template
  * src/my_code.c - solution template
  * tests/tests.py - student tests
  * tests/testmain.c - main() for C function test
  * tests/realtests.py - teacher tests (optional)

exercises/helpers - helper functions

`python create_student_pack.py` - Create student pack\
`python test_all_submissions.py` - Run all tests

../submissions.zip - file from Moodle\
../results.txt - output points

config.py - Configuration file
  * Set `use_docker=False` if you don't use Docker isolation

---

**Required software**
|     | Windows | Ubuntu | macOS |
|-----|---------|-------|-------|
|Base system| [Python](https://www.microsoft.com/en-us/search/shop/Apps?q=python+3.9) (from App Store)| Python | Python(for example [anaconda](https://www.anaconda.com/products/individual)) |
|||||
|C# support| [Mono](https://www.mono-project.com/download/stable/) | Mono | [Mono](https://www.mono-project.com/download/stable/) |
| | `path=%path%;C:\Program Files (x86)\Mono\bin` | | |
| |OR `path=%path%;C:\Program Files\Mono\bin` | | |
|||||
|C support | [MinGW](http://mingw.osdn.io/) | gcc | gcc (for example [homebrew](https://brew.sh/))|
| |`path=%path%;C:\MinGW\bin`  | | |
|||||
|Test isolation| [Docker](https://www.docker.com/get-started) | Docker | [Docker](https://www.docker.com/get-started)|

* Python version >=3.7
* If multiple python versions are installed, you shall use `python3`.
* In Ubuntu, use packet manager to install required components.

