class Pizza():
    tamano = ""
    ingredientes = []

    def __init__(self, tamano, ingredientes):
        self.tamano = tamano
        self.ingredientes = ingredientes

    def preparar(self):
        print(f"Preparando pizza {self.tamano} con {self.ingredientes}")

pizza_hawaiana = Pizza("Grande", ["Piña", "Jamón", "Queso"])
pizza_hawaiana.preparar()

pizza_pepperoni = Pizza("Mediana", ["Pepperoni", "Queso"])
pizza_pepperoni.preparar()