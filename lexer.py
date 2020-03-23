from pyparsing import Word, nums, alphas
int  =  Word(nums)            # simple unsigned integer
var = Word(alphas)   # single letter variable, such as x, z, m, etc.
math  = Word('+-*/', max=1)   # arithmetic operators
eql = Word('=')
bool = Word('==')
equation = var + eql + int + math + int    # will match "x=2+2", etc.
print(equation.parseString('alp = 23 * 3'))
 
