#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os


# Conectando ao Banco de Dados:
conexao = sqlite3.connect("biblioteca.bd")
cursor = conexao.cursor()



# Criando as Tabelas caso já não estejam criadas:
cursor.execute("CREATE TABLE IF NOT EXISTS Livros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(50) NOT NULL, autor VARCHAR(30) NOT NULL, editora VARCHAR(30) NOT NULL, ano INTEGER NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS Clientes (cpf INTEGER PRIMARY KEY, nome VARCHAR(30) NOT NULL, idade INTEGER NOT NULL, telefone INTEGER, email VARCHAR(50))")



# Função Menu:
def Menu():
    os.system("clear")
    print("- Biblioteca em Python -")
    print("1 - Cadastrar Livro")
    print("2 - Cadastrar Cliente")
    print("0 - Sair")
    return int(input("Opção: "))



# Função para Cadastrar Livros:
def CadastrarLivro():
    os.system("clear")
    print("- Cadastrar Livro -")
    
    # ERRO - No momento não é possível cadastrar informações contendo acentuação!
    
    # Recolhe as informações do usuário:
    print("\nInforme:")
    titulo = raw_input("Título: ")
    autor = raw_input("Autor: ")
    editora = raw_input("Editora: ")
    ano = int(input("Ano: "))
    
    # Realiza ou não o cadastro do Livro:
    x = 0
    while(x != 1 and x != 2):
        x = int(input("\nDeseja cadastrar esse Livro?\n(1 - Sim / 2 - Não): "))
        
        # Caso Sim:
        if(x == 1):
            cursor.execute("INSERT INTO Livros (titulo, autor, editora, ano) VALUES (?,?,?,?)", (titulo, autor, editora, ano))
            conexao.commit()
            os.system("clear")
            print("Livro Cadastrado com Sucesso!")
            
        # Caso Não:
        elif(x == 2):
            os.system("clear")
            print("Livro Não Cadastrado!")
            
        else:
            print("\nOpção Inválida!")
            raw_input("\nEnter para Continuar!")
            os.system("clear")
    
    raw_input("\nEnter para Continuar!")
    
    
    
# Função para Cadastrar Clientes:
def CadastrarCliente():
    os.system("clear")
    print("- Cadastrar Cliente -")

    # ERRO - No momento não é possível cadastrar informações contendo acentuação!    

    # Recolhe as informações do usuário:
    print("\nInforme:")
    cpf = int(input("CPF: "))
    nome = raw_input("Nome: ")
    idade = int(input("Idade: "))
    telefone = int(input("Telefone: "))
    email = raw_input("Email: ")
    
    # Realiza ou não o cadastro do Cliente:
    x = 0
    while(x != 1 and x != 2):
        x = int(input("\nDeseja cadastrar esse Cliente?\n(1 - Sim / 2 - Não): "))
        
        # Caso Sim:
        if(x == 1):
            cursor.execute("INSERT INTO Clientes (cpf, nome, idade, telefone, email) VALUES (?,?,?,?,?)", (cpf, nome, idade, telefone, email))
            conexao.commit()
            os.system("clear")
            print("Cliente Cadastrado com Sucesso!")
            
        # Caso Não:
        elif(x == 2):
            os.system("clear")
            print("Cliente Não Cadastrado!")
            
        else:
            print("\nOpção Inválida!")
            raw_input("\nEnter para Continuar!")
            os.system("clear")
    
    raw_input("\nEnter para Continuar!")

    
    
# Código Principal:
opcao = Menu()
while(opcao != 0):
    if(opcao == 1):
        CadastrarLivro()
    elif(opcao == 2):
        CadastrarCliente()
    else:
        print("\nOpção Inválida!")
        raw_input("Enter para Continuar!")
    opcao = Menu()


    
# Finalizando o Programa:
conexao.close()
os.system("clear")