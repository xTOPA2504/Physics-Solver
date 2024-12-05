import math

def solve_alpinist_potential_energy_change():
    print("Cambio de energía potencial (Alpinista)")

    # Solicitar valores necesarios
    m = float(input("Introduce la masa del alpinista (en kg): "))
    g = 9.81  # Aceleración debida a la gravedad (m/s^2)
    h_initial = float(input("Introduce la altura inicial (en m): "))
    h_final = float(input("Introduce la altura final (en m): "))

    # Cálculo de energía potencial inicial, final y el cambio
    E_p_initial = m * g * h_initial
    E_p_final = m * g * h_final
    delta_E_p = E_p_final - E_p_initial

    # Mostrar fórmula y procedimiento
    print("\nFórmula del cambio en energía potencial:")
    print("ΔE_p = m * g * (h_final - h_initial)")
    print("\nProcedimiento:")
    print(f"Se sustituye m = {m} kg, g = {g} m/s^2, h_initial = {h_initial} m y h_final = {h_final} m.")
    print(f"ΔE_p = {m} * {g} * ({h_final} - {h_initial})")
    print(f"ΔE_p = {delta_E_p:.2f} J")

    return delta_E_p

def solve_flour_bag():
    print("Fuerza y trabajo (Saco de harina)")
    
    # Solicitar los valores necesarios
    F = float(input("Introduce la fuerza (en N): "))
    d = float(input("Introduce la distancia (en m): "))
    
    # Cálculo del trabajo
    W = F * d  # Suponiendo que la fuerza es en la dirección del movimiento
    
    # Mostrar la fórmula y el procedimiento
    print("\nFórmula del trabajo:")
    print("W = F * d")
    print("\nProcedimiento:")
    print(f"Se sustituye F = {F} N y d = {d} m en la fórmula.")
    print(f"W = {F} * {d}")
    print(f"W = {W:.2f} J")
    
    return W

def solve_trampoline_jump():
    """
    Calcula la velocidad de un nadador tras saltar desde un trampolín.
    """
    print("\nVelocidad de un nadador (Trampolín)")
    m = float(input("Introduce la masa del nadador (en kg): "))
    h = float(input("Introduce la altura del trampolín (en m): "))
    g = 9.81  # Gravedad (m/s^2)
    v = math.sqrt(2 * g * h)

    # Mostrar resultados
    print("\nFórmula: v = √(2 * g * h)")
    print(f"Procedimiento: v = √(2 * {g} * {h})")
    print(f"Resultado: v = {v:.2f} m/s\n")
    return v

def solve_spring_potential_energy():
    print("Energía potencial de un resorte")
    
    # Solicitar los valores
    k = float(input("Introduce la constante del resorte (k) en N/m: "))
    x = float(input("Introduce la elongación o compresión (x) en m: "))
    
    # Calcular la energía potencial
    E_pe = 0.5 * k * x**2
    
    # Mostrar la fórmula y el procedimiento
    print("\nFórmula de energía potencial elástica:")
    print("E_pe = (1/2) * k * x^2")
    print("\nProcedimiento:")
    print(f"Se sustituye k = {k} N/m y x = {x} m en la fórmula.")
    print(f"E_pe = (1/2) * {k} * ({x}^2)")
    print(f"E_pe = {E_pe:.2f} J")
    
    return E_pe

def solve_friction_work():
    print("Trabajo realizado por fricción (Caja circular)")
    
    # Solicitar los valores
    mu = float(input("Introduce el coeficiente de fricción: "))
    N = float(input("Introduce la fuerza normal (en N): "))
    d = float(input("Introduce la distancia recorrida (en m): "))
    
    # Calcular la fuerza de fricción
    F_f = mu * N
    
    # Calcular el trabajo
    W_f = F_f * d
    
    # Mostrar la fórmula y el procedimiento
    print("\nFórmula del trabajo por fricción:")
    print("W_f = F_f * d")
    print("F_f = μ * N")
    print("\nProcedimiento:")
    print(f"Se calcula F_f = {mu} * {N}")
    print(f"F_f = {F_f} N")
    print(f"El trabajo realizado por la fricción es W_f = F_f * d")
    print(f"W_f = {F_f} * {d}")
    print(f"W_f = {W_f:.2f} J")
    
    return W_f

def solve_friction_coefficient():
    print("Coeficiente de fricción (Paquete en el arco)")
    
    # Solicitar los valores
    F_f = float(input("Introduce la fuerza de fricción (en N): "))
    N = float(input("Introduce la fuerza normal (en N): "))
    
    # Calcular el coeficiente de fricción
    mu = F_f / N
    
    # Mostrar la fórmula y el procedimiento
    print("\nFórmula para el coeficiente de fricción:")
    print("μ = F_f / N")
    print("\nProcedimiento:")
    print(f"Se sustituye F_f = {F_f} N y N = {N} N en la fórmula.")
    print(f"μ = {F_f} / {N}")
    print(f"μ = {mu:.2f}")
    
    return mu

