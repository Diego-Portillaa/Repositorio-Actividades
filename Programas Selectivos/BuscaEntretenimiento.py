print('''--- Buscador de Información de Entretenimiento ---''')

print("Opciones disponibles:\n- Frank Sinatra\n- Inception\n- Breaking Bad\n- Ludovico Einaudi\n- Interstellar")
busqueda = input("Ingresa el nombre del artista, película o serie: ").strip().lower()
#Aqui no hay pierde ya que lo hay es lo que hay
match busqueda:
    case "frank sinatra":
        #Aqui podemos utilizar \n para hacer un salto de linea y que el mensaje sea mas legible
        print("\n[Artista] Cantante y actor estadounidense, considerado una de las figuras más influyentes de la música popular del siglo XX.")
    case "inception":
        print("\n[Película] Dirigida por Christopher Nolan. Trata sobre un ladrón que roba secretos a través del uso de la tecnología de compartir sueños.")
    case "breaking bad":
        print("\n[Serie] Dramática de televisión sobre un profesor de química que se transforma en un metódico magnate de las drogas.")
    case "ludovico einaudi":
        print("\n[Artista] Pianista y compositor italiano conocido por sus famosas obras de música neoclásica e instrumental.")
    case "interstellar":
        print("\n[Película] Ciencia ficción épica que sigue a un grupo de astronautas que viajan a través de un agujero de gusano en busca de un nuevo hogar.")
    case _:
        print("\nError: No se encontró información para el término ingresado.")