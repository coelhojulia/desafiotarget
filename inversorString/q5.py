def inverte_string(string):
    lista_caracteres = list(string)
    
    lista_caracteres.reverse()
    
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