compania = "FreeCodeCamp"

print("Aprende a programar  con" + compania)   #concatenacion
print("Aprende a programar con {}".format(compania)) #metodo format
print(f"Aprende a programar con { compania }") #f-string

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo:")
sustantivo_plural = input("Sustantivo (plural): ")

fun_lib = print(f"programar es tan {adj}! Siempre me emociona porque me encante {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!")

print(fun_lib)
