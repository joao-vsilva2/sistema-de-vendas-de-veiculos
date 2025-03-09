from tkinter import BOTH, YES
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Cadastro import abrir_janela_cadastro_cliente, abrir_janela_cadastro_veiculo
from .Funcao_vendedor import *

botao = ttk.Button

# Função para abrir a janela principal do vendedor
def abrir_janela_vendedor():
    # Criar a janela principal para o vendedor
    janela = ttk.Toplevel()
    janela.title("Área do Vendedor")
    janela.geometry("800x600")
    style = ttk.Style()
    style.theme_use("superhero")

    # Frame para as opções do vendedor
    frame_opcoes = ttk.Frame(janela)
    frame_opcoes.pack(fill=BOTH, expand=YES)

    # Lista de botões com seus textos e comandos
    botoes = [
        ("Cadastrar Cliente", abrir_janela_cadastro_cliente),
        ("Visualizar Feedbacks", visualizar_feedbacks),
        ("Gerenciar Manutenções", gerenciar_manutencoes),
        ("Criar Proposta", criar_proposta),
        ("Cadastrar Veículo", abrir_janela_cadastro_veiculo),
        ("Iniciar Venda", criar_venda),
    ]

    # Configuração do grid para organizar os botões
    colunas_por_linha = 3  # Número de botões por linha
    for i, (texto, comando) in enumerate(botoes):
        linha = i // colunas_por_linha  # Calcula a linha atual
        coluna = i % colunas_por_linha  # Calcula a coluna atual

        # Cria o botão e o posiciona no grid
        botao(
            frame_opcoes,
            text=texto,
            bootstyle=(PRIMARY, OUTLINE),
            command=comando
        ).grid(row=linha, column=coluna, padx=10, pady=10, sticky="nsew")

        # Configuração para que as colunas se expandam igualmente
        frame_opcoes.columnconfigure(coluna, weight=1)

    # Chamar a função para exibir as vendas
    exibir_todas_vendas(janela)

    # Iniciar a janela
    janela.mainloop()