

codigo_producto = int(input("Ingresar codigo del producto: "))
nombre_producto = (input("Nombre del producto: "))
cantidad = int(input("Cantidad a comprar: "))
valor_unitario = int(input("Valor unitario del producto sin iva: "))

valor_producto = cantidad*valor_unitario
iva = 0.19*valor_producto
valor_final_producto = valor_producto + iva

print(f"""
Bienvenidos a la tienda market

factura de compra
============

codigo       nombre      cantidad  valor unitario       iva       valor final
{codigo_producto},    {nombre_producto},            {cantidad},       ${valor_unitario},        ${iva},             ${valor_final_producto}


""")


