import sqlite3
from tkinter import messagebox, Toplevel
from ttkbootstrap import Style, Frame, Label, Entry, Button
from ttkbootstrap.constants import *

CAMINHO = "Dados/SQLite/db.sqlite"

def criar_venda():
    def salvar_venda():
        # Obter os valores dos campos
        veiculo_id = entry_veiculo_id.get()
        cliente_id = entry_cliente_id.get()
        vendedor_id = entry_vendedor_id.get()
        data_venda = entry_data_venda.get()  # Data agora é um Entry simples
        valor = entry_valor.get()

        # Validar campos obrigatórios
        if not veiculo_id or not cliente_id or not vendedor_id or not data_venda or not valor:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")
            return

        try:
            # Converter valores numéricos
            veiculo_id = int(veiculo_id)
            cliente_id = int(cliente_id)
            vendedor_id = int(vendedor_id)
            valor = float(valor)

            # Conectar ao banco de dados
            conexao = sqlite3.connect(CAMINHO)
            cursor = conexao.cursor()

            # Verificar se o veículo existe antes de prosseguir
            cursor.execute("SELECT * FROM Veiculos WHERE id = ?", (veiculo_id,))
            veiculo = cursor.fetchone()
            if not veiculo:
                messagebox.showerror("Erro", "Veículo não encontrado!")
                conexao.close()
                return

            # Inserir a venda na tabela Vendas
            cursor.execute("""
                INSERT INTO Vendas (veiculo_id, cliente_id, vendedor_id, data_venda, valor)
                VALUES (?, ?, ?, ?, ?)
            """, (veiculo_id, cliente_id, vendedor_id, data_venda, valor))

            # Remover o veículo da tabela Veiculos
            cursor.execute("DELETE FROM Veiculos WHERE id = ?", (veiculo_id,))

            # Commit e fechar a conexão
            conexao.commit()
            conexao.close()

            # Exibir mensagem de sucesso
            messagebox.showinfo("Sucesso", "Venda registrada com sucesso! O veículo foi removido do estoque.")

            # Limpar os campos após o registro
            entry_veiculo_id.delete(0, 'end')
            entry_cliente_id.delete(0, 'end')
            entry_vendedor_id.delete(0, 'end')
            entry_data_venda.delete(0, 'end')
            entry_valor.delete(0, 'end')

        except ValueError:
            messagebox.showerror("Erro", "Certifique-se de que os IDs e o valor são números válidos.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao registrar a venda: {str(e)}")

    # Configurar o tema "superhero"
    style = Style(theme="superhero")

    # Criar a janela principal
    janela = Toplevel()  
    janela.title("Criar Venda")
    janela.geometry("400x500")

    # Frame principal
    frame = Frame(janela, padding=10)
    frame.pack(fill="both", expand=True)

    # Campo Veículo ID
    Label(frame, text="ID do Veículo:", anchor="w").pack(fill="x", pady=5)
    entry_veiculo_id = Entry(frame)
    entry_veiculo_id.pack(fill="x", pady=5)

    # Campo Cliente ID
    Label(frame, text="ID do Cliente:", anchor="w").pack(fill="x", pady=5)
    entry_cliente_id = Entry(frame)
    entry_cliente_id.pack(fill="x", pady=5)

    # Campo Vendedor ID
    Label(frame, text="ID do Vendedor:", anchor="w").pack(fill="x", pady=5)
    entry_vendedor_id = Entry(frame)
    entry_vendedor_id.pack(fill="x", pady=5)

    # Campo Data da Venda
    Label(frame, text="Data da Venda (DD-MM-AAAA):", anchor="w").pack(fill="x", pady=5)
    entry_data_venda = Entry(frame)  # Usando Entry simples para evitar erros
    entry_data_venda.pack(fill="x", pady=5)

    # Campo Valor
    Label(frame, text="Valor da Venda:", anchor="w").pack(fill="x", pady=5)
    entry_valor = Entry(frame)
    entry_valor.pack(fill="x", pady=5)

    # Botão Salvar
    btn_salvar = Button(frame, text="Salvar Venda", command=salvar_venda, bootstyle=SUCCESS)
    btn_salvar.pack(fill="x", pady=20)