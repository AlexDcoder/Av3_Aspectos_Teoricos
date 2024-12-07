from sintatic import lexer, parser


class PyturgueseCompiler():
    @staticmethod
    def generate_tree(code):
        return parser.parse(code, lexer=lexer)
