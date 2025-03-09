import sqlite3
from tkinter import BOTH, YES, messagebox
import ttkbootstrap as ttk

CAMINHO = "Dados/SQLite/db.sqlite"

def exibir_todas_vendas(janela):
        # Criar um Treeview para exibir as vendas
        colunas = ("ID", "Veículo ID", "Cliente ID", "Vendedor ID", "Data da Venda", "Valor")
        tree_vendas = ttk.Treeview(janela, columns=colunas, show="headings", height=15)
        tree_vendas.pack(fill=BOTH, expand=YES, pady=10)

        # Configurar os cabeçalhos das colunas
        for coluna in colunas:
            tree_vendas.heading(coluna, text=coluna)
            tree_vendas.column(coluna, width=100, anchor="center")

        # Carregar os dados das vendas do banco de dados
        try:
            with sqlite3.connect(CAMINHO) as conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                    SELECT id, veiculo_id, cliente_id, vendedor_id, data_venda, valor FROM Vendas
                """)
                vendas = cursor.fetchall()

            # Adicionar os dados ao Treeview
            for venda in vendas:
                tree_vendas.insert("", "end", values=venda)

        except Exception as e:
            print(f"Erro ao carregar vendas: {e}")
            messagebox.showerror("Erro", f"Ocorreu um erro ao carregar as vendas: {e}")