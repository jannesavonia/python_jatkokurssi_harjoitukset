import unittest
from helpers import *

#Comment out if no python functions are tested
#NOTE: If this is not commented out, src/my_code.py will be executed.
#(You can abuse this, for example, if you like to check global variables etc.)
from my_code import *



started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_C(self):
        #Test C program
        self.startTest()
        self.assertEqual(callC(cmdline_args=[], input='\n').strip(), 'a b c')
        self.endTest()


    def test_CS(self):
        #Test C# program
        self.startTest()
        self.assertEqual(callCS(cmdline_args=[], input='\n').strip(), 'a b c')
        self.endTest()

    def test_Python(self):
        #Test python program
        self.startTest()
        self.assertEqual(callpython(cmdline_args=['a', 'b'], input='\n').strip(), 'a b')
        self.endTest()

    def test_CFunction(self):
        #Test C function. You have to implement tests/testmain.c
        #which tests the function.
        self.startTest()
        self.assertEqual(callCFunction(cmdline_args=['2','3'], input='\n').strip(), '5')
        self.endTest()

    def test_CSFunction(self):
        #Test C# program
        self.startTest()
        self.assertEqual(callCSFunction(cmdline_args=[], input='\n').strip(), 'a b c')
        #self.assertEqual(callCSFunction(cmdline_args=['2','3'], input='\n').strip(), '5')
        self.endTest()

    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #my_code must be imported
        self.startTest()
        self.assertEqual(combine('123', 'b'), '123b')
        self.endTest()

    def startTest(self):
        global started_tests
        started_tests=started_tests+1
        print('\nStart test', started_tests)

    def endTest(self):
        global completed_tests
        print('End test', started_tests)
        completed_tests=completed_tests+1


def completed():
    global completed_tests
    return completed_tests

def started():
    global started_tests
    return started_tests

