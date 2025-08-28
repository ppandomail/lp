# Pa11y

* Es una herramienta gratuita y de código abierto que permite ejecutar pruebas de AW a través de línea de comandos o Node.js
* Ayuda a diseñadores y desarrolladores a hacer páginas web accesibles.
* Toma como fuentes las WCAG 2.0 [HTML-CodeSniffer](https://squizlabs.github.io/HTML_CodeSniffer/)
* El informe muestra los errores con información de que principios de las WCAG se están violando.
* No hay un link directo a ninguna documentación.
* URL: [pa11y](https://github.com/pa11y/pa11y)
* Links:
  * [Tutorial pa11y](https://webdesign.tutsplus.com/es/tutorials/web-accessibility-testing-via-the-command-line-with-pa11y--cms-34538)
  * [Pruebas de AW con pa11y](https://bitsofco.de/pa11y/)
  * [AW con Travis CI](https://cruft.io/posts/automated-accessibility-testing-node-travis-ci-pa11y/)

## Instalación pa11y

* Requiere Node.js 12+

```sh
# Instalación global en la máquina
$npm install -g pa11y
```

```sh
# Instalación en el proyecto
$mkdir <nom_proy>
$cd <nom_proy>
$npm init -y
$npm install pa11y
```

```json
// Modificar el archivo package.json agregándole el siguiente script:
"scripts": {
  "start": "pa11y"
}
```

## Ejecución pa11y por línea de comando

  ```sh
  # Default: standard:WCAG2AA y reporter:cli
  # Acepta como entrada url o file
  $npm start https://example.com
  ```

  ```sh
  # Niveles de AW: WCAG2A, WCAG2AA, WCAG2AAA 
  $npm start -- --standard WCAG2A https://example.com
  ```

  ```sh
  # Reportes: cli, csv, json, html
  $npm start -- --reporter csv https://example.com > report.csv
  ```

  ```sh
  # Ignorar tipos de mensajes: 
  # notice (aviso general, ejemplo: Verifique que el elemento del título describa el documento)
  # warning (advertencia, ejemplo: El elemento img esta marcado para que la tecnología de asistencia lo ignore)
  # error (problema, ejemplo: Este elemento de entrada de texto no tiene un nombre disponible para una API de accesibilidad)
  $npm start -- --ignore "warning;notice" https://example.com
  ```

  ```sh
  # Umbral de fallas: cant de mensajes que deben permitirse para que la página "pase" la prueba de AW.
  # En este caso devolverá 0 (no hay errores) en una página con 9 errores.
  $npm start -- --threshold 10 https://example.com
  ```

  ```sh
  # Oculta elementos (ejemplo widgets de terceros) usando CSS selector
  $npm start -- --hide-elements "#ads .sr-only [aria-role='presentation']" https://example.com
  ```

### Ejemplo [Sitio AFIP](https://www.afip.gob.ar/landing/default.asp)

  ```sh
  $npm start https://www.afip.gob.ar/landing/default.asp

  > a11y-pa11y@1.0.0 start
  > pa11y "https://www.afip.gob.ar/landing/default.asp"


  Welcome to Pa11y

  > Running Pa11y on URL https://www.afip.gob.ar/landing/default.asp

  Results for URL: https://www.afip.gob.ar/landing/default.asp

  • Error: This element has insufficient contrast at this conformance level. Expected a contrast ratio of at least 4.5:1, but text in this element has a contrast ratio of 3.03:1. Recommendation:  change background to #007eb4.
    ├── WCAG2AA.Principle1.Guideline1_4.1_4_3.G18.Fail
    ├── #cajaClaveFiscal > div:nth-child(2) > a > span
    └── <span>Iniciar sesión</span>

  • Error: This element has insufficient contrast at this conformance level. Expected a contrast ratio of at least 4.5:1, but text in this element has a contrast ratio of 3.03:1. Recommendation:  change background to #007eb4.
    ├── WCAG2AA.Principle1.Guideline1_4.1_4_3.G18.Fail
    ├── #lnkNovedades > span
    └── <span class="small">Ver todas las novedades</span>

  2 Errors
  ```

### Ejemplo [Sitio Accessible University](https://www.washington.edu/accesscomputing/AU/before.html)

![Reporte cli](img/pa11y.png)

## Ejecución pa11y programáticamente

* Debido a que Pa11y se basa en promesas, puede usar funciones async y la palabra clave await

  ```javascript
  async function runPa11y() {
      try {
          const results = await pa11y('https://example.com/');
          // Do something with the results
      } catch (error) {
          // Handle the error
      }
  }
  runPa11y()
  ```

* El objeto **results** contiene detalles sobre la página y problemas de accesibilidad de HTML CodeSniffer:

  ```plain
  {
      documentTitle: 'The title of the page that was tested',
      pageUrl: 'The URL that Pa11y was run against',
      issues: [
          {
              code: 'WCAG2AA.Principle1.Guideline1_1.1_1_1.H30.2',
              context: '<a href="https://example.com/"><img src="example.jpg" alt=""/></a>',
              message: 'Img element is the only content of the link, but is missing alt text. The alt text should describe the purpose of the link.',
              selector: 'html > body > p:nth-child(1) > a',
              type: 'error',
              typeCode: 1
          }
          // more issues appear here
      ]
  }
  ```

### Ejemplo JS

  ```javascript
  'use strict';

  const pa11y = require('pa11y');

  runExample();

  async function runExample() {
    try {
      const result = await pa11y('https://example.com', 
      {
        hideElements: '.advert, #modal, div[aria-role=presentation]', // selectores CSS para ocultar elementos de las pruebas
        ignore: [
          'WCAG2AA.Principle4.Guideline4_1.4_1_1.F77'
        ],
        includeNotices: true,     // default false
        includeWarnings: true,    // default false  
        log: {                    // para informar errores
          debug: console.log,
          error: console.error,
          info: console.info
        },
        rootElement: '#app',     // testear un subset de la page en oposición al documento completo. Default es null, es decir, se probará el documento completo
        rules: [                // pautas de WCAG2.1 a incluir en el stándar actual
           'Principle1.Guideline1_3.1_3_1_AAA'
        ]
        screenCapture: '/e.png', // ruta de archivo para guardar una captura de pantalla de la página probada
        standard: 'WCAG2A',      // default 'WCAG2AA'
        timeout: 5000,           // default 30000 milseg tiempo de espera para la ejecución de la prueba completa (incluido el tiempo para inicializar Chrome, cargar la página y ejecutar las pruebas)
        viewport: {              // configuración de la ventana gráfica
          width: 320,            // default: 1280
          height: 480,           // default: 1024
          deviceScaleFactor: 2,
          isMobile: true
        },
        wait: 500,               // tiempo en milisegundos de espera antes de ejecutar HTML CodeSniffer en la página. Default es 0
        actions: [               // interacciones antes de ejecutar las pruebas
          'click element #tab-1',
          'wait for element #tab-1-content to be visible',
          'set field #fullname to Pablo Pandolfo',
          'clear field #middlename',
          'check field #terms-and-conditions',
          'uncheck field #subscribe-to-marketing',
          'screen capture example.png',
          'wait for fragment to be #page-2',
          'wait for path to not be /login',
          'wait for url to be https://example.com/',
          'wait for #my-image to emit load',
          'navigate to https://another-example.com/'
        ]
      });
          console.log(result);
    } catch (error) {
      console.error(error.message);
    }
  }
  ```

* Ejecución del script

```json
...
"scripts": {
  ...
  "start-basic": "node index-basic.js",
}
...
```

```sh
$npm run start-basic
```
