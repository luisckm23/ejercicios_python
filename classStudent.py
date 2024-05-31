class Student:
    def __init__(self, name, house, ):
        if not name:
            raise ValueError("Missing name")
        self.name = name #Estamos asignando los valores de los parámetros nanme, house a las instancias self.name, self.house para llamar a estos objetos
        self.house = house
        

    def __str__(self):
        return f"{self.name} from {self.house}" #Hacemos la sobrecarga para el objeto student que imprimimos en def main()
    
    #Getter es una funcion de la clase que permite obtener el valor de un atributo de un objeto
    @property #Decorator le indica a Python tratar el metodo como un getter
    def house(self):
        return self._house
    
    #Setter es una funcion de la clase que permite establecer el valor de un atributo de un objeto
    @house.setter #
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house
    #Los metodos getter y setter ayudan al control de acceso, validacion de datos y encapsulacion
   

def main():
    student = get_student() #Declaramos la variable para posteriormente traer los valores de la funcion get_student
    print(student) #aquí imprimimos la sobrecarga del método __str__ 
    


def get_student(): #en esta funcion obtenemos name, house y patronus por el usuario
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) #Esta línea crea una nueva instancia de la clase Student utilizando los valores ingresados por el usuario. 

if __name__ == "__main__": #Esta condición verifica si el archivo se está ejecutando directamente.
    main()
