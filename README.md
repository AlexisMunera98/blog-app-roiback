# blog-app-roiback
Prueba tecnica roiback
## Urls
- /blog/auth/signup -> Registro de un usuario
- /blog/auth/login -> Login de un usuario
- /blog/posts -> Lista de posts
- /blog/posts/<int:id> -> Detalle de un post y sus comentarios
- /blog/posts/<int:id>/like -> Dar like a un post
- /blog/posts/create -> Creacion de un post
- /blog/posts/update/<int:id> -> Vista de actualizacion de post
- /blog/posts/delete/<int:id> -> Borrar un posts


## Dependencias usadas
- django-background-tasks: Usado para crear tareas que publiquen o desactiven los posts. Se hace verificacion cada 3min.
- django-bootstrap-datepicker-plus: Usado para renderizar los selectores de fecha de publicacion y desactivacion.
- django-filter: Usado para el filtro de los posts en la vista de lista de posts.
- django-widget-tweaks: Usado para mejorar el css de los widgets renderizados por los paquetes externos.
