import sys
import time


def combine(a, b):
    return a+b

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   res = ''
   for s in sys.argv[1:]:
       res = res + s + ' '

   time.sleep(0.25)

   s = input()

   print(res + s)
   time.sleep(0.25)
