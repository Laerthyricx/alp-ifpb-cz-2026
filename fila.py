fila = []
print('Olá, bem vindo a fila da merenda do ifspb!')
add= str(input('Deseja adicionar alguem na fila?:'))
while add == 'sim':
    p= str(input('Quem?:'))
    fila.append(p)
    print('a fila atual é:')
    print(fila)
    p2= str(input('Deseja adicionar mais alguem?:'))
if add != 'sim':
    print('Certo, bom lanche!')
for p in fila:
    print(p)
