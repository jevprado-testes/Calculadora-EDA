nota1 = float(input("Qual a sua nota de atividade: "))
nota2 = float(input("Qual a sua nota da P1: "))
nota3 = float(input("Qual a sua nota da P2: "))
nota4 = float(input("Qual a sua nota da P3: "))
nota5 = float(input("Qual a sua nota da P4: "))


notas = nota1*1 + nota2*2 + nota3*2 + nota4*2 + nota5*3
media = notas/10


if media > 5.0: 
    print(f"A sua nota na disciplina de Estrutura de Dados foi: {media}! Parabéns, voce está aprovado!")
else: 
    print(f"A sua nota na disciplina de Estrutura de Dados foi: {media}! Infelizmente, voce está reprovado!")