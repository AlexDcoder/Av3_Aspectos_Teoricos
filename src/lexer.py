import ply.lex as lex

# Define tokens and reserved words
reserved = {
    'se': 'SE',
    'enquanto': 'ENQUANTO',
    'quebre': 'QUEBRE',
    'retorne': 'RETORNE',
    'funcao': 'FUNCAO'
}

tokens = (
    'FRASE', 'VARIAVEL', 'NUMERO', 'MAIS', 'MENOS', 'VEZES', 'DIVIDIDO', 'RECEBE',
    'IGUAL', 'MAIOR', 'MAIOR_IGUAL', 'MENOR', 'MENOR_IGUAL', 'VIRGULA',
    'PARENTESE_D', 'PARENTESE_E', 'CHAVE_D', 'CHAVE_E', "NEWLINE"
) + tuple(reserved.values())

# Rules for simple tokens
t_MAIS = r'\+'
t_MENOS = r'-'
t_VEZES = r'\*'
t_DIVIDIDO = r'/'
t_RECEBE = r'='
t_IGUAL = r'=='
t_MAIOR = r'>'
t_MAIOR_IGUAL = r'>='
t_MENOR = r'<'
t_MENOR_IGUAL = r'<='
t_VIRGULA = r','
t_PARENTESE_E = r'\('
t_PARENTESE_D = r'\)'
t_CHAVE_E = r'\{'
t_CHAVE_D = r'\}'

# Defining rules for more complex tokens


def t_VARIAVEL(t):
    r'\w+'
    t.type = reserved.get(t.value, 'VARIAVEL')
    return t


def t_FRASE(t):
    r'"\w+(\d)*"'
    t.type = reserved.get(t.value, 'FRASE')
    return t


def t_FUNCAO(t):
    r'\w+\(\)'
    return t


def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Ignored characters
t_ignore = ' \t'

lexer = lex.lex()


def get_lexer():
    return lexer


if __name__ == '__main__':
    lexer = lex.lex()

    data = """
"adsadsadad"
"""
    lexer.input(data)
    for token in lexer:
        print(f"{token.type}({token.value}) at line {token.lineno}")
