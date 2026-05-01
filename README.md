# Validador de DNI español

Herramienta de línea de comandos para validar DNIs españoles.
Comprueba que la letra corresponde con la parte numérica usando el algoritmo oficial.

## Uso

**Modo interactivo:**
```bash
python dni.py
```

**Pasando el DNI directamente:**
```bash
python dni.py 12345678Z
```

## Cómo funciona

El algoritmo divide el número entre 23 y usa el resto para buscar
la letra correspondiente en la tabla oficial:

## Tecnologías

- Python 3.13+