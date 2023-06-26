#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except ZeroDivisionError as zde:
        print("Exception: {}".format(zde), file=sys.stderr)
        return
    except IndexError as ie:
        print("Exception: {}".format(ie), file=sys.stderr)
        return
