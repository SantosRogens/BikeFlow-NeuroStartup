# Model Card — BikeFlow

## Uso pretendido
Prever o número aproximado de bicicletas compartilhadas alugadas por hora, para planejamento de disponibilidade e redistribuição em cenários históricos comparáveis.

## Não usar para
Não usar para punir trabalhadores, definir preços individuais discriminatórios, negar atendimento, tomar decisões de segurança ou justificar investimentos sem revisão humana.

## Dados
UCI Bike Sharing (Capital Bikeshare, Washington, D.C., 2011–2012): **17379** registros horários reais. Atributos: season, mnth, hr, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed. Excluídas as colunas `casual` e `registered` para evitar vazamento de resposta.

## Modelo e avaliação
Rede neural Keras com camadas **64-32**, Dropout (15%) e Early Stopping, comparada a regressão Ridge e árvore de decisão.
Divisão cronológica em 60% treino / 20% validação / 20% teste. Seleção feita apenas na validação.
**MAE no teste:** rede **90.06** bicicletas/h; Ridge **115.88**; árvore **134.73**. RMSE da rede: **127.01**.

## Limitações
Dados de 2011–2012 de Washington; não generalizar para 2026, outras cidades, alterações de hábitos ou novas estações. O dataset é histórico e observacional; a sazonalidade, a coleta e a mudança de demanda causam desvios. Avaliar justiça e impactos operacionais, validar dados de entrada, acompanhar o erro e realizar re-treinamento com dados atuais. Esta demonstração não utiliza disponibilidade de bicicletas por estação, trânsito, eventos nem previsão meteorológica.

## Fonte e licença
Fanaee-T, H. (2013). *Bike Sharing*. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894 — CC BY 4.0.
