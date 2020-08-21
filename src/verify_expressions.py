finish = [
    'sair', 'finalizar', 'acabar', 'terminar', 'encerrar'
]

def verifyExpression(expression, command = finish):
    expression = expression.lower()
    word = expression.split()
    #print(word) # lista de palavras da frase
    for i in command:
        for j in word:                
            # por enquanto, a verificação é apenas na variável finish
            if (j == i.lower()):
                print ('> ' + i)
                # caso der match, encerra o loop
                return False
    else:
        # caso não ser match no comando
        return True