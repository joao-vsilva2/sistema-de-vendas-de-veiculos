import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Caminho para o banco de dados (você pode alterar conforme necessário)
CAMINHO = "Dados/SQLite/db.sqlite"

# Função para carregar e exibir os veículos cadastrados
def carregar_veiculos(tree):
    try:
        # Conectar ao banco de dados e buscar os veículos
        conexao = sqlite3.connect(CAMINHO)
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT modelo, marca, ano, cor, preco, status FROM Veiculos
        """)
        veiculos = cursor.fetchall()
        conexao.close()

        # Limpar a tabela antes de atualizar
        for row in tree.get_children():
            tree.delete(row)

        # Adicionar os veículos à tabela
        for veiculo in veiculos:
            tree.insert("", "end", values=veiculo)

    except Exception as e:
        print(f"Erro ao carregar veículos: {e}")

# Função para abrir a janela de login do cliente
def abrir_login_cliente():
    from Login import abrir_janela_login_cliente
    abrir_janela_login_cliente()

def abrir_login_vendedor():
    from Login import abrir_janela_login_vendedor
    abrir_janela_login_vendedor()

# Função principal para criar a janela principal
def menu_principal():
    # Criar a janela principal com o tema "superhero"
    root = ttk.Window(title="Menu Principal", themename="superhero")
    root.geometry("800x600")

    # Variável para verificar se a janela principal está ativa
    root.is_active = True

    # Função para lidar com o fechamento da janela
    def on_close():
        root.is_active = False  # Marca a janela como inativa
        root.destroy()          # Fecha a janela

    # Configurar o manipulador de fechamento da janela
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Frame para os botões de login no canto superior direito
    frame_botoes_login = ttk.Frame(root)
    frame_botoes_login.pack(side=TOP, anchor=NE, padx=10, pady=10)

# Botão de Login do Vendedor
    botao_login_vendedor = ttk.Button(
    frame_botoes_login,
    text="Login Vendedor",
    bootstyle=(PRIMARY, OUTLINE),
    command=abrir_login_vendedor
    )
    botao_login_vendedor.pack(side=RIGHT, padx=5)

    # Botão de Login do Cliente
    botao_login_cliente = ttk.Button(
        frame_botoes_login,
        text="Login Cliente",
        bootstyle=(PRIMARY, OUTLINE),
        command=abrir_login_cliente
    )
    botao_login_cliente.pack(side=RIGHT, padx=5)

    # Frame para exibir os veículos cadastrados
    frame_veiculos = ttk.Frame(root)
    frame_veiculos.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    # Título da seção de veículos
    titulo_veiculos = ttk.Label(frame_veiculos, text="Veículos Cadastrados", font=("Helvetica", 14, "bold"), bootstyle=PRIMARY)
    titulo_veiculos.pack(pady=10)

    # Treeview para exibir os veículos em formato de tabela
    colunas = ("Modelo", "Marca", "Ano", "Cor", "Preço", "Status")
    tree = ttk.Treeview(frame_veiculos, columns=colunas, show="headings", height=15)
    tree.pack(fill=BOTH, expand=YES)

    # Configurar as colunas da tabela
    for coluna in colunas:
        tree.heading(coluna, text=coluna)
        tree.column(coluna, width=100, anchor=CENTER)

    # Carregar os veículos cadastrados
    carregar_veiculos(tree)

    # Iniciar o loop principal
    root.mainloop()

if __name__ == "__main__":
    menu_principal()