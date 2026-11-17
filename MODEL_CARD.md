# Model Card — BikeFlow

> **Documento preliminar.** O notebook substituirá este arquivo por uma versão com resultados medidos após treinamento no dataset real.

## Uso pretendido
Prever quantidade aproximada de bicicletas compartilhadas alugadas por hora para auxiliar planejamento operacional.

## Não usar para
Não usar para punição de trabalhadores, preços individualizados discriminatórios, decisões de segurança, negação de serviço ou decisão automática sem revisão humana.

## Dados
[UCI Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset): dados históricos de Washington, D.C., de 2011–2012. O notebook usa `hour.csv` e exclui `casual` e `registered` para impedir vazamento de resposta.

## Avaliação
Divisão cronológica de treino, validação e teste; MAE da rede Keras, Ridge e árvore de decisão. **Resultados: pendentes de execução do notebook.**

## Limitações
Dataset histórico, apenas uma cidade, diferenças de mobilidade, estações e clima; requer validação local, monitoramento de deriva e atualização com dados recentes antes de qualquer implantação.

## Licença / crédito
Fanaee-T, H. (2013). *Bike Sharing*. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894. CC BY 4.0.