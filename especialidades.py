class especialidades :
  def __init__(self, nomeEspecialidade,preco ):
    self.nomeEspecialidade= nomeEspecialidade
    self.preco= preco
   
  def escolher_especialidade(self):
    especialidade = int(input('\n 1-Massagista \n 2-Cabelereira \n 3-Maquiadora \n 4-Esteticista \n 5-Manicure \n 6- Designer de sobrancelha \n \n QUAL ESPECIALIDADE VOCÊ ESTÁ PROCURANDO? \n ' ))
    
    if especialidade== 1:
      print( ' especialidade (Massagista)')
    if especialidade == 2:
      print(' especialidade (Cabeleira)')
    if especialidade== 3:
      print(' especialidade (Maquiadora)')
    if especialidade== 4:
      print(' especialidade (esteticista)')
    if especialidade== 5:
      print(' especialidade (Manicure)')
    if especialidade== 6:
      print(' especialidade (designer de sobrancelha)')