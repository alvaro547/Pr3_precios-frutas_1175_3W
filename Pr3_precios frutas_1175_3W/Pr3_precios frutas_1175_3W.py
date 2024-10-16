print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Definimos un diccionario que contiene los precios de las frutas.
precios_frutas = {
    'manzana': 2.5,  # precio por kilo
    'banana': 1.2,
    'naranja': 3.0,
    'fresa': 4.5
}

# Pedimos al usuario que ingrese una fruta.
fruta = input("Introduce el nombre de una fruta (manzana, banana, naranja, fresa): ").lower()

# Pedimos al usuario que ingrese el número de kilos.
kilos = float(input("Introduce el número de kilos: "))

# Verificamos si la fruta está en el diccionario.
if fruta in precios_frutas:
    # Si está, calculamos el precio total.
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: ${precio_total:.2f}")
else:
    # Si no está, mostramos un mensaje informando que la fruta no está en el diccionario.
    print("La fruta no está en el diccionario.")
