from django.http import HttpResponse

# Página principal
def inicio(request):
    contenido = """
    <html>
        <head><title>Inicio</title></head>
        <body style='font-family: Arial;'>
            <h1>Bienvenido al portal CursosDjango</h1>
            <p>Este sitio tiene como objetivo ofrecerte información sobre cursos básicos de programación y tecnología.</p>

            <hr>
            <h3>Menú de navegación</h3>
            <a href="/">Inicio</a> |
            <a href="/cursos/">Cursos</a> |
            <a href="/contacto/">Contacto</a>
        </body>
    </html>
    """
    return HttpResponse(contenido)


# Página de cursos
def cursos(request):
    # Usamos una lista (como viste en arreglos)
    lista_cursos = ["Base de Datos", "Programación", "Desarrollo Web", "Seguridad Informática"]

    # Convertimos la lista a formato HTML con un ciclo
    lista_html = ""
    for curso in lista_cursos:
        lista_html += f"<li>{curso}</li>"

    contenido = f"""
    <html>
        <head><title>Cursos</title></head>
        <body style='font-family: Arial;'>
            <h1>Lista de Cursos Disponibles</h1>
            <ul>{lista_html}</ul>

            <hr>
            <h3>Menú de navegación</h3>
            <a href="/">Inicio</a> |
            <a href="/cursos/">Cursos</a> |
            <a href="/contacto/">Contacto</a>
        </body>
    </html>
    """
    return HttpResponse(contenido)


# Página de contacto
def contacto(request):
    # Diccionario con cursos (como viste en diccionarios)
    cursos_disponibles = {
        "BD": "Base de Datos",
        "PR": "Programación",
        "DW": "Desarrollo Web",
        "SI": "Seguridad Informática"
    }

    # Generamos una lista HTML de los cursos
    opciones_html = ""
    for clave, nombre in cursos_disponibles.items():
        opciones_html += f"<li>{nombre}</li>"

    contenido = f"""
    <html>
        <head><title>Contacto</title></head>
        <body style='font-family: Arial;'>
            <h1>Contacto</h1>
            <p>Para solicitar información sobre alguno de nuestros cursos, llena el siguiente formulario (ejemplo ilustrativo):</p>

            <form>
                <label>Nombre:</label><br>
                <input type="text" placeholder="Tu nombre"><br><br>

                <label>Correo electrónico:</label><br>
                <input type="email" placeholder="correo@ejemplo.com"><br><br>

                <label>Curso de interés:</label><br>
                <ul>{opciones_html}</ul><br>

                <label>Comentarios:</label><br>
                <textarea placeholder="Escribe tus comentarios aquí"></textarea><br><br>

                <button>Enviar</button>
            </form>

            <hr>
            <h3>Menú de navegación</h3>
            <a href="/">Inicio</a> |
            <a href="/cursos/">Cursos</a> |
            <a href="/contacto/">Contacto</a>
        </body>
    </html>
    """
    return HttpResponse(contenido)
