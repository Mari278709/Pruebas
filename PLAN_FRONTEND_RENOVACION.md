# 🎨 Plan de Renovación de Frontend — Portal ISTTE

> **Objetivo:** Modernizar el frontend del portal institucional del **Instituto Tecnológico Superior Tecnoecuatoriano (ISTTE)** hasta un nivel **premium, dinámico y profesional**, fusionando el "ADN de diseño" de institutos/universidades de referencia — **sin rehacer la app desde cero ni migrar a React/SPA**.

---

## 1. Resumen ejecutivo

El portal ISTTE es una app **Django (server-side rendering)** con ~31 páginas institucionales, plantillas Bootstrap 5 + Bootstrap Icons + AOS + **Alpine.js (ya cargado)** + `custom.css` (~1.370 líneas) + `main.js` (vanilla JS). La lógica y el contenido están listos; el problema es **visual y de experiencia**, no de arquitectura.

**Propuesta:** renovación en 3 ejes, todos compatibles con tus plantillas Django actuales:

1. **Visual — "Editorial-Tech Premium":** fusión de estilos de 5 referencias (TEC Monterrey, ESPOL, Uniandes, INTEC, EPFL) sobre tu marca azul/verde ISTTE.
2. **Interactividad — HTMX + Alpine.js:** dinamismo tipo app moderna (búsquedas, formularios, filtros, carrusel) **sin API ni build, sin Node, sin React**.
3. **Componentización — design system reutilizable:** limpiar el CSS repetido y crear componentes consistentes en las 31 páginas.

> ✅ **No se reescribe la app.** Se conservan Django templates, URLs, vistas, modelos y forms. Se renueva la capa de presentación y se añade interactividad incremental con HTMX.

---

## 2. Diagnóstico del estado actual

| Aspecto | Estado actual | Observación |
|---|---|---|
| Arquitectura | Django 5 + templates SSR | ✅ Sólida, no se toca |
| CSS framework | Bootstrap 5.3.2 (CDN) | Bueno, pero `custom.css` creció a ~1.370 líneas dispersas |
| JS | Vanilla `main.js` + **Alpine.js ya cargado** + AOS | Alpine presente = ya tienes el 50% del patrón moderno |
| Tipografía | Outfit + Caveat | Moderna; Caveat resta seriedad institucional |
| Paleta | Azul `#0b3a6f` + Verde `#2eb62e` | Correcta, falta jerarquía y tokens consistentes |
| Hero | `index.html` con esferas/glow + `hero-girl.png` | Visualmente denso; le falta impacto editorial |
| Navegación | Navbar + offcanvas + dropdowns | Funcional, sin mega-menú con previews |
| Componentes | Cards, carrusel, tabs organigrama | Base correcta; necesitan pulido visual |
| Formularios | `forms.py` (inscripción, contacto) | Ideales para HTMX (envío sin recargar) |
| Interactividad | Búsqueda trámites + filtros agenda (JS vanilla) | Candidatos claros a HTMX |
| Accesibilidad | Focus verde, contraste razonable | Mejorable (semántica, ARIA, dark mode) |
| Mobile | Offcanvas, responsive básico | Revisar jerarquía móvil |

---

## 3. Objetivos

- **V1 — Primera impresión:** hero cinematográfico que transmita "instituto tecnológico moderno".
- **V2 — Navegación fluida:** mega-menú con previews, transiciones sin parpadeo (HTMX).
- **V3 — Coherencia visual:** design system con tokens únicos (color, tipo, espacio, sombra, radio).
- **V4 — Dinamismo sutil:** animaciones de scroll (AOS), contadores, hover premium, reveal.
- **V5 — Interactividad real:** formularios y búsquedas que respondan sin recargar (HTMX + Alpine).
- **V6 — Accesibilidad y rendimiento:** contraste AA, semántica HTML, lazy-load, CSS optimizado.
- **V7 — Mantenibilidad:** componentes reutilizables, menos CSS duplicado.

---

## 4. Referencias de inspiración (ADN de diseño a fusionar)

No se copian estilos a ciegas: se extrae **qué hace que cada una se sienta premium** y se adapta a la marca ISTTE.

| # | Referencia | Qué tomar (fusionar) | Cómo se adapta a ISTTE |
|---|---|---|---|
| 1 | **TEC de Monterrey** (`tec.mx`) | Hero editorial a pantalla completa + overlay degradado; **mega-menú con tarjetas-preview**; tarjetas de programas con hover elegante; **stats con contadores animados**; tipografía sans moderna; paleta navy + acento. | Hero cinematográfico en `index.html`; mega-menú en `base.html`; stats ISTTE (egresados, empleabilidad, carreras). |
| 2 | **ESPOL** (`espol.edu.ec`) | Relevancia cultural ecuatoriana; **navegación por audiencias**; grilla de carreras; sección de noticias; footer institucional completo. | Estructura de carreras adaptada a tus 4 carreras (software, ciberseguridad, administración, conducción); footer más rico. |
| 3 | **Universidad de los Andes** (`uniandes.edu.co`) | **Tipografía editorial fuerte**; layouts asimétricos; **tarjetas con imágenes grandes**; espacio en blanco generoso; micro-interacciones sutiles. | Más respiración visual; tarjetas de noticias/servicios con imágenes dominantes; jerarquía tipográfica clara. |
| 4 | **INTEC** (`intec.edu.do`) | Instituto tecnológico latino; **admisiones destacadas con CTAs verdes**; badges; **carrusel de testimonios/egresados**. | Refuerzo de admisiones con CTA verde (`--istte-green-accent`); sección de testimonios de egresados. |
| 5 | **EPFL** (`epfl.ch`) | **Minimalismo suizo**; grilla precisa; acento de color único; tipografía neutra; **claridad y accesibilidad**. | Limpieza de `custom.css`, grilla consistente, accesibilidad AA, acento verde bien dosificado. |

### Concepto de fusión: **"Editorial-Tech Premium"**
- **Cinemático + editorial** (TEC + Andes) en el hero y páginas clave.
- **Claridad institucional ecuatoriana** (ESPOL + INTEC) en carreras, admisiones y footer.
- **Precisión y accesibilidad suiza** (EPFL) en el sistema de diseño global.
- Todo sobre tu **marca ISTTE** (azul `#0b3a6f` + verde `#2eb62e`).

---
## 5. Stack técnico recomendado (sin React, sin build obligatorio)

```
Django 5 (SSR)  ← NO se toca la arquitectura
├─ Templates (base.html + 31 páginas) ← se renuevan
├─ Vistas → devuelven HTML (partial-friendly para HTMX)
└─ forms.py (inscripción, contacto)

Capa de presentación (lo que renovamos):
├─ Bootstrap 5 (base, se conserva) + Design System propio
├─ Bootstrap Icons (conserva)
├─ AOS (animaciones scroll — ya está)
├─ Alpine.js (interactividad declarativa — ya está)
└─ HTMX (interactividad server-driven — NUEVO, vía CDN)

Sin: Node, Webpack/Vite, React, DRF/API JSON
```

**Decisión clave sobre CSS (dos caminos):**
- **Camino 1 (recomendado, menor riesgo):** conservar Bootstrap + rediseñar `custom.css` como design system robusto + componentes a medida. Cero reescritura de las 31 páginas.
- **Camino 2 (más "look 2025", más esfuerzo):** migrar a **Tailwind + DaisyUI**. Visual muy premium rápido, pero requiere tocar las clases de las 31 plantillas.

> En este plan proponemos el **Camino 1** para Fase 1–2 (impacto rápido, bajo riesgo) y dejamos el Camino 2 como evolución opcional en Fase 4.

**HTMX (lo que da el "feeling React" sin React):**
- Se añade `htmx.min.js` por CDN en `base.html` (1 línea).
- Las vistas Django siguen devolviendo HTML; HTMX intercambia fragmentos.
- Casos puntuales (no toda la app): búsqueda de trámites, envío de formularios, filtros de agenda, paginación de noticias, detalle de carrera.

---

## 6. Sistema de diseño (design tokens) — la fusión visual

