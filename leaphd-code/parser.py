import lexer

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
