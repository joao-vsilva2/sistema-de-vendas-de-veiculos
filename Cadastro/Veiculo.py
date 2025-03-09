import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sqlite3

# Caminho para o banco de dados (você pode alterar conforme necessário)
CAMINHO = "Dados/SQLite/db.sqlite"

# Função para abrir a janela de cadastro de veículo
def abrir_janela_cadastro_veiculo():
    # Criar a janela principal para cadastro de veículo
    janela = ttk.Toplevel()
    janela.title("Cadastro de Veículo")
    janela.geometry("700x600")  # Tamanho inicial da janela
    janela.minsize(600, 400)   # Tamanho mínimo da janela
    # Aplicar o tema "superhero"
    style = ttk.Style()
    style.theme_use("superhero")

    # Variáveis para armazenar os valores dos campos
    modelo_var = ttk.StringVar()
    marca_var = ttk.StringVar()
    ano_var = ttk.IntVar(value=2023)  # Valor padrão 2023
    cor_var = ttk.StringVar()
    quilometragem_var = ttk.IntVar(value=0)  # Valor padrão 0
    preco_var = ttk.DoubleVar(value=0.0)     # Valor padrão 0.0
    status_var = ttk.StringVar(value="Disponível")  # Valor padrão "Disponível"

    # Função para salvar os dados do veículo no banco de dados
    def salvar_veiculo():
        # Obter os valores dos campos
        modelo = modelo_var.get().strip()
        marca = marca_var.get().strip()
        ano = ano_var.get()
        cor = cor_var.get().strip()
        quilometragem = quilometragem_var.get()
        preco = preco_var.get()

        # Verificar se todos os campos obrigatórios estão preenchidos
        if not modelo or not marca or not ano or not cor or not preco:
            mensagem_label.config(text="Erro: Preencha todos os campos obrigatórios!", bootstyle=DANGER)
            return

        try:
            # Conectar ao banco de dados e inserir os dados
            conexao = sqlite3.connect(CAMINHO)
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO Veiculos (modelo, marca, ano, cor, quilometragem, preco, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (modelo, marca, ano, cor, quilometragem, preco, "Disponível"))
            conexao.commit()
            conexao.close()

            # Exibir mensagem de sucesso
            mensagem_label.config(text="Veículo cadastrado com sucesso!", bootstyle=SUCCESS)

            # Limpar os campos após o cadastro
            modelo_var.set("")
            marca_var.set("")
            ano_var.set("")
            cor_var.set("")
            quilometragem_var.set(0)
            preco_var.set(0.0)

        except Exception as e:
            # Exibir mensagem de falha em caso de erro
            mensagem_label.config(text=f"Erro ao cadastrar veículo: {e}", bootstyle=DANGER)

    # Criar os widgets da interface usando grid
    row_index = 0  # Índice para controlar as linhas
    col_index = 0  # Índice para controlar as colunas

    def adicionar_campo(label_text, entry_var, default_value=None, width=None):
        nonlocal row_index, col_index
        # Label
        ttk.Label(janela, text=label_text, bootstyle=PRIMARY).grid(
            row=row_index, column=col_index, padx=5, pady=5, sticky=W
        )
        # Entry
        entry = ttk.Entry(janela, textvariable=entry_var, bootstyle=SUCCESS, width=width)
        entry.grid(row=row_index, column=col_index + 1, padx=5, pady=5, sticky=W+E)
        if default_value is not None:
            entry_var.set(default_value)
        # Avançar para a próxima coluna ou linha
        col_index += 2
        if col_index >= 4:  # Se atingir o limite de colunas, volta para a próxima linha
            col_index = 0
            row_index += 1

    # Adicionar os campos na grade
    adicionar_campo("Modelo:", modelo_var)
    adicionar_campo("Marca:", marca_var)
    adicionar_campo("Ano:", ano_var, default_value=2023, width=10)
    adicionar_campo("Cor:", cor_var)
    adicionar_campo("Quilometragem:", quilometragem_var, default_value=0, width=10)
    adicionar_campo("Preço:", preco_var, default_value=0.0, width=10)

    # Botão para salvar o veículo
    ttk.Button(janela, text="Cadastrar", bootstyle=(SUCCESS, OUTLINE), command=salvar_veiculo).grid(
        row=row_index + 1, column=0, columnspan=4, pady=20, sticky=W+E
    )

    # Label para exibir mensagens de sucesso ou falha
    mensagem_label = ttk.Label(janela, text="", font=("Helvetica", 12))
    mensagem_label.grid(row=row_index + 2, column=0, columnspan=4, pady=10, sticky=W+E)

    # Configurar o redimensionamento das linhas e colunas
    for i in range(4):  # Configurar 4 colunas
        janela.columnconfigure(i, weight=1)
    for i in range(row_index + 3):  # Configurar todas as linhas usadas
        janela.rowconfigure(i, weight=1)

    # Iniciar a janela
    janela.mainloop()