def solve_block_spring_motion():
    """
    Calcula el movimiento de un bloque unido a un resorte, considerando la energía mecánica total.
    """
    print("\nMovimiento de bloque en resorte")
    k = float(input("Introduce la constante del resorte (k) en N/m: "))
    x = float(input("Introduce la deformación inicial del resorte (x) en m: "))
    m = float(input("Introduce la masa del bloque (m) en kg: "))

    # Energía mecánica total (E = K.E. + P.E.)
    g = 9.81  # Gravedad
    v_max = math.sqrt(k / m) * x  # Velocidad máxima
    E_potential = 0.5 * k * x**2  # Energía potencial
    E_kinetic = 0.5 * m * v_max**2  # Energía cinética máxima

    # Mostrar resultados
    print("\nFórmulas:")
    print("1. Velocidad máxima: v_max = √(k/m) * x")
    print("2. Energía potencial: E_p = (1/2) * k * x^2")
    print("3. Energía cinética máxima: E_k = (1/2) * m * v_max^2")
    print("\nProcedimiento:")
    print(f"v_max = √({k}/{m}) * {x} = {v_max:.2f} m/s")
    print(f"E_p = (1/2) * {k} * ({x}^2) = {E_potential:.2f} J")
    print(f"E_k = (1/2) * {m} * ({v_max:.2f}^2) = {E_kinetic:.2f} J")

    return {
        "Velocidad máxima (m/s)": v_max,
        "Energía potencial (J)": E_potential,
        "Energía cinética máxima (J)": E_kinetic
    }
    
def solve_automobile_kinetic_energy():
    print("Energía cinética de un automóvil")
    
    # Solicitar los valores
    m = float(input("Introduce la masa del automóvil (en kg): "))
    v = float(input("Introduce la velocidad del automóvil (en m/s): "))
    
    # Calcular la energía cinética
    E_kin = 0.5 * m * v**2
    
    # Mostrar la fórmula y el procedimiento
    print("\nFórmula de energía cinética:")
    print("E_k = (1/2) * m * v^2")
    print("\nProcedimiento:")
    print(f"Se sustituye m = {m} kg y v = {v} m/s en la fórmula.")
    print(f"E_k = (1/2) * {m} * ({v}^2)")
    print(f"E_k = {E_kin:.2f} J")
    
    return E_kin

def solve_kinetic_energy():
    print("Energía cinética")
    
    # Solicitar los valores
    m = float(input("Introduce la masa del objeto (en kg): "))
    v = float(input("Introduce la velocidad del objeto (en m/s): "))
    
    # Calcular la energía cinética
    E_kin = 0.5 * m * v**2
    
    # Mostrar la fórmula y el procedimiento
    print("\nFórmula de energía cinética:")
    print("E_k = (1/2) * m * v^2")
    print("\nProcedimiento:")
    print(f"Se sustituye m = {m} kg y v = {v} m/s en la fórmula.")
    print(f"E_k = (1/2) * {m} * ({v}^2)")
    print(f"E_k = {E_kin:.2f} J")
    
    return E_kin

def solve_work_done():
    print("Trabajo realizado por una fuerza constante")
    
    # Solicitar los valores
    F = float(input("Introduce la fuerza (en N): "))
    d = float(input("Introduce la distancia (en m): "))
    theta = float(input("Introduce el ángulo entre la fuerza y el desplazamiento (en grados): "))
    
    # Convertir el ángulo a radianes
    theta_rad = math.radians(theta)
    
    # Calcular el trabajo
    W = F * d * math.cos(theta_rad)
    
    # Mostrar la fórmula y el procedimiento
    print("\nFórmula del trabajo:")
    print("W = F * d * cos(θ)")
    print("\nProcedimiento:")
    print(f"Se sustituye F = {F} N, d = {d} m y θ = {theta}° en la fórmula.")
    print(f"W = {F} * {d} * cos({theta_rad:.2f})")
    print(f"W = {W:.2f} J")
    
    return W

def solve_friction():
    """
    Calcula la fuerza de fricción utilizando el coeficiente de fricción y la fuerza normal.
    """
    print("\nCálculo de la Fuerza de Fricción")

    # Solicitar los valores
    mu = float(input("Introduce el coeficiente de fricción (μ): "))
    N = float(input("Introduce la fuerza normal (N) en Newtons: "))

    # Calcular la fuerza de fricción
    F_f = mu * N

    # Mostrar la fórmula y el procedimiento
    print("\nFórmulas:")
    print("F_f = μ * N")
    print("\nProcedimiento:")
    print(f"Se sustituye μ = {mu} y N = {N} N en la fórmula.")
    print(f"F_f = {mu} * {N}")
    print(f"F_f = {F_f:.2f} N")

    return F_f

