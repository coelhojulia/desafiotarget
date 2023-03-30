def inverte_string(string):
    lista_caracteres = list(string)
    
    for i in range(len(lista_caracteres)//2):
        lista_caracteres[i], lista_caracteres[len(lista_caracteres)-i-1] = lista_caracteres[len(lista_caracteres)-i-1], lista_caracteres[i]
    
    string_invertida = ''.join(lista_caracteres)
    
    return string_invertida

print('INVERSAO DE STRING')
print('.'*25)
string_original = "Desafio Target!"
string_invertida = inverte_string(string_original)

print(f"A string original é: {string_original}")
print(f"A string invertida é: {string_invertida}")

print('.'*25)
print('FIM!')
print('.'*25)
