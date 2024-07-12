*** ReviewRealm ***

Agradecemos darte el tiempo de visitar nuestro royecto, somo el grupo número 1 del curso 006V, los autores de este proyecto son
- DarthBane1138: Patricio Leiva
- evil976: Jordan Órdenes

El link ha nuestro repositorio de Github

https://github.com/DarthBane1138/ReviewRealmDjango.git

El super usuario de la página es
Usuario: admin
Contraseña: administrador

El usuario Darthbane tiene categoría de Stafd, por lo que puede acceder a las páginas del crud, y modificar datos de los juegos desde el administrador de django
Usuario 1: DarthBane
Contraseña: thxx1138

Este es un usuario normal y corriente. No tiene acceso a páginas de Adminstrador (CRUD)
Usuario 2: EstoyProbando
Contraseña: Prueba123

Reglas de Negocio: Se han establecido las reglas de negocio que se detallan a continuación para darle uso a la base de datos db.sqlite 3 creada en este proyecto
- Se han credo dos tablas, los cuales tienen sus propios CRUD para editar los estados de estos. Además se ha habilitado el uso de sesiones de django.
- Juego: Que representa los datos de cada juego, con campos como id_juego, título, año de publicación, género del juego, etc.
- Genero_Juego: Este representa el género de los juegos, se han establecido 20 géneros distintos
- Los formularios de django se han usado para dos propósitos. para crear y editar valores de el modelo Genero_Juego, y para el inicio de sesión de usuarios.
- Al ingresar como superusuario, en el index de ReaviewRealm se habilitará el link de "Mantendor", el cual redireccionará a la página para la mantención del sitio web, teniendo
	acceso a modificar con más libertad.
- El usuario por otro lado tiene la posibilidad de crear instancias de juegos.
- Una de las reglas de negocio estipuladas antes se ha elaborado una sección llamada "Categorías", en la cual se despliega una lista con todos los géneros que contengan una instancia de "Juego".
	Con lo cual lo simulado anteriormente con una tabla, ahora es una tabla dinámica que interactúa con la base de datos, mostrando esta el total de los juegos registrados
	categorizados por género, si no hay juegos para este género, el género no aparecerá en la lista.
	El nombre de cada género será un link, el cual si se presiona, el usuario será llevado a otra página donde se listan los juegos correspondientes a esta categoría o género.
	Si se presiona sobre el nombre de algún juego, el usuario será llevado a una página donde se mostrarán los detalles de cada juego seleccionado. No se
	requiere que se inicie sesión para esta funcionalidad.
- Se ha implementado una página para que, de forma aleatoria, se pueda mostrar un juego al azar de entre los que estan disponibles en la base de datos, anteriormente esto se
	simulaba por medio de un documento json, ahora esta selección viene de la base de datos. No se requiere inicio de sesión para esta funcionalidad.
- Tiene una página "Buscar Juegos", en la cual se habilita un buscador que permite buscar por coincidencias parciales en los nombres de los juegos al escribir y presionar enter.
	¡Se ha implementado la búsqueda por año de lanzamiento!
- En esta misma página se te permite ingresar algún juego mediante un formulario. Esta funcionalidad sí requiere inicio de sesión

Se adjunta también presentación en Powerpoint
Complementos en requirements.txt (Django y Pillow)