def solve_gravitational_potential_energy():
    """
    Calcula la energía potencial gravitacional de un objeto.
    """
    print("\nCálculo de Energía Potencial Gravitacional")

    # Solicitar los valores
    m = float(input("Introduce la masa del objeto (en kg): "))
    h = float(input("Introduce la altura respecto al punto de referencia (en m): "))
    g = 9.81  # Valor constante de la gravedad

    # Calcular la energía potencial gravitacional
    E_p = m * g * h

    # Mostrar la fórmula y el procedimiento
    print("\nFórmulas:")
    print("E_p = m * g * h")
    print("\nProcedimiento:")
    print(f"Se sustituye m = {m} kg, g = {g} m/s^2 y h = {h} m en la fórmula.")
    print(f"E_p = {m} * {g} * {h}")
    print(f"E_p = {E_p:.2f} J")

    return E_p

def solve_conservation_of_energy():
    """
    Conservación de energía: calcula energías iniciales y finales en un sistema simple.
    """
    print("\nConservación de energía")
    m = float(input("Introduce la masa del objeto (en kg): "))
    h_initial = float(input("Introduce la altura inicial (en m): "))
    h_final = float(input("Introduce la altura final (en m): "))
    v_initial = float(input("Introduce la velocidad inicial (en m/s): "))
    v_final = float(input("Introduce la velocidad final (en m/s): "))
    g = 9.81  # Gravedad

    # Energía inicial
    E_p_initial = m * g * h_initial
    E_k_initial = 0.5 * m * v_initial**2
    E_initial = E_p_initial + E_k_initial

    # Energía final
    E_p_final = m * g * h_final
    E_k_final = 0.5 * m * v_final**2
    E_final = E_p_final + E_k_final

    # Mostrar procedimiento
    print("\nFórmulas:")
    print("E_p = m * g * h")
    print("E_k = 0.5 * m * v^2")
    print("\nProcedimiento:")
    print(f"E_inicial = E_p_inicial + E_k_inicial = {E_p_initial:.2f} + {E_k_initial:.2f}")
    print(f"E_final = E_p_final + E_k_final = {E_p_final:.2f} + {E_k_final:.2f}")
    print(f"E_inicial = {E_initial:.2f} J, E_final = {E_final:.2f} J")

    return E_initial, E_final

def solve_hookes_law():
    """
    Aplica la Ley de Hooke para calcular la fuerza de un resorte.
    """
    print("\nLey de Hooke")
    k = float(input("Introduce la constante del resorte (en N/m): "))
    x = float(input("Introduce la deformación del resorte (en m): "))
    F = k * x

    print("\nFórmula:")
    print("F = k * x")
    print("\nProcedimiento:")
    print(f"Se sustituye k = {k} y x = {x} en la fórmula.")
    print(f"F = {k} * {x} = {F:.2f} N")

    return F

def solve_horizontal_friction_work():
    """
    Calcula el trabajo por fricción en una superficie horizontal.
    """
    print("\nTrabajo por fricción en superficie horizontal")
    mu = float(input("Introduce el coeficiente de fricción: "))
    N = float(input("Introduce la fuerza normal (en N): "))
    d = float(input("Introduce la distancia recorrida (en m): "))
    W_f = mu * N * d

    print("\nFórmula:")
    print("W_f = μ * N * d")
    print("\nProcedimiento:")
    print(f"Se sustituye μ = {mu}, N = {N}, d = {d}.")
    print(f"W_f = {mu} * {N} * {d} = {W_f:.2f} J")

    return W_f

def solve_trampoline_jump():
    """
    Calcula energía en un salto desde un trampolín.
    """
    print("\nSalto trampolín")
    m = float(input("Introduce la masa del nadador (en kg): "))
    h = float(input("Introduce la altura del trampolín (en m): "))
    v = float(input("Introduce la velocidad inicial al salir del trampolín (en m/s): "))
    g = 9.81

    # Energía potencial inicial
    E_p = m * g * h
    # Energía cinética inicial
    E_k = 0.5 * m * v**2

    print("\nFórmulas:")
    print("E_p = m * g * h")
    print("E_k = 0.5 * m * v^2")
    print("\nProcedimiento:")
    print(f"E_p = {m} * {g} * {h} = {E_p:.2f} J")
    print(f"E_k = 0.5 * {m} * ({v}^2) = {E_k:.2f} J")
    print(f"E_total = E_p + E_k = {E_p + E_k:.2f} J")

    return E_p + E_k

