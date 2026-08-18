# Flask-Aula1

A minimal Flask web app used for an intro Flask class. The single entrypoint is `app.py`, which defines a handful of routes (`/`, `/sobre`, `/info`, `/bem-vindo`, `/bemvindo/<usuario>`, `/home`).

## Cursor Cloud specific instructions

- Dependencies: `pip install -r requirements.txt` (only Flask). This is already run on VM startup.
- Run the dev server: `python3 app.py`. It starts Werkzeug in debug mode with hot-reload on `0.0.0.0:5000`. There is no separate build step.
- There is no lint config or test suite in this repo; "verification" means hitting the routes (e.g. `curl http://localhost:5000/` returns `Olá, mundo!`).
- Note: `sobre.hmtl` is a standalone HTML file (note the misspelled extension) and is not served by any route; the `/sobre` route returns an inline string.
