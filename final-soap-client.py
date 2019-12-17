from zeep import Client

client = Client('http://app2.unwanted.software:7777/ws/UrlWebService?wsdl')

while True:
    print('1 - Listado de URL dado un usuario')
    print('2 - Acortar URL, dado un usuario')
    print('3 - Salir')
    op = int(input('Elija la opcion deseada: '))

    if(op == 1):
        username = input('Introduzca el nombre de usuario: ')
        password = input('Introduzca la contraseña: ')
        result = client.service.getUrlsByUser(username)
        i = 1
        for url in result:
            print("\nURL #{0}. Corta: https://app2.unwanted.software/s/{1}. Original: {2}. Creada: {3}. Stats: ".format(
                i, url['shortVersion'], url['originalVersion'], url['createdAt']))
            j = 1
            print("")
            for info in url['myInfos']:
                print("Acceso #{0}. Fecha: {1}. Navegador: {2}. O.S.: {3}. IP: {4}".format(
                    j, info['date'], info['browser'], info['os'], info['ip']))
                j += 1
            i += 1
    elif(op == 2):
        url = input('Introduzca la URL a acortar: ')
        username = input('Introduzca el nombre de usuario: ')
        password = input('Introduzca la contraseña: ')
        result = client.service.getShortUrl(url, username)
        print("URL creada exitosamente! Informacion: ")
        print("Acortada: https://app2.unwanted.software/s/{0}. Original: {1}. Creada: {2}. Imagen Base 64: {3}".format(
            result['shortVersion'], result['originalVersion'], result['createdAt'], result['imageBase']))
    elif(op == 3):
        break
