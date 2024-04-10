INSERT INTO Endereco (numero, rua, bairro, cidade, uf) VALUES
(123, 'Rua das Flores', 'Centro', 'São Paulo', 'SP'),
(456, 'Avenida dos Anjos', 'Vila Nova', 'Rio de Janeiro', 'RJ'),
(789, 'Rua das Palmeiras', 'Jardim América', 'Belo Horizonte', 'MG'),
(1011, 'Rua das Águias', 'Centro', 'Brasília', 'DF'),
(1213, 'Avenida das Rosas', 'Campo Grande', 'Salvador', 'BA');

INSERT INTO Cliente (nome, sobrenome, dataNascimento, telContato, dataCadastro, cpf, idEndereco) VALUES
('João', 'Silva', '1990-05-15', '(11) 9999-8888', '2024-03-25', '123.456.789-01', 1),
('Maria', 'Santos', '1985-10-20', '(21) 7777-6666', '2024-03-25', '987.654.321-09', 2),
('Pedro', 'Oliveira', '1988-12-30', '(31) 3333-2222', '2024-03-25', '456.789.123-45', 3),
('Ana', 'Martins', '1995-04-05', '(61) 5555-4444', '2024-03-25', '789.123.456-78', 4),
('Lucas', 'Rodrigues', '1993-08-12', '(71) 1111-0000', '2024-03-25', '987.654.321-00', 5);


INSERT INTO Funcionario (nome, sobrenome, dataNascimento, telContato, dataAdmissao, cargo, estaAtivo, salario, cpf, idEndereco) VALUES
('Carlos', 'Santana', '1980-03-10', '(11) 3333-2222', '2020-01-15', 'Gerente', TRUE, 5000.00, '333.444.555-66', 1),
('Amanda', 'Oliveira', '1992-07-20', '(21) 8888-7777', '2021-05-20', 'Vendedor', TRUE, 3000.00, '222.333.444-55', 2),
('Mariana', 'Almeida', '1987-11-05', '(31) 4444-3333', '2019-03-10', 'Atendente', TRUE, 2500.00, '111.222.333-44', 3),
('Rodrigo', 'Sousa', '1985-09-18', '(61) 9999-8888', '2023-02-28', 'Vendedor', TRUE, 2800.00, '444.555.666-77', 4),
('Patrícia', 'Ferreira', '1990-12-25', '(71) 6666-5555', '2022-08-15', 'Atendente', TRUE, 2600.00, '555.666.777-88', 5);


INSERT INTO Fornecedor (nome, cnpj, email, telefone, idEndereco) VALUES
('Fornecedor A', '12.345.678/0001-01', 'fornecedorA@email.com', '(11) 2222-1111', 1),
('Fornecedor B', '98.765.432/0001-02', 'fornecedorB@email.com', '(21) 4444-3333', 2),
('Fornecedor C', '11.223.344/0001-03', 'fornecedorC@email.com', '(31) 6666-5555', 3),
('Fornecedor D', '44.556.677/0001-04', 'fornecedorD@email.com', '(61) 8888-7777', 4),
('Fornecedor E', '99.887.766/0001-05', 'fornecedorE@email.com', '(71) 0000-9999', 5);


INSERT INTO Produto (nome, valor, dataValidade) VALUES
('Produto A', 50.00, '2024-06-30'),
('Produto B', 35.00, '2024-08-15'),
('Produto C', 70.00, '2024-07-20'),
('Produto D', 25.00, '2024-09-10'),
('Produto E', 40.00, '2024-07-31');


INSERT INTO FormaPagamento (nome) VALUES
('Cartão de Crédito'),
('Cartão de Débito'),
('Dinheiro'),
('Pix'),
('Boleto');


INSERT INTO Venda (dataVenda, valorTotal, status, idFormaPagamento, idFuncionario, idCliente) VALUES
('2024-03-25', 150.00, 'Concluída', 1, 1, 1),
('2024-03-26', 200.00, 'Concluída', 2, 2, 2),
('2024-03-27', 120.00, 'Pendente', 3, 3, 3),
('2024-03-28', 80.00, 'Concluída', 4, 4, 4),
('2024-03-29', 90.00, 'Concluída', 5, 5, 5);


INSERT INTO ItemVenda (qtd, idVenda, idProduto) VALUES
(2, 1, 1),
(3, 2, 2),
(1, 3, 3),
(4, 4, 4),
(2, 5, 5);


INSERT INTO Devolucao (valorDevolucao) VALUES
(30.00),
(40.00),
(25.00),
(15.00),
(20.00);


INSERT INTO ItemDevolucao (qtde, idProduto, idDevolucao) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(1, 4, 4),
(2, 5, 5),
(9, 2, 1);


INSERT INTO Convenio (especialidade, dataInicioConvenio, cnpj, idCliente) VALUES
('Pediatra', '2023-01-01', '23.456.789/0001-01', 1);

