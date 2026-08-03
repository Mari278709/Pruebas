/**
 * main.js - Lógica e Interactividad Portal ISTTE
 * Maneja el buscador predictivo de trámites y el filtrado del cronograma académico.
 */

document.addEventListener("DOMContentLoaded", function() {
    // ----------------------------------------------------
    // PREMIUM THEME TOGGLE
    // ----------------------------------------------------
    const themeCheckboxes = document.querySelectorAll('.theme-switch-input');
    
    function applyTheme(theme) {
        if (theme === 'light') {
            document.documentElement.setAttribute('data-theme', 'light');
            document.documentElement.setAttribute('data-bs-theme', 'light');
            themeCheckboxes.forEach(cb => cb.checked = true);
        } else {
            document.documentElement.removeAttribute('data-theme');
            document.documentElement.setAttribute('data-bs-theme', 'dark');
            themeCheckboxes.forEach(cb => cb.checked = false);
        }
    }

    // Cargar preferencia
    const savedTheme = localStorage.getItem('istte-theme');
    if (savedTheme) {
        applyTheme(savedTheme);
    }

    // Escuchar el switch
    themeCheckboxes.forEach(cb => {
        cb.addEventListener('change', function(e) {
            const newTheme = e.target.checked ? 'light' : 'dark';
            applyTheme(newTheme);
            localStorage.setItem('istte-theme', newTheme);
        });
    });
    // ----------------------------------------------------
    // Inicializar componentes interactivos
    initSearchTramites();
    initFilterAgenda();
    initFormValidation();
});

/**
 * Módulo de búsqueda en tiempo real para Trámites en Línea
 */
function initSearchTramites() {
    const searchInput = document.getElementById('search-tramites');
    const cards = document.querySelectorAll('.card-tramite-container');
    const noResultsMsg = document.getElementById('no-tramites-message');
    
    if (!searchInput || cards.length === 0) return;
    
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        let visibleCount = 0;
        
        cards.forEach(card => {
            const title = card.querySelector('.tramite-title').textContent.toLowerCase();
            const desc = card.querySelector('.tramite-description').textContent.toLowerCase();
            
            // Comprobar si coincide con título o descripción
            if (title.includes(query) || desc.includes(query)) {
                card.style.display = 'block';
                // Añadir micro-animación de entrada al reaparecer
                card.classList.add('animate-fade-in');
                visibleCount++;
            } else {
                card.style.display = 'none';
                card.classList.remove('animate-fade-in');
            }
        });
        
        // Mostrar mensaje si no hay resultados
        if (noResultsMsg) {
            if (visibleCount === 0) {
                noResultsMsg.classList.remove('d-none');
            } else {
                noResultsMsg.classList.add('d-none');
            }
        }
    });
}

/**
 * Módulo de filtrado por categoría para Agenda Académica
 */
function initFilterAgenda() {
    const filterButtons = document.querySelectorAll('.btn-filter-istte');
    const timelineItems = document.querySelectorAll('.timeline-item');
    const noEventsMsg = document.getElementById('no-events-message');
    
    if (filterButtons.length === 0 || timelineItems.length === 0) return;
    
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remover clase activa de todos los botones
            filterButtons.forEach(btn => btn.classList.remove('active'));
            
            // Añadir clase activa al presionado
            button.classList.add('active');
            
            const category = button.getAttribute('data-filter');
            let visibleCount = 0;
            
            timelineItems.forEach(item => {
                const itemCategory = item.getAttribute('data-category');
                
                if (category === 'all' || itemCategory === category) {
                    item.style.display = 'block';
                    visibleCount++;
                } else {
                    item.style.display = 'none';
                }
            });
            
            // Mostrar mensaje si no hay eventos en la categoría seleccionada
            if (noEventsMsg) {
                if (visibleCount === 0) {
                    noEventsMsg.classList.remove('d-none');
                } else {
                    noEventsMsg.classList.add('d-none');
                }
            }
        });
    });
}

/**
 * Módulo de validación e interactividad en formularios (Inscripción y Contacto)
 */
function initFormValidation() {
    const forms = [
        { id: 'form-inscripcion', alertId: 'alert-insc-success' },
        { id: 'form-contacto', alertId: 'alert-contacto-success' }
    ];
    
    forms.forEach(item => {
        const formEl = document.getElementById(item.id);
        const alertEl = document.getElementById(item.alertId);
        
        if (!formEl) return;
        
        formEl.addEventListener('submit', (e) => {
            e.preventDefault();
            e.stopPropagation();
            
            if (formEl.checkValidity()) {
                // Formulario es válido, simular envío
                const submitBtn = formEl.querySelector('button[type="submit"]');
                const originalText = submitBtn.innerHTML;
                
                // Deshabilitar botón y mostrar spinner/loading
                submitBtn.disabled = true;
                submitBtn.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Enviando...`;
                
                setTimeout(() => {
                    // Restablecer botón
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;
                    
                    // Mostrar alerta de éxito con animación
                    if (alertEl) {
                        alertEl.classList.remove('d-none');
                        alertEl.style.opacity = '0';
                        alertEl.style.transition = 'opacity 0.5s ease';
                        // Forzar reflow
                        alertEl.offsetHeight;
                        alertEl.style.opacity = '1';
                        
                        // Auto-scroll hacia la alerta
                        alertEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                    
                    // Resetear formulario y clases de validación
                    formEl.reset();
                    formEl.classList.remove('was-validated');
                    
                    // Ocultar alerta después de 5 segundos
                    setTimeout(() => {
                        if (alertEl) {
                            alertEl.style.opacity = '0';
                            setTimeout(() => {
                                alertEl.classList.add('d-none');
                            }, 500);
                        }
                    }, 5000);
                    
                }, 1500);
            } else {
                formEl.classList.add('was-validated');
            }
        });
    });
}
