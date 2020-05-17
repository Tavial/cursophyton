
    function previewImage() {
        var reader = new FileReader();
        reader.readAsDataURL(document.getElementById('foto').files[0]);
        reader.onload = function (e) {
            document.getElementById('imagen').src = e.target.result;
        };
        const fi = document.getElementById('foto');
        // Se comprueba el fichero que es seleccionado
        if (fi.files.length > 0) {
            for (const i = 0; i <= fi.files.length - 1; i++) {

                const fsize = fi.files.item(i).size;
                const file = Math.round((fsize / 1024));
                // El tamaño del fichero
                if (file > 512) {
                    alert(
                      "Archivo demasiado grande. Por favor, escoge un archivo de menos de 0.5 MB");
                    fi.value =""; // Reseteamos el valor
                    fi.files[0].name="";
                }
            }
        }
    }
