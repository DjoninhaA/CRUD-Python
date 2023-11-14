# import mysql.connector
#
# conexao = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='bdcrud',
# )


print("_________________________________________"
      "\n___________ Seja Bem vindo! ______________"
      "\n__________________________________________")


from functions import CriaElementos
def exibir_menu():
    print("Menu:")
    print("1. Criar elemento")
    print("2. Ler elemento")
    print("3. Atualizar elemento")
    print("4. Deletar elemento")
    print("5. Sair")

def menu():
    while True:
        exibir_menu()
        escolha = input("Escolha uma das opções acima: ")

        if escolha == "1":
            CriaElementos()
        elif escolha == "2":
            ler_elemento()
        elif escolha == "3":
            atualizar_elemento()
        elif escolha == "4":
            deletar_elemento()
        elif escolha == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()



# CREATE
# nome_produto = "pera"
# valor = 2
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit()

# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute((comando))
# resultado = cursor.fetchall()
# print(resultado)

# UPDATE
# nome_produto = "todynho"
# valor =6
# comando = f'UPDATE vendas SET valor = "{valor}" WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

# DELETE
# nome_produto = "todynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()
