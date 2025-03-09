import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Cadastro import abrir_janela_cadastro_vendedor
from Tela import abrir_janela_vendedor
import sqlite3

# Caminho para o banco de dados (você pode alterar conforme necessário)
CAMINHO = "Dados/SQLite/db.sqlite"

# Senha específica para permitir o cadastro de novos vendedores
SENHA_ESPECIFICA = "admin"

# Função para abrir a janela de login do vendedor
def abrir_janela_login_vendedor():
    # Criar a janela principal para login do vendedor
    janela = ttk.Toplevel()
    janela.title("Login do Vendedor")
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

        # Verificar se os campos estão preenchidos
        if not cpf or not senha:
            mensagem_label.config(text="Erro: Preencha todos os campos!", bootstyle=DANGER)
            return

        try:
            # Conectar ao banco de dados e verificar as credenciais
            conexao = sqlite3.connect(CAMINHO)
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT id FROM Vendedor WHERE cpf = ? AND senha = ?
            """, (cpf, senha))
            resultado = cursor.fetchone()
            conexao.close()

            if resultado:
                # Credenciais válidas
                mensagem_label.config(text="Login bem-sucedido!", bootstyle=SUCCESS)
                janela.destroy()
                abrir_janela_vendedor()
            else:
                # CPF ou senha inválidos
                mensagem_label.config(text="CPF ou senha inválido(s)", bootstyle=DANGER)

                # Verificar se o CPF existe no banco de dados
                conexao = sqlite3.connect(CAMINHO)
                cursor = conexao.cursor()
                cursor.execute("""
                    SELECT id FROM Vendedor WHERE cpf = ?
                """, (cpf,))
                resultado_cpf = cursor.fetchone()
                conexao.close()

                if not resultado_cpf:
                    # CPF não existe, abrir janela para solicitar SENHA_ESPECIFICA
                    abrir_janela_senha_especifica(cpf)  # Passa o CPF como argumento

        except Exception as e:
            # Exibir mensagem de falha em caso de erro
            mensagem_label.config(text=f"Erro ao verificar credenciais: {e}", bootstyle=DANGER)

    # Função para abrir a janela de validação da senha específica
    def abrir_janela_senha_especifica(cpf):
        # Criar uma nova janela para validar a senha específica
        janela_senha = ttk.Toplevel()
        janela_senha.title("Validação de Senha Específica")
        janela_senha.geometry("400x200")

        # Variável para armazenar a senha inserida
        senha_especifica_var = ttk.StringVar()

        # Função para validar a senha específica
        def validar_senha_especifica():
            senha_digitada = senha_especifica_var.get().strip()

            if senha_digitada == SENHA_ESPECIFICA:
                # Senha válida, redirecionar para o cadastro do vendedor
                mensagem_senha_label.config(text="Senha válida! Redirecionando...", bootstyle=SUCCESS)
                janela_senha.after(1500, lambda: [janela_senha.destroy(), abrir_janela_cadastro_vendedor()])
            else:
                # Senha inválida
                mensagem_senha_label.config(text="Senha inválida! Insira a senha correta.", bootstyle=DANGER)

        # Criar os widgets da interface
        ttk.Label(janela_senha, text="Insira a Senha Específica:", bootstyle=PRIMARY).pack(pady=10)
        ttk.Entry(janela_senha, textvariable=senha_especifica_var, show="*", bootstyle=SUCCESS).pack(pady=5)
        ttk.Button(janela_senha, text="Validar Senha", bootstyle=(PRIMARY, OUTLINE), command=validar_senha_especifica).pack(pady=10)

        # Label para exibir mensagens de sucesso ou falha
        mensagem_senha_label = ttk.Label(janela_senha, text="", font=("Helvetica", 12))
        mensagem_senha_label.pack(pady=10)

    # Criar os widgets da interface
    ttk.Label(janela, text="CPF do Vendedor:", bootstyle=PRIMARY).pack(pady=10)
    ttk.Entry(janela, textvariable=cpf_var, bootstyle=SUCCESS).pack(pady=5)

    ttk.Label(janela, text="Senha do Vendedor:", bootstyle=PRIMARY).pack(pady=10)
    ttk.Entry(janela, textvariable=senha_var, show="*", bootstyle=SUCCESS).pack(pady=5)

    # Botão para verificar as credenciais
    ttk.Button(janela, text="Entrar", bootstyle=(SUCCESS, OUTLINE), command=verificar_credenciais).pack(pady=20)

    # Label para exibir mensagens de sucesso ou falha
    mensagem_label = ttk.Label(janela, text="", font=("Helvetica", 12))
    mensagem_label.pack(pady=10)

    # Iniciar a janela
    janela.mainloop()