### Archivo Main:

Este archivo se encarga de inicializar el juego y mostrar los frames de movimiento del personaje. Aquí hay una descomposición de las secciones más importantes:

- **`clock`**: Permite configurar los FPS (frames por segundo) que utilizará el juego.
  
- **`background, bg_image = get_background("Blue.png")`**: Esta función será detallada más adelante en el archivo. Devuelve las baldosas o la posición de las superficies y el fondo aplicado según los parámetros de la función.

- **`fire, objects`**: Clases que se comportan como objetos tocables y colisionadores. En el caso de `fire`, inflige daño.

- **`offset_x`**: Variable que actúa como movimiento de la cámara.

Estos son algunos de los métodos más importantes del archivo principal.

### Archivo Screen:

Este archivo contiene funciones relacionadas con la pantalla del juego:

- **`get_background`**: Recibe un fondo como parámetro, obtiene las dimensiones de una baldosa y itera para cubrir la pantalla del jugador.

- **`draw_main`**: Dibuja la pantalla y las baldosas principales.

- **`menu_view`**: Configura un menú en caso de presionar "esc".

### Archivo Utilities:

Este archivo es crítico ya que contiene variables inicializadoras de Pygame y funciones esenciales:

- **`load_sprite_sheets`**: Divide las dimensiones de una imagen para convertirla en frames. Dependiendo de la dirección, retorna imágenes de derecha a izquierda o en su estado normal.

- **`flip`**: Voltea la imagen a su estado contrario.

- **`Traps, Player, Objects`**: Clases que hacen uso de "Sprite" y permiten los frames de los objetos. En el caso de `Player`, tiene métodos adicionales que le permiten controlar al jugador, recibir daño, saltar, etc.

- **`movement`**: Permite configurar eventos que mueven al jugador y actualizar sus métodos.

- **`Collisions`**: Restablece valores específicos del jugador en caso de colisionar con objetos.