from modelo import GraficaSimulacion, SimuladorClima

# Datos de entrada de la guia
horas = [
    '06:00',
    '08:00',
    '10:00',
    '12:00',
    '14:00',
    '16:00',
    '18:00',
    '20:00',
    '22:00',
]
humedad = [65, 70, 68, 60, 75, 85, 92, 88, 80]
nubosidad = [40, 50, 45, 30, 70, 85, 95, 90, 75]
temp = [14, 16, 18, 22, 20, 18, 16, 17, 15]

if __name__ == '__main__':
  # 1. Modelo Original (0.5H + 0.3N + 0.2Tf)
  sim_orig = SimuladorClima(humedad, nubosidad, temp, 0.5, 0.3, 0.2)
  H, N, Tf, I_orig, est_orig = sim_orig.calcular()

  # 2. Modelo Ajustado (0.4H + 0.4N + 0.2Tf)
  sim_ajust = SimuladorClima(humedad, nubosidad, temp, 0.4, 0.4, 0.2)
  _, _, _, I_ajust, est_ajust = sim_ajust.calcular()

  # Impresion de la Tabla del Modelo Original
  print('=== TABLA MODELO ORIGINAL (0.5H + 0.3N + 0.2Tf) ===')
  print('Hora | H | N | Tf | Indice | Estado')
  print('-' * 45)
  for k in range(len(horas)):
    print(
        f'{horas[k]} | {H[k]:.2f} | {N[k]:.2f} | {Tf[k]:.2f} |'
        f' {I_orig[k]:.3f} | {est_orig[k]}'
    )

  # Impresion de la Tabla del Modelo Ajustado
  print('\n=== TABLA MODELO AJUSTADO (0.4H + 0.4N + 0.2Tf) ===')
  print('Hora | H | N | Tf | Indice | Estado')
  print('-' * 45)
  for k in range(len(horas)):
    print(
        f'{horas[k]} | {H[k]:.2f} | {N[k]:.2f} | {Tf[k]:.2f} |'
        f' {I_ajust[k]:.3f} | {est_ajust[k]}'
    )

  # Mostrar Grafica 1 (Original)
  GraficaSimulacion.mostrar_grafica_original(horas, I_orig, K=0.75)

  # Mostrar Grafica 2 (Ajustado)
  GraficaSimulacion.mostrar_grafica_ajustada(horas, I_ajust, K=0.75)