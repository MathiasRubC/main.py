None
dict={
    "Causa":"Amigo o Compañero",
    "Pe": "Muletilla abreviada de pues al final de una oración",
    "Salado":"Persona con mala suerte",
    "Florear":"Decir mentiras paraobtener algo a cambio",
    "Jatear":"Dormir",
    "Manyado(a)":"Persona de clase alta o que se cree de esta misma"
}
for x in range(1,6):
    palabra= input("Escribe alguna palabra que no entiendas:")
    if palabra in dict.keys():
        print(palabra, "significa:", dict[palabra])
    else:
        print("Esa palabra no está en el diccionario")
