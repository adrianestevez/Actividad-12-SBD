import mysql.connector 

bd = mysql.connector.connect(user='adrian', password= '12345678', database='mascotas')

cursor= bd.cursor()

while True:
    print('1.- Agregar veterinaria')
    print('2.- Mostrar veterinarias ')
    print('0.- Salir ')
    op = input()

    if op == '1':
        cant_duennos = input('Cantidad de dueños: ')
        cant_mascotas = input('Cantidad de mascotas: ')
        correo = input('Correo: ')
        telefono = input('Telefono: ')

        consulta = "INSERT INTO veterinaria (cant_duennos, cant_mascotas, correo, telefono)" \
                    "VALUES (%s, %s, %s, %s)"
        
        cursor.execute(consulta, (cant_duennos,cant_mascotas, correo, telefono))
        bd.commit()

        if cursor.rowcount:
            print("Se agrego la veterinaria ")
        
        else:
            print("Error al agregar la veterinaria")        
    elif op == '2':
        consulta = "SELECT * FROM veterinaria"
        cursor.execute(consulta)

        for row in cursor.fetchall():
            print('Id: ', row[0])
            print('Cantidad de Dueños: ', row[1])
            print('Cantidad de Mascotas: ', row[2])
            print('Correo: ', row[3])
            print('Telefono: ', row[4])


    elif op == '0':
        break;

        
