import ply.yacc as yacc
from lexer import tokens, get_lexer  # Importa os tokens definidos no lexer

lexer = get_lexer()

# Nós da árvore sintática abstrata (AST)


class Node:
    def __init__(self, node_type, children=None, value=None):
        self.node_type = node_type
        self.children = children if children else []
        self.value = value

    def __repr__(self):
        return self.to_string()

    def to_string(self, level=0):
        ret = "  " * level + \
            f"Node(type={self.node_type}, value={self.value})\n"
        for child in self.children:
            if isinstance(child, Node):
                ret += child.to_string(level + 1)
            else:
                ret += "  " * (level + 1) + f"Value: {child}\n"
        ret += "\n"
        return ret


# Regras de produção
def p_program(p):
    """program : function
            | statements"""
    p[0] = Node("program", [p[1]])


def p_function(p):
    """function : FUNCAO VARIAVEL PARENTESE_E params PARENTESE_D CHAVE_E statements CHAVE_D"""
    p[0] = Node("function", [p[4], p[7]], p[2])


def p_params(p):
    """params : VARIAVEL
              | VARIAVEL VIRGULA params
              | empty"""
    if len(p) == 2:
        p[0] = Node("params", value=p[1])
    elif len(p) == 4:
        p[0] = Node("params", [Node("param", value=p[1]), p[3]])
    else:
        p[0] = Node("params")


def p_statements(p):
    """statements : statement
                  | statement statements"""
    if len(p) == 2:
        p[0] = Node("statements", [p[1]])
    else:
        p[0] = Node("statements", [p[1], p[2]])


def p_statement(p):
    """statement : expression NEWLINE
                 | ENQUANTO PARENTESE_E expression PARENTESE_D CHAVE_E statements CHAVE_D
                 | SE PARENTESE_E expression PARENTESE_D CHAVE_E statements CHAVE_D
                 | QUEBRE
                 | RETORNE expression"""
    if p[1] == "enquanto":
        p[0] = Node("while", [p[3], p[6]])
    elif p[1] == "se":
        p[0] = Node("if", [p[3], p[6]])
    elif p[1] == "quebre":
        p[0] = Node("break")
    elif p[1] == "retorne":
        p[0] = Node("return", [p[2]])
    else:
        p[0] = p[1]


def p_statement_assignment(p):
    """statement : VARIAVEL RECEBE expression"""
    p[0] = Node("assignment", [p[1], p[3]], "=")


def p_expression(p):
    """expression : term
                  | expression MAIS term
                  | expression MENOS term
                  | comparison"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("expression", [p[1], p[3]], p[2])


# def p_expression_string(p):
#     '''expression : FRASE'''
#     p[0] = Node("frase", [p[0]])


# def p_expression_number(p):
#     '''expression : NUMERO'''
#     p[0] = Node("frase", [p[0]])


def p_comparison(p):
    """comparison : expression MAIOR term
                  | expression MENOR term
                  | expression MAIOR_IGUAL term
                  | expression MENOR_IGUAL term
                  | expression IGUAL term"""
    p[0] = Node("comparison", [p[1], p[3]], p[2])


def p_term(p):
    """term : factor
            | term VEZES factor
            | term DIVIDIDO factor"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("term", [p[1], p[3]], p[2])


def p_factor(p):
    """factor : NUMERO
              | VARIAVEL
              | PARENTESE_E expression PARENTESE_D
              | FRASE"""
    if len(p) == 2:
        p[0] = Node("factor", value=p[1])
    else:
        p[0] = p[2]


def p_empty(p):
    """empty :"""
    p[0] = Node("empty")


def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} ({p.value}) on line {p.lineno}")
    else:
        print("Syntax error at EOF")


# Construtor do parser
parser = yacc.yacc()

if __name__ == "__main__":
    code = """
    x = "DASDSADS"
    """
    result = parser.parse(code, lexer=lexer)
    print(result)
