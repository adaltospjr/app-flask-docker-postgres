import psycopg2


def connect():
    host = "db"
    dbname = "postgres"
    user = "postgres"
    password = "123456"
    port = "5432"

    conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )

    return conn


def consulta():
    conn = connect()

    cur = conn.cursor()

    cur.execute("select * from Produto")

    dados = cur.fetchall()
    conn.close()
    cur.close()

    return dados


def gravar(nome, categoria, preco):
    conn = connect()

    cur = conn.cursor()

    comando = """ INSERT INTO Produto (nome, categoria, preco) VALUES (%s,%s,%s)"""

    insert = (nome, categoria, preco)

    cur.execute(comando, insert)

    conn.commit()
    conn.close()
    cur.close()

    return "OK"


def create_table():
    sql = """
    CREATE TABLE Produto (
        nome varchar(200), 
        categoria varchar(200), 
        preco varchar(20)
    );
    """

    conn = connect()

    cur = conn.cursor()

    cur.execute(sql)

    conn.commit()
    conn.close()
    cur.close()


try:
    create_table()
except Exception as err:
    print(err)
