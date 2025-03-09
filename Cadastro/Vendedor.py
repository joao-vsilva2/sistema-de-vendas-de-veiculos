import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sqlite3

# Caminho para o banco de dados (você pode alterar conforme necessário)
CAMINHO = "Dados/SQLite/db.sqlite"

# Função para abrir a janela de cadastro de vendedor
def abrir_janela_cadastro_vendedor():
    # Criar a janela principal para cadastro de vendedor
    janela = ttk.Toplevel()
    janela.title("Cadastro de Vendedor")
    janela.geometry("800x600")  # Tamanho inicial da janela
    janela.minsize(600, 400)   # Tamanho mínimo da janela
    # Aplicar o tema "superhero"
    style = ttk.Style()
    style.theme_use("superhero")

    # Variáveis para armazenar os valores dos campos
    nome_var = ttk.StringVar()
    cpf_var = ttk.StringVar()
    data_nascimento_var = ttk.StringVar()
    email_var = ttk.StringVar()
    telefone_var = ttk.StringVar()
    endereco_var = ttk.StringVar()
    data_contratacao_var = ttk.StringVar()
    salario_var = ttk.DoubleVar()
    status_var = ttk.StringVar(value="Ativo")  # Valor padrão "Ativo"
    senha_var = ttk.StringVar()

    # Função para salvar os dados do vendedor no banco de dados
    def salvar_vendedor():
        # Obter os valores dos campos
        nome = nome_var.get().strip()
        cpf = cpf_var.get().strip()
        data_nascimento = data_nascimento_var.get().strip()
        email = email_var.get().strip()
        telefone = telefone_var.get().strip()
        endereco = endereco_var.get().strip()
        data_contratacao = data_contratacao_var.get().strip()
        salario = salario_var.get()
        status = status_var.get().strip()
        senha = senha_var.get().strip()

        # Verificar se todos os campos obrigatórios estão preenchidos
        if not nome or not cpf or not data_nascimento or not telefone or not endereco or not data_contratacao or not salario or not status:
            mensagem_label.config(text="Erro: Preencha todos os campos obrigatórios!", bootstyle=DANGER)
            return

        try:
            # Conectar ao banco de dados e inserir os dados
            conexao = sqlite3.connect(CAMINHO)
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO Vendedor (nome, cpf, data_nascimento, email, telefone, endereco, data_contratacao, salario, status, senha)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nome, cpf, data_nascimento, email, telefone, endereco, data_contratacao, salario, status, senha))
            conexao.commit()
            conexao.close()

            # Exibir mensagem de sucesso
            mensagem_label.config(text="Vendedor cadastrado com sucesso!", bootstyle=SUCCESS)

            # Limpar os campos após o cadastro
            nome_var.set("")
            cpf_var.set("")
            data_nascimento_var.set("")
            email_var.set("")
            telefone_var.set("")
            endereco_var.set("")
            data_contratacao_var.set("")
            salario_var.set(0.0)
            status_var.set("Ativo")
            senha_var.set("")

        except sqlite3.IntegrityError:
            # Exibir mensagem de falha em caso de CPF duplicado
            mensagem_label.config(text="Erro: CPF já cadastrado!", bootstyle=DANGER)
        except Exception as e:
            # Exibir mensagem de falha em caso de outro erro
            mensagem_label.config(text=f"Erro ao cadastrar vendedor: {e}", bootstyle=DANGER)

    # Criar os widgets da interface usando grid
    row_index = 0  # Índice para controlar as linhas
    col_index = 0  # Índice para controlar as colunas

    def adicionar_campo(label_text, entry_var, show=None):
        nonlocal row_index, col_index
        # Label
        ttk.Label(janela, text=label_text, bootstyle=PRIMARY).grid(
            row=row_index, column=col_index, padx=5, pady=5, sticky=W
        )
        # Entry
        entry = ttk.Entry(janela, textvariable=entry_var, bootstyle=SUCCESS, show=show)
        entry.grid(row=row_index, column=col_index + 1, padx=5, pady=5, sticky=W+E)
        # Avançar para a próxima coluna ou linha
        col_index += 2
        if col_index >= 4:  # Se atingir o limite de colunas, volta para a próxima linha
            col_index = 0
            row_index += 1

    # Adicionar os campos na grade
    adicionar_campo("Nome do Vendedor:", nome_var)
    adicionar_campo("CPF do Vendedor:", cpf_var)
    adicionar_campo("Data de Nascimento (DD-MM-AAAA):", data_nascimento_var)
    adicionar_campo("Email do Vendedor (opcional):", email_var)
    adicionar_campo("Telefone do Vendedor:", telefone_var)
    adicionar_campo("Endereço do Vendedor:", endereco_var)
    adicionar_campo("Data de Contratação (DD-MM-AAAA):", data_contratacao_var)
    adicionar_campo("Salário do Vendedor:", salario_var)
    adicionar_campo("Status do Vendedor:", status_var)
    adicionar_campo("Senha do Vendedor:", senha_var, show="*")

    # Botão para salvar o vendedor
    ttk.Button(janela, text="Cadastrar", bootstyle=(SUCCESS, OUTLINE), command=salvar_vendedor).grid(
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