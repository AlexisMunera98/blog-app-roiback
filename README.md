# blog-app-roiback
Prueba tecnica roiback

## Despligue
La aplicacion se encuentra hosteada en Gcloud en el siguiente enlace: [Blog-app](https://blog-app-239400.appspot.com/blog/)
### Se usaron los siguientes servicios:
- **App engine:** Usado para ejecutar el wsgi de django.
- **SQL:** Se creo una instancia de Postgresl 11 para conectar la aplicacion.
- **Cloud Storage Bucket:** Se usa para servir los archivos estaticos requeridos por la aplicacion.

### Urls
- */blog/auth/signup* -> Registro de un usuario
- */blog/auth/login* -> Login de un usuario
- */blog/posts* -> Lista de posts
- */blog/posts/<int:id>* -> Detalle de un post y sus comentarios
- */blog/posts/<int:id>/like* -> Dar like a un post
- */blog/posts/create* -> Creacion de un post
- */blog/posts/update/<int:id>* -> Vista de actualizacion de post
- */blog/posts/delete/<int:id>* -> Borrar un posts


### Dependencias usadas
- **Python:** 3.7
- **Django:** 2.2
- **django-background-tasks:** Usado para crear tareas que publiquen o desactiven los posts. Se hace verificacion cada 3min.
- **django-bootstrap-datepicker-plus:** Usado para renderizar los selectores de fecha de publicacion y desactivacion.
- **django-filter:** Usado para el filtro de los posts en la vista de lista de posts.
- **django-widget-tweaks:** Usado para mejorar el css de los widgets renderizados por los paquetes externos.
