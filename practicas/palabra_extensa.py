#Dado los dos primeros párrafos del artículo Catedral de la Asunción en Jaén, 
#desarrolla un programa en Python que nos permita conocer la palabra con más letras en el texto.

texto = "La Santa Iglesia Catedral de la Asunción de la Virgen es la catedral "\
        "renacentista de Jaén, sede del obispado de Jaén, en la comunidad "\
        "autónoma de Andalucía, España. Se ubica en la Plaza de Santa María, "\
        "frente al Palacio Municipal y el Palacio Episcopal. La catedral "\
        "actual fue concebida en el siglo xvi para sustituir al anterior "\
        "templo gótico del siglo xv. La construcción se prolongó durante "\
        "varios siglos, a pesar de lo cual la idea original permaneció "\
        "intacta. Destacan la sala capitular y la sacristía, que son la obra "\
        "cumbre de Andrés de Vandelvira, y una de la obras más importantes "\
        "del renacimiento español. También es sobresaliente su fachada "\
        "principal, una de las principales obras del barroco español, "\
        "construida tras la consagración del templo en 1660. Igualmente, "\
        "destaca el coro neoclásico debido a su belleza y al gran número de "\
        "sitiales que lo convierten en uno de los más grandes de España. Una "\
        "vez finalizadas las obras del edificio, las mismas continuaron en "\
        "los siglos siguientes principalmente en la decoración interior y de "\
        "las capillas. Además, a consecuencia del terremoto de Lisboa de 1755 "\
        "fueron necesarias obras de consolidación en la fachada norte, así "\
        "como la construcción de la Iglesia del Sagrario."

def palabra_mas_extensa(t):
    pal_myr_len = ""

    lista_palabras = t.rsplit(" ")

    for pal in lista_palabras:
        if len(pal) > len(pal_myr_len):
            pal_myr_len = pal

    return pal_myr_len


palabra = palabra_mas_extensa(texto)
print("La palabra más extensa en los dos primeros párrafos del artículo\n"\
	  "Catedral de la Asunción de Jaén es {} y tiene {} carácteres".format(
	  	palabra, 
	  	len(palabra))
	  )
