# Atividade no caderno — Aula IAML 08

## Parte A — Lendo curvas de treino

**1. Desenhe as duas curvas.** A curva de treinamento começa alta e cai continuamente até zero na época 7. A curva de validação cai até o menor ponto na época 4 e sobe nas épocas 5, 6 e 7.

**2. Quando começou a decorar?** A partir da época 5. Enquanto o erro de treino continuou caindo, o de validação subiu, indicando overfitting.

**3. Qual modelo guardar com Early Stopping?** A versão da época 4, que apresentou o menor erro de validação.

**4. Duas soluções:** Dropout para reduzir dependência de neurônios individuais e Early Stopping para interromper o treinamento ao deixar de melhorar na validação.

## Parte B — Model Card de risco de evasão

- **Uso pretendido:** identificar estudantes com maior risco de abandono e oferecer apoio acadêmico.
- **Não usar para:** expulsar alunos, negar matrícula, retirar bolsas ou discriminar pessoas.
- **Dados:** presença, notas, participação acadêmica e histórico educacional, com proteção de dados e base legal adequada.
- **Como medir se está bom:** recall dos alunos que realmente evadiram, precisão, F1 e taxas de erro por grupo; acompanhamento após intervenção.
- **Limitações:** erros de classificação, possíveis vieses, registros incompletos e fatores pessoais não representados nos dados; revisão humana obrigatória.

## Parte C — Reflexão de mercado (até 8 linhas)

**1. Por que registrar tentativas?** O `experimentos.csv` permite comparar arquiteturas, métricas e decisões, garantindo rastreabilidade e reprodução dos testes. Também evita repetir experiências ruins e explica por que a melhor opção foi escolhida.

**2. Dois cuidados antes de lançar:** validar as previsões em entregas reais e monitorar o erro após implantação. É importante verificar mudanças de trânsito, clima e demanda, com atualização segura do modelo quando necessário.