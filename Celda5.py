nombre_hero = "Guerrero"
nivel_hero = 2
vida_max_hero = 80
vida_hero = vida_max_hero
ataque_hero = 18
defensa_hero = 8

enemigos = [
    ("Goblin", 40, 8),
    ("Orco", 70, 14),
    ("Dragon", 120, 25)
]

def combatir(vidaHero, ataqueHero, defHero, vidaEnemigo, ataqueEnemigo, nombreEnemigo):
    ronda = 1
    while vidaHero > 0 and vidaEnemigo > 0:
        # Héroe ataca
        dano_hero = max(1, ataqueHero - 0) 
        vidaEnemigo -= dano_hero

    
        dano_enemigo = max(1, ataqueEnemigo - defHero)
        vidaHero -= dano_enemigo

        print(f"Ronda {ronda}: Hero={vidaHero} | {nombreEnemigo}={vidaEnemigo}")
        ronda += 1

    return vidaHero, vidaEnemigo


derrotados = 0
for nombre, vidaE, ataqueE in enemigos:
    print(f"\n>>> Combate contra {nombre} <<<")
    vida_hero, vidaE = combatir(vida_hero, ataque_hero, defensa_hero, vidaE, ataqueE, nombre)

    if vida_hero <= 0:
        print("El héroe ha caído... DERROTA")
        break
    else:
        print(f"{nombre} derrotado!")
        derrotados += 1
        vida_hero = min(vida_hero + 20, vida_max_hero)
        print(f"El héroe se cura. Vida actual: {vida_hero}")

if derrotados == len(enemigos):
    print("\n>>> VICTORIA! El héroe venció a todos los enemigos <<<")
else:
    print(f"\nFin del juego. Enemigos derrotados: {derrotados}, Vida restante: {vida_hero}")
