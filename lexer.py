with open('lexer.txt') as f:
    base = f.readlines()
    f.close()
base = [x.strip() for x in base]
print(base)

with open('test.lpd','r') as lpdf:
    prog = lpdf.read()
lex = []

print(type(3))
print(str(type(3))=='<class \'int\'>')

for i in range(len(prog)):
    if prog[i].isdigit() == True:
        print('int found!')
    else:
        print('not an int')
