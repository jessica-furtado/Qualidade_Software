# 🧮 Projeto: Calculadora com Testes Unitários

Este projeto implementa uma calculadora com operações matemáticas básicas em **Python**, acompanhada de **testes unitários com Pytest**, com foco na qualidade e cobertura de diferentes cenários, incluindo casos de erro.

---

## 📂 Estrutura do Projeto

```
calculadora.py           # Implementação da classe Calculadora
test_calculadora.py      # Arquivo com os testes unitários usando pytest
README.md                # Documentação do projeto
```

---

## ⚙️ Funcionalidades da Calculadora

A classe `Calculadora` possui os seguintes métodos:

- `soma(a, b)` → Retorna a soma de dois números
- `subtracao(a, b)` → Retorna a subtração entre dois números
- `multiplicacao(a, b)` → Retorna a multiplicação entre dois números
- `divisao(a, b)` → Retorna a divisão entre dois números, com **tratamento para divisão por zero**
- `fatorial(n)` → Calcula o fatorial de um número, com **tratamento para negativos**
- `potencia(base, expoente)` → Calcula a base elevada ao expoente (inclusive negativos)

---

## 🧪 Testes Unitários com Pytest

Os testes incluem:

- Operações com **números positivos, negativos e zero**
- Divisões com **valores decimais** e **verificação de erro ao dividir por zero**
- Fatorial com **valores válidos** e verificação de **erro com negativos**
- Potência com **expoentes positivos e negativos**
- Uso de **fixture** para reutilizar o objeto calculadora

---

## 🚀 Como Executar os Testes

### 1. Instale o `pytest` (se ainda não tiver instalado):

```bash
pip install pytest
```

### 2. Execute os testes no terminal:

```bash
python -m pytest test_calculadora.py
```

Se tudo estiver certo, você verá uma saída parecida com:

```
============================= test session starts =============================
collected 6 items

test_calculadora.py ......                                           [100%]

============================== 6 passed in 0.05s ==============================
```

---

## 📌 Requisitos atendidos

- ✅ Código limpo e organizado
- ✅ Tratamento de exceções (como divisão por zero e fatorial de número negativo)
- ✅ Cobertura de testes variados
- ✅ Testes escritos seguindo boas práticas

---

## 👩‍💻 Desenvolvido por

Jessica Furtado e Waldir Pontual
Projeto da disciplina de **Qualidade de Software – UNIESP**  
Utilizando boas práticas de testes automatizados com Python 💛
