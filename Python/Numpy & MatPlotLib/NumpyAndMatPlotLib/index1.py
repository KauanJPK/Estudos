import numpy as np

class App:
    def __init__(self):
        self.arr = np.random.randint(100, size=(10))
        print(self.arr)
        print("Média:", self.calcular_media())
        print("Desvio Padrão:", self.calcular_desvio_padrao())
        print("Menor e Maior:", self.maioremenor()[0], self.maioremenor()[1])

    def calcular_media(self):
        return np.mean(self.arr)
    
    def calcular_desvio_padrao(self):
        return np.std(self.arr)
    
    def maioremenor(self):
        return np.min(self.arr), np.max(self.arr)
    
 