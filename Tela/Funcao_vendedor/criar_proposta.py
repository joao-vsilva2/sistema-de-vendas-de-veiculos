import sqlite3
from tkinter import StringVar, IntVar, DoubleVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

CAMINHO = "Dados/SQLite/db.sqlite"

def criar_proposta():
        # Criar uma nova janela para criar propostas
        janela_proposta = ttk.Toplevel()
        janela_proposta.title("Criar Proposta")
        janela_proposta.geometry("600x600")

        # Variáveis para os campos
        veiculo_id_var = IntVar()
        cliente_id_var = IntVar()
        vendedor_id_var = IntVar()
        data_proposta_var = StringVar()
        valor_oferecido_var = DoubleVar()
        status_var = StringVar(value="Pendente")

        # Função para salvar a proposta
        def salvar_proposta():
            try:
                veiculo_id = int(veiculo_id_var.get())
                cliente_id = int(cliente_id_var.get())
                vendedor_id = int(vendedor_id_var.get())
                data_proposta = str(data_proposta_var.get())
                valor_oferecido = float(valor_oferecido_var.get())
                status = str(status_var.get())

                # Validar campos obrigatórios
                if not veiculo_id or not cliente_id or not data_proposta or not valor_oferecido or not status:
                    mensagem_proposta.config(text="Erro: Preencha todos os campos!", bootstyle=DANGER)
                    return

                # Conectar ao banco de dados e salvar a proposta
                with sqlite3.connect(CAMINHO) as conexao:
                    cursor = conexao.cursor()
                    cursor.execute("""
                        INSERT INTO Propostas (veiculo_id, cliente_id, vendedor_id, data_proposta, valor_oferecido, status)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (veiculo_id, cliente_id, vendedor_id, data_proposta, valor_oferecido, status))
                    conexao.commit()
                mensagem_proposta.config(text="Proposta criada com sucesso!", bootstyle=SUCCESS)

            except Exception as e:
                mensagem_proposta.config(text=f"Erro ao criar proposta: {e}", bootstyle=DANGER)

        # Widgets da interface
        ttk.Label(janela_proposta, text="ID do Veículo:", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_proposta, textvariable=veiculo_id_var, bootstyle=SUCCESS).pack(pady=5)
        
        ttk.Label(janela_proposta, text="ID do Cliente:", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_proposta, textvariable=cliente_id_var, bootstyle=SUCCESS).pack(pady=5)

        ttk.Label(janela_proposta, text="ID do Vendedor:", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_proposta, textvariable=vendedor_id_var, bootstyle=SUCCESS).pack(pady=5)
        
        ttk.Label(janela_proposta, text="Data da Proposta (DD-MM-AAAA):", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_proposta, textvariable=data_proposta_var, bootstyle=SUCCESS).pack(pady=5)
        
        ttk.Label(janela_proposta, text="Valor Oferecido:", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_proposta, textvariable=valor_oferecido_var, bootstyle=SUCCESS).pack(pady=5)
        
        ttk.Label(janela_proposta, text="Status:", bootstyle=PRIMARY).pack(pady=5)
        ttk.Entry(janela_proposta, textvariable=status_var, bootstyle=SUCCESS).pack(pady=5)
        
        ttk.Button(janela_proposta, text="Salvar Proposta", bootstyle=(SUCCESS, OUTLINE), command=salvar_proposta).pack(pady=10)
        
        mensagem_proposta = ttk.Label(janela_proposta, text="", font=("Helvetica", 12))
        mensagem_proposta.pack(pady=10)