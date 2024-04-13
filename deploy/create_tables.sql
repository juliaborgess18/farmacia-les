DROP TABLE IF EXISTS Fornecedor; 
DROP TABLE IF EXISTS ItemVenda;
DROP TABLE IF EXISTS Venda;
DROP TABLE IF EXISTS Funcionario; 
DROP TABLE IF EXISTS FormaPagamento; 
DROP TABLE IF EXISTS ItemDevolucao; 
DROP TABLE IF EXISTS Produto; 
DROP TABLE IF EXISTS Devolucao;
DROP TABLE IF EXISTS Convenio; 
DROP TABLE IF EXISTS Cliente ;
DROP TABLE IF EXISTS Endereco;

CREATE TABLE Endereco (
  idEndereco SERIAL NOT NULL,
  numero INT NOT NULL,
  rua VARCHAR(45) NOT NULL,
  bairro VARCHAR(45) NOT NULL,
  cidade VARCHAR(45) NOT NULL,
  uf CHAR(2) NOT NULL,
  PRIMARY KEY (idEndereco)
 );

CREATE TABLE Cliente (
  idCliente SERIAL NOT NULL,
  nome VARCHAR(45) NOT NULL,
  sobrenome VARCHAR(45) NOT NULL,
  dataNascimento DATE NOT NULL,
  telContato VARCHAR(45) NOT NULL,
  dataCadastro DATE NOT NULL,
  cpf CHAR(14) NOT NULL UNIQUE,
  foiDeletado BOOL DEFAULT FALSE,
  dataDelete DATE,
  idEndereco INT NOT NULL,
  PRIMARY KEY (idCliente),
  CONSTRAINT fk_Cliente_Endereco1
    FOREIGN KEY (idEndereco)
    REFERENCES Endereco (idEndereco)
);

CREATE TABLE Funcionario (
  idFuncionario SERIAL NOT NULL,
  nome VARCHAR(45) NOT NULL,
  sobrenome VARCHAR(45) NOT NULL,
  dataNascimento DATE NOT NULL,
  telContato VARCHAR(45) NOT NULL,
  dataAdmissao DATE NOT NULL,
  cargo VARCHAR(45) NOT NULL,
  estaAtivo BOOLEAN NOT NULL,
  salario DECIMAL NOT NULL,
  cpf CHAR(14) NOT NULL UNIQUE,
  foiDeletado BOOL DEFAULT FALSE,
  dataDelete DATE,
  idEndereco INT NOT NULL,
  PRIMARY KEY (idFuncionario),
  CONSTRAINT fk_Funcionario_Endereco1
    FOREIGN KEY (idEndereco)
    REFERENCES Endereco (idEndereco)
);

CREATE TABLE Fornecedor (
  idFornecedor SERIAL NOT NULL,
  nome VARCHAR(45) NOT NULL,
  cnpj CHAR(18) NOT NULL UNIQUE,
  email VARCHAR(45) NOT NULL,
  telefone VARCHAR(45) NOT NULL,
  foiDeletado BOOL DEFAULT FALSE,
  dataDelete DATE,
  idEndereco INT NOT NULL,
  PRIMARY KEY (idFornecedor, idEndereco),
  CONSTRAINT fk_Fornecedor_Endereco1
    FOREIGN KEY (idEndereco)
    REFERENCES Endereco (idEndereco)
);

CREATE TABLE Produto (
  idProduto SERIAL NOT NULL,
  nome VARCHAR(45) NOT NULL,
  valor DECIMAL NOT NULL,
  dataValidade DATE NOT NULL,
  foiDeletado BOOL DEFAULT FALSE,
  dataDelete DATE,
  PRIMARY KEY (idProduto)
);

CREATE TABLE FormaPagamento (
  idFormaPagamento SERIAL NOT NULL,
  nome VARCHAR(45) NOT NULL,
  PRIMARY KEY (idFormaPagamento)
);

CREATE TABLE Venda (
  idVenda SERIAL NOT NULL,
  dataVenda DATE NOT NULL,
  valorTotal DECIMAL NOT NULL,
  status VARCHAR(45) NOT NULL,
  foiDeletado BOOL DEFAULT FALSE,
  dataDelete DATE,
  idFormaPagamento INT NOT NULL,
  idFuncionario INT NOT NULL,
  idCliente INT NOT NULL,
  PRIMARY KEY (idVenda),
  CONSTRAINT fk_Venda_FormaPagamento1
    FOREIGN KEY (idFormaPagamento)
    REFERENCES FormaPagamento (idFormaPagamento),
  CONSTRAINT fk_Venda_Funcionario1
    FOREIGN KEY (idFuncionario)
    REFERENCES Funcionario (idFuncionario),
  CONSTRAINT fk_Venda_Cliente1
    FOREIGN KEY (idCliente)
    REFERENCES Cliente (idCliente)
);

CREATE TABLE ItemVenda (
  qtd INT NOT NULL,
  idVenda INT NOT NULL,
  idProduto INT NOT NULL,
  PRIMARY KEY (idVenda, idProduto),
  CONSTRAINT fk_ItemVenda_Venda
    FOREIGN KEY (idVenda)
    REFERENCES Venda (idVenda),
  CONSTRAINT fk_ItemVenda_Produto1
    FOREIGN KEY (idProduto)
    REFERENCES Produto (idProduto)
);

CREATE TABLE Devolucao (
  idDevolucao SERIAL NOT NULL,
  valorDevolucao DECIMAL NOT NULL,
  foiDeletado BOOL DEFAULT FALSE,
  dataDelete DATE,
  PRIMARY KEY (idDevolucao)
);

CREATE TABLE ItemDevolucao (
  qtde INT NOT NULL,
  idProduto INT NOT NULL,
  idDevolucao INT NOT NULL,
  PRIMARY KEY (idProduto, idDevolucao),
  CONSTRAINT fk_ItemDevolucao_Produto1
    FOREIGN KEY (idProduto)
    REFERENCES Produto (idProduto),
  CONSTRAINT fk_ItemDevolucao_Devolucao1
    FOREIGN KEY (idDevolucao)
    REFERENCES Devolucao (idDevolucao)
);

CREATE TABLE Convenio (
  idConvenio SERIAL NOT NULL,
  especialidade VARCHAR(45) NOT NULL,
  dataInicioConvenio DATE NOT NULL,
  cnpj CHAR(18) NOT NULL UNIQUE,
  foiDeletado BOOL DEFAULT FALSE,
  dataDelete DATE,
  idCliente INT NOT NULL,
  PRIMARY KEY (idConvenio, idCliente),
  CONSTRAINT fk_Convenio_Cliente1
    FOREIGN KEY (idCliente)
    REFERENCES Cliente (idCliente)
);
