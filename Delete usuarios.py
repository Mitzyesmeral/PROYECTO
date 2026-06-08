# González Esparza Mitzy Esmeralda 4_D
# Proyecto: CRUD con Flet y SQLite
# (Crear, Leer, Actualizar y Eliminar) + botón para salir
# Proyecto: captura datos mediante un formulario, con validaciones
# para campos vacíos y entradas numérica.
# almacenando en base de datos


import flet as ft   # Se Importa flet y se le nombra con el alias ft
import sqlite3      # Se importa la base de datos    
import sys          # Libreria para usar herramienas del sistema

# Inicializa la página prinipal y se nombra con la variable "page"
def main(page: ft.Page):

    # CONFIGURACIÓN DE LA VENTANA PRINCIPAL
    page.title = "CRUD Usuarios"          # Se le asign aun titulo
    page.bgcolor = ft.Colors.BLUE_50      # Fondo de la app: Azul muy claro y limpio
    
    # Se prepara para que todos los widgets que se agreguen queden alineados al centro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # BASE DE DATOS

    conn = sqlite3.connect("datos.db")
    cursor = conn.cursor()

    # si no existe Crea La tabla usuarios2 con su llave primaria y campos 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            correo TEXT,
            edad INTEGER
        )
    """)
    conn.commit() # Confirma y guarda los cambios realizados en la base de datos

 
    # CAJAS DE TEXTO (Formulario con texto y etiquetas en NEGRO)

    id_usuario = ft.TextField(label="ID", width=250, read_only=True, label_style=ft.TextStyle(color=ft.Colors.BLACK), text_style=ft.TextStyle(color=ft.Colors.BLACK))
    nombre = ft.TextField(label="Nombre", autofocus=True, width=250, label_style=ft.TextStyle(color=ft.Colors.BLACK), text_style=ft.TextStyle(color=ft.Colors.BLACK))
    correo = ft.TextField(label="Correo", width=250, label_style=ft.TextStyle(color=ft.Colors.BLACK), text_style=ft.TextStyle(color=ft.Colors.BLACK))
    edad = ft.TextField(label="Edad", width=250, label_style=ft.TextStyle(color=ft.Colors.BLACK), text_style=ft.TextStyle(color=ft.Colors.BLACK))

    # Variable que guardará mensajes en pantalla
    resultado = ft.Text(value="", size=14, weight="bold")    
    
    # Caja blanca donde se cargan los registros
    lista_datos = ft.Container(          
        content=ft.Column(scroll=ft.ScrollMode.AUTO),
        height=150,
        width=350,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        padding=5,
        border=ft.border.all(1, ft.Colors.BLUE_200) 
    )

    # FUNCIONES
    # Limpia campos
    def limpiar(e):
        id_usuario.value = ""
        nombre.value = ""
        correo.value = ""
        edad.value = ""
        resultado.value = ""
        page.update()
    # consulta datos
    def consultar(e): 
        lista_datos.content.controls.clear()
        resultado.value = ""
        cursor.execute("SELECT id, nombre, correo, edad FROM usuarios2") 
        registros = cursor.fetchall()    
        
        for id_, nom, cor, ed in registros: 
            def seleccionar(e, id_=id_, nom=nom, cor=cor, ed=ed):
                id_usuario.value = str(id_)
                nombre.value = nom
                correo.value = cor
                edad.value = str(ed)

                resultado.value = f"Seleccionado ID: {id_}"
                resultado.color = ft.Colors.BLACK # Texto de ID seleccionado
                page.update()

            lista_datos.content.controls.append(
                ft.ListTile(
                    title=ft.Text(f"{nom} ({ed})", color=ft.Colors.BLACK, weight="bold"),
                    subtitle=ft.Text(cor, color=ft.Colors.BLACK),
                    on_click=seleccionar 
                )
            )
        page.update()

    def guardar(e):
        if not nombre.value or not correo.value or not edad.value:
            resultado.value = "⚠️ Campos obligatorios"
            resultado.color = "red"
        elif not edad.value.isdigit():
            resultado.value = "⚠️ Edad inválida"
            resultado.color = "red"
        else:
            cursor.execute(
                "INSERT INTO usuarios2 (nombre, correo, edad) VALUES (?, ?, ?)",
                (nombre.value, correo.value, edad.value)
            )
            conn.commit() 
            resultado.value = "✅ Registro guardado"
            resultado.color = "green"
            limpiar(None)
            consultar(None)
        page.update()

    def actualizar(e):
        if not id_usuario.value:
            resultado.value = "⚠️ Selecciona un registro"
            resultado.color = "red"
        else:
            cursor.execute(
                "UPDATE usuarios2 SET nombre=?, correo=?, edad=? WHERE id=?",
                (nombre.value, correo.value, edad.value, id_usuario.value)
            )
            conn.commit() 
            resultado.value = "✏️ Registro actualizado"
            resultado.color = ft.Colors.BLACK 
            consultar(None)
        page.update()

    def eliminar(e):
        if not id_usuario.value:
            resultado.value = "⚠️ Selecciona un registro"
            resultado.color = "red"
            page.update()
            return

        cursor.execute("DELETE FROM usuarios2 WHERE id=?", (id_usuario.value,))
        conn.commit() 

        if cursor.rowcount == 0:
            resultado.value = "⚠️ No se encontró el registro"
            resultado.color = "orange"
        else:
            limpiar(None)
            consultar(None)
            resultado.value = "🗑️ Registro eliminado"
            resultado.color = "red"
        page.update()

    def salir(e):
        conn.close()
        sys.exit()

   
    # BOTONES

    btn_guardar = ft.ElevatedButton("Guardar", on_click=guardar, width=100, bgcolor=ft.Colors.BLUE_200, color=ft.Colors.BLACK)
    btn_consultar = ft.ElevatedButton("Consultar", on_click=consultar, width=110, bgcolor=ft.Colors.BLUE_100, color=ft.Colors.BLACK)
    btn_actualizar = ft.ElevatedButton("Actualizar", on_click=actualizar, width=115, bgcolor=ft.Colors.BLUE_300, color=ft.Colors.BLACK)

    btn_eliminar = ft.ElevatedButton("Eliminar", on_click=eliminar, width=105, bgcolor=ft.Colors.RED_200, color=ft.Colors.BLACK)
    btn_limpiar = ft.ElevatedButton("Limpiar", on_click=limpiar, width=100, color=ft.Colors.BLACK)
    btn_salir = ft.ElevatedButton("Salir", on_click=salir, width=100, bgcolor=ft.Colors.BLUE_GREY_100, color=ft.Colors.BLACK)

    fila1 = ft.Row( 
        [btn_guardar, btn_consultar, btn_actualizar],
        alignment=ft.MainAxisAlignment.CENTER
    )

    fila2 = ft.Row( 
        [btn_eliminar, btn_limpiar, btn_salir],    
        alignment=ft.MainAxisAlignment.CENTER
    )


    # INTERFAZ PRINCIPAL
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    # Título de la app
                    ft.Text("CRUD USUARIOS", size=20, weight="bold", color=ft.Colors.BLACK),
                    id_usuario,
                    nombre,
                    correo,
                    edad,
                    fila1,
                    fila2,
                    resultado,
                    lista_datos
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            padding=20,
            border_radius=15,
            bgcolor=ft.Colors.WHITE, 
            width=400,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLUE_100) 
        )
    )

    consultar(None)

ft.run(main)
