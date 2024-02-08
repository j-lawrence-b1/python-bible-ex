#!/bin/env /usr/local/bin/python

def foo ():
    return("foo!")

def main ():
    ret = foo()
    print(ret)
    return(ret)

if __name__ == "__main__":
    main()