package model;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

/**
 * Lógica de negocio (MODELO) que simula la interacción de la población paso a paso.
 */
public class ModeloSIR {
    private final int poblacionTotal;
    private final double beta;   // Tasa de transmisión
    private final double gamma;  // Tasa de recuperación
    private final List<Individuo> poblacion;
    private final Random random;
    private int tiempoActual;

    public ModeloSIR(int poblacionTotal, int infectadosIniciales, double beta, double gamma) {
        this.poblacionTotal = poblacionTotal;
        this.beta = beta;
        this.gamma = gamma;
        this.poblacion = new ArrayList<>(poblacionTotal);
        this.random = new Random();
        this.tiempoActual = 0;

        inicializarPoblacion(infectadosIniciales);
    }

    private void inicializarPoblacion(int infectadosIniciales) {
        for (int i = 0; i < poblacionTotal; i++) {
            if (i < infectadosIniciales) {
                poblacion.add(new Individuo(i, Estado.INFECTADO));
            } else {
                poblacion.add(new Individuo(i, Estado.SUSCEPTIBLE));
            }
        }
    }

    /**
     * Avanza un paso discreto (tick) evaluando contagios y recuperaciones.
     */
    public void avanzarPaso() {

    List<Estado> estadosAnteriores = poblacion.stream()
            .map(Individuo::getEstado)
            .collect(Collectors.toList());

    List<Integer> susceptibles = new ArrayList<>();
    List<Integer> infectados = new ArrayList<>();

    for (int i = 0; i < poblacionTotal; i++) {
        if (estadosAnteriores.get(i) == Estado.SUSCEPTIBLE) {
            susceptibles.add(i);
        } else if (estadosAnteriores.get(i) == Estado.INFECTADO) {
            infectados.add(i);
        }
    }

    // Probabilidad de contagio según el modelo SIR
    double probabilidadContagio =
            beta * infectados.size() / poblacionTotal;

    // Contagios: se evalúan los susceptibles del inicio del paso
    for (Integer idSusceptible : susceptibles) {
        if (random.nextDouble() < probabilidadContagio) {
            poblacion.get(idSusceptible)
                    .setEstado(Estado.INFECTADO);
        }
    }

    // Recuperaciones: solo los infectados del inicio del paso
    for (Integer idInfectado : infectados) {
        if (random.nextDouble() < gamma) {
            poblacion.get(idInfectado)
                    .setEstado(Estado.RECUPERADO);
        }
    }

    tiempoActual++;
}

    public Resultado obtenerResultadoActual() {
        int s = 0, i = 0, r = 0;
        for (Individuo ind : poblacion) {
            switch (ind.getEstado()) {
                case SUSCEPTIBLE:
                    s++;
                    break;
                case INFECTADO:
                    i++;
                    break;
                case RECUPERADO:
                    r++;
                    break;
            }
        }
        return new Resultado(tiempoActual, s, i, r);
    }
}