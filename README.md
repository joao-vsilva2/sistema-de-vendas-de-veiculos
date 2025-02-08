# Sistema de Venda de Automóveis

## Descrição do Projeto

O **Sistema de Venda de Automóveis** é uma solução tecnológica desenvolvida para otimizar e integrar os processos de gestão de concessionárias de veículos. O objetivo principal do projeto é criar uma plataforma que facilite a administração de estoque, clientes, vendas e pós-vendas, proporcionando maior eficiência operacional e melhorando a experiência do cliente.

Com este sistema, concessionárias podem cadastrar veículos com informações detalhadas (modelo, marca, ano, cor, quilometragem, preço), controlar o estoque, registrar propostas de venda, emitir contratos e notas fiscais, além de gerenciar serviços de pós-venda, como manutenções e feedbacks dos clientes. 

Através de relatórios analíticos, as concessionárias poderão tomar decisões estratégicas baseadas em dados reais de vendas, desempenho da equipe e satisfação do cliente.

### Público-Alvo
O público-alvo deste sistema são concessionárias de veículos de todos os portes (pequenas, médias ou grandes) que buscam modernizar e automatizar seus processos de vendas e gestão. 

### Benefícios
- Redução de erros manuais.
- Aumento da produtividade da equipe.
- Melhoria na experiência do cliente, com atendimento mais personalizado e ágil.
- Integração com APIs de pagamento e financiamento para agilizar o processo de vendas.
- Sistema de fidelidade e promoções personalizadas para aumentar a retenção de clientes.

---

## Funcionalidades Principais

1. **Cadastro de Veículos**: Permite o cadastro de veículos com informações detalhadas, como modelo, marca, ano, cor, quilometragem, preço e status (disponível, vendido, etc.).
2. **Controle de Estoque**: Facilita o gerenciamento de entrada e saída de veículos, rastreando quais estão disponíveis ou já foram vendidos.
3. **Cadastro de Clientes**: Armazena informações dos clientes, como nome, e-mail, telefone e endereço, facilitando o contato e histórico de compras.
4. **Histórico de Compras**: Registra todas as compras realizadas por cada cliente, permitindo consultas rápidas e personalização de promoções.
5. **Registro de Propostas**: Permite o registro e acompanhamento de propostas de venda, com status (pendente, aceita, rejeitada) e valor oferecido.
6. **Processo de Vendas**: Integra o registro de vendas, emissão de contratos e notas fiscais, além de facilitar a integração com sistemas de pagamento e financiamento.
7. **Agendamento de Manutenções**: Permite agendar serviços de manutenção e revisões para veículos vendidos, com registro de data, descrição e custo.
8. **Feedback dos Clientes**: Coleta feedbacks dos clientes sobre a experiência de compra e pós-venda, com uma escala de satisfação (1 a 5) e comentários.
9. **Relatórios de Vendas**: Gera relatórios periódicos com dados de vendas, desempenho da equipe e receita total, auxiliando na tomada de decisões.
10. **Sistema de Fidelidade**: Oferece promoções personalizadas e benefícios para clientes fiéis, aumentando a retenção e a satisfação.
11. **Interface Responsiva**: Garantindo dinamismo e responsividade.

---

## Estrutura do Sistema

O sistema está organizado em módulos, cada um responsável por uma parte específica da funcionalidade. Abaixo está a descrição de cada módulo:

### 1. Módulo de Persistência de Dados
- **Responsabilidade**: Gerenciar a interação com o banco de dados relacional.
- **Funcionalidades**:
  - Conexão com o banco de dados.
  - Execução de consultas SQL (SELECT, INSERT, UPDATE, DELETE).
  - Validação de dados antes de persistir.
- **Arquivo**: `persistencia.py`

### 2. Módulo CRUD de Operações
- **Responsabilidade**: Realizar operações básicas de criação, leitura, atualização e exclusão (CRUD) para todas as entidades do sistema (veículos, clientes, vendas, etc.).
- **Funcionalidades**:
  - Cadastro de veículos, clientes, vendas, propostas, manutenções e feedbacks.
  - Atualização e exclusão de registros.
  - Consulta de dados (por exemplo, listar veículos disponíveis ou clientes cadastrados).
- **Arquivo**: `crud_operacoes.py`

### 3. Módulo de Interface Gráfica (UI)
- **Responsabilidade**: Fornecer uma interface amigável para interação do usuário com o sistema.
- **Funcionalidades**:
  - Telas para cadastro e consulta de veículos, clientes, vendas, etc.
  - Formulários para entrada de dados.
  - Exibição de relatórios e feedbacks.
- **Biblioteca**: Tkinter
- **Arquivo**: `interface_grafica.py`

### 4. Módulo de Relatórios e Análises
- **Responsabilidade**: Gerar relatórios e análises com base nos dados do sistema.
- **Funcionalidades**:
  - Relatórios de vendas por período.
  - Análise de desempenho de vendedores.
  - Gráficos e estatísticas de satisfação do cliente.
- **Arquivo**: `relatorios.py`

### 5. Módulo de Pós-Venda
- **Responsabilidade**: Gerenciar atividades relacionadas ao pós-venda, como manutenções e feedbacks.
- **Funcionalidades**:
  - Agendamento de manutenções.
  - Registro de feedbacks dos clientes.
  - Gerenciamento de garantias e serviços adicionais.
- **Arquivo**: `pos_venda.py`

### 6. Módulo de Autenticação e Segurança
- **Responsabilidade**: Garantir a segurança do sistema e controlar o acesso de usuários.
- **Funcionalidades**:
  - Autenticação de usuários (login e senha).
  - Controle de permissões (por exemplo, vendedor vs. administrador).
  - Criptografia de dados sensíveis.
- **Arquivo**: `autenticacao.py`

### 7. Módulo de Integração com APIs Externas
- **Responsabilidade**: Integrar o sistema com APIs de terceiros, como pagamentos e financiamentos.
- **Funcionalidades**:
  - Processamento de pagamentos online.
  - Consulta de opções de financiamento.
- **Arquivo**: `integracao_apis.py`

### 8. Módulo Principal (Main)
- **Responsabilidade**: Coordenar a execução do sistema, importando e utilizando os outros módulos.
- **Funcionalidades**:
  - Inicialização do sistema.
  - Chamada dos módulos conforme a necessidade (por exemplo, abrir a interface gráfica ou gerar um relatório).
- **Arquivo**: `main.py`

---

## Estrutura de Dados Utilizada

1. **Cadastro de Veículos**:
   - Array de objetos: Cada posição do array representa um veículo.
   - Exemplo: Para acessar o segundo veículo, basta usar `veiculos[1]`.

2. **Histórico de Vendas**:
   - Array de listas: Cada posição do array principal representa um veículo, e cada posição interna representa uma venda.

3. **Opções de Cores e Modelos**:
   - Arrays simples.

---

## Bibliotecas Utilizadas

![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white): O SQLite é leve e armazena o banco de dados em um único arquivo, facilitando a portabilidade.

---

## Tecnologias Utilizadas

![Logo Python](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/120px-Python-logo-notext.svg.png)  
_Linguagem de programação Python_

![Logo SQLite](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/120px-SQLite370.svg.png)  
_Banco de dados SQLite_
