import db
import functions 

def verifyExpression(phase, action = 'action'):
    phase = phase.lower()
    word = phase.split()
    
    command = db.readExpression()

    """
    Funções cadastradas (coluna 1 do banco):
    --------------------
    quit - finalizar o programa
    """
    

    for con in command:
        for wor in word:                
            if (wor == con[1]): # se a palavra está cadastrada no banco de verbos, coluna 0
                
                print ('> match: ' + con[1])
                print ('> comando: ' + con[2])
                
                exec('functions.'+con[2]+'()')
                                
                # Criar uma função para cada action, no arquivo functions
                # A frase pode ser passada na função como parametro, inteira ou refinada
                
                return False
                
    else:
        # caso não ser match no comando
        return True
