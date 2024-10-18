import argparse


if __name__ == "__main__":
    
    description = """Ejemplo de uso:
        + Escaneo basico:
            -target 127.0.0.1
        + Indica un puerto especifico:
            -target 127.0.0.1 -port 21
        + Indica una lista de puertos:
            -target 127.0.0.1 -port 21,22"""
    parser = argparse.ArgumentParser(description='Port Scanning', epilog=description, #argumento para dar descripcion del script y sus parametros
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument("-target", metavar='TARGET', dest="target", #Parametro de target
                        help="target to scan", required=True)
    parser.add_argument("-ports", dest="ports", #Parametro de puertos con valor de default
                        help="Please specify the target ports separated by coma[80,8080 by default]", 
                        default = "80,8080")
    params = parser.parse_args() #agrega los parametros
    portlist = params.ports.split(',') #crea una lista con los puertos con split
    for i in range(len(portlist)): #itera y separa los puertos en enteros
        print("Puerto:", portlist[i])
        portlist[i] = int(portlist[i])
    print(params) #imprime los parametros que se dieron entrada