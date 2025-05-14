import random

palabras = ["gato", "perro", "elefante", "jirafa", "tigre"]
indice = random.randint(0, len(palabras) - 1)
palabra = palabras[indice]

letras_adivinadas = []
intentos = 6
palabra_oculta = "_" * len(palabra)

while intentos > 0 and "_" in palabra_oculta:
    print("\nPalabra:")
    for letra in palabra_oculta:
        print(letra, " ")
        print("\nPalabra:")
        print(" ".join(palabra_oculta))  # Ahora los guiones bajos están correctamente espaciados
        print(f"\nIntentos restantes: {intentos}")

    letra = input("Ingresa una letra (o escribe 'salir' para terminar): ").lower()

    if letra == "salir":
        print("Has salido del juego.")
        break

    if letra in palabra and letra not in letras_adivinadas:
        print("La letra está en la palabra.")
        letras_adivinadas.append(letra)
    else:
        print("La letra no está en la palabra.")
        intentos -= 1

    nueva_palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            nueva_palabra_oculta += letra
        else:
            nueva_palabra_oculta += "_"
    
    palabra_oculta = nueva_palabra_oculta

if "_" not in palabra_oculta:
    print(f"¡Ganaste! La palabra era: {palabra}")
elif letra != "salir":
    print(f"Has perdido. La palabra era {palabra}.")
    
    print("Gracias por jugar")
