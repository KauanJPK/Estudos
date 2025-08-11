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
    
    def matrizes(self):
        m1 = np.random.randint(100, size=(3, 3))
        m2 = np.random.randint(100, size=(3, 3))
        print("Matriz 1:\n", m1)
        print("Produto da matriz 1:\n", np.dot(m1, m1))
        print("Matriz 2:\n", m2)
        print("Produto da matriz 2:\n", np.dot(m2, m2))
        print("Produto das Matrizes:\n", np.dot(m1, m2))


    def valoresespacados(self):
        self.arr = np.linspace(0, np.pi, 50)
        print("Valores Espaçados:\n", self.arr)
        print("Seno dos Valores Espaçados:\n", np.sin(self.arr))
        print("Cosseno dos Valores Espaçados:\n", np.cos(self.arr))
App()