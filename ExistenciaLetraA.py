# 2. Verificar existência da letra 'a' e contar suas ocorrências
def count_letter_a(string):
    count = string.lower().count('a')
    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Entrada para a string
string = input("Informe uma string para verificar a ocorrência da letra 'a': ")
count_letter_a(string)