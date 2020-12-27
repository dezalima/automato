estado_atual = 0
resultado = " "
posicao = 0
entrada = input("Digite uma atribuição:")
caracteres = list(entrada)

def verificaFim(i):
    global resultado
    if(i == (len(caracteres)-1) and (estado_atual !=7)):
        resultado = "Atribuição inválida"
    elif((estado_atual==7) and (i == (len(caracteres)-1))):
        resultado = "Atribuição correta"
    else:
        resultado = "Atribuição inválida"

def verificaSimb(i, v):
    global resultado
    if(i == (len(caracteres)-1) and (v=="=" or v==".")):
        resultado = "Atribuição inválida"
        return False
    return True
    

if estado_atual == 0:
    if (ord(caracteres[0]) >= 97) and (ord(caracteres[0]) <= 122):
        estado_atual = 1
        verificaFim(0)
    else:
        resultado = "Atribuição inválida"
        
if estado_atual == 1:
    i = 1
    while(i < len(caracteres)):
        if ((ord(caracteres[i]) >= 97) and (ord(caracteres[i]) <= 122)) or ((ord(caracteres[i]) >= 48 and ord(caracteres[i]) <= 57) or caracteres[i] == '_'):
            estado_atual = 1
            verificaFim(i)
        elif caracteres[i] == '=':
            if(verificaSimb(i, caracteres[i])):
                estado_atual = 2 
                posicao = i
                i = 0
                break
        else:
            resultado = "Atribuição inválida"
            break
        i += 1

if estado_atual == 2:
    i = int(posicao+1)
    if (ord(caracteres[i]) >= 97) and (ord(caracteres[i]) <= 122):
        estado_atual = 3
        verificaFim(i)
        posicao = i
        i = 0
    elif (ord(caracteres[i]) >= 48 and ord(caracteres[i]) <= 57):
        estado_atual = 4
        verificaFim(i)
        posicao = i
        i = 0
    else:
        resultado = "Atribuição inválida"

if estado_atual == 3:
    i = int(posicao+1)
    while (i < len(caracteres)):
        if ((ord(caracteres[i]) >= 97) and (ord(caracteres[i]) <= 122)) or ((ord(caracteres[i]) >= 48 and ord(caracteres[i]) <= 57) or caracteres[i] == '_'):
            estado_atual = 3
            verificaFim(i)
        elif caracteres[i] == ';':
            estado_atual = 7
            break
        else:
            resultado = "Atribuição inválida"
            break
        i += 1

if estado_atual == 4:
    i = int(posicao+1)
    while(i < len(caracteres)):
        if (ord(caracteres[i]) >= 48 and ord(caracteres[i]) <= 57):
            estado_atual = 4
            verificaFim(i)
        elif caracteres[i] == '.':
            if(verificaSimb(i, caracteres[i])):
                estado_atual = 5
                posicao = i
                i = 0
                break
        elif caracteres[i] == ';':
            estado_atual = 7
            break
        else:
            resultado = "Atribuição inválida"
            break
        i += 1

if estado_atual == 5:
    i = int(posicao+1)
    if(ord(caracteres[i]) >= 48 and ord(caracteres[i]) <= 57):
        estado_atual = 6
        verificaFim(i)
        posicao = i
        i = 0
    else:
        resultado ="Atribuição inválida"

if estado_atual == 6:
    i = int(posicao+1)
    while(i < len(caracteres)):
        if (ord(caracteres[i]) >= 48 and ord(caracteres[i]) <= 57):
            estado_atual = 6
            verificaFim(i)
        elif caracteres[i] == ';':
            estado_atual = 7
            break
        else:
            resultado = "Atribuição inválida"
            break
        i +=1

if estado_atual == 7:
    verificaFim(i)
    

print(resultado)

