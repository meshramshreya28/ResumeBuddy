const dragArea = document.getElementById('drag-area');

if (dragArea) {

    const input = dragArea.querySelector('input');

    // Drag Over
    dragArea.addEventListener('dragover', (e) => {

        e.preventDefault();

        dragArea.style.borderColor = '#8b5cf6';
        dragArea.style.background = 'rgba(255,255,255,0.08)';
    });

    // Drag Leave
    dragArea.addEventListener('dragleave', () => {

        dragArea.style.borderColor = 'rgba(255,255,255,0.3)';
        dragArea.style.background = 'transparent';
    });

    // Drop File
    dragArea.addEventListener('drop', (e) => {

        e.preventDefault();

        dragArea.style.borderColor = 'rgba(255,255,255,0.3)';
        dragArea.style.background = 'transparent';

        const files = e.dataTransfer.files;

        input.files = files;

        // Show selected file name
        if (files.length > 0) {

            document.getElementById('file-name').textContent =
            input.files[0].name;
        }
    });

    // Manual File Selection
    input.addEventListener('change', () => {

        if (input.files.length > 0) {

            document.getElementById('file-name').textContent =
            files[0].name;
        }
    });
}
/* Loading Animation */

const form = document.querySelector('form');

const loadingOverlay =
    document.getElementById('loadingOverlay');

if(form){

    form.addEventListener('submit', () => {

        loadingOverlay.style.display = 'flex';
    });
}
/* ===== MICRO INTERACTIONS ===== */

// Smooth card entry animation
document.querySelectorAll(".card").forEach((card, i) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(20px)";

    setTimeout(() => {
        card.style.transition = "0.5s ease";
        card.style.opacity = "1";
        card.style.transform = "translateY(0)";
    }, i * 100);
});