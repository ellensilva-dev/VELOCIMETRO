# Velocímetro com Multa

Programa em Python que simula um radar de velocidade. O usuário informa a velocidade do carro, e o programa diz se ele está dentro do limite ou se foi multado.

## Regras

- Limite da via: **80 km/h**
- Acima do limite, a multa é de **R$ 7,00 por cada km/h excedido**

Fórmula: `multa = (velocidade - 80) × 7`

## Como usar

1. Tenha o Python 3 instalado.
2. Execute no terminal:

   ```bash
   python velocimetro.py
   ```

3. Digite a velocidade do carro quando o programa pedir.

## Exemplo de execução

```
Qual é a velocidade do carro? 100
Um momento...
MULTADO!! Você excedeu o limite permitido  que é de 80km/h 
Você deverá pagar uma multa de R$140.0,00
Tenha um bom dia!
```

Com velocidade igual ou menor que 80 km/h:

```
Qual é a velocidade do carro? 70
Um momento...
Você está no limite da via! Continue digirindo em segurança!
```

## O que pratiquei

- Entrada de dados com `input()` e conversão para decimal com `float()`
- Estruturas condicionais (`if` / `else`)
- Cálculos com operadores matemáticos
- Pausa na execução com `sleep()` do módulo `time`
- Formatação de texto com f-strings e quebra de linha (`\n`)

## Próximos passos

- Formatar o valor da multa com duas casas decimais (por exemplo, `R$ 140,00`)
- Tratar entradas que não são número
- Remover a função `lin()`, que foi criada mas não é usada
