import sqlite3

CAMINHO = "Dados/SQLite/db.sqlite"  

conexao = sqlite3.connect(CAMINHO)
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE Veiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo VARCHAR(100),
        marca VARCHAR(100),
        ano INT,
        cor VARCHAR(50),
        quilometragem INT,
        preco DECIMAL(10, 2),
        status VARCHAR(50) -- Disponível, Vendido, etc.
    );""")


cursor.execute("""
    -- Tabela de Modelos
    CREATE TABLE Modelos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        marca_id INT,
        FOREIGN KEY (marca_id) REFERENCES Marcas(id)
    );""")

cursor.execute("""
    -- Tabela de Marcas
    CREATE TABLE Marcas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100)
    );""")

cursor.execute("""
    -- Tabela de Clientes
    CREATE TABLE Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        email VARCHAR(100),
        telefone VARCHAR(20),
        endereco VARCHAR(255)
    );""")

cursor.execute("""
    -- Tabela de Vendas
    CREATE TABLE Vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        veiculo_id INT,
        cliente_id INT,
        data_venda DATE,
        valor DECIMAL(10, 2),
        FOREIGN KEY (veiculo_id) REFERENCES Veiculos(id),
        FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
    );""")

cursor.execute("""
    -- Tabela de Propostas de Venda
    CREATE TABLE Propostas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        veiculo_id INT,
        cliente_id INT,
        data_proposta DATE,
        valor_oferecido DECIMAL(10, 2),
        status VARCHAR(50), -- Pendente, Aceita, Rejeitada, etc.
        FOREIGN KEY (veiculo_id) REFERENCES Veiculos(id),
        FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
    );""")

cursor.execute("""
    -- Tabela de Manutenções
    CREATE TABLE Manutencoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        veiculo_id INT,
        data_manutencao DATE,
        descricao TEXT,
        custo DECIMAL(10, 2),
        FOREIGN KEY (veiculo_id) REFERENCES Veiculos(id)
    );""")

cursor.execute("""
    -- Tabela de Relatórios de Vendas
    CREATE TABLE Relatorios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        periodo_inicio DATE,
        periodo_fim DATE,
        total_vendas INT,
        receita_total DECIMAL(10, 2)
    );""")

cursor.execute("""
    -- Tabela de Feedback dos Clientes
    CREATE TABLE Feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INT,
        veiculo_id INT,
        data_feedback DATE,
        comentarios TEXT,
        satisfacao INT, -- Escala de 1 a 5
        FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
        FOREIGN KEY (veiculo_id) REFERENCES Veiculos(id)
    );""")

conexao.close()