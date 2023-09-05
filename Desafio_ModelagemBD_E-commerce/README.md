# Descrição do Projeto

  Assim como demonstrado durante o desafio, realize a criação do Script SQL para criação do esquema do banco de dados. Posteriormente, realize a persistência de dados para realização de testes. Especifique ainda queries mais complexas dos que apresentadas durante a explicação do desafio. Sendo assim, crie queries SQL com as cláusulas abaixo:
  
  - [Recuperações simples com SELECT Statement;](#querys-para-recuperação-de-dados-através-do-select-com-filtro-where-e-join)
  - [Filtros com WHERE Statement;](#querys-para-recuperação-de-dados-através-do-select-com-filtro-where-e-join)
  - [Crie expressões para gerar atributos derivados;](#criando-filtros-para-gerar-atributos-derivados)
  - [Defina ordenações dos dados com ORDER BY;](#utilizando-clausulas-order-by)
  - [Condições de filtros aos grupos – HAVING Statement;](#condições-de-filtros-aos-grupos---having-statement)
  - [Crie junções entre tabelas para fornecer uma perspectiva mais complexa dos dados.](#condições-de-filtros-aos-grupos---having-statement)
    
## Diretrizes 

  - Não há um mínimo de queries a serem realizadas;
  - Os tópicos supracitados devem estar presentes nas queries;
  - Elabore perguntas que podem ser respondidas pelas consultas;
  - As cláusulas podem estar presentes em mais de uma query;

# Desenvolvimento do Projeto: 
## Ferramentas Utilizadas: 

  - MySql Workbench  8.0 CE
  - Visual Studio Code
    
## Diagrama Relacional: 
![GitHub Logo](https://github.com/anacschmitz/Bootcamp_CienciasDeDados/blob/main/Desafio_ModelagemBD_E-commerce/Modelagem_e_commerce.png)

# Criação Lógica do Banco de dados: 

```
create database if not exists e_commerce;

use e_commerce;

create table produtos (
	id int auto_increment primary key,
    categoria varchar(45), 
    preço float,
    tamanho_peso varchar(45)
    );
    
ALTER TABLE produtos
ADD nomeProduto varchar(45);

create table estoque (
	id int auto_increment primary key,
    local varchar(255),
    nome varchar(50)
);

create table produto_estoque(
	quantidade int, 
    fk_produto_estoque_produtoId int,
    fk_Produto_estoque_Estoque int, 
    foreign key (fk_produto_estoque_produtoId) 
		references produtos(id)
        on delete cascade
		on update cascade,
    foreign key (fk_Produto_estoque_Estoque) 
		references estoque(id)
        on delete cascade
		on update cascade
);

create table cliente(
	id int auto_increment primary key,
    Pnome varchar(10), 
    Mnome varchar(20),
    sobrenome varchar(20),  
    endereco varchar(45), 
    cpf char(11),
    dataNascimento date
);

create table carteira_cliente(
	id int auto_increment primary key,
    nomeCartao varchar(45),
    tipoCartao enum('credito', 'debito'),
    numeroCartao varchar(16),
    num_cvc varchar(3),
    vencimento_cartao date,
    fk_carteira_cliente_ClienteId int,
    foreign key (fk_carteira_cliente_ClienteId)
		references cliente(id)
        on delete cascade
		on update cascade
);

create table pedido(
	id int auto_increment primary key,
    statusPedido ENUM('Em andamento', 'Processando', 'Enviado'),
    descricao varchar (45),
	valorFrete float,
    fk_pedido_ClienteId int,
    foreign key (fk_pedido_ClienteId) references cliente(id)
);

ALTER TABLE pedido
ADD valorPedido float;

create table entrega (
	id int auto_increment primary key,
    codigo int, 
    status Enum('rota de entrega', 'entregue', 'processamento'),
    fk_entrega_pedido_PedidoId int, 
    foreign key (fk_entrega_pedido_PedidoId)
		references pedido(id)
		on delete cascade
		on update cascade  
);

create table produtos_pedido(
	id int auto_increment primary key,
    quantidade varchar (45),
    status ENUM('Disponivel', 'Sem estoque'),
    fk_produto_pedido_ProdutoId int,
    fk_produto_pedido_clienteId int,
    fk_produtos_pedido_pedidoId int,
    foreign key (fk_produto_pedido_ProdutoId)
		references produtos(id)
		on delete cascade
		on update cascade,
	foreign key (fk_produto_pedido_clienteId)
		references cliente(id)
		on delete cascade
		on update cascade,
	foreign key (fk_produtos_pedido_pedidoId)
		references pedido(id)
		on delete cascade
		on update cascade
);

create table vendedores_externos (
	id int auto_increment primary key,
    nomeFantasia varchar(45),
    razaoSocial varchar(45),
    cnpj char(15),
    local_cidade varchar(45),
    contato varchar (45)
);


create table produtos_vendedores_externos(
	id int auto_increment primary key,
    quantidade int,
    fk_produtos_vendedores_externos_vendedorId int,
    fk_produtos_vendedores_externos_produtoId int,
    foreign key (fk_produtos_vendedores_externos_vendedorId)
		references vendedores_externos(id)
		on delete cascade
		on update cascade,
    foreign key (fk_produtos_vendedores_externos_produtoId)
		references produtos(id)
		on delete cascade
		on update cascade
);

```

## Dados Persistidos: 
```
#Produto

INSERT INTO produtos (categoria, preço, tamanho_peso, nomeProduto)
VALUES ('Eletrônicos', 899.99, '15 x 10 x 2 cm', 'AirFryer');

INSERT INTO produtos (categoria, preço, tamanho_peso, nomeProduto)
VALUES ('Moda', 49.99, 'M', 'calça Jeans');

INSERT INTO produtos (categoria, preço, tamanho_peso, nomeProduto)
VALUES ('Livros', 29.95, '14 x 21 cm', 'A menina que roubava livros');

INSERT INTO produtos (categoria, preço, tamanho_peso, nomeProduto)
VALUES ('Brinquedos', 39.99, '30 x 30 x 10 cm', 'Barbie');

INSERT INTO produtos (categoria, preço, tamanho_peso, nomeProduto)
VALUES ('Jóias', 299.50, 'Ouro 18K', 'brinco prata');

INSERT INTO produtos (categoria, preço, tamanho_peso, nomeProduto)
VALUES ('Esportes', 79.99, 'Tamanho Único', 'chuteira masculina Nike');

INSERT INTO produtos (categoria, preço, tamanho_peso, nomeProduto)
VALUES ('Móveis', 399.00, '80 x 120 x 60 cm', 'cabeceira modulada');

INSERT INTO produtos (categoria, preço, tamanho_peso, nomeProduto)
VALUES ('Alimentos', 5.99, '500g', 'pasta de amendoin');

INSERT INTO produtos (categoria, preço, tamanho_peso, nomeProduto)
VALUES ('Eletrônicos', 149.99, '20 x 15 x 5 cm', 'TC Samsung');

INSERT INTO produtos (categoria, preço, tamanho_peso, nomeProduto)
VALUES ('Moda', 79.95, 'G', 'top academia');

#Cliente

INSERT INTO Cliente (Pnome, Mnome, sobrenome, endereco, cpf, dataNascimento) 
VALUES ('José', 'Carlos', 'Silva', 'Rua João Febronio de Oliveira', '00145787877', '1992-01-10');

INSERT INTO Cliente (Pnome, Mnome, sobrenome, endereco, cpf, dataNascimento) 
VALUES ('Ana', 'Maria', 'Santos', 'Avenida das Flores', '12345678900', '1985-05-20');

INSERT INTO Cliente (Pnome, Mnome, sobrenome, endereco, cpf, dataNascimento) 
VALUES ('Carlos', 'Eduardo', 'Pereira', 'Rua das Palmeiras', '98765432101', '1990-11-15');

INSERT INTO Cliente (Pnome, Mnome, sobrenome, endereco, cpf, dataNascimento) 
VALUES ('Maria', 'Luiza', 'Rocha', 'Travessa dos Artistas', '55555555555', '1978-08-30');

INSERT INTO Cliente (Pnome, Mnome, sobrenome, endereco, cpf, dataNascimento) 
VALUES ('Fernando', 'José', 'Oliveira', 'Avenida Principal', '44444444444', '2000-03-05');

INSERT INTO Cliente (Pnome, Mnome, sobrenome, endereco, cpf, dataNascimento) 
VALUES ('Luana', 'Silva', 'Costa', 'Rua dos Girassóis', '33333333333', '1987-07-12');

INSERT INTO Cliente (Pnome, Mnome, sobrenome, endereco, cpf, dataNascimento) 
VALUES ('Pedro', 'Henrique', 'Fernandes', 'Alameda das Árvores', '22222222222', '1995-12-25');

INSERT INTO Cliente (Pnome, Mnome, sobrenome, endereco, cpf, dataNascimento) 
VALUES ('Sandra', 'Regina', 'Machado', 'Rua dos Passarinhos', '66666666666', '1980-09-08');

INSERT INTO Cliente (Pnome, Mnome, sobrenome, endereco, cpf, dataNascimento) 
VALUES ('João', 'Victor', 'Santana', 'Avenida dos Esportes', '77777777777', '1998-04-18');

INSERT INTO Cliente (Pnome, Mnome, sobrenome, endereco, cpf, dataNascimento) 
VALUES ('Mariana', 'Ferreira', 'Nunes', 'Rua das Lojas', '88888888888', '1982-06-28');

#Carteira_cliente

-- Inserção 1 (relacionada ao primeiro cliente)
INSERT INTO carteira_cliente (nomeCartao, tipoCartao, numeroCartao, num_cvc, vencimento_cartao, fk_carteira_cliente_ClienteId)
VALUES ('João Silva', 'credito', '1234567812345678', '123', '2025-12-31', 1);

-- Inserção 2 (relacionada ao segundo cliente)
INSERT INTO carteira_cliente (nomeCartao, tipoCartao, numeroCartao, num_cvc, vencimento_cartao, fk_carteira_cliente_ClienteId)
VALUES ('Ana Santos', 'debito', '9876543210987654', '456', '2024-09-30', 2);

-- Inserção 3 (relacionada ao terceiro cliente)
INSERT INTO carteira_cliente (nomeCartao, tipoCartao, numeroCartao, num_cvc, vencimento_cartao, fk_carteira_cliente_ClienteId)
VALUES ('Carlos Pereira', 'credito', '5555222233334444', '789', '2023-11-15', 3);

-- Inserção 4 (relacionada ao quarto cliente)
INSERT INTO carteira_cliente (nomeCartao, tipoCartao, numeroCartao, num_cvc, vencimento_cartao, fk_carteira_cliente_ClienteId)
VALUES ('Maria Rocha', 'debito', '1111222233334444', '234', '2024-08-30', 4);

-- Inserção 5 (relacionada ao quinto cliente)
INSERT INTO carteira_cliente (nomeCartao, tipoCartao, numeroCartao, num_cvc, vencimento_cartao, fk_carteira_cliente_ClienteId)
VALUES ('Fernando Oliveira', 'credito', '4444333322221111', '567', '2025-01-05', 5);

-- Inserção 6 (relacionada ao sexto cliente)
INSERT INTO carteira_cliente (nomeCartao, tipoCartao, numeroCartao, num_cvc, vencimento_cartao, fk_carteira_cliente_ClienteId)
VALUES ('Luana Costa', 'debito', '7777888899990000', '789', '2024-07-12', 6);

-- Inserção 7 (relacionada ao sétimo cliente)
INSERT INTO carteira_cliente (nomeCartao, tipoCartao, numeroCartao, num_cvc, vencimento_cartao, fk_carteira_cliente_ClienteId)
VALUES ('Pedro Fernandes', 'credito', '9999888877776666', '234', '2024-12-25', 7);

-- Inserção 8 (relacionada ao oitavo cliente)
INSERT INTO carteira_cliente (nomeCartao, tipoCartao, numeroCartao, num_cvc, vencimento_cartao, fk_carteira_cliente_ClienteId)
VALUES ('Sandra Machado', 'debito', '5555444433332222', '456', '2023-09-08', 8);

-- Inserção 9 (relacionada ao nono cliente)
INSERT INTO carteira_cliente (nomeCartao, tipoCartao, numeroCartao, num_cvc, vencimento_cartao, fk_carteira_cliente_ClienteId)
VALUES ('João Santana', 'credito', '1111333344445555', '789', '2025-04-18', 9);

-- Inserção 10 (relacionada ao décimo cliente)
INSERT INTO carteira_cliente (nomeCartao, tipoCartao, numeroCartao, num_cvc, vencimento_cartao, fk_carteira_cliente_ClienteId)
VALUES ('Mariana Nunes', 'debito', '7777666677778888', '234', '2023-06-28', 10);



##Estoque:

INSERT INTO estoque (local, nome)
VALUES
    ('Armazém A', 'Estoque Central'),
    ('Armazém B', 'Estoque Secundário 1'),
    ('Armazém C', 'Estoque Secundário 2'),
    ('Armazém D', 'Estoque Regional 1'),
    ('Armazém E', 'Estoque Regional 2'),
    ('Armazém F', 'Estoque Regional 3'),
    ('Armazém G', 'Estoque Temporário 1'),
    ('Armazém H', 'Estoque Temporário 2'),
    ('Armazém I', 'Estoque Temporário 3'),
    ('Armazém J', 'Estoque Temporário 4');

## Inserções na tabela "produto_estoque" relacionando produtos a estoques
-- Estoque Central (Armazém A)
INSERT INTO produto_estoque (quantidade, fk_produto_estoque_produtoId, fk_Produto_estoque_Estoque)
VALUES
    (100, 1, 1),
    (50, 2, 1),
    (75, 3, 1);

-- Estoque Secundário 1 (Armazém B)
INSERT INTO produto_estoque (quantidade, fk_produto_estoque_produtoId, fk_Produto_estoque_Estoque)
VALUES
    (40, 4, 2),
    (20, 5, 2);

-- Estoque Regional 1 (Armazém D)
INSERT INTO produto_estoque (quantidade, fk_produto_estoque_produtoId, fk_Produto_estoque_Estoque)
VALUES
    (30, 6, 4),
    (15, 7, 4);

-- Estoque Temporário 1 (Armazém G)
INSERT INTO produto_estoque (quantidade, fk_produto_estoque_produtoId, fk_Produto_estoque_Estoque)
VALUES
    (10, 8, 7),
    (5, 9, 7),
    (8, 10, 7);
    
#Pedidos
INSERT INTO pedido (statusPedido, descricao, valorFrete, valorPedido, fk_pedido_ClienteId)
VALUES
    ('Em andamento', 'Pedido 1', 10.00, 50.00, 1),
    ('Processando', 'Pedido 2', 8.50, 45.00, 2),
    ('Enviado', 'Pedido 3', 15.00, 60.00, 3),
    ('Em andamento', 'Pedido 4', 12.00, 48.00, 6),
    ('Processando', 'Pedido 5', 9.50, 47.50, 7),
    ('Enviado', 'Pedido 6', 18.00, 68.00, 8),
    ('Em andamento', 'Pedido 7', 11.50, 57.50, 9),
    ('Processando', 'Pedido 8', 7.75, 42.75, 10),
    ('Enviado', 'Pedido 9', 14.50, 59.50, 1),
    ('Em andamento', 'Pedido 10', 13.00, 53.00, 2);

#Entrega
INSERT INTO entrega (codigo, status, fk_entrega_pedido_PedidoId)
VALUES
	(12345, 'rota de entrega', 1),
    (54321, 'entregue', 2),
    (98765, 'processamento', 3),
    (11111, 'rota de entrega', 4),
    (22222, 'entregue', 5),
    (33333, 'processamento', 6),
    (44444, 'rota de entrega', 7),
    (55555, 'entregue', 8),
    (66666, 'processamento', 9),
    (77777, 'rota de entrega', 10),
    (88888, 'entregue', 1),
    (99999, 'processamento', 2),
    (12345, 'entregue', 3);

##Inserções na tabela "produtos_pedido" relacionando produtos, clientes e pedidos
-- Pedido 1
INSERT INTO produtos_pedido (quantidade, status, fk_produto_pedido_ProdutoId, fk_produto_pedido_clienteId, fk_produtos_pedido_pedidoId)
VALUES
    ('2 unidades', 'Disponivel', 1, 1, 1),
    ('3 unidades', 'Disponivel', 2, 2, 1);

-- Pedido 2
INSERT INTO produtos_pedido (quantidade, status, fk_produto_pedido_ProdutoId, fk_produto_pedido_clienteId, fk_produtos_pedido_pedidoId)
VALUES
    ('1 unidade', 'Disponivel', 3, 3, 2);

-- Pedido 3
INSERT INTO produtos_pedido (quantidade, status, fk_produto_pedido_ProdutoId, fk_produto_pedido_clienteId, fk_produtos_pedido_pedidoId)
VALUES
    ('4 unidades', 'Disponivel', 4, 4, 3),
    ('2 unidades', 'Disponivel', 5, 5, 3);
    
-- Pedido 4
INSERT INTO produtos_pedido (quantidade, status, fk_produto_pedido_ProdutoId, fk_produto_pedido_clienteId, fk_produtos_pedido_pedidoId)
VALUES
    ('5 unidades', 'Disponivel', 1, 6, 4),
    ('2 unidades', 'Disponivel', 2, 7, 4);

-- Pedido 5
INSERT INTO produtos_pedido (quantidade, status, fk_produto_pedido_ProdutoId, fk_produto_pedido_clienteId, fk_produtos_pedido_pedidoId)
VALUES
    ('3 unidades', 'Disponivel', 3, 8, 5);

-- Pedido 6
INSERT INTO produtos_pedido (quantidade, status, fk_produto_pedido_ProdutoId, fk_produto_pedido_clienteId, fk_produtos_pedido_pedidoId)
VALUES
    ('6 unidades', 'Disponivel', 4, 9, 6),
    ('4 unidades', 'Disponivel', 5, 10, 6);

-- Pedido 7
INSERT INTO produtos_pedido (quantidade, status, fk_produto_pedido_ProdutoId, fk_produto_pedido_clienteId, fk_produtos_pedido_pedidoId)
VALUES
    ('1 unidade', 'Disponivel', 6, 1, 7);

-- Pedido 8
INSERT INTO produtos_pedido (quantidade, status, fk_produto_pedido_ProdutoId, fk_produto_pedido_clienteId, fk_produtos_pedido_pedidoId)
VALUES
    ('2 unidades', 'Disponivel', 7, 2, 8);

-- Pedido 9
INSERT INTO produtos_pedido (quantidade, status, fk_produto_pedido_ProdutoId, fk_produto_pedido_clienteId, fk_produtos_pedido_pedidoId)
VALUES
    ('4 unidades', 'Disponivel', 8, 3, 9),
    ('3 unidades', 'Disponivel', 9, 4, 9);

-- Pedido 10
INSERT INTO produtos_pedido (quantidade, status, fk_produto_pedido_ProdutoId, fk_produto_pedido_clienteId, fk_produtos_pedido_pedidoId)
VALUES
    ('1 unidade', 'Disponivel', 10, 5, 10);
    
##Vendedores Externos
INSERT INTO vendedores_externos (nomeFantasia, razaoSocial, cnpj, local_cidade, contato)
VALUES
    ('Vendedor1', 'Empresa1', '12345678901234', 'Cidade A', 'Contato1'),
    ('Vendedor2', 'Empresa2', '56789012345678', 'Cidade B', 'Contato2'),
    ('Vendedor3', 'Empresa3', '90123456789012', 'Cidade C', 'Contato3'),
    ('Vendedor4', 'Empresa4', '34567890123456', 'Cidade D', 'Contato4'),
    ('Vendedor5', 'Empresa5', '78901234567890', 'Cidade E', 'Contato5'),
    ('Vendedor6', 'Empresa6', '23456789012345', 'Cidade F', 'Contato6'),
    ('Vendedor7', 'Empresa7', '67890123456789', 'Cidade G', 'Contato7'),
    ('Vendedor8', 'Empresa8', '01234567890123', 'Cidade H', 'Contato8'),
    ('Vendedor9', 'Empresa9', '45678901234567', 'Cidade I', 'Contato9'),
    ('Vendedor10', 'Empresa10', '89012345678901', 'Cidade J', 'Contato10');

##Produtos_vendedores_externos
INSERT INTO produtos_vendedores_externos (quantidade, fk_produtos_vendedores_externos_vendedorId, fk_produtos_vendedores_externos_produtoId)
VALUES
    (50, 1, 1),
    (30, 2, 2),
    (20, 3, 3),
    (40, 4, 4),
    (60, 5, 5),
    (25, 6, 6),
    (35, 7, 7),
    (45, 8, 8),
    (15, 9, 9),
    (55, 10, 10);
    
```

## Query's para recuperação de dados através do SELECT com filtro WHERE e JOIN:

Selecionar todos os pedidos da tabela "pedido" com seus clientes associados:
```
SELECT pedido.*, cliente.*
FROM pedido
INNER JOIN cliente ON pedido.fk_pedido_ClienteId = cliente.id;
```
Selecionar o nomeFantasia e o contato de todos os vendedores externos da tabela "vendedores_externos":
```
SELECT nomeFantasia, contato
FROM vendedores_externos;
```
Selecionar os produtos vendidos por um vendedor externo específico (por exemplo, vendedor com ID 1) da tabela "produtos_vendedores_externos":
```
SELECT produtos.*
FROM produtos
INNER JOIN produtos_vendedores_externos ON produtos.id = produtos_vendedores_externos.fk_produtos_vendedores_externos_produtoId
WHERE produtos_vendedores_externos.fk_produtos_vendedores_externos_vendedorId = 1;
```

Selecionar todos os pedidos em andamento (status "Em andamento") da tabela "pedido" com informações de entrega associadas:
```
SELECT pedido.*, entrega.*
FROM pedido
LEFT JOIN entrega ON pedido.id = entrega.fk_entrega_pedido_PedidoId
WHERE pedido.statusPedido = 'Em andamento';
```
## Criando Filtros para gerar atributos derivados:

Calcular o valor total de um pedido com base no preço do produto e na quantidade, assumindo que,  o valor do produto será buscado na tabela produtos através do join:
```
SELECT pp.id, pp.quantidade, p.preço, pp.quantidade * p.preço AS valor_total
FROM produtos_pedido pp
JOIN produtos p ON pp.fk_produto_pedido_ProdutoId = p.id;
```

Calcular a idade dos clientes com base em sua data de nascimento:
```
SELECT id, Pnome, Mnome, sobrenome, dataNascimento, YEAR(CURDATE()) - YEAR(dataNascimento) AS idade
FROM cliente;
```

Calcular o valor médio dos produtos em uma determinada categoria:
```
SELECT categoria, AVG(preço) AS valor_médio
FROM produtos
GROUP BY categoria;
```

Calcular o prazo de entrega estimado em dias com base na data do pedido e na data de entrega planejada:
```
SELECT id, statusPedido, DATEDIFF(dataEntregaPlanejada, dataPedido) AS prazo_entrega_em_dias
FROM pedido;
```
## Utilizando Clausulas ORDER BY:

Ordenar produtos por preço em ordem crescente (do mais barato para o mais caro):
```
SELECT * FROM produtos
ORDER BY preço ASC;
```

Ordenar clientes por sobrenome em ordem alfabética crescente:
```
SELECT * FROM cliente
ORDER BY sobrenome ASC;
```                                        

Ordenar entregas por código em ordem crecente:
```
SELECT * FROM entrega
ORDER BY codigo ASC;
```

Ordenar vendedores externos por nome fantasia em ordem alfabética descrescente:
```
SELECT * FROM vendedores_externos
ORDER BY nomeFantasia DESC;
```

## Condições de filtros aos grupos - HAVING Statement:

Filtrar grupos com mais 2 pedidos:
```
SELECT fk_pedido_ClienteId, COUNT(*) AS total_pedidos
FROM pedido
GROUP BY fk_pedido_ClienteId
HAVING total_pedidos > 0;
```

Filtrar grupos com um valor médio de pedido superior à RS500,0:
```
SELECT fk_pedido_ClienteId, AVG(valorPedido) AS valor_medio_pedido
FROM pedido
GROUP BY fk_pedido_ClienteId
HAVING valor_medio_pedido > 10;
```

Filtrar grupos com mais de 2 produtos vendidos:
```
SELECT fk_produto_pedido_ProdutoId, SUM(quantidade) AS total_unidades_vendidas
FROM produtos_pedido
GROUP BY fk_produto_pedido_ProdutoId
HAVING SUM(quantidade) > 2;
```

## Junções entre tabelas para fornecer uma perspectiva mais complexa dos dados:

Listar todos os pedidos com detalhes dos clientes:
```
SELECT p.id AS pedido_id, c.Pnome AS cliente_nome, c.Mnome AS cliente_sobrenome, c.sobrenome AS cliente_sobrenome
FROM pedido p
INNER JOIN cliente c ON p.fk_pedido_ClienteId = c.id;
```

Listar produtos em estoque de um determinado local:
```
SELECT e.local, p.nomeProduto AS produto_nome
FROM estoque e
INNER JOIN produto_estoque pe ON e.id = pe.fk_Produto_estoque_Estoque
INNER JOIN produtos p ON pe.fk_produto_estoque_produtoId = p.id
WHERE e.local = 'Armazém A';
```

Listar produtos em um pedido específico:
```
SELECT p.id AS pedido_id, pr.nomeProduto AS produto_nome, pp.quantidade
FROM pedido p
INNER JOIN produtos_pedido pp ON p.id = pp.fk_produtos_pedido_pedidoId
INNER JOIN produtos pr ON pp.fk_produto_pedido_ProdutoId = pr.id
WHERE p.id = 1;
```

Listar todas as entregar e seus pedidos correspondentes:
```
SELECT e.id AS entrega_id, p.descricao AS pedido_descricao
FROM entrega e
INNER JOIN pedido p ON e.fk_entrega_pedido_PedidoId = p.id;
```

Listar vendedores externos e seus produtos associados:
```
SELECT ve.nomeFantasia AS vendedor_nome, pve.quantidade, pr.nomeProduto AS produto_nome
FROM vendedores_externos ve
INNER JOIN produtos_vendedores_externos pve ON ve.id = pve.fk_produtos_vendedores_externos_vendedorId
INNER JOIN produtos pr ON pve.fk_produtos_vendedores_externos_produtoId = pr.id;
```

Listar os pedidos com status 'Enviado' e seus detalhes de entrega
```
SELECT p.id AS pedido_id, p.statusPedido, e.codigo AS entrega_codigo
FROM pedido p
INNER JOIN entrega e ON p.id = e.fk_entrega_pedido_PedidoId
WHERE p.statusPedido = 'Enviado';
```

Listar os clientes que não fizeram nenhum pedido até o momento:
```
SELECT c.Pnome AS cliente_nome
FROM cliente c
LEFT JOIN pedido p ON c.id = p.fk_pedido_ClienteId
WHERE p.id IS NULL;
```

Listar os produtos que estão em estoque e sua quantidade disponível:
```
SELECT pr.nomeProduto AS produto_nome, pe.quantidade AS quantidade_em_estoque
FROM produtos pr
INNER JOIN produto_estoque pe ON pr.id = pe.fk_produto_estoque_produtoId;
```

