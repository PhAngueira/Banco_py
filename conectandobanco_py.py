import Oracledb

def getConnection():
    try:
        connection = Oracledb.connect(user = "rm$##@$", password = "$$$$%", host="oracle.fiap.com.br", port = "1521", service_name = "orcl")
    except Exception as e:
        print(f'Erro ao obter a conexâo: {e}')
    return connection

def select():
    connection = getConnection()
    cursor = connection.cursor()
    sql_query = "SELECT * from CEO_DETAILS "
    cursor.execute(sql_query)
    for result in cursor:
        print(result)
    connection.close()
    cursor.close()

def insert():
    connection = getConnection()
    cursor = connection.cursor()
    sql_query = "INSERT into CEO_DETAILS values('Steve', 'Jobs', 'Apple', '50')"
    cursor.execute(sql_query)
    connection.commit()
    print("CEO adicionado com sucesso!")

def update():
    try:
         connection = getConnection()
         cursor = connection.cursor()
         sql_query = "UPDATE CEO_DETAILS set AGE = '55' WHERE LAST_NAME = 'Gates')"
         cursor.execute(sql_query)
         connection.commit()
         print("CEO details updated")
    except Exception as e:
        print(f"Something went wrong {e}")

def delete():
    connection = getConnection()
    cursor = connection.cursor()
    sql_query = "DELETE from CEO_DETAILS where FIRT_NAME = 'Steve')"
    cursor.execute(sql_query)
    connection.commit()
    print('CEO removed!')

def close_connection(connection):
    connection.close()

#Principal
    conn= getConnection()
    print(f'Conexao: {getConnection().version}')
    print('Mostrando os dados da tabela CEO_DETAILS:')
    select()
    insert()
    select()
    update()
    select()
    delete()
    select()
    close_connection(conn)