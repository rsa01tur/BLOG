import MySQLdb
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    db="cadastro"
)

def connectar(cpfa, nomea, oia, quala, telefonea):
    cursor = connection.cursor()
    ##adicionado do crud

    sql = "INSERT INTO pessoas (cpf, nome, oi, qual, telefone) VALUES (%s, %s, %s, %s, %s)"
    data = (cpfa,
    nomea, oia, quala, telefonea
    )

    cursor.execute(sql, data)
    connection.commit()
 