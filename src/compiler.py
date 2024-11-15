from ply.lex import lex
from ply.yacc import yacc


class PyturgueseCompiler(object):
    reserved = {
        'se': 1,
        'enquanto': 1,
        'quebra': 1,
        '': 1
    }
    tokens = [] + list(reserved.values())


if __name__ == '__main__':
    pass
