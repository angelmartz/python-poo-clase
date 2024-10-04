from abc import ABC, abstractmethod

class Pizza(ABC):

    def __init__(self, tamano):
        self._tamano = tamano

    @abstractmethod
    def preparar(self):
        pass

    def hornear(self):
        print(f"Horneando pizza {self._tamano} por 15 minutos a 180 grados")
    
    def cortar(self):
        print(f"Cortando pizza {self._tamano} en 8 porciones")

    def empacar(self):
        print("Empacando pizza en caja")

class PizzaHawaiana(Pizza):
    def __init__(self, tamano):
        super().__init__(tamano)
        self.__ingredientes = ["Piña", "Jamón", "Queso"] # Encapsulamiento
    
    def preparar(self): # Contrato con la clase padre, se debe implementar
        print(f"Preparando pizza de {self._tamano} con {'. '.join(self.__ingredientes)}.")

class PizzaPepperoni(Pizza):
    def __init__(self, tamano):
        super().__init__(tamano)
        self.__ingredientes = ["Pepperoni", "Queso"] # Encapsulamiento

    def preparar(self):
        print(f"Preparando pizza de {self._tamano} con {', '.join(self.__ingredientes)}.")


class Pizzeria:
    def order_pizza(self, tipo, tamano):
        if tipo == "Hawaiana":
            pizza = PizzaHawaiana(tamano)
        elif tipo == "Pepperoni":
            pizza = PizzaPepperoni(tamano)
        else:
            raise ValueError("Tipo de pizza no disponible")
        
        pizza.preparar()
        pizza.hornear()
        pizza.cortar()
        pizza.empacar()


pizza_hawaiana = PizzaHawaiana("Grande")
pizza_hawaiana.preparar()
pizza_hawaiana.hornear()
pizza_hawaiana.cortar()
pizza_hawaiana.empacar()

pizza_pepperoni = PizzaPepperoni("Mediana")
pizza_pepperoni.preparar()
pizza_pepperoni.hornear()
pizza_pepperoni.cortar()
pizza_pepperoni.empacar()


pizzeria = Pizzeria()
print("Pedido 1: Pizza Hawaiana")
pizzeria.order_pizza("Hawaiana", "Grande")

print("")

print("Pedido 2: Pizza Pepperoni")
pizzeria.order_pizza("Pepperoni", "Mediana")

print("")

print("Pedido 3: Pizza de Pepperoni Chica")
pizzeria.order_pizza("Pepperoni", "Chica")

print("")
print("Pedido 4: Pizza de Hawaiana Mediana")
pizzeria.order_pizza("Hawaiana", "Mediana")
