import matplotlib.pyplot as plt
import numpy as np


class InterpoladorTf:

  def __init__(self):
    self.t_ref = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    self.tf_ref = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]

  def calcular_tf(self, temp):
    # Interpola Tf segun la tabla de la practica
    return float(np.interp(temp, self.t_ref, self.tf_ref))


class ClasificadorEstado:

  @staticmethod
  def clasificar(i):
    # Reglas de decision segun el valor de I
    if i < 0.40:
      return "Sin lluvia"
    elif i <= 0.60:
      return "Baja posibilidad"
    elif i <= 0.75:
      return "Lluvia probable"
    else:
      return "Lluvia"


class SimuladorClima:

  def __init__(self, humedad, nubosidad, temp, w_h=0.5, w_n=0.3, w_tf=0.2):
    self.humedad = humedad
    self.nubosidad = nubosidad
    self.temp = temp
    # Pesos de la formula (suman 1.0)
    self.w_h = w_h
    self.w_n = w_n
    self.w_tf = w_tf
    self.interpolador = InterpoladorTf()

  def calcular(self):
    # Normalizacion de datos
    H = np.array(self.humedad) / 100
    N = np.array(self.nubosidad) / 100

    # Obtener Tf
    Tf = np.array([self.interpolador.calcular_tf(t) for t in self.temp])

    # Formula del modelo I = w_h*H + w_n*N + w_tf*Tf
    I = (self.w_h * H) + (self.w_n * N) + (self.w_tf * Tf)

    # Clasificar estados
    estados = [ClasificadorEstado.clasificar(val) for val in I]

    return H, N, Tf, I, estados


class GraficaSimulacion:

  @staticmethod
  def mostrar_grafica_original(t, P, K=0.75):
    # -----------------------------
    # Gráfica para las practicas
    # -----------------------------
    plt.figure(figsize=(10, 5))
    plt.plot(t, P, label="Índice I (Modelo Original)")
    plt.axhline(
        y=K, linestyle="--", color="r", label=f"Umbral de lluvia (I = {K})"
    )
    plt.xlabel("Tiempo (Horas)")
    plt.ylabel("Índice de Lluvia (I)")
    plt.title("Simulación del modelo atmosférico")
    plt.grid(True)
    plt.legend()
    plt.show()

  @staticmethod
  def mostrar_grafica_ajustada(t, P, K=0.75):
    # -----------------------------
    # Gráfica para las practicas
    # -----------------------------
    plt.figure(figsize=(10, 5))
    plt.plot(t, P, label="Índice I (Modelo Ajustado)", color="orange")
    plt.axhline(
        y=K, linestyle="--", color="r", label=f"Umbral de lluvia (I = {K})"
    )
    plt.xlabel("Tiempo (Horas)")
    plt.ylabel("Índice de Lluvia (I)")
    plt.title("Simulación del modelo atmosférico (Ajustado)")
    plt.grid(True)
    plt.legend()
    plt.show()