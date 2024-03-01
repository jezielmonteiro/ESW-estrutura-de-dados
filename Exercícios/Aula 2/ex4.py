"""Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um
cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame."""

""" - Se a média estiver entre 0.0 e 4.0, o aluno está reprovado"""
""" - Se a média estiver entre 4.1 e 6.0, o aluno pegou exame"""
""" - Se a média for maior do que 6.0, o aluno está aprovado"""
""" - Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está repro
vado"""

M1 = float(input("Informe sua primeira nota: "))
M2 = float(input("Informe sua segunda nota: "))
M3 = float(input("Informe sua terceira nota: "))
print(f"A nota 1 foi {M1}, a nota 2 foi {M2} e a nota 3 foi {M3}.")

media = (M1 + M2 + M3) / 3
print(f"Média: {round(media, 1)}")
if (0.0 < media <= 4.0):
    print("O aluno está reprovado.")
if (4.1 <= media <= 6.0):
    print("O aluno pegou exame.")
    exame = float(input("Informa a nota do exame: "))
    print(exame)
    if exame > 6.0:
        print("Aprovado no exame.")
    else:
        print("Reprovado no exame.")
if (media > 6.0):
    print("O aluno está aprovado.")