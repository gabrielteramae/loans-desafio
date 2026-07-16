# Loans API

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)

Solução para o desafio [`backend-br/desafios/loans`](https://github.com/backend-br/desafios/blob/master/loans/PROBLEM.md): determinar quais modalidades de empréstimo um cliente tem acesso, com base em idade, salário e localização.

## Regras de elegibilidade

| Modalidade      | Taxa | Regra                                                                                   |
|------------------|:----:|-------------------------------------------------------------------------------------------|
| `PERSONAL`         | 4%   | Salário <= R$ 3000, **ou** salário entre R$ 3000 e R$ 5000 com idade < 30 e localização SP |
| `GUARANTEED`         | 3%   | Mesmas condições do empréstimo pessoal                                                       |
| `CONSIGNMENT`         | 2%   | Salário >= R$ 5000                                                                              |

> **Nota:** o JSON de exemplo no `PROBLEM.md` do desafio ilustra apenas o formato da resposta, não o resultado literal calculado a partir das regras — usando exatamente aquele payload de entrada (idade 26, renda R$ 7000, SP), o resultado real segundo os Requisitos é só `CONSIGNMENT` (nenhuma regra descrita libera PERSONAL/GUARANTEED para renda acima de R$ 5000). A lógica implementada aqui segue estritamente a seção "Requisitos" do desafio.

## Stack

- **FastAPI** para a API REST
- **Pydantic** para validação de entrada/saída
- Motor de elegibilidade isolado em `loan_engine.py`, sem dependência de framework — fácil de testar unitariamente

## Estrutura

```
app/
├── main.py          # endpoint POST /customer-loans
├── schemas.py         # request/response (Pydantic)
└── loan_engine.py      # regras de negocio puras
```

## Como rodar

```bash
git clone <seu-repo>
cd loans-api
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8002
```

## Endpoint

```
POST /customer-loans
```

**Request**
```json
{
  "age": 26,
  "cpf": "275.484.389-23",
  "name": "Vuxaywua Zukiagou",
  "income": 7000.00,
  "location": "SP"
}
```

**Response**
```json
{
  "customer": "Vuxaywua Zukiagou",
  "loans": [
    { "type": "CONSIGNMENT", "interest_rate": 2 }
  ]
}
```

## Exemplos testados

| Perfil                                  | Resultado                          |
|-------------------------------------------|---------------------------------------|
| Renda <= 3000                                | PERSONAL + GUARANTEED                    |
| Renda 3000-5000, idade < 30, SP                | PERSONAL + GUARANTEED                       |
| Renda 3000-5000, idade >= 30 (ou fora de SP)     | Nenhum empréstimo                              |
| Renda >= 5000                                     | CONSIGNMENT                                       |

---

© 2026 Gabriel Teramae Chan
