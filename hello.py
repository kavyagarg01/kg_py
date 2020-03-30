#! /usr/bin/python
import sys
def main():
 print sys.argv
 print sys.argv[0],sys.argv[1]
 print "Hello"
if __name__ == '__main__':
 main()
# to see all the functions which can be used with it
 dir(sys)
#to show the man page of sys
 help(sys)
#to exit from sys
 sys.exit()
 dir(sys)
 print "hello"
