import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Cadastro import abrir_janela_cadastro_cliente 
from Tela import abrir_janela_cliente
import sqlite3

# Caminho para o banco de dados (você pode alterar conforme necessário)
CAMINHO = "Dados/SQLite/db.sqlite"

# Função para abrir a janela de login do cliente
def abrir_janela_login_cliente():
    # Criar a janela principal para login do cliente
    janela = ttk.Toplevel()
    janela.title("Login do Cliente")
    janela.geometry("400x300")

    # Aplicar o tema "superhero"
    style = ttk.Style()
    style.theme_use("superhero")

    # Variáveis para armazenar os valores dos campos
    cpf_var = ttk.StringVar()
    senha_var = ttk.StringVar()

    # Função para verificar as credenciais no banco de dados
    def verificar_credenciais():
        # Obter os valores dos campos
        cpf = cpf_var.get().strip()
        senha = senha_var.get().strip()

        # Verificar se o campo CPF está vazio
        if not cpf:
            mensagem_label.config(text="Erro: O campo CPF é obrigatório!", bootstyle=DANGER)
            return

        # Verificar se as credenciais estão no banco de dados
        try:
            conexao = sqlite3.connect(CAMINHO)
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT id FROM Clientes WHERE cpf = ? AND senha = ?
            """, (cpf, senha))
            resultado = cursor.fetchone()
            conexao.close()

            if resultado:
                # Credenciais válidas (redirecionamento simulado)
                mensagem_label.config(text="Login bem-sucedido!", bootstyle=SUCCESS)
                janela.destroy()
                abrir_janela_cliente(resultado)
            else:
                # Credenciais inválidas
                #mensagem_label.config(text="CPF ou senha inválido(s)", bootstyle=DANGER)
                abrir_janela_cadastro_cliente()

        except Exception as e:
            # Exibir mensagem de falha em caso de erro
            mensagem_label.config(text=f"Erro ao verificar credenciais: {e}", bootstyle=DANGER)

    # Criar os widgets da interface
    ttk.Label(janela, text="CPF do Cliente:", bootstyle=PRIMARY).pack(pady=10)
    entry_cpf = ttk.Entry(janela, textvariable=cpf_var, bootstyle=SUCCESS)
    entry_cpf.pack(pady=5)

    ttk.Label(janela, text="Senha do Cliente:", bootstyle=PRIMARY).pack(pady=10)
    entry_senha = ttk.Entry(janela, textvariable=senha_var, show="*", bootstyle=SUCCESS)
    entry_senha.pack(pady=5)

    # Botão para verificar as credenciais
    ttk.Button(janela, text="Entrar", bootstyle=(SUCCESS, OUTLINE), command=verificar_credenciais).pack(pady=20)

    # Label para exibir mensagens de sucesso ou falha
    mensagem_label = ttk.Label(janela, text="", font=("Helvetica", 12))
    mensagem_label.pack(pady=10)

    # Iniciar a janela
    janela.mainloop()