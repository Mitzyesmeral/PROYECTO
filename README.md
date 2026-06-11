# PROYECTO

¿Qué hace mi app?

- Interfaz moderna y simple: Todo está organizado en un contenedor central con tonos azules y blancos. Los bordes redondeados y las sombras le dan un toque actual y agradable.

- Base de datos lista para usar: Al iniciar, la app se conecta automáticamente a `datos.db` y crea la tabla si no existe. Así, puedes empezar a usarla de inmediato, sin complicaciones.

-Validaciones prácticas: Si dejas un campo vacío o escribes letras en la edad, la app muestra una alerta en rojo para evitar errores.

- Lista interactiva de usuarios: Los registros aparecen en la parte inferior. Solo tienes que hacer clic en uno para que sus datos se carguen automáticamente en el formulario, listo para editar o borrar al instante.

- Cierre seguro: Hay un botón de salida que primero cierra la conexión con la base de datos y luego termina la app, asegurando que todo quede guardado correctamente.



Para que funcione perfecto con las últimas versiones de Flet, solo me faltaría actualizar la última línea de `ft.run(main)` a `ft.app(target=main)`.
