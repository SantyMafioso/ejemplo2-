#Valor de un vehiculo
int_nacionales = 30000000
int_importados = 20000000
int_control = 0
import os 
os.system ('cls')
while int_control == 0:
        int_cliente = int(input('ingrese su edad: ')) 
        if int_cliente >= 18:
            print('Puede continuar con el --REGISTRO-- ')
            print('Y tambien a obtener infromacion sobre los --VEHICULO--')
            enter = print('presione <ENTER> para continuar ')
            os.system ('cls')
        else:
            print('usted no puede continuar con el --REGISTRO--')
            print('Y tampoco a obtener infromacion sobre los --VEHICULOS--')
            break
            os.system('cls')

        print('---SELECCIONE PARA SEGUIR---')
        int_opcion = int(input('\n1. Registro \n2. Informacion de vehiculos \n3. salir \n->'))
        enter = print('Presione <ENTER> para continuar: ')
        os.system ('cls')

        if int_opcion == 1:    
            str_nombre = input('nombre: ')
            str_documentacion = input('documentacion: ')
            str_numero = input('numero: ')
            str_correo = input('correo: ')
            print('Usted se a registrado CORRECTAMENTE')
            enter = print('Presione <ENTER> para volver a atras: ')
            os.system('cls')

        if int_opcion == 2:
            print('---BIENVENIDO A LA PARTE DE INFROMACION---')
            int_tipvehiculos = int(input('\n1. Nacionales \n2. Importados \n3. Salir \n-> '))
            os.system ('cls')
            if int_tipvehiculos == 1:
                int_autosnacio = int(input('\n1. Chevrolet \n2. Mazda \n3. Renault \n4. Kia \n5. SALIR \n-> '))
                int_descuento = int_nacionales * 0.15
                int_total = int_nacionales - int_descuento 
                print('--FACTURA--')
                print('nombre', str_nombre)
                print('documentacion', str_documentacion)
                print('numero', str_numero)
                print('correo', str_correo)
                print( 'se le aplico un descuento de:', int_descuento)
                print('total a pagar es: ', int_total)

            if int_tipvehiculos == 2:
                int_autosimport = int(input('\n1. Ferrari \n2. Lamborghini \n3. BMW \n4. Kawasaki \n5. Salir \n-> '))
                int_arancel = int_importados * 0.35
                int_impuesto = int_importados * 0.15
                int_total = int_importados + int_arancel + int_impuesto
                print('--FACTURA--')
                print('nombre', str_nombre)
                print('documentacion', str_documentacion)
                print('numero', str_numero)
                print('correo', str_correo)
                print('Se le aplico un aumento de:', int_arancel + int_impuesto)
                print('total a pagar es: ', int_total)
                        
                


