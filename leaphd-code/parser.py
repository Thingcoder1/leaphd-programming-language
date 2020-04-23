import lexer

brackets = 0
parens = 0
str = 0
var = 0
end = 0
varstr = ''
strtype = ''
parsedTree = []

def parse(filename):
    parsedLex = lexer.lex(filename)
    brackets = 0
    parens = 0
    str = 0
    var = 0
    end = 0
    varstr = ''
    strtype = ''
    for i in range(len(parsedLex)):
        if parsedLex[i][0] == 'dec':
            var = var + 1
            if parsedLex[i+2][0] == 'eql':
                parsedTree.append(['var',(parsedLex[i+1][1],[''])])
            elif parsedLex[i+2] == 'fwa':
                parsedTree.append(['func',(parsedLex[i+1][1],[''])])
        if parsedLex[i][1] == ';':
            end = end + 1
        if var != 0 and end != var and parsedLex[i][1] != ';':
            parsedTree[var-1][1][1][0] += (parsedLex[i][1]+' ')
    for i in range(len(parsedTree)):
        parsedTree[i][1][1][0] = parsedTree[i][1][1][0][4 + len(parsedTree[i][1][0]):]
        parsedTree[i][1][1][0] = parsedTree[i][1][1][0].strip()
    print(parsedTree)

parse('test.lpd')
