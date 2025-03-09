import sqlite3

# Caminho para o banco de dados
CAMINHO = "Dados/SQLite/db.sqlite"

# Conexão com o banco de dados
conexao = sqlite3.connect(CAMINHO)
cursor = conexao.cursor()

# Tabela de Veículos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Veiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo VARCHAR(100),
        marca VARCHAR(100),
        ano INT,
        cor VARCHAR(50),
        quilometragem INT,
        preco DECIMAL(10, 2),
        status VARCHAR(50) -- Disponível, Vendido, Manutenção etc.
    );
""")

# Tabela de Clientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        cpf VARCHAR(14) UNIQUE NOT NULL,
        data_nascimento DATE,
        email VARCHAR(100),
        telefone VARCHAR(20),
        endereco VARCHAR(255),
        senha VARCHAR(255) NOT NULL
    );
""")

# Tabela de Vendas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        veiculo_id INT,
        cliente_id INT,
        vendedor_id INT,
        data_venda DATE,
        valor DECIMAL(10, 2),
        FOREIGN KEY (veiculo_id) REFERENCES Veiculos(id),
        FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
        FOREIGN KEY (vendedor_id) REFERENCES Vendedor(id)
    );
""")

# Tabela de Propostas de Venda
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Propostas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        veiculo_id INT,
        cliente_id INT,
        vendedor_id INT,
        data_proposta DATE,
        valor_oferecido DECIMAL(10, 2),
        status VARCHAR(50), -- Pendente, Aceita, Rejeitada, etc.
        FOREIGN KEY (veiculo_id) REFERENCES Veiculos(id),
        FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
        FOREIGN KEY (vendedor_id) REFERENCES Vendedor(id)
    );
""")

# Tabela de Manutenções
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Manutencoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendedor_id INT,
        veiculo_id INT,
        data_manutencao DATE,
        descricao TEXT,
        custo DECIMAL(10, 2),
        FOREIGN KEY (veiculo_id) REFERENCES Veiculos(id),
        FOREIGN KEY (vendedor_id) REFERENCES Vendedor(id)
    );
""")

# Tabela de Relatórios de Vendas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Relatorios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendedor_id INT NOT NULL,
        periodo_inicio DATE NOT NULL,
        periodo_fim DATE NOT NULL,
        total_vendas INT DEFAULT 0,
        receita_total DECIMAL(10, 2) DEFAULT 0.0,
        total_manutencoes INT DEFAULT 0,
        custo_total_manutencoes DECIMAL(10, 2) DEFAULT 0.0,
        total_propostas INT DEFAULT 0, 
        propostas_aceitas INT DEFAULT 0, 
        propostas_rejeitadas INT DEFAULT 0, 
        FOREIGN KEY (vendedor_id) REFERENCES Vendedor(id)
    );
""")

# Tabela de Feedback dos Clientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INT,
        veiculo_id INT,
        data_feedback DATE,
        comentarios TEXT,
        satisfacao INT, -- Escala de 1 a 5
        FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
        FOREIGN KEY (veiculo_id) REFERENCES Veiculos(id)
    );
""")

# Tabela de Vendedores
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vendedor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        cpf VARCHAR(14) UNIQUE NOT NULL,
        data_nascimento DATE,
        email VARCHAR(100) UNIQUE,
        telefone VARCHAR(20),
        endereco VARCHAR(255),
        data_contratacao DATE,
        salario DECIMAL(10, 2),
        status VARCHAR(50),
        senha VARCHAR(255) NOT NULL
    );
""")

# Fechar a conexão
conexao.close()