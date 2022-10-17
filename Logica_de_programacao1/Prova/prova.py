provas = [['Teo', 8], ['João', 5], ['Marília', 7], ['Jonathan',9]]


qtd_alunos = 0
while not(qtd_alunos <= 5 and qtd_alunos > 1):
    qtd_alunos = int(input('Digite o números de aluno que serão adicionados a lista: '))


for i in range(qtd_alunos):
    entrada = input('Digite o nome do aluno e sua nota separados por virgula: ')
    aluno, nota = entrada.split(',')
    prova = [aluno, nota]
    for j in range(len(provas)):
        if (prova[0] == provas[j][0]):
            print(f'O aluno {prova[0]} já foi lançado!')
            break
        if not(int(prova[1]) >= 0) and (int(prova[1]) <= 10):
            print('Nota inválida!')
            break
    else:
        provas.append(prova)


soma = 0
for prova in provas:
    soma += int(prova[1])
    media = soma / len(provas)
print(media)


aprovados = []
for prova in provas:
    if int(prova[1]) >= media:
        aprovados.append(prova)


print(provas)
print(aprovados)
