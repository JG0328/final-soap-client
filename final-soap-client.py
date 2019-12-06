from zeep import Client

client = Client('http://localhost:7777/ws/UrlWebService?wsdl')

while True:
    print('1 - Listado de URL dado un usuario')
    print('2 - Acortar URL, dado un usuario')
    print('3 - Salir')
    op = int(input('Elija la opcion deseada: '))

    if(op == 1):
        username = input('Introduzca el nombre de usuario: ')
        result = client.service.getUrlsByUser(username)
        # print(result)
        for url in result:
            i = 1
            print("\nURL #{0}. Corta: {1}. Original: {2}. Creada: {3}. Stats: ".format(
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
        result = client.service.getShortUrl(url, username)
        print("URL creada exitosamente! Informacion: ")
        print("Acortada: {0}. Original: {1}. Creada: {2}. Imagen Base 64: {3}".format(
            result['shortVersion'], result['originalVersion'], result['createdAt'], result['imageBase']))
    elif(op == 3):
        break
