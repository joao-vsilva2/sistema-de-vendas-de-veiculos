import sqlite3
from tkinter import StringVar, IntVar, DoubleVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

CAMINHO = "Dados/SQLite/db.sqlite"

def gerenciar_manutencoes():
        # Criar uma nova janela para gerenciar manutenções
        janela_manutencao = ttk.Toplevel()
        janela_manutencao.title("Gerenciar Manutenções")
        janela_manutencao.geometry("800x500")

        # Variáveis para os campos
        veiculo_id_var = IntVar()
        vendedor_id_var = IntVar()
        data_manutencao_var = StringVar()
        descricao_var = StringVar()
        custo_var = DoubleVar()

        # Função para adicionar uma nova manutenção
        def adicionar_manutencao():
            try:
                veiculo_id = int(veiculo_id_var.get())
                vendedor_id = int(vendedor_id_var.get())
                data_manutencao = str(data_manutencao_var.get())
                descricao = str(descricao_var.get())
                custo = float(custo_var.get())

                # Validar campos obrigatórios
                if not veiculo_id or not data_manutencao or not descricao or not custo:
                    mensagem_manutencao.config(text="Erro: Preencha todos os campos!", bootstyle=DANGER)
                    return

                # Conectar ao banco de dados e salvar a manutenção
                with sqlite3.connect(CAMINHO) as conexao:
                    cursor = conexao.cursor()
                    cursor.execute("""
                        INSERT INTO Manutencoes (vendedor_id, veiculo_id, data_manutencao, descricao, custo)
                        VALUES (?, ?, ?, ?, ?)
                    """, (vendedor_id, veiculo_id, data_manutencao, descricao, custo))
                    conexao.commit()
                mensagem_manutencao.config(text="Manutenção adicionada com sucesso!", bootstyle=SUCCESS)

            except Exception as e:
                mensagem_manutencao.config(text=f"Erro ao adicionar manutenção: {e}", bootstyle=DANGER)

        # Widgets da interface
        ttk.Label(janela_manutencao, text="ID do Veículo:", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_manutencao, textvariable=veiculo_id_var, bootstyle=SUCCESS).pack(pady=5)

        ttk.Label(janela_manutencao, text="ID do Vendedor:", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_manutencao, textvariable=vendedor_id_var, bootstyle=SUCCESS).pack(pady=5)
        
        ttk.Label(janela_manutencao, text="Data da Manutenção (DD-MM-AAAA):", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_manutencao, textvariable=data_manutencao_var, bootstyle=SUCCESS).pack(pady=5)
        
        ttk.Label(janela_manutencao, text="Descrição:", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_manutencao, textvariable=descricao_var, bootstyle=SUCCESS).pack(pady=5)
        
        ttk.Label(janela_manutencao, text="Custo:", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_manutencao, textvariable=custo_var, bootstyle=SUCCESS).pack(pady=5)
        
        ttk.Button(janela_manutencao, text="Adicionar Manutenção", bootstyle=(SUCCESS, OUTLINE), command=adicionar_manutencao).pack(pady=10)
        
        mensagem_manutencao = ttk.Label(janela_manutencao, text="", font=("Helvetica", 12))
        mensagem_manutencao.pack(pady=10)