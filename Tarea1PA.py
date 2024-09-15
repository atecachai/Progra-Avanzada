#clase que me entrega cantidad de maneras de moverme de A a B
# in: Dimensiones (NxM)
# out: Cantidad de maneras de llegar de A a B, graficos con el tiempo de demora para distintos casos, y los tiempos de demora

import time
import matplotlib.pyplot as plt

class Grilla:
    def __init__(self, N, M):
        self.ancho = N
        self.largo = M
        self.tiempoejecucion = []
    
    @staticmethod    
    def tiempodemora(funcion):
        def medidor(self, *args, **kwargs):
            inicio = time.time()
            resultado = funcion(self, *args, **kwargs)
            fin = time.time()
            tiempo_ej = float(fin - inicio)
            self.tiempoejecucion.append(tiempo_ej)
            return resultado
        return medidor

    #primer metodo para calcular la cantidad de caminos posibles usando la intiucion de combinatoria
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n-1)
    @tiempodemora
    def caminos_1(self):
        num = self.factorial(self.ancho+self.largo)
        den = self.factorial(self.ancho)*self.factorial(self.largo)
        return (num/den) #cantidad de caminos
    
    #segundo metodo para calcular la cantidad de caminos posibles
    #cada item es un vertice de la grilla
    @tiempodemora
    def caminos_2(self):
        grid = [[0 for i in range(0,self.ancho+1)] for i in range(0,self.largo+1)] #debemos agregar 1 fila y columna mas debido a que en este caso, esta matriz simboliza estar dentro de alguna celda de la grilla, y no en su esquina, como en el caso de combinatoria
        
        for i in range(0, self.largo+1):
            grid[i][0] = 1
        for i in range(0, self.ancho+1):
            grid[0][i] = 1
        
        for i in range(1, self.largo+1):
            for j in range(1, self.ancho+1):
                grid[i][j] = grid[i][j-1]+grid[i-1][j]
        
        return float(grid[self.largo][self.ancho]) #cantidad de caminos
    
   
    def ejecutar(self, metodo): #metodo para seleccionar el metodo
        caminos = [] #cantidad de caminos para cada grilla de tamaño NxN
        for i in range(1,100):
            self.ancho = i
            self.largo = i
            if metodo == '1':    
                caminos.append(self.caminos_1())
            if metodo == '2':
                caminos.append(self.caminos_2())
        
    def grafico(self,filename):
        plt.figure(figsize=(8,6))
        plt.title('Tiempo de ejecución para distintos tamaños de grilla')
        plt.xlabel('Tamaño de la Grilla (NxN)')
        plt.ylabel('Tiempo de Ejecución (segundos)')
        plt.plot(self.tiempoejecucion,label='Segundos')
        plt.legend()
        plt.grid(True)
        #plt.savefig(filename)  #opcion para guardar imagenes en PNG
        plt.savefig(filename, format="svg")
        plt.show()


#codigo para calcular con el metodo 1 y 2
clase = Grilla(1,1) 
metodo = '1'
clase.ejecutar(metodo)
clase.grafico(metodo)
metodo = '2'
clase.ejecutar(metodo)
clase.grafico(metodo)
