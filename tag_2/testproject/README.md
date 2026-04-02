Kurz, dann strukturiert:

## Was ist `uv`

`uv` ist ein schneller Python Package Manager + venv Tool (Rust-basiert).
Ersatz für: `pip`, `venv`, teilweise `poetry`.

→ Fokus: **Speed + reproducible environments + kein Activate nötig**

Website: Astral (Projekt `uv`)

---

## Installation

```powershell
pip install uv
```

Check:

```powershell
uv --version
```

---

## 1. Projekt erstellen

```powershell
uv init
```

Erzeugt:

* `pyproject.toml`
* Projektstruktur

Minimaler Inhalt:

```toml
[project]
name = "my-project"
version = "0.1.0"
dependencies = []
```

---

## 2. Paket hinzufügen

```powershell
uv add pandas
```

→ schreibt in `pyproject.toml`
→ installiert direkt in isolierter Umgebung

---

## 3. Paket entfernen

```powershell
uv remove pandas
```

→ entfernt aus:

* dependencies
* environment

---

## 4. Dependency Tree anzeigen

```powershell
uv tree
```

Beispiel:

```
pandas
├── numpy
└── python-dateutil
```

→ wichtig für:

* Debugging
* Verständnis von Abhängigkeiten

---

## 5. Environment synchronisieren

```powershell
uv sync
```

→ stellt sicher:

* Environment = exakt `pyproject.toml`

Use Cases:

* nach git pull
* nach manuellen Änderungen

```powershell
uv sync --frozen
```
## Bedeutung

Installiert Dependencies **exakt wie gelockt**, ohne etwas zu verändern.

→ nutzt Lockfile (`uv.lock`)

---

## Verhalten

* installiert **nur exakt definierte Versionen**
* **keine Updates**
* **keine Neuauflösung**
* Fehler, wenn:

  * `pyproject.toml` ≠ `uv.lock`

---

## Vergleich

| Command            | Verhalten                   |
| ------------------ | --------------------------- |
| `uv sync`          | darf Lockfile neu berechnen |
| `uv sync --frozen` | strikt reproduzierbar       |

---

## Wann verwenden

* CI/CD
* Produktion
* reproduzierbare Builds
---

## 6. Script ausführen

```powershell
uv run main.py
```

→ nutzt automatisch das richtige Environment

---

## Typischer Workflow (kompakt)

```powershell
uv init
uv add pandas
uv run main.py
```

