import random
import csv

POBLACION = 100
INFECTADOS_INICIALES = 5
SUSCEPTIBLES_INICIALES = POBLACION - INFECTADOS_INICIALES
BETA = 0.30
GAMMA = 0.10
PASOS = 100

def simular_sir():
    poblacion = [1] * INFECTADOS_INICIALES + [0] * SUSCEPTIBLES_INICIALES
    resultados = []
    
    for paso in range(PASOS + 1):
        s = poblacion.count(0)
        i = poblacion.count(1)
        r = poblacion.count(2)
        
        resultados.append([paso, s, i, r])
        
        if i == 0:
            continue
            
        prob_contagio = (BETA * i) / POBLACION
        nueva_poblacion = poblacion.copy()
        
        for idx in range(POBLACION):
            if poblacion[idx] == 0:
                if random.random() < prob_contagio:
                    nueva_poblacion[idx] = 1
            elif poblacion[idx] == 1:
                if random.random() < GAMMA:
                    nueva_poblacion[idx] = 2
                    
        poblacion = nueva_poblacion
        
    with open("resultados_python.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["tiempo", "susceptibles", "infectados", "recuperados"])
        writer.writerows(resultados)
        
    print("¡Simulación en Python finalizada con éxito! Archivo 'resultados_python.csv' generado.")

if __name__ == "__main__":
    simular_sir()