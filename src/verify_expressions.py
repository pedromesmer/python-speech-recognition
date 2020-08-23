import connect_db as db

def verifyExpression(phase, action = 'action'):
    phase = phase.lower()
    word = phase.split()
    
    command = db.readExpressions()
    

    for con in command:
        for wor in word:                
            # por enquanto, a verificação é apenas na variável finish
            if (wor == con[0]):
                
                print ('> match: ' + con[0])
                print ( '> comando: ' + con[1])
                
                # Criar uma função para cada action, a frase pode ser passada como parametro inteira ou refinada
                
                return False
    else:
        # caso não ser match no comando
        return True