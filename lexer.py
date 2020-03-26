from pyparsing import Word, nums, alphas, alphanums # dependencies

# these are the types of "parts of speech" (tokens) i.e.: int, variables, comma, you get the idea
int  =  Word(nums)
var = Word(alphas, alphanums+"-_")
math = Word('+-*/', max=1)
eql = Word('=')
eol = Word(';')
dec = Word(':')
opa = Word('(')
cpa = Word(')')
sep = Word(',')
pnt = Word('.')
fwa = Word('>')
bka = Word('<')

#set of these token types
lexset = [int,var,math,eql,eol,dec,opa,cpa,sep,pnt,fwa,bka]
#the names of the token types
nameset = ['int','var','math','eql','eol','dec','opa','cpa','sep','pnt','fwa','bka']

#opening the selected .lpd document
with open('test.lpd', 'r') as f:
    lpd = f.read()

#list to put the broken-down program in. Different tokens are separated in this
lexed = []

#strings to count the characters and ints
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
    if char.isalpha() == True :
        charstring += char

    else:
        #testing for digits to put in lexed
        if char.isdigit() == False:
            lexed.append(intstring)
            intstring = ''
            lexed.append(char)
            charprinted = 1 #this is to tell the program not to duplicate
                            #chars b/c it already got one

        #testing for chars to put in lexed
        if char.isalpha() == False and char.isdigit() == False:
            #check if it already lexed a char
            if charprinted == 1:
                pass
            elif charprinted != 1 and charprinted == 0:
                lexed.append(charstring)
                charstring = ''
                lexed.append(char)
                charprinted = 0#reset it to make sure it can lex chars again

#the list for the chars w/ labels
parsedLex = []

#for loop
for i in range(len(lexed)):
    for a in range(len(lexset)):
        #try to get rid of this to improve efficency
        try:
            lexset[a].parseString(lexed[i])
            parsedLex.append([nameset[a],lexed[i]])#format of [name,char]
        except:
            pass
print(parsedLex)#print out the list of parsed lexed chars