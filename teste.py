
from tkcalendar import Calendar
import customtkinter

def selecionar_data():
    def obter_data_selecionada():
        data_selecionada = cal.get_date()
        print("Data selecionada:", data_selecionada)
        janela_data.destroy()

    janela_data = customtkinter.CTk()
    cal = Calendar(janela_data, selectmode='day', year=2024, month=2, day=14)
    cal.pack(padx=10, pady=10)
    botao_confirmar = customtkinter.CTkButton(janela_data, text="Confirmar", command=obter_data_selecionada)
    botao_confirmar.pack(padx=10, pady=10)
    janela_data.mainloop()

# Crie uma instância da janela principal
janela = customtkinter.CTk()

# Botão para abrir o seletor de data
botao_selecionar_data = customtkinter.CTkButton(janela, text="Selecionar Data", command=selecionar_data)
botao_selecionar_data.pack(padx=10, pady=10)

# Execute o loop principal da janela
janela.mainloop()