estojo = []
print(estojo)
r= str(input('Quer adicionar algum item:'))
while r == 'sim':
    i= str(input('Qual item?:'))
    estojo.append(i)
    print('o conteudo atual é:')
    print(estojo)
    r= str(input('Quer adicionar algum item:'))

for i in estojo:
     print(i)
    
         
        
        