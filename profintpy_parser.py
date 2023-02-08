## Criado por Leo
## 03/09/22

import sys

flags = {
    'all': False,
    'time': False,
    'vtime': None,
    'func': False,
    'vfunc': None,
    }

syntax_error = '''
Syntax:
python3 ./profintpy.py <name> <args> <flags>
In the same directory

Example of usage:
python3 ./profintpy.py file1.py 10
python3 ./profintpy.py file2.py

if there isn't any <arg> the default value is None.

    -a  Show all functions, independent
        if they were executed or not.

    -l  Show only functions that didn't
        overrun time

    EXAMPLE: -l <time> (SECONDS)

    -f  Show only time and value for
        specified function
   
    EXAMPLE: -f <func_name>

'''

time_error = '''
Please, when use '-l' flag specify a valid time
-l 3 (It will show only functions that do not overrun this period in SECONDS)
'''

sys_argv = sys.argv[2:]

def file_check():
    return '.py' in sys.argv[1]

def all_functions_check():
    #Show all functions, indepedent 
    #if the were executed or not.
    if '-a' in sys_argv:
        sys_argv.remove('-a')
        flags['all'] = True

def time_lapse_check():
    #Show only functions that didn't
    #overrun time
    if '-l' in sys_argv:
        index = sys_argv.index('-l')
        sys_argv.remove('-l')
        try:
            time = sys_argv[index]
            sys_argv.remove(time)
            flags['time'] = True
            flags['vtime'] = float(time)
        except:
            exit(time_error)

def specify_function_check():
    #Show only time and value for
    #specified function
    if '-e' in sys_argv:
        index = sys_argv.index('-e')
        sys_argv.remove('-e')
        name = sys_argv[index]
        sys_argv.remove(name)
        flags['func'] = True
        flags['vfunc'] = name


def get_flags():
    all_functions_check()
    time_lapse_check()
    specify_function_check()

    return [flags, sys_argv]
    