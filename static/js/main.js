/**
 * main.js - Lógica e Interactividad Portal ISTTE
 * Maneja el buscador predictivo de trámites y el filtrado del cronograma académico.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Inicializar componentes interactivos
    initPreloader();
    initSearchTramites();
    initFilterAgenda();
    initFormValidation();
    initScrollReveal();
    initDarkMode();
});

/**
 * Animación de aparición progresiva al hacer scroll
 */
function initScrollReveal() {
    const elements = document.querySelectorAll('.reveal-on-scroll');
    const counters = document.querySelectorAll('.counter-number');

    if (!elements.length && !counters.length) return;

    if (typeof IntersectionObserver === 'undefined') {
        elements.forEach((element) => element.classList.add('is-visible'));
        counters.forEach((counter) => animateCounter(counter));
        return;
    }

    const revealObserver = new IntersectionObserver((entries, obs) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;

            const target = entry.target;
            target.classList.add('is-visible');
            obs.unobserve(target);
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -8% 0px'
    });

    const counterObserver = new IntersectionObserver((entries, obs) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;

            const counterValue = entry.target;
            const delay = Number(counterValue.getAttribute('data-delay') || 0);

            window.setTimeout(() => {
                animateCounter(counterValue);
            }, delay);

            obs.unobserve(counterValue);
        });
    }, {
        threshold: 0.2,
        rootMargin: '0px 0px -5% 0px'
    });

    elements.forEach((element, index) => {
        const delay = element.getAttribute('data-delay');
        const normalizedDelay = delay ? Number(delay) : index * 80;
        element.style.transitionDelay = `${Math.min(normalizedDelay, 500)}ms`;
        revealObserver.observe(element);
    });

    counters.forEach((counter) => {
        counterObserver.observe(counter);
    });
}

function animateCounter(counterValue) {
    if (!counterValue || counterValue.dataset.animated === 'true') return;

    const targetValue = Number(counterValue.getAttribute('data-target') || 0);
    const suffix = counterValue.getAttribute('data-suffix') || '';
    const duration = 1400;
    const startTime = performance.now();

    counterValue.dataset.animated = 'true';
    counterValue.textContent = '0';
    counterValue.style.transform = 'scale(0.9)';
    counterValue.style.opacity = '0.7';

    const step = (now) => {
        const progress = Math.min((now - startTime) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const currentValue = Math.round(targetValue * eased);

        counterValue.textContent = `${currentValue}${suffix}`;
        counterValue.style.transform = `scale(${0.9 + (progress * 0.1)})`;
        counterValue.style.opacity = `${0.7 + (progress * 0.3)}`;

        if (progress < 1) {
            requestAnimationFrame(step);
        } else {
            counterValue.textContent = `${targetValue}${suffix}`;
            counterValue.style.transform = 'scale(1)';
            counterValue.style.opacity = '1';
        }
    };

    requestAnimationFrame(step);
}

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

/**
 * Inicializa y controla el estado del Modo Oscuro
 */
function initDarkMode() {
    const toggleBtn = document.getElementById('theme-toggle');
    if (!toggleBtn) return;

    // Comprobar la preferencia guardada o el esquema del sistema
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Aplicar el estado inicial
    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
        document.body.classList.add('dark-mode');
        toggleBtn.classList.add('active');
    } else {
        document.body.classList.remove('dark-mode');
        toggleBtn.classList.remove('active');
    }

    // Escuchar el evento click para alternar el modo
    toggleBtn.addEventListener('click', () => {
        const isDarkMode = document.body.classList.toggle('dark-mode');
        toggleBtn.classList.toggle('active', isDarkMode);
        
        // Guardar la preferencia
        localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
    });
}

/**
 * Controla la pantalla de carga inicial (Preloader)
 */
function initPreloader() {
    const preloader = document.getElementById('preloader');
    if (!preloader) return;

    // Lógica para desvanecer el preloader
    const fadeOutPreloader = () => {
        setTimeout(() => {
            preloader.classList.add('fade-out');
        }, 350); // Pequeña demora para un efecto visual suave
    };

    if (document.readyState === 'complete') {
        fadeOutPreloader();
    } else {
        window.addEventListener('load', fadeOutPreloader);
    }
}
