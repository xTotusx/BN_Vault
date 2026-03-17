document.addEventListener("DOMContentLoaded", function() {
    const tipoField = document.querySelector("#id_tipo_item");

    function updateFields() {
        if (!tipoField) return;
        const val = tipoField.value;

        // Ocultar todos los bloques
        document.querySelectorAll(".grupo-cpu, .grupo-escaner, .grupo-monitor, .grupo-cajon, .grupo-impresora").forEach(el => {
            el.style.display = "none";
        });

        // Mostrar solo el que se eligió en el menú
        if (val === "CPU") {
            document.querySelectorAll(".grupo-cpu").forEach(el => el.style.display = "block");
        } else if (val === "ESCANER") {
            document.querySelectorAll(".grupo-escaner").forEach(el => el.style.display = "block");
        } else if (val === "MONITOR") {
            document.querySelectorAll(".grupo-monitor").forEach(el => el.style.display = "block");
        } else if (val === "CAJON") {
            document.querySelectorAll(".grupo-cajon").forEach(el => el.style.display = "block");
        } else if (val === "IMPRESORA") {
            document.querySelectorAll(".grupo-impresora").forEach(el => el.style.display = "block");
        }
    }

    if (tipoField) {
        tipoField.addEventListener("change", updateFields);
        updateFields(); 
    }
});