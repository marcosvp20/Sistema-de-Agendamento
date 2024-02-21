from tela_de_login import tela_de_login
from tela_de_agendamento import tela_de_agendamento
tela = tela_de_login()
tela_erro = tela_de_agendamento()
try:
    tela.main()
except Exception as erro:
    tela_erro.tela_erro(erro)