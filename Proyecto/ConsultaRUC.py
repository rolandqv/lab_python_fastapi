import http.client
from fileinput import filename

import urllib3
import shutil
from zipfile import ZipFile
from os import remove
from os import path
def consultaruc(ruc):
    # Consultamos el codigo Random
    conn = http.client.HTTPSConnection("e-consultaruc.sunat.gob.pe")
    payload = ''
    headers = {}
    conn.request("GET", "/cl-ti-itmrconsmulruc/captcha?accion=random", payload, headers)
    res = conn.getresponse()
    data = res.read()
    random =  data.decode("utf-8")
    #Consultamos Cookies
    conn1 = http.client.HTTPSConnection("e-consultaruc.sunat.gob.pe")
    payload = ''
    headers = {}
    conn1.request("GET", "/cl-ti-itmrconsmulruc/jrmS00Alias", payload, headers)
    res = conn1.getresponse()
    respuestadcookie = str(res.getheaders())
    pinicio1 = respuestadcookie.find("'Set-Cookie', '",0) + len("'Set-Cookie', '")
    pfin1 = respuestadcookie.find("; path=/; HttpOnly'")
    cookie = respuestadcookie[pinicio1:pfin1]
    pinicio2 = respuestadcookie.find("'Set-Cookie', '",pinicio1) + len("'Set-Cookie', '")
    pfin2 = respuestadcookie.find("; Path=/; Domain=.e-consultaruc.sunat.gob.pe'")
    cookie = cookie + "; " + respuestadcookie[pinicio2:pfin2]
    #Consulta RUC
    conn2 = http.client.HTTPSConnection("e-consultaruc.sunat.gob.pe")
    payload = "accion=consManual&selRuc=" + ruc + "&random=" + random
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '' + cookie + ''
    }
    #print(headers)
    conn2.request("POST", "/cl-ti-itmrconsmulruc/jrmS00Alias", payload, headers)
    res2 = conn2.getresponse()
    #data2 = res2.read()
    data2 = str(res2.read())
    #return data2
    pinicio3 =  data2.find("https://www.sunat.gob.pe/cl-at-framework-unloadfile/descargaArchivoAlias",0)
    pfin3 = data2.find('" target=',pinicio3)
    pinicio4 =  data2.find('_blank">',pfin3) + len('_blank">')
    pfin4 = data2.find('</a>',pinicio4)
    filename = data2[pinicio4:pfin4]
    #Descargamos el archivo
    #return data2[pinicio3:pfin3]
    print(data2[pinicio3:pfin3])
    url = data2[pinicio3:pfin3]
    c = urllib3.PoolManager()
    #print(filename)
    #filename = "prueba.zip"
    with c.request('GET', url, preload_content=False) as respuesta, open(filename, 'wb') as archivo_salida:
        shutil.copyfileobj(respuesta, archivo_salida)
    #Extraemos el ZIP
    test_file_name = filename
    print(filename)
    with ZipFile(test_file_name, 'r') as zip:
        zip.extractall()
    # Eliminamos el ZIP
    if path.exists(filename): remove(filename)
    # Leemos el txt
    f = open(filename.replace("zip","txt"), "r")
    for linea in f:
        if linea.find(ruc) == 0: datosruc = linea.split("|")
    f.close()
    if path.exists(filename.replace("zip","txt")): remove(filename.replace("zip","txt"))
    print(datosruc[1]) #Razon Social
    print(datosruc[4]) #Nombre Comercial
    print(datosruc[5]) #Estado
    print(datosruc[6]) #Condicion
    print(datosruc[12]) #Direccion
    return datosruc
print(consultaruc("20405708290"))