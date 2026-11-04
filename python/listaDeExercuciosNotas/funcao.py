def aluno(nome, nota1, nota2):
    nomeAluno = nome
    media = (nota1 + nota2) / 2
    return f"nome: {nomeAluno} nota: {media}"

print(aluno("carlos", 5, 6))
