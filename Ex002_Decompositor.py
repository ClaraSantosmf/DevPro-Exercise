centena_resu = dezena_resu = unidade_resu = ""

numero = int(input("Qual número será decomposto?"))
centena, numero = divmod(numero, 100)
dezena, numero = divmod(numero, 10)
unidade = numero

if centena == 1:
    centena_resu = "Esse número possui 1 centena,"
elif centena > 1:
    centena_resu = f"Esse número possui {centena} centenas,"
else:
    centena_resu = "Esse número não possui centenas,"

if dezena == 1:
    dezena_resu = "possui 1 dezena"
elif dezena > 1:
    dezena_resu = f"{dezena} dezenas"
else:
    dezena_resu = "não possui dezenas"

if unidade == 1:
    unidade_resu = "e 1 unidade"
elif unidade > 1:
    unidade_resu = f"e {unidade} unidades"
else:
    unidade_resu = "e nenhuma unidade"

print(centena_resu, dezena_resu, unidade_resu)