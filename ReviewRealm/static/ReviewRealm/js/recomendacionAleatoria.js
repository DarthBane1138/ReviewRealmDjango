window.onload = function() {
    // Cargar recomendaciones desde el archivo JSON
    $.getJSON("/static/ReviewRealm/recomendaciones.json", function(data) {
        // Obtener un índice aleatorio dentro del rango de la longitud del array de recomendaciones
        var randomIndex = Math.floor(Math.random() * data.length);
        // Obtener la recomendación aleatoria
        var recomendacion = data[randomIndex];

        // Actualizar el título del juego
        $("#titulo_juego").text(recomendacion.titulo);
        // Actualizar la imagen del juego
        var imagenUrl = recomendacion.imagen;
        $("#imagen_juego").attr("src", imagenUrl);

        // Vaciar la lista de detalles del juego
        $("#detalles_juego").empty();
        // Agregar cada detalle del juego a la lista
        recomendacion.detalles.forEach(function(detalle) {
            $("#detalles_juego").append('<li>' + detalle + '</li>');
        });
    }).fail(function(jqXHR, textStatus, errorThrown) {
        console.error("Error al cargar el archivo JSON: ", textStatus, errorThrown);
    });
};