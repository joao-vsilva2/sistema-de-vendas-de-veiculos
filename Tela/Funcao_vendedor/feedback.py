import sqlite3
from tkinter import BOTH, YES, messagebox
import ttkbootstrap as ttk

CAMINHO = "Dados/SQLite/db.sqlite"

def visualizar_feedbacks():
    """
    Carrega todos os feedbacks do banco de dados e exibe-os em um Treeview.
    """
    try:
        with sqlite3.connect(CAMINHO) as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT * FROM Feedback
            """)
            feedbacks = cursor.fetchall()

        # Criar uma nova janela para exibir os feedbacks
        janela_feedback = ttk.Toplevel()
        janela_feedback.title("Feedbacks dos Clientes")
        janela_feedback.geometry("800x400")

        # Treeview para exibir os feedbacks
        colunas = ("ID", "Cliente ID", "Veículo ID", "Data", "Comentários", "Satisfação")
        tree = ttk.Treeview(janela_feedback, columns=colunas, show="headings", height=15)
        tree.pack(fill=BOTH, expand=YES)

        # Adicionar scrollbar ao Treeview
        scrollbar = ttk.Scrollbar(janela_feedback, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        for coluna in colunas:
            tree.heading(coluna, text=coluna)
            tree.column(coluna, width=100, anchor="center", stretch=True)

        for feedback in feedbacks:
            tree.insert("", "end", values=feedback)

    except sqlite3.Error as e:
        print(f"Erro ao carregar feedbacks: {e}")
        messagebox.showerror("Erro", f"Ocorreu um erro ao carregar os feedbacks: {e}")
