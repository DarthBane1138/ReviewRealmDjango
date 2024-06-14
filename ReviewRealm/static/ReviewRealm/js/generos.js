function updateGeneros(checkbox) {
    const generosInput = document.getElementById('generos');
    let generosSeleccionados = generosInput.value ? generosInput.value.split(',') : [];

    if (checkbox.checked) {
        generosSeleccionados.push(checkbox.value);
    } else {
        generosSeleccionados = generosSeleccionados.filter(genero => genero !== checkbox.value);
    }

    generosInput.value = generosSeleccionados.join(',');
}