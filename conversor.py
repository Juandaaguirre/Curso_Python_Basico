def conversor (tipo_moneda , valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_moneda + " tienes?: ")
    pesos = float (pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")
menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor('colombianos', 4800)
elif opcion == 2:
    conversor('argentinos', 300)
elif opcion == 3:
    conversor('mexicanos', 45)
else:
    print('Ingrese una opción valida ')
