print("*"*10)
codigo = input("Ingresar código: ")
nota_1 = input("nota 1 :")
nota_2 = input("nota 2 :")
nota_3 = input("nota 3 :")
nombre = input("nombre: ")
print("*"*10)

nota_final = ( float(nota_1) + float(nota_2) + float(nota_3) )/ 3
nota_final = round(nota_final,2)
if nota_final >= 3.2:
    mensaje = "aprobado"
else:
    mensaje = "reprobado"
print(f"La nota final de {nombre} es: {nota_final}, estado {mensaje}")
print("*"*10)