import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sqlite3

# Caminho para o banco de dados
CAMINHO = "Dados/SQLite/db.sqlite"

# Função para abrir a janela principal do cliente
def abrir_janela_cliente(cliente_id):
    id_cliente = cliente_id
    # Criar a janela principal para o cliente
    janela = ttk.Toplevel()
    janela.title("Área do Cliente")
    janela.geometry("800x600")
    style = ttk.Style()
    style.theme_use("superhero")

    # Frame para exibir notificações
    frame_notificacoes = ttk.Frame(janela)
    frame_notificacoes.pack(fill=X, pady=10)

    # Label para exibir notificações
    notificacao_label = ttk.Label(frame_notificacoes, text="", font=("Helvetica", 12), bootstyle=INFO)
    notificacao_label.pack()

    # Função para verificar notificações (compras ou manutenções finalizadas)
    def verificar_notificacoes():
        try:
            conexao = sqlite3.connect(CAMINHO)
            cursor = conexao.cursor()

            # Verificar novas compras
            cursor.execute("""
                SELECT veiculo_id, data_venda FROM Vendas WHERE cliente_id = ?
            """, (id_cliente,))
            compras = cursor.fetchall()

            # Verificar manutenções finalizadas
            cursor.execute("""
                SELECT veiculo_id, data_manutencao FROM Manutencoes WHERE cliente_id = ? AND status = 'Finalizada'
            """, (id_cliente,))
            manutencoes_finalizadas = cursor.fetchall()

            conexao.close()

            # Exibir notificações
            if compras or manutencoes_finalizadas:
                mensagem = ""
                if compras:
                    mensagem += "Novas Compras:\n"
                    for compra in compras:
                        mensagem += f"- Veículo ID: {compra[0]}, Data: {compra[1]}\n"
                if manutencoes_finalizadas:
                    mensagem += "Manutenções Finalizadas:\n"
                    for manutencao in manutencoes_finalizadas:
                        mensagem += f"- Veículo ID: {manutencao[0]}, Data: {manutencao[1]}\n"
                notificacao_label.config(text=mensagem, bootstyle=SUCCESS)
            else:
                notificacao_label.config(text="Nenhuma nova notificação.", bootstyle=SECONDARY)

        except Exception as e:
            notificacao_label.config(text=f"Erro ao verificar notificações: {e}", bootstyle=DANGER)

    # Botão para verificar notificações
    ttk.Button(frame_notificacoes, text="Verificar Notificações", bootstyle=(PRIMARY, OUTLINE), command=verificar_notificacoes).pack(pady=5)

    # Frame para exibir feedbacks
    frame_feedbacks = ttk.Frame(janela)
    frame_feedbacks.pack(fill=BOTH, expand=YES, pady=10)

    ttk.Label(frame_feedbacks, text="Seus Feedbacks", font=("Helvetica", 14, "bold"), bootstyle=PRIMARY).pack(pady=10)

    # Treeview para exibir os feedbacks
    colunas_feedback = ("ID", "Veículo ID", "Data", "Comentários", "Satisfação")
    tree_feedback = ttk.Treeview(frame_feedbacks, columns=colunas_feedback, show="headings", height=10)
    tree_feedback.pack(fill=BOTH, expand=YES)

    for coluna in colunas_feedback:
        tree_feedback.heading(coluna, text=coluna)
        tree_feedback.column(coluna, width=100, anchor=CENTER)

    # Carregar feedbacks do cliente
    def carregar_feedbacks():
        try:
            conexao = sqlite3.connect(CAMINHO)
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT id, veiculo_id, data_feedback, comentarios, satisfacao FROM Feedback WHERE cliente_id = ?
            """, (id_cliente,))
            feedbacks = cursor.fetchall()
            conexao.close()

            # Limpar a tabela antes de atualizar
            for row in tree_feedback.get_children():
                tree_feedback.delete(row)

            # Adicionar os feedbacks à tabela
            for feedback in feedbacks:
                tree_feedback.insert("", "end", values=feedback)

        except Exception as e:
            print(f"Erro ao carregar feedbacks: {e}")

    carregar_feedbacks()

    # Frame para exibir compras
    frame_compras = ttk.Frame(janela)
    frame_compras.pack(fill=BOTH, expand=YES, pady=10)

    ttk.Label(frame_compras, text="Suas Compras", font=("Helvetica", 14, "bold"), bootstyle=PRIMARY).pack(pady=10)

    # Treeview para exibir as compras
    colunas_compras = ("ID", "Veículo ID", "Data da Compra", "Valor")
    tree_compras = ttk.Treeview(frame_compras, columns=colunas_compras, show="headings", height=10)
    tree_compras.pack(fill=BOTH, expand=YES)

    for coluna in colunas_compras:
        tree_compras.heading(coluna, text=coluna)
        tree_compras.column(coluna, width=100, anchor=CENTER)

    # Carregar compras do cliente
    def carregar_compras():
        try:
            conexao = sqlite3.connect(CAMINHO)
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT id, veiculo_id, data_venda, valor FROM Vendas WHERE cliente_id = ?
            """, (id_cliente,))
            compras = cursor.fetchall()
            conexao.close()

            # Limpar a tabela antes de atualizar
            for row in tree_compras.get_children():
                tree_compras.delete(row)

            # Adicionar as compras à tabela
            for compra in compras:
                tree_compras.insert("", "end", values=compra)

        except Exception as e:
            print(f"Erro ao carregar compras: {e}")

    carregar_compras()

    # Iniciar a janela
    janela.mainloop()