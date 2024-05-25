# Solicita ao usuário que insira o primeiro número e armazena na variável 'numero1'
numero1 = float(input("Por favor, insira o primeiro número: "))

# Solicita ao usuário que insira o segundo número e armazena na variável 'numero2'
numero2 = float(input("Por favor, insira o segundo número: "))

# Solicita ao usuário que insira a operação desejada e armazena na variável 'operacao'
# A operação deve ser uma das seguintes: +, -, *, /
operacao = input("Por favor, insira a operação desejada (+, -, *, /): ")

# Inicializa a variável 'resultado' como None
resultado = None

# Verifica qual operação foi escolhida e realiza a operação correspondente
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    # Verifica se o segundo número não é zero antes de realizar a divisão
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Erro: Operação inválida.")

# Se a operação foi válida e o resultado foi calculado, exibe o resultado
if resultado is not None:
    print(f"O resultado de {numero1} {operacao} {numero2} é: {resultado}")
