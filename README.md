# Projeto de IA e Web em Python - Teste Seletivo Estágio Altox

- Versão Python Utilizada: 3.10.12
- O projeto foi desenvolvido no ambiente Ubuntu (WSL)

## Criação e configuração do ambiente virtual

Após clonar o repositório, crie o ambiente virtual

```bash
pip install virtualenv
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

Para executar o treinamento, basta rodas todas as células do notebook [Notebook](model_trainer.ipynb). Para isso, utilizei as extensões do Jupyter Notebook do VSCode.

## Aplicação Web

- Utilizado Python + Flask

Instale o Flask:

```bash
pip install flask
```

Para rodar/fazer deploy da aplicação, basta executar:

```bash
python3 app.py
```

## Estrutura de arquivos

```bash
├── README.md
├── app.py # Aplicação Flask / Backend
├── data 
│   ├── AID_1645841_datatable.csv # Base de dados
├── lib
│   └── descriptor_gen.py # Código do Descritor
├── model_trainer.ipynb # Notebook de treinamento do modelo
├── models
│   ├── model.pkl # Modelo padrão
│   └── oversampled_model.pkl # Modelo oversampled
├── prediction.py # Código com a função de predição, utilizado pelo App
├── project_env # Ambiente virtual
├── requirements.txt # Bibliotecas usadas no treinamento
└── standalone # Pasta do Ketcher / Frontend
    ├── apple-touch-icon.png
    ├── asset-manifest.json
    ├── favicon-16x16.png
    ├── favicon-32x32.png
    ├── favicon.ico
    ├── iframe_page.html # Página principal da aplicação, com IFrame do Ketcher e script de requisição ao Backend
    ├── index.html # Página do Ketcher
    ├── logo.svg
    ├── manifest.json
    ├── robots.txt
    ├── static
    │   ├── css
    │   │   └── main.e770f74b.css
    │   └── js
    │       ├── 58.d4158b49.chunk.js
    │       ├── 58.d4158b49.chunk.js.LICENSE.txt
    │       ├── main.1cd53ef5.js
    │       └── main.1cd53ef5.js.LICENSE.txt
    └── style.css # Estilização da página principal
```