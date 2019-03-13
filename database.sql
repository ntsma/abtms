--
-- AuthDB
--

--
-- Criando database AuthDB
--
CREATE DATABASE authdb;

--
-- Selecionando database AuthDB
--
USE authdb;

--
-- Criando a tabela usuários
--
CREATE TABLE users (
	code INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	cpf VARCHAR(255) NOT NULL UNIQUE,
	phone VARCHAR(255),
  isStudent INTEGER NOT NULL,
  studentType VARCHAR(255) NOT NULL,
	isPaid INTEGER NOT NULL
);

--
-- Atribuindo valores padrões para os campos da table users
--
ALTER TABLE users MODIFY COLUMN isStudent INTEGER DEFAULT 0;

ALTER TABLE users MODIFY COLUMN studentType INTEGER DEFAULT "nd";

ALTER TABLE users MODIFY COLUMN isPaid INTEGER DEFAULT 0;

--
-- Criando a tabela Empresas
--
CREATE TABLE bussiness (
	code INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	cnpj VARCHAR(255) NOT NULL UNIQUE,
	phone VARCHAR(255),
	isPaid INTEGER NOT NULL
);

--
-- Atribuindo valores padrões para os campos da table users
--
ALTER TABLE bussiness MODIFY COLUMN isPaid INTEGER DEFAULT 0;

--
-- Criando a tabela Módulos
--
CREATE TABLE modules(
	code INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255)
);

--
-- Inserindo módulos iniciais a tabela modules
--
INSERT INTO modules (name) values ("Associação");
INSERT INTO modules (name) values ("Administrador");

--
-- Criando a tabela Acesso
--
CREATE TABLE access(
	user INTEGER,
	bussiness INTEGER,
	module INTEGER,
	FOREIGN KEY (user) REFERENCES users(code),
	FOREIGN KEY (bussiness) REFERENCES bussiness(code),
	FOREIGN KEY (module) REFERENCES modules(code)

);

--
-- Criando a tabela Declaração de Estudante
--
CREATE TABLE studentStatement(
  code INTEGER AUTO_INCREMENT PRIMARY KEY,
  path VARCHAR(255),
  user INTEGER,
  createdAt VARCHAR(255),
	status VARCHAR(255),

  FOREIGN KEY(user) REFERENCES users(code)

);

--
-- Criando a tabela de boletos
--
CREATE TABLE bankingBillets (
  code INTEGER AUTO_INCREMENT PRIMARY KEY,
  charge_id VARCHAR(255) NOT NULL UNIQUE,
  cpf VARCHAR(255),
	cnpj VARCHAR(255),
  expire_at VARCHAR(255) NOT NULL,
  created_at VARCHAR(255) NOT NULL,
  value double NOT NULL

);

--
-- Criando a tabela de boletos
--
CREATE TABLE comprovante_pessoa(
	code INTEGER AUTO_INCREMENT PRIMARY KEY,
	user INTEGER NOT NULL,
	status VARCHAR(255) NOT NULL,
	year VARCHAR(255) NOT NULL,
	charge_id VARCHAR(255) NOT NULL,
	path VARCHAR(255) NOT NULL,

	FOREIGN KEY (user) REFERENCES users(code)
);

--
-- Criando a tabela de boletos
--
CREATE TABLE comprovante_pessoa(
	code INTEGER AUTO_INCREMENT PRIMARY KEY,
	bussiness INTEGER NOT NULL,
	status VARCHAR(255) NOT NULL,
	year VARCHAR(255) NOT NULL,
	charge_id VARCHAR(255) NOT NULL,
	path VARCHAR(255) NOT NULL,

	FOREIGN KEY (bussiness) REFERENCES bussiness(code)
);
