import sys

tokens = {
    "add" : 1,
    "sub" : 2,
    "mul" : 3,
    "mov" : 4,
    "lod" : 5,
    "str" : 6,
    "jmp" : 7,
    "beq" : 8,
    "bgt" : 9,
    "rdn" : 10,
    "ptn" : 11,
    "hlt" : 12
    }

class lexer():
    fsm = dict()
    state = 0
    def __init__(self):
        for token_name in tokens.keys[]:
            

# get filename
try:
    source_file_name = sys.argv[1]
except IndexError:
    print( "Enter file name as argument is in 'python3 interp.py <file_name>'" )
    sys.exit(1)

with open( source_file_name, "r" ) as source_file_input:
    line = source_file_input.readline().strip()

