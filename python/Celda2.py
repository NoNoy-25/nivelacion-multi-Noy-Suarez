vida_enemigo = 40
ataque = 35
nivel_jugador = 6
bonificacion = 10 if nivel_jugador >= 5 else 0

dano_total = ataque + bonificacion
vida_restante = vida_enemigo - dano_total

if vida_restante <= 0:
    print("Enemigo derrotado! +50 XP")
elif vida_restante <= 20:
    print("Enemigo en estado critico")
else:
    print(f"Enemigo resiste. Vida restante: {vida_restante}")