def solve_gravitational_potential_energy_change():
    print("Cambio en la energía potencial gravitacional")
    
    # Solicitar los valores
    m = float(input("Introduce la masa del objeto (en kg): "))
    g = 9.81  # Aceleración debida a la gravedad (m/s^2)
    h_initial = float(input("Introduce la altura inicial (en m): "))
    h_final = float(input("Introduce la altura final (en m): "))
    
    # Calcular el cambio en la energía potencial
    E_p_initial = m * g * h_initial
    E_p_final = m * g * h_final
    delta_E_p = E_p_final - E_p_initial
    
    # Mostrar la fórmula y el procedimiento
    print("\nFórmula de cambio en la energía potencial gravitacional:")
    print("ΔE_p = m * g * (h_final - h_initial)")
    print("\nProcedimiento:")
    print(f"Se sustituye m = {m} kg, g = {g} m/s^2, h_initial = {h_initial} m y h_final = {h_final} m.")
    print(f"ΔE_p = {m} * {g} * ({h_final} - {h_initial})")
    print(f"ΔE_p = {delta_E_p:.2f} J")
    
    return delta_E_p

def solve_potential_energy_system():
    """
    Calcula la energía potencial de un sistema de partículas.
    """
    print("\nEnergía potencial de un sistema de partículas")
    n = int(input("Introduce el número de partículas en el sistema: "))
    g = 9.81  # Gravedad

    total_energy_potential = 0
    for i in range(1, n + 1):
        m = float(input(f"Introduce la masa de la partícula {i} (en kg): "))
        h = float(input(f"Introduce la altura de la partícula {i} (en m): "))
        E_p = m * g * h
        total_energy_potential += E_p
        print(f"Energía potencial de la partícula {i}: {E_p:.2f} J")

    print(f"\nEnergía potencial total del sistema: {total_energy_potential:.2f} J")
    return total_energy_potential

def other_energy_work_problems():
    """
    Muestra un submenú para resolver otros problemas de energía y trabajo.
    """
    while True:
        print("\nOtros problemas de energía y trabajo:")
        print("1. Energía cinética de un automóvil")
        print("2. Trabajo realizado por una fuerza constante")
        print("3. Energía potencial de un sistema de partículas")
        print("4. Trabajo realizado por fricción")
        print("5. Regresar al menú principal")

        sub_choice = int(input("Selecciona una opción (1-5): "))
        if sub_choice == 1:
            solve_automobile_kinetic_energy()
        elif sub_choice == 2:
            solve_work_done()
        elif sub_choice == 3:
            solve_potential_energy_system()
        elif sub_choice == 4:
            solve_horizontal_friction_work()
        elif sub_choice == 5:
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


def main():
    while True:
        print("\nSelecciona el tipo de problema:")
        print("1. Cambio de energía potencial (Alpinista)")
        print("2. Fuerza y trabajo (Saco de harina)")
        print("3. Velocidad de un nadador (Trampolín)")
        print("4. Energía potencial de un resorte")
        print("5. Trabajo por fricción (Caja circular)")
        print("6. Coeficiente de fricción (Paquete en el arco)")
        print("7. Movimiento de bloque en resorte")
        print("8. Energía cinética")
        print("9. Trabajo")
        print("10. Cambio de energía potencial")
        print("11. Fricción")
        print("12. Energía potencial gravitacional")
        print("13. Conservación de energía")
        print("14. Ley de Hooke")
        print("15. Trabajo por fricción en superficie horizontal")
        print("16. Salto trampolín")
        print("17. Energía cinética de automóvil y otros problemas de energía")
        print("18. Otros problemas de energía y trabajo")
        print("19. Salir")
        
        choice = int(input("Ingresa tu elección (1-19): "))
        
        if choice == 1:
            solve_alpinist_potential_energy_change()
        elif choice == 2:
            solve_flour_bag()
        elif choice == 3:
            solve_trampoline_jump()
        elif choice == 4:
            solve_spring_potential_energy()
        elif choice == 5:
            solve_friction_work()
        elif choice == 6:
            solve_friction_coefficient()
        elif choice == 7:
            solve_block_spring_motion()
        elif choice == 8:
            solve_kinetic_energy()
        elif choice == 9:
            solve_work_done()
        elif choice == 10:
            solve_gravitational_potential_energy_change()
        elif choice == 11:
            solve_friction()
        elif choice == 12:
            solve_gravitational_potential_energy()
        elif choice == 13:
            solve_conservation_of_energy()
        elif choice == 14:
            solve_hookes_law()
        elif choice == 15:
            solve_horizontal_friction_work()
        elif choice == 16:
            solve_trampoline_jump()
        elif choice == 17:
            solve_automobile_kinetic_energy()
        elif choice == 18:
            other_energy_work_problems()
        elif choice == 19:
            print("Salir.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
