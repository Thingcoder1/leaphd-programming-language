import lexer

path_to_file = '/home/ian/github/leaphd-programming-language/leaphd-code/test.lpd'

def parse(filename):
    #things to store
    tokens = lexer.lex(filename)
    vartypes = ['int']
    variables = []
    operations = []
    #control variables
    setvar = 0
    newvar = 0
    quotes = 0

    for i in range(len(tokens)):
        if tokens[i][0] == 'dec':
            newvar = 1
        if tokens[i][0] == 'string' and tokens[i][1] in vartypes and newvar == 1:
            variables.append(['', tokens[i][1], ''])
        if tokens[i][0] == 'string' and tokens[i][1] not in vartypes and newvar == 1 and setvar == 0:
            variables[-1][0] = tokens[i][1]
        if tokens[i][0] == 'eql' and newvar == 1:
            setvar = 1
        if tokens[i][0] == 'quote':
            if quotes == 0:
                quotes = 1
            elif quotes == 1:
                quotes = 0
        if tokens[i][0] == 'num' and setvar == 1:
            variables[-1][2] = tokens[i][1] + ' '

    print(variables)
    print(tokens)

parse(path_to_file)


#this is old code
#lets rewrite it for fun!
'''
parsedTree = []
def parse(filename):
    #get the lexed tokens
    parsedLex = lexer.lex(filename)
    #count brackets, parens, strings. will use in future.
    brackets = 0
    parens = 0
    str = 0
    #check if a variable/function is being made.
    var = 0
    #check if a variable is being ended.
    end = 0
    #dunno what these are for. will leave them in just in case.
    varstr = ''
    strtype = ''
    #parse the tokens:
    for i in range(len(parsedLex)):
        #check if a variable is being made
        if parsedLex[i][0] == 'dec':
            #add a count to total variable counts.
            var = var + 1
            #check if the variable is actually a variable.
            if parsedLex[i+2][0] == 'eql':
                parsedTree.append(['var',(parsedLex[i+1][1],[''])])
            #check if the variable is actually a function.
            elif parsedLex[i+2] == 'fwa':
                parsedTree.append(['func',(parsedLex[i+1][1],[''])])
            #check if a variable's definition has ended.
        if parsedLex[i][1] == ';':
            end = end + 1
        #if none of the previous have applied,
        #add the token to the variable's definition.
        if var != 0 and end != var and parsedLex[i][1] != ';':
            parsedTree[var-1][1][1][0] += (parsedLex[i][1]+' ')
    #now, remove the ':variable =' from the definition
    #and strip of extra whitespace.
    for i in range(len(parsedTree)):
        parsedTree[i][1][1][0] = parsedTree[i][1][1][0][4 + len(parsedTree[i][1][0]):]
        parsedTree[i][1][1][0] = parsedTree[i][1][1][0].strip()
    #print out the tree (TESTING ONLY).
    print(parsedTree)
    
    #return the tree.
    return parsedTree

#this is only for testing.
parse('test.lpd')
'''