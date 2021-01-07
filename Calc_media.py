def calcular_media(notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma/quantidade
  print('O Aluno tirou: ',media)
  verificar_aprovacao(media)

def verificar_aprovacao(media):
  if media >=6:
    print('Aluno Aprovado')
  else:
    print('Aluno Reprovado')

calcular_media([10,4,2,3])
