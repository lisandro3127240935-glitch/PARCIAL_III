import pymysql

try:
    conexion = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_estudiantes'
    )
    cursor = conexion.cursor()
except Exception as e:
    print("por el momento no es posible conectarse con la base de datos intentelo mas tarde")
    conexion = None
    cursor = None