import customtkinter
from tela_de_agendamento import tela_de_agendamento
from PIL import Image, ImageTk

#inicializando a janela

class tela_de_login:
    def confere_usuario(self,usuario):
        dados = []
        with open('dados.txt','r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                dados.append(linha)
                if dados[0] == str(usuario):
                    return True
                else:
                    return False
            arquivo.close()
    def troca_senha(self, usuario, senha):
        
        if self.confere_usuario(usuario):
            with open('dados.txt','w') as arquivo1:
                arquivo1.write(str(usuario))
                arquivo1.write('\n')
                arquivo1.write(str(senha))
                arquivo1.close()
                janela_senha_trocada = customtkinter.CTk()
                mensagem = customtkinter.CTkLabel(janela_senha_trocada, text='senha trocada com sucesso!')
                mensagem.pack(padx = 10, pady = 10)
                janela_senha_trocada.mainloop()
        else:
            janela_senha_trocada = customtkinter.CTk()
            mensagem = customtkinter.CTkLabel(janela_senha_trocada, text='Usuario não encontrado')
            mensagem.pack(padx = 10, pady = 10)
            janela_senha_trocada.mainloop()
            
            
        
    def click_esqueci_senha(self):
        janela_esqueci_senha = customtkinter.CTk()
        janela_esqueci_senha.geometry('500x300')
        campo_usuario = customtkinter.CTkEntry(janela_esqueci_senha, placeholder_text='Usuário')
        campo_usuario.pack(padx = 10, pady = 10)
        
        campo_nova_senha = customtkinter.CTkEntry(janela_esqueci_senha, placeholder_text='Nova senha', show = '*')
        campo_nova_senha.pack(padx = 10, pady = 10)
        
        campo_repetir_senha = customtkinter.CTkEntry(janela_esqueci_senha, placeholder_text='Repita a nova senha', show = '*')
        campo_repetir_senha.pack(padx = 10, pady = 10)
        
        botao_trocar_senha = customtkinter.CTkButton(janela_esqueci_senha, text='Trocar senha',command=lambda:self.troca_senha(campo_usuario.get(), campo_nova_senha.get()))
        botao_trocar_senha.pack(padx = 10, pady = 10)
        
        janela_esqueci_senha.mainloop()
        

    def click_login(self, caixa_usuario, caixa_senha,janela):
        dados = []
        with open('dados.txt','r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                dados.append(linha)

        usuario = caixa_usuario.get()
        senha = caixa_senha.get()
        print(dados[0])
        print(dados[1])
        if usuario == dados[0] and senha == dados[1]:
            #janela_bem_vindo()
            tela = tela_de_agendamento()
            tela.main(janela)
        
        else:
            texto_senha_incorreta = customtkinter.CTkLabel(janela, text='Usuário ou senha incorretos', text_color='red')
            texto_senha_incorreta.pack(padx = 10, pady = 10)
            
            
    def main(self):
        
        janela = customtkinter.CTk()
        janela.title('Login')
        janela.geometry('500x300')

        imagem = Image.open('pessoa.png').resize((50,50), Image.LANCZOS)
        imagem_ctk = ImageTk.PhotoImage(imagem)
        label_imagem = customtkinter.CTkLabel(janela, text='', image=imagem_ctk)
        label_imagem.pack(padx = 10, pady = 10)
        #inicializando os botoes e caixas de texto
        caixa_usuario = customtkinter.CTkEntry(janela, placeholder_text='Usuario')
        caixa_usuario.pack(padx = 10, pady = 10)
        caixa_senha = customtkinter.CTkEntry(janela, placeholder_text='Senha', show = '*')
        caixa_senha.pack(padx = 10, pady = 10)
        botao_login = customtkinter.CTkButton(janela, text= 'Login', command=lambda:self.click_login(caixa_usuario, caixa_senha,janela))
        botao_login.pack(padx = 10, pady = 10)
        botao_esqueci_senha = customtkinter.CTkButton(janela, text='Esqueci minha senha', fg_color='transparent',command=self.click_esqueci_senha)
        botao_esqueci_senha.pack(padx = 5, pady = 5)
        janela.mainloop()
   
            