#Si utilizamos un loop para recorrer un diccionario, el for va a recorrer las llaves del diccionario y podemos utilizar las llaves para acceder a los valores.

some_dict = {
    "name": "valentina",
    "lastname": "ojeda",
    "weigth": 80,
    "heigth":1.60
    }
for key in some_dict:
   print(key, some_dict[key])