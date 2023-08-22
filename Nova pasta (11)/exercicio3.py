alunos = []

while True:
    
    continuar = input("deseja continuar ?(S/N)")
    if continuar == "s" or continuar == "S":
        nome = input ("digite o nome do aluno :")
        nota = input ("digitet a nota do aluno :")
        print ("aluno",nome,"nota",nota)
    else:
        if continuar == "n" or continuar == "N":
            break

