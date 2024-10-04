class Pizza():
    tamano = "" # Atributo
    ingredientes = [] # Atributo

    def __init__(self, tamano, ingredientes): # Contructor de la clase Pizza
        self.tamano = tamano
        self.ingredientes = ingredientes

    def preparar(self): # Método
        print(f"Preparando pizza {self.tamano} con {self.ingredientes}")
    
    def hornear(self):
        print("Horneando pizza por 15 minutos a 180 grados")

    def cortar(self):
        print("Cortando pizza en 8 porciones")
    
    def empacar(self):
        print("Empacando pizza en caja")

# Objeto Pizza Hawaiana
pizza_hawaiana = Pizza("Grande", ["Piña", "Jamón", "Queso"])
pizza_hawaiana.preparar()

# Objeto Pizza Pepperoni
pizza_pepperoni = Pizza("Mediana", ["Pepperoni", "Queso"])
pizza_pepperoni.preparar()