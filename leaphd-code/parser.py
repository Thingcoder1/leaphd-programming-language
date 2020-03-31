import lexer

brackets = 0
parens = 0
str = 0

def parse(filename):
    parsedLex = lexer.lex(filename)
    print(parsedLex)

parse('test.lpd')
