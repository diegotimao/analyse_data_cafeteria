# Analise de dados lanchonet

Este é um projeto que visa analisar dados de pedidos feitos em uma lanchonete chamada "Pão na Chapa". O objetivo é gerar informações importantes para ações de marketing e controle de estoque, proporcionando uma visão detalhada do comportamento dos clientes e dos ingredientes utilizados nos pratos.

Este é um projeto que visa analisar dados de pedidos feitos em uma lanchonete chamada "Pão na Chapa". O objetivo é gerar informações importantes para ações de marketing e controle de estoque.

Requisitos
```
Python 3.x
```

### Executando o Projeto

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

Acesse o diretório do projeto:

```
cd seu-repositorio
```

Instale as dependências:

```
pip install -r requirements.txt
```

Execute o projeto:

```
python main.py
```

### Funcionalidades

#### Análise de Log
 
 O módulo analyze_log.py contém funções que analisam o arquivo de log de pedidos e respondem a perguntas como:

- Qual o prato mais pedido por 'maria'?
- Quantas vezes 'arnaldo' pediu 'hamburguer'?
- Quais pratos 'joao' nunca pediu?
- Quais dias 'joao' nunca foi à lanchonete?
- Controle de Estoque (Requisito Bônus)
- O módulo inventory_control.py implementa o controle de estoque e fornece uma lista de compras. O estoque é atualizado automaticamente após cada pedido. Se algum ingrediente acabar, os pratos que o utilizam são removidos do cardápio.

#### Análise Contínua

A classe ```TrackOrders``` no módulo ```track_orders.py``` gera informações contínuas sobre os pedidos, como:

- Prato favorito por cliente.
- Pratos nunca pedidos por cada cliente.
- Dias nunca visitados por cada cliente.
- Dia mais movimentado.
- Dia menos movimentado.

### Dependências

Bibliotecas Python especificadas estão disponíveis no arquivo ```requirements.txt```

```
-r requirements.txt

pytest==7.1.1
pytest-json==0.4.0
flake8==3.8.4
black==20.8b1
pytest-cov==2.10.1
pubsub==0.1.2

```