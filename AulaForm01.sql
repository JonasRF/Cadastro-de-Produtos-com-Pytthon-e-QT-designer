create database cadastro_produtos;
use cadastro_produtos;
create table produtos(
id INT NOT NULL auto_increment,
codigo Int,
descricao varchar(50),
preco double,
categoria varchar(50),
primary key (id)
);
use cadastro_produtos;
INSERT INTO produtos(codigo, descricao, preco, categoria) VALUES(123, "impressora",500.00,"informatica");

select*from produtos;
