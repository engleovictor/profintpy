## Criado Por Léo
## 03/09/22

from time import time as tm
import sys
from  inspect import getmembers, isfunction
from importlib import import_module
import profintpy_parser as pfip

try:
    mod = import_module(sys.argv[1].split('.')[0]) if pfip.file_check() else exit(pfip.syntax_error)
except:
    exit(pfip.syntax_error)

flags, func_args = pfip.get_flags()

if flags['func']:
    for fname_funcs in getmembers(mod):
        if (isfunction(fname_funcs[1]) and flags['vfunc'] == fname_funcs[0]):
            funcs = [fname_funcs[1]]
            break
    if len(funcs) == 0:
        exit('There is no function with this name!!')
else:
    funcs = [func[1] for func in getmembers(mod) if isfunction(func[1])]

func_args = [int(i) if i.isnumeric() else i  for i in func_args ]

print(f'Results: arg = {func_args}')

for func in funcs:
    try:
        time = tm()    
        retval = func(*func_args)
        time = tm() - time
        if flags['time'] and flags['vtime'] < time:
            continue
        print(f'{func.__name__: >20} <> Value: {retval: >23} <> Time: {time: >7}')
    except:
        if flags['all']:
            print(f'{func.__name__: >20} <> No Value (No args compatibily) <> No time')
