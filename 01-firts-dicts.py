#Un diccionario es como una lista pero más general, es decir, en un diccionario los indices pueden ser casi de cualquier tipo. 
#En los diccionarios los indíces son llamados (llaves) o en inglés (keys) y tiene asociado sus respectivos valores.
#NOTA: Los diccionarios son con llaves {} y las listas con corchetes []
#Ejemplo:
english_to_spanish = {} #Las llaves solo es para declarar y luego se usan corchetes []

empty_dict = {"mochi":"mailen"} #Crea un diccionario vacío
print(empty_dict)
english_to_spanish = {"one":"uno", "two":"dos"}

#Los elementos se agregan en pares, es decir, llave-valor

english_to_spanish["hello"] = "hola"
english_to_spanish["bye"] = "chao"

print(english_to_spanish)


#Para acceder a el valor de una llave en específico usamos la notación con []
print(english_to_spanish["two"])

#El largo de un diccionario se puede obtener con la función len(), igual que con las listas 
print(len(english_to_spanish)) #=> 4 
print(len(empty_dict))
