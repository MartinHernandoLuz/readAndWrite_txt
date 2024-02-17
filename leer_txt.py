def leerArchivoTXT(documento = "nuevo_documento"):
    a = True
    with open(f"{documento}.txt",'w', encoding="UTF-8") as archivo:
        while a == True:
            entrada = input("quieres escribir en el documento?, responde SI o NO: ")
            entrada = entrada.lower()
            if entrada == 'si':
                texto = input("escribe lo que quieres guardar: ")
                archivo.writelines([f'{texto}\n'])
                print("listo, archivo guardado...")
                print("de nuevo: ")
            else:
                a = False
        

