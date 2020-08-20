finish = [
    'sair', 'finalizar', 'acabar', 'terminar', 'encerrar'
]

def verifyExpression(expression, command = finish):
    for content in command:
        # por enquanto, a verificação é apenas na variável finish
        if (expression.lower() == content.lower()):
            print ('> ' + content)
            return False
    else:
        return True