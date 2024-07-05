*** ReviewRealm ***

Agradecemos darte el tiempo de visitar nuestro royecto, somo el grupo número 1 del curso 006V, los autores de este proyecto son
- DarthBane1138: Patricio Leiva
- evil976: Jordan Órdenes

El link ha nuestro repositorio de Github

https://github.com/DarthBane1138/ReviewRealmDjango.git

El super usuario de la página es
Usuario: admin
Contraseña: administrador

Se crearon otros usuarios, los cuales fueron hechos a modeo de usuarios normales, sin la posibilidad de hacer modificaciones en el CRUD
Usuario 1: DarthBane
Contraseña: thxx1138

Usuario 2: EstoyProbando
Contraseña: Prueba123

Reglas de Negocio: Se han establecido las reglas de negocio que se detallan a continuación para darle uso a la base de datos creada en este proyecto
- Se han credo dos tablas, los cuales tienen sus propios CRUD para editar los estados de estos
- Juego: Que representa los datos de cada juego, con campos como id_juego, título, año de publicación, género del juego, etc.
- Genero_Juego: Este representa el género de los juegos, se han establecido 20 géneros distintos
- Con lo anteriormente dicho, se ha elaborado una sección llamada "Categorías", en la cual se despliega una lista con todos los géneros que contengan una instancia de "Juego".
	Aparecerá el total de los juegos registrados en esta categoría o género, si no hay juegos para este género, el género no aparecerá en la lista.
	El nombre de cada género será un link, el cual si se presiona, el usuario será llevado a otra página donde se listan los juegos correspondientes a esta categoría o género.
	Si se presiona el juego en cuestión, el usuario será llevado a una página donde se mostrarán los detalles de cad juego seleccionado.
- Se ha implementado una página para que, de forma aleatoria, se pueda mostrar un juego al azar de entre los que est´pan disponibles en la base de datos, anteriormente esto se
	simulaba por medio de un documento json, ahora esta selección viene de la base de datos.