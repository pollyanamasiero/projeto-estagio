# Questão 5
# Escreva um programa que inverta os caracteres de um string.

def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

string = input("Informe a string: ")
print(f"String invertida: {inverter_string(string)}")
