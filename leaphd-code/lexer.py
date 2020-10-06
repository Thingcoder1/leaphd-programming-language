from pyparsing import Word, nums, alphas, alphanums # dependencies

# these are the types of "parts of speech" (tokens) i.e.: int, variables, comma, you get the idea
num  =  Word(nums)
string = Word(alphas, alphanums+"-_")
math = Word('+-*/^%!', max=1)
eql = Word('=')
eol = Word(';')
dec = Word(':')
opa = Word('(')
cpa = Word(')')
sep = Word(',')
pnt = Word('.')
fwa = Word('>')
bka = Word('<')
qstn = Word('?')
quote = Word('\'"')

#set of these token types
lexset = [num,string,math,eql,eol,dec,opa,cpa,sep,pnt,fwa,bka,quote,qstn]
#the names of the token types
nameset = ['num','string','math','eql','eol','dec','opa','cpa','sep','pnt','fwa','bka','quote','qstn']

def lex(filename): #made the lexer a function so it can be called by the parser
    #opening the selected .lpd document
    with open(filename, 'r') as f:
        lpd = f.read()

    #list to put the broken-down program in. Different tokens are separated in this
    lexed = []

    #strings to count the characteintrs and ints
    #ints b/c if they aren't grouped together at some point they will become x=1 5 not x=15
    charstring = ''
    intstring = ''

    #list of the chars in the .lpd document
    charlist = []

    #adding chars to charlist
    [charlist.append(char) for i,char in enumerate(lpd)]

    #HUGE for loop. put respective tokens together in lexed list
    for i,char in enumerate(lpd):
        #testing for digits to put in intlist
        if char.isdigit() == True:
            intstring += char

        #testing for chars to put in charlist
        if char.isalpha() == True:
            charstring += char

        else:
            #testing for digits to put in lexed
            if char.isdigit() == False:
                lexed.append(intstring)
                lexed.append(charstring)
                intstring = ''
                charstring = ''
                lexed.append(char)


    #the list for the chars w/ labels
    parsedLex = []

    lexed = [x for x in lexed if x.strip()] #stripping lexed list of whitespace and newlines as well as this: ''
    #for loop
    for i in range(len(lexed)):
        for a in range(len(lexset)):
            if lexed[i] == ' ' or lexed[i] == '\n':
                del lexed[i]
            if lexed[i-1] == '=' and lexed[i] == '=':
                del parsedLex[i-1]
                parsedLex.append(('bool','=='))
            else:
                #try to get rid of this to improve efficency
                try:
                    lexset[a].parseString(lexed[i])
                    parsedLex.append((nameset[a],lexed[i]))#format of [name,char]
                except:
                    pass


    return(parsedLex)#print out the list of parsed lexed chars
