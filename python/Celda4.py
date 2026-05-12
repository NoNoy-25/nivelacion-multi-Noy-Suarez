def subir_nivel(xp_actual: int, xp_necesario: int, nivel_actual: int) -> int:
    if xp_actual >= xp_necesario:
        nivel_actual += 1
        xp_actual = 0  # reinicia XP
        print(f'¡Nivel {nivel_actual} alcanzado!')
    return nivel_actual

# Pruebas
xp, xp_necesario, nivel = 110, 100, 3
print("Resultado:", subir_nivel(xp, xp_necesario, nivel))

xp, xp_necesario, nivel = 80, 100, 3
print("Resultado:", subir_nivel(xp, xp_necesario, nivel))  
