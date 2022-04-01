#     """1. Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y
# “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos.
#     """
# 2. Agregarle a la clase anterior un constructor que reciba nombre y edad.
# 3. Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.
# 4. Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la
# del objeto actual.
# 5. Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad
# mayor.

class persona():
    def __init__(self,n,e):
        self.nombre=n
        self.edad=e
    
    #metodos
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        return False
    def __gt__(self,persona):
        return self.edad > persona.edad

    def es_mayor_que(self,persona):
        if self.edad > persona.edad:
            return "{} es mayor que {}".format(self.nombre,persona.nombre)
        else:
            return "{} es menor que {}".format(self.nombre,persona.nombre)
    #setters /getters
    def set_nombre(self,nombre):
        self.nombre = nombre
        print("Ahora el tipo se llama {}".format(nombre))
    def set_edad(self,edad):
        self.edad = edad
        print("AHora tenes {} años".format(edad))

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad
    def get_mayor(self,persona):
        if self > persona:
            return "El mayor es {}".format(self.nombre)
        else:
            return "El mayor es {}".format(persona.nombre)

tipo1 = persona("Paco",15)
tipo2 = persona("Jorge",60)


print(tipo1.nombre,tipo1.edad,tipo1.es_mayor_de_edad())
print(tipo2.nombre, tipo2.edad,tipo2.es_mayor_de_edad())
print(tipo1.es_mayor_que(tipo2))
print(tipo1.get_mayor(tipo2))