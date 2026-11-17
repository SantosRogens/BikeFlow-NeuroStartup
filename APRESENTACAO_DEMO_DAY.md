# Roteiro curto — Demo Day da BikeFlow (aprox. 2 minutos)

**Problema (20 s):** “Uma operadora de bicicletas compartilhadas precisa saber em quais horários esperar maior procura. Sem previsão, pode haver falta de bicicletas ou redistribuição ineficiente.”

**Dados (20 s):** “Usamos dados reais de aluguel horário em Washington, D.C., entre 2011 e 2012, disponíveis no repositório UCI. Dois gráficos exploram a demanda por hora e a relação com o clima.”

**Método (35 s):** “Separamos treino, validação e teste cronologicamente. Comparamos uma regressão linear com três redes neurais em Keras e também uma árvore de decisão. Usamos Dropout, Early Stopping e registramos cada tentativa no experimentos.csv. Não usamos colunas que entregam a resposta.”

**Resultados (25 s):** “A melhor rede teve MAE de **[INSERIR MÉTRICA REAL]** bicicletas/h, versus **[INSERIR BASELINE REAL]** no modelo linear. Isso representa **[INSERIR COMPARAÇÃO REAL]**.”

**Demonstração (15 s):** “Aqui alteramos hora, temperatura e clima no painel e mostramos quantos aluguéis o modelo estima.”

**Responsabilidade (5 s):** “É um protótipo acadêmico: dados históricos não substituem medição atual, monitoramento e revisão humana.”

**Antes da apresentação:** execute o notebook, substitua os campos entre colchetes pelos resultados efetivos e faça uma captura da tela funcionando.