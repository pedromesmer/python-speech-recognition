finish = [
    'sair', 'finalizar', 'acabar', 'terminar', 'encerrar'
]

def verifyExpression(expression, command = finish):
    for content in command:
        if (expression.lower() == content.lower()):
            print ('> ' + content)
            return False
    else:
        return True