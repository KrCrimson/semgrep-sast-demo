<<<<<<< HEAD
# semgrep-sast-demo
Demo de análisis SAST con Semgrep: detección de inyección SQL en Python  Este repositorio contiene un ejemplo mínimo de una aplicación Python vulnerable a inyección SQL y una regla personalizada de Semgrep para detectar este tipo de vulnerabilidad. Incluye integración con GitHub Actions para análisis automático en cada push o pull request.
=======
# Demo SAST con Semgrep: SQL Injection en Python

Este repositorio contiene un ejemplo mínimo de análisis SAST usando [Semgrep](https://semgrep.dev/) para detectar vulnerabilidades de inyección SQL en código Python.

## Estructura

```
archivo/
├── vulnerable.py                  # Script Python vulnerable a SQL Injection
├── rules/
│   └── sql-injection.yml          # Regla personalizada de Semgrep
└── .github/
    └── workflows/
        └── semgrep.yml            # Workflow de GitHub Actions para análisis automático
```

## ¿Cómo funciona?

- `vulnerable.py` contiene una consulta SQL insegura usando concatenación de strings.
- `rules/sql-injection.yml` define una regla personalizada para detectar este patrón inseguro.
- `.github/workflows/semgrep.yml` ejecuta Semgrep automáticamente en cada push o pull request.

## Uso local

1. Instala Semgrep:
   ```sh
   pip install semgrep
   ```
2. Ejecuta el análisis:
   ```sh
   semgrep --config archivo/rules/sql-injection.yml archivo/vulnerable.py
   ```

## Resultado esperado

Semgrep debe detectar la vulnerabilidad y mostrar un mensaje como:
```
archivo/vulnerable.py
  8:     cursor.execute(query)
     Possible SQL Injection: avoid string concatenation in SQL queries.
```

## Créditos
- Inspirado en prácticas de SAST y ejemplos de la documentación oficial de Semgrep.
>>>>>>> 2afdb1c (Demo SAST con Semgrep: SQL Injection en Python)
