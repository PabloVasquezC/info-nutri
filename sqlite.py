import sqlite3

def eliminar_tabla(tabla):
    try:
        conexion = sqlite3.connect("BD.db")
        cursor = conexion.cursor()

        # Intenta ejecutar una consulta SQL para obtener los datos de la tabla
        cursor.execute(f"DROP TABLE {tabla}")
        
        # Guarsar cambios en Base de Datos
        conexion.commit()
        
        print(f"Se elimino correctamente la tabla {tabla}")

        # Cierra la conexión con la base de datos
        conexion.close()


    except sqlite3.OperationalError:
        print(f"Lo sentimos, la tabla '{tabla}' no existe en la Base de Datos.")
    
# def mostrar_tabla(tabla):
#     try:
#         conexion = sqlite3.connect("BD.db")
#         cursor = conexion.cursor()

#         # Intenta ejecutar una consulta SQL para obtener los datos de la tabla
#         cursor.execute(f"SELECT * FROM {tabla}")

#         # Obtén los resultados de la consulta
#         resultados = cursor.fetchall()

#         # Cierra la conexión con la base de datos
#         conexion.close()
#         print("   ID   Nombre                 Precio                Temporada")
#         print("----------------------------------------------------------------------------")
#         # Imprime los resultados
#         for fila in resultados:
#             print(f"|| {fila[0]:<2}|| {fila[1]:<20}|| {fila[2]:<20}|| {fila[3]:<20}||")

#     except sqlite3.OperationalError:
#         print(f"Lo sentimos, la tabla '{tabla}' no existe en la Base de Datos.")


# conexion = sqlite3.connect('BD.db')
# cursor = conexion.cursor()
# cursor.execute("UPDATE 'FRUTOS_SECOS' SET 'Kcal./100Gr.' = 662 WHERE NOMBRE = 'PISTACHOS'")
# print(cursor.fetchall())





# # # tabla = 'frutas'

# # # nombre_columna = 'KCAL'
# # # tipo_de_dato = 'INTEGER'
# # sentencia_sql = f"select * from frutas"


# # cursor.execute(sentencia_sql)
# # print(cursor.fetchall())
# conexion.commit()
# conexion.close



     

def mostrar_tabla(tabla):
    try:
        # Conectar a la base de datos
        with sqlite3.connect("BD.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute(f"SELECT * FROM {tabla}")
            resultados = cursor.fetchall()

            if not resultados:
                print(f"No se encontraron registros en la tabla '{tabla}'.")
            else:
                # Imprimir encabezados
                print("{:<5} {:<30} {:<10} {:<10} {:<10} ".format("||ID", " || Nombre", "   || Precio", "   || Temporada", "|| Kcal./100Gr."))
                print("-" * 80)
                # print("{:<5} {:<20} {:<10} {:<20}".format("||ID", " ||Nombre", "   ||Precio", "    ||Temporada"))
                # print("-" * 80)
                for fila in resultados:
                    print("||{:<5}|| {:<30}|| {:<10}|| {:<10}|| {:<10}|| ".format(fila[0], fila[1], fila[2], fila[3], fila[4]))

    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
        print(f"Lo sentimos, la tabla '{tabla}' no existe en la Base de Datos.")

def mostrar_tabla_por_precio(tabla):
    try:
        conexion = sqlite3.connect("BD.db")
        cursor = conexion.cursor()

        # Intenta ejecutar una consulta SQL para obtener los datos de la tabla
        cursor.execute(f"SELECT * FROM {tabla} ORDER BY PRECIO DESC")

        # Obtén los resultados de la consulta
        resultados = cursor.fetchall()

        # Cierra la conexión con la base de datos
        conexion.close()
        print("   ID   Nombre                 Precio                 Temporada")
        print("----------------------------------------------------------------------------")
        # Imprime los resultados
        for fila in resultados:
            print(f"|| {fila[0]:<2}|| {fila[1]:<20}|| {fila[2]:<20}|| {fila[3]:<20}||")

    except sqlite3.OperationalError:
        print(f"Lo sentimos, la tabla '{tabla}' no existe en la Base de Datos.")

def insertar_registro(tabla, nombre, precio, temporada):
    nombre = nombre.upper()
    temporada = temporada.upper()
    
    try:
        conexion = sqlite3.connect("BD.db")
        cursor = conexion.cursor()

        # Intenta ejecutar una consulta SQL para obtener los datos de la tabla
        cursor.execute(f"INSERT INTO {tabla} (nombre, precio, temporada) VALUES (?, ?, ?)", (nombre, precio, temporada))
        
        # Guarsar cambios en Base de Datos
        conexion.commit()
        
        print(f"el registro se inserto con exito en la tabla {tabla}")

        # Cierra la conexión con la base de datos
        conexion.close()


    except sqlite3.OperationalError:
        print(f"Lo sentimos, la tabla '{tabla}' no existe en la Base de Datos.")

def eliminar_registro_por_nombre(tabla, nombre):
    nombre = nombre.upper()
    try:
        conexion = sqlite3.connect("BD.db")
        cursor = conexion.cursor()
        
        cursor.execute(f"DELETE FROM {tabla} WHERE NOMBRE='{nombre}'")
        
        # Obtén el número de filas afectadas por la operación DELETE
        filas_afectadas = cursor.rowcount
        
        # Guardar cambios en la Base de Datos
        conexion.commit()
        
        if filas_afectadas > 0:
            print(f"Registro eliminado.")
        else:
            print(f"No se encontró el registro en la tabla.")

        
        conexion.close()
        
    except sqlite3.OperationalError:
        print(f"Lo sentimos, la tabla {tabla} no existe en la Base de Datos.")  
        
# def eliminar_registro_por_id(tabla, id):
#     try:
#         conexion = sqlite3.connect("BD.db")
#         cursor = conexion.cursor()
        
#         cursor.execute(f"DELETE FROM {tabla} WHERE ID='{id}'")
        
#         # Obtén el número de filas afectadas por la operación DELETE
#         filas_afectadas = cursor.rowcount
        
#         # Guardar cambios en la Base de Datos
#         conexion.commit()
        
#         if filas_afectadas > 0:
#             print(f"Registro eliminado.")
#         else:
#             print(f"No se encontró el registro en la tabla.")

        
#         conexion.close()
        
#     except sqlite3.OperationalError:
#         print(f"Lo sentimos, la tabla {tabla} no existe en la Base de Datos.")  

def eliminar_registro_por_id(tabla, id):
    try:
        # Conectar a la base de datos
        with sqlite3.connect("BD.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute(f"DELETE FROM {tabla} WHERE ID = ?", (id,))
            filas_afectadas = cursor.rowcount
            
            if filas_afectadas > 0:
                print("Registro eliminado.")
            else:
                print("No se encontró el registro en la tabla.")
    
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")

def ejecutar_query(query):
    query = query.upper()
    try:
        conexion = sqlite3.connect("BD.db")
        cursor = conexion.cursor()
        
        cursor.execute(f"{query}")
        
        # Guardar cambios en la Base de Datos
        conexion.commit()

        conexion.close()
        
    except sqlite3.OperationalError:
        print(f"Lo sentimos, la ejecucion de la query '{query}' no es valida .")  
    