### 6.1 Paleta fusionada (sobre la marca ISTTE)

```css
:root {
  /* Primarios — azul institucional */
  --istte-blue-primary: #0b3a6f;
  --istte-blue-dark:    #04213a;
  --istte-blue-darker:  #021122;
  --istte-blue-sky:     #08315a;
  --istte-blue-50:      #E6F0FB;
  --istte-blue-100:     #C9DBF2;

  /* Acento — verde (CTA, énfasis) */
  --istte-green:        #2eb62e;
  --istte-green-hover:  #1f8a28;
  --istte-green-soft:   rgba(124,232,39,0.15);

  /* Neutros (editorial, tipo Andes/EPFL) */
  --istte-ink:          #0E1B32;
  --istte-ink-soft:     #44546a;
  --istte-muted:        #8a99ad;
  --istte-line:         #e3e9f2;
  --istte-surface:      #ffffff;
  --istte-surface-alt:  #F6F9FF;
  --istte-surface-dark: #08172F;

  /* Estado */
  --istte-success:#2eb62e; --istte-warning:#f4b740;
  --istte-danger:#e23c4d;  --istte-info:#2f6fed;

  /* Sombras (suaves/editoriales) */
  --shadow-xs:0 1px 2px rgba(14,27,50,.06);
  --shadow-sm:0 4px 12px rgba(14,27,50,.08);
  --shadow-md:0 10px 28px rgba(14,27,50,.10);
  --shadow-lg:0 24px 60px rgba(14,27,50,.16);
  --shadow-blue:0 16px 40px rgba(11,58,111,.28);

  /* Radios */
  --radius-sm:10px; --radius-md:16px;
  --radius-lg:24px; --radius-pill:999px;

  /* Espaciado */
  --space-1:.25rem; --space-2:.5rem; --space-3:1rem;
  --space-4:1.5rem; --space-5:2rem; --space-6:3rem;
  --space-7:4rem;  --space-8:6rem;

  /* Tipografía */
  --font-sans:'Outfit', system-ui, -apple-system, sans-serif;
  --font-display:'Outfit', system-ui, sans-serif;
  /* Caveat se elimina o se reserva SOLO para acentos muy puntuales */

  --ease:cubic-bezier(.4,0,.2,1);
  --t-fast:.18s var(--ease); --t-base:.28s var(--ease);
  --container-max:1200px;
}
```

### 6.2 Tipografía — jerarquía editorial

| Elemento | Familia | Peso | Tamaño (desktop) |
|---|---|---|---|
| Display / H1 hero | Outfit | 800 | clamp(2.6rem, 5vw, 4.2rem) |
| H2 sección | Outfit | 700 | clamp(2rem, 3vw, 2.8rem) |
| H3 | Outfit | 600 | 1.5rem |
| H4 / card title | Outfit | 600 | 1.15rem |
| Lead / subtítulo | Outfit | 400 | 1.15rem, line-height 1.6 |
| Cuerpo | Outfit | 400 | 1rem, line-height 1.7 |
| Caption/meta | Outfit | 500 | .85rem, uppercase, letter-spacing .04em |

> **Decisión:** eliminar el uso decorativo de *Caveat* en títulos principales (resta seriedad institucional). Mantener *Outfit* como única familia para coherencia premium.

### 6.3 Principios visuales de la fusión

1. **Respiración:** más espacio en blanco (tipo Andes/EPFL). Secciones con `padding: var(--space-7)`.
2. **Una grilla, un ritmo:** contenedor `max-width 1200px`, grilla de 12 columnas consistente.
3. **Acento único:** el verde se usa **solo para CTAs y énfasis** (no decorativo por todas partes).
4. **Imagen dominante:** tarjetas con foto grande arriba (tipo Andes/TEC).
5. **Bordes suaves + sombras suaves:** radios `16–24px`, sombras `--shadow-sm/md`.
6. **Micro-interacciones:** hover con `translateY(-6px)` + sombra `--shadow-lg`; reveal con AOS.
7. **Modo oscuro opcional** en footer/header (ya tienes fondo oscuro).

---

## 7. Componentes UI a crear o reformar

Lista de componentes del design system (todos sobre Bootstrap + `custom.css`):

| Componente | Estado | Acción | Inspiración |
|---|---|---|---|
| **Hero cinematográfico** | Reformar | Overlay degradado azul, headline editorial, CTA verde + secundario, imagen/video lateral, badges de features | TEC + Andes |
| **Mega-menú con previews** | Nuevo | Dropdowns anchos con tarjetas-icono por sección | TEC |
| **Navbar premium** | Reformar | Sticky con blur, shrink al hacer scroll, logo + menú + CTA verde | TEC + EPFL |
| **Tarjeta de carrera/programa** | Reformar | Imagen dominante, título, tag de modalidad, hover lift | ESPOL + Andes |
| **Tarjeta de noticia/servicio** | Reformar | Imagen grande, fecha, badge de categoría, leer más | Andes |
| **Sección de stats (contadores)** | Nuevo | 4 KPIs con animación de conteo al hacer scroll | TEC |
| **Sección de testimonios** | Nuevo | Carrusel de egresados con foto + cita | INTEC |
| **Línea de tiempo / agenda** | Reformar | Filtros por categoría (HTMX), diseño vertical moderno | ESPOL |
| **Buscador de trámites** | Reformar | Input con resultados en vivo (HTMX), tarjetas filtradas | TEC |
| **Formulario premium** | Reformar | Campos flotantes, validación server-side (HTMX), estados loading/éxito | EPFL |
| **Carrusel de noticias** | Reformar | Cards más amplias, controles rediseñados, autoplay suave | INTEC |
| **Tabs (organigrama)** | Reformar | Estilo premium, transiciones suaves | EPFL |
| **Footer institucional** | Reformar | 4 columnas: marca, enlaces, contacto, redes + legal | ESPOL |
| **Botón flotante WhatsApp** | Conservar | Pulir sombra y hover | — |
| **Breadcrumbs** | Nuevo | Navegación contextual en subpáginas | EPFL |
| **Badges / chips** | Nuevo | Categorías, modalidades, estados | INTEC |
| **Sección CTA banner** | Nuevo | Banda azul/verde con CTA "Inscríbete" entre secciones | TEC |

---

## 8. Plan por páginas (las 31 + base)

### 8.1 Shell común (`base.html`) — prioridad 1
- Navbar premium + mega-menú con previews (5 secciones).
- Footer institucional de 4 columnas.
- Breadcrumbs dinámicos por página (block opcional).
- Añadir HTMX vía CDN + Alpine (ya está) + AOS (ya está).
- Contenedor unificado `--container-max`.

### 8.2 Inicio (`index.html`) — prioridad 1
- Hero cinematográfico (TEC).
- Stats con contadores animados (egresados, empleabilidad, carreras, años).
- Grilla de 4 carreras con tarjetas premium.
- Sección "Por qué ISTTE" con iconos.
- CTA banner "Inscríbete".
- Carrusel de noticias rediseñado.
- Testimonios de egresados (carrusel).

### 8.3 Carreras (`carreras`, `detalle_carreras`, `registro_carreras`) — prioridad 2
- Grilla de carreras con tarjetas imagen-dominante.
- Detalle: hero de carrera, malla curricular (accordion), perfil de egreso, campo laboral (tabs HTMX).
- Registro: formulario premium con HTMX.

### 8.4 Admisiones (`proceso_admision`, `becas_incentivos`, `inscripcion`, `validacion_experiencia`) — prioridad 2
- Stepper visual del proceso de admisión.
- Tabla de requisitos/fechas premium.
- Becas: tarjetas con ícono + monto + requisitos.
- Inscripción: form multi-paso con HTMX (validación server-side, progreso).
- Validación de experiencia: form + carga de documentos.

### 8.5 Institucional (`presentacion_institucional`, `autoridades`, `organigrama`, `planificacion_estrategica`, `aseguramiento_calidad`, `transparencia`, `gaceta_institucional`) — prioridad 3
- Plantilla "página institucional" reutilizable: hero compacto + sidebar + contenido + descargas.
- Autoridades: tarjetas de equipo con foto + cargo.
- Organigrama: árbol visual interactivo (tabs ya existe → pulir).
- Transparencia/Gaceta: listado de documentos con búsqueda HTMX.

### 8.6 Unidades académicas (`bienestar`, `vinculacion`, `investigacion`, `tecno_informativo`, `cec_tecno`, `unidad_titulacion`, `asociacion_graduados`) — prioridad 3
- Plantilla "unidad" reutilizable: hero + presentación + servicios (cards) + galería + contacto.
- Investigación: líneas + proyectos (cards).
- Asociación de graduados: registro + beneficios.

### 8.7 Servicios y multimedia (`biblioteca`, `soporte_tecnico`, `portal_empleo`, `sedes_campus`, `multimedia`, `upload_media`) — prioridad 3
- Biblioteca: catálogo con buscador HTMX.
- Portal de empleo: ofertas con filtros HTMX.
- Sedes: mapa + tarjetas de campus.
- Multimedia: galería filtrable (noticias/videos) con HTMX y paginación.
- Upload media: panel admin pulido.

### 8.8 Legal y contacto (`contacto`, `aviso_legal`, `politica_privacidad`) — prioridad 3
- Contacto: form premium HTMX + mapa + datos.
- Legal: plantilla de texto legal limpio.

> **Plantillas reutilizables a crear** (vía `{% include %}` / bloques): `_hero_compacto.html`, `_seccion_stats.html`, `_tarjeta_carrera.html`, `_tarjeta_noticia.html`, `_cta_banner.html`, `_testimonios.html`, `_breadcrumbs.html`. Esto reduce el CSS duplicado y acelera el rediseño de las 31 páginas.

---

## 9. Fases de implementación (roadmap)

### Fase 0 — Preparación (0.5 día)
- Crear rama `feature/frontend-renovacion` (git).
- Backups de `custom.css`, `base.html`, `main.js`.
- Añadir HTMX vía CDN en `base.html`.
- Definir tokens en nuevo `design-tokens.css` (importado antes que `custom.css`).

### Fase 1 — Fundación visual (1–2 días) ⭐ impacto alto
- Rediseñar `base.html`: navbar premium + mega-menú + footer 4 columnas + breadcrumbs.
- Aplicar tokens y tipografía editorial.
- Plantillas reutilizables: `_hero_compacto`, `_cta_banner`, `_breadcrumbs`, `_tarjeta_noticia`.

### Fase 2 — Home de impacto (1–2 días) ⭐ impacto alto
- `index.html`: hero cinematográfico, stats con contadores, grilla de carreras, CTA, carrusel noticias, testimonios.
- Demo visible: primera impresión premium.

### Fase 3 — Interactividad HTMX (1–2 días)
- Búsqueda de trámites en vivo (partial en `views.py` + template `_resultados_tramites.html`).
- Filtros de agenda (partial).
- Formularios inscripción/contacto con validación server-side y mensajes parciales.
- Carrusel/multimedia paginado.

### Fase 4 — Páginas prioritarias (2–3 días)
- Carreras + detalle + registro.
- Admisiones (stepper, becas, inscripción multi-paso).

### Fase 5 — Páginas restantes (2–4 días)
- Institucional, unidades, servicios, legal — usando las plantillas reutilizables.

### Fase 6 — Pulido y QA (1 día)
- Accesibilidad AA, responsive, performance (lazy-load, CSS crítico), pruebas cross-browser.
- (Opcional) evolución a Tailwind+DaisyUI si se desea el "look 2025" total.

**Total estimado:** ~8–14 días según profundidad.

---

## 10. Entregables por fase
- **Fase 0:** `design-tokens.css`, HTMX integrado, rama git.
- **Fase 1:** `base.html` renovado, mega-menú, footer, plantillas `_*.html`.
- **Fase 2:** `index.html` premium + `main.js` (contadores, reveal).
- **Fase 3:** vistas partials + formularios HTMX.
- **Fase 4–5:** 31 páginas rediseñadas.
- **Fase 6:** informe de accesibilidad/performance + ajustes.

---

