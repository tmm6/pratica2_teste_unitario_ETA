# ETA
Exercício da prática 2 referente à disciplina de Testes unitários, da pós de Testes Ágeis.

## Escopo
 1. Escrever testes unitários 
 2. Achar bugs 
 3. Melhorar código 
 4. Corrigir bugs 
 5. Usar TDD para adicionar o método:
    * change_number(self, name, number)
 6. Usar TDD para adicionar o método:
    * get_name_by_number(self, number)

---
## Setup

```bash
pip install -r requirements.txt
```

## Unittest

```bash
python -m unittest -v
```

## Pytest

```bash
pytest .
```

## Test Coverage

- `coverage` and `pytest-cov` packages are required
- Add `pragma: no cover` to exclude code from coverage report

### With `pytest`

Terminal report:

 ```bash
pytest --cov-report term-missing --cov .
 ```

HTML report:

```bash
pytest --cov-report html --cov .
```

### With `unittest`

To generate report:

```bash
python -m coverage run -m unittest
```

To view report in terminal:

```bash
python -m coverage report
```

To view report in HTML:

```bash
python -m coverage html
```

