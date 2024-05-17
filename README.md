## Análise de Bots no Twitter utilizando Redes Neurais

Este projeto consiste em uma análise de bots na antiga plataforma 'Twitter' (atualmete **X**), utilizando técnicas de aprendizado de máquina, especificamente redes neurais. 
O objetivo é detectar contas automatizadas (bots) com base em diversas características dos perfis, como fonte de postagem, número de seguidores, entre outros.

## Desenvolvimento do Projeto 

Esse projeto desenvolvido durante disciplina de Inteligência Artificial, ministrada pelo Professor Dr. Hesdras Viana, Incluiu as seguintes etapas:

1. Carregamento e análise inicial do conjunto de dados.
2. Pré-processamento dos dados, incluindo tratamento de valores nulos, codificação de colunas categóricas e normalização das features.
3. Implementação e treinamento de uma rede neural supervisionada para classificação de bots.
4. Implementação de uma rede neural não supervisionada (KMeans) para agrupamento dos dados.
5. Avaliação dos modelos e visualização dos resultados, incluindo a construção de uma matriz de confusão e gráficos do comportamento da rede ao longo das épocas.
6. Publicação do projeto no GitHub.

## Atendimento aos Requisitos da Proposta

Este projeto atende integralmente aos requisitos propostos para a disciplina, conforme descrito abaixo:

1. **Implementação e Teste de Redes Supervisionadas e Não-Supervisionadas**:
   - Foram implementadas e testadas pelo menos uma rede neural supervisionada e uma não-supervisionada.

2. **Duas Arquiteturas de Redes**:
   - Foram exploradas duas arquiteturas de redes neurais diferentes, cada uma com configurações distintas de hiperparâmetros.

3. **Análise da Base de Dados**:
   - Foi realizada uma análise da base de dados para identificar a necessidade de normalização ou padronização, bem como a presença de outliers.

4. **Métricas de Avaliação**:
   - As métricas de precisão, recall e acurácia foram calculadas para avaliar o desempenho dos modelos treinados.

5. **Gráfico do Comportamento da Rede ao Longo das Interações**:
   - Gráficos foram gerados para visualizar o comportamento das redes durante o treinamento ao longo das épocas.


## Fonte do Conjunto de Dados

O conjunto de dados utilizado neste projeto foi obtido a partir do Kaggle, uma plataforma online que hospeda conjuntos de dados públicos. O conjunto de dados "Dataset para detecção de bots no Twitter" está disponível em [Kaggle](https://www.kaggle.com/datasets/diegoslmarques/dataset-para-deteco-de-bots-no-twitter).

## Descrição do Conjunto de Dados

Este dataset foi construído em um período de 3 a 4 meses, no início de 2023, durante o desenvolvimento de um TCC para Ciência da Computação. Mais detalhes sobre esse trabalho podem ser encontrados [neste repositório](https://github.com/diegomarques1/tcc-twitter-bots).

No total, essa base possui 1020 dados, 510 sendo potenciais bots e 510 sendo humanos. Para cada conta inserida, também foram obtidos 19 atributos que dizem respeito às suas informações, como quantidade de seguidores ou de postagens.

## Conteúdo do Repositório

- `bots_analysis.ipynb`: Jupyter Notebook contendo o código Python utilizado para realizar a análise de bots no Twitter utilizando redes neurais.
- `twitter_bots.xlsx`: Conjunto de dados contendo informações sobre contas do Twitter, incluindo características dos perfis e rótulos indicando se são bots ou não.
- `README.md`: Este arquivo que você está lendo agora.

  (O projeto está sujeito a possiveis alterações)
