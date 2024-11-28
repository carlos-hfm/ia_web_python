# Projeto de IA e Web em Python - Teste Seletivo Estágio Altox

- Versão Python Utilizada: 3.10.12
- O projeto foi desenvolvido no ambiente Ubuntu (WSL)

## Criação e configuração do ambiente virtual

Após clonar o repositório, crie o ambiente virtual

```bash
virtualenv project_env
```

Entre no ambiente

```bash
source project_env/bin/activate
```

Instale o RDKit

```bash
pip install rdkit
```

## Treinamento do Modelo Multiclasse

Instalação das bibliotecas necessárias

```bash
pip install -r requirements.txt
```

Foi criado um [Notebook](model_trainer.ipynb) que segue o passo a passo do [Notebook original](https://patwalters.github.io/practicalcheminformatics/jupyter/multiclass/pubchem/imbalanced/2021/08/28/multiclass-classification.html), e no fim exporta os modelos gerados em formato pkl.

Para executar o treinamento novamente, basta rodas todas as células do notebook [Notebook](model_trainer.ipynb). Para isso, utilizei as extensões do Jupyter Notebook do VSCode.

## Aplicação Web

- Utilizado Python + Flask

```bash
pip install flask
```