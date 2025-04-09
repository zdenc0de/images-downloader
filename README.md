# Revista Downloader

Este script en Python permite descargar todas las imágenes (páginas) de revistas alojadas en el sitio [revisteriaponchito.com](https://revisteriaponchito.com). Cada revista se descarga y guarda en una carpeta separada, con las imágenes ordenadas por página.

---

## Características

- Descarga automática de todas las páginas de una revista.
- Las imágenes se guardan como `01.jpg`, `02.jpg`, etc.
- Las revistas se almacenan en carpetas separadas según la URL.
- Soporte para múltiples descargas en paralelo (más rápido).
- Compatible con revistas como:
  - `https://revisteriaponchito.com/5x/3/`
  - `https://revisteriaponchito.com/5x/4/`
  - entre otras.

---

## Requisitos

- Python 3.x
- Librerías:
  - `requests`
  - `beautifulsoup4`

Puedes instalarlas con:

```bash
pip install requests beautifulsoup4
```

## Cómo usarlo
python magazines.py
El script creará carpetas como revista_5x_3 y descargará las imágenes dentro de ellas.

## Estructura de carpetas
revista-downloader/
├── .gitignore
├── README.md
├── magazines.py
└── revista_5x_3/
    ├── 01.jpg
    ├── 02.jpg
    └── ...

## Notas
El sitio tiene certificados SSL mal configurados, así que el script desactiva la verificación de seguridad (verify=False) para poder descargar las imágenes sin errores.

## Autor
Emilio Zdenko Abarca Cruz
Estudiante de Ingeniería en Computación
Universidad Autónoma del Estado de México
