# Empréstimos — modalidades a partir de renda, idade e UF

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi&logoColor=white)

Um POST, sem banco. `loan_engine.determine_loans` devolve as modalidades e um número de taxa. O CPF entra no JSON e não é usado.

## Por que uma função pura

| Escolha | Efeito |
| --- | --- |
| Regras em função, sem I/O | O teste chama a função direto. Não há cliente salvo nem histórico. |
| Tabela de regras no banco | Daria para mudar taxa sem deploy. Este código não faz isso. |

Condições em `loan_engine.py`:

| Condição | Modalidades |
| --- | --- |
| `income <= 3000` | PERSONAL (taxa 4) e GUARANTEED (taxa 3) |
| `3000 < income <= 5000`, `age < 30` e `location == "SP"` | as mesmas duas |
| `income >= 5000` | CONSIGNMENT (taxa 2), somada às anteriores se a faixa do meio também valer |

`location` é string livre: só o valor exato `"SP"` entra na segunda regra. A unidade da taxa não está no código — o campo sai como 4, 3 ou 2.

## Stack

- Python (sem versão pinada no repositório)
- FastAPI 0.115.0 e Uvicorn 0.30.6
- `unittest` da biblioteca padrão

## Estrutura

```
app/
├── main.py          # POST /customer-loans
├── loan_engine.py   # regras e taxas
└── schemas.py       # age > 0, income >= 0, cpf, name, location
tests/
└── test_loan_engine.py
requirements.txt
```

## Como rodar

```bash
git clone https://github.com/gabrielteramae/loans-desafio.git
cd loans-desafio
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

| Método | Rota | Resposta |
| --- | --- | --- |
| POST | `/customer-loans` | `{"customer":"<name>","loans":[{"type","interest_rate"}]}` |

Corpo: `age`, `cpf`, `name`, `income`, `location`.

## Testes realizados

`tests/test_loan_engine.py` cobre três casos da função, sem HTTP: renda 3000 leva PERSONAL e GUARANTEED; 29 anos, renda 4500 e `SP` também; renda 7000 leva só CONSIGNMENT.

```bash
python -m unittest tests.test_loan_engine
```

O caso em que renda 5000, idade menor que 30 e `SP` acumulam as três modalidades não está no teste.

---

© 2026 Gabriel Teramae Chan
