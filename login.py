import flet as ft

def main(page: ft.Page):

    # CONFIGURACIÓN DE LA VENTANA
    page.title = "Iniciar Sesión"
    page.bgcolor = ft.Colors.PURPLE_50

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # CAMPOS
    txt_user = ft.TextField(
        label="Usuario",
        width=280,
        autofocus=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        text_style=ft.TextStyle(color=ft.Colors.BLACK)
    )

    txt_pass = ft.TextField(
        label="Contraseña",
        width=280,
        password=True,
        can_reveal_password=True,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        text_style=ft.TextStyle(color=ft.Colors.BLACK)
    )

    lbl_msg = ft.Text(
        value="",
        size=14,
        weight=ft.FontWeight.BOLD
    )

    # VALIDAR LOGIN
    def validar_ingreso(e):

        if txt_user.value == "admin" and txt_pass.value == "123":

            lbl_msg.value = "✅ ¡Acceso concedido con éxito!"
            lbl_msg.color = ft.Colors.GREEN

            # Aquí puedes abrir otra pantalla

        else:

            lbl_msg.value = "❌ Usuario o contraseña incorrectos"
            lbl_msg.color = ft.Colors.RED

        page.update()

    tarjeta_login = ft.Container(
        content=ft.Column(
            [
                ft.Icon(
                    name=ft.Icons.LOCK_PERSON_ROUNDED,
                    color=ft.Colors.PURPLE_600,
                    size=50
                ),

                ft.Text(
                    "INICIAR SESIÓN",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),

                ft.Divider(
                    height=5,
                    color=ft.Colors.PURPLE_100
                ),

                txt_user,
                txt_pass,

                ft.ElevatedButton(
                    "Ingresar",
                    on_click=validar_ingreso,
                    width=280,
                    bgcolor=ft.Colors.PURPLE_200,
                    color=ft.Colors.BLACK
                ),

                lbl_msg
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),

        padding=30,
        border_radius=15,
        bgcolor=ft.Colors.WHITE,
        width=350,

        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.Colors.PURPLE_100
        )
    )

    page.add(tarjeta_login)

if __name__ == "__main__":
    ft.app(target=main)