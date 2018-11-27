# PANDAS TSE 2018
Este projeto consiste na mineiração dos dados do primeiro turno das eleições presidenciais de 2018 para fins de um estudo 
estatístico sobre a apuração dos presidenciáveis para o Brasil.

## MINEIRAÇÃO DOS DADOS
Os dados são obtidos através do [portal da agência do Tribunal Superior Eleitoral](http://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1/repositorio-de-dados-eleitorais) atavés dos hyperlinks lá disponíveis. Para
agilizar o download desses dados, foi utilizado o conceito de raspagem de dados utilizando a linguagem de programação Python
e a biblioteca URLLIB.
Para execução do algorítimo, utilize os comandos abaixo:
```
pip3 install -f requirements.txt
python3 download_zips.py
```
Esses dados estarão disponíveis em arquivos CSV, cada um representando uma Unidade Federativa brasileira. Cada um dos arquivos
contém dados das contagens de votos para cada candidato disponível naquele estado. Por exemplo, no estado da Bahia haverá somente
os candidatos à deputados estaduais, deputados federais, senadores e governador desse estado. Além disso, haverá também a contagem
de votos dos candidatos à presidência da república.

## ESTUDOS DOS DADOS ESTATÍSTICOS UTILIZANDO O PANDAS
Através desses dados, foi possível carregá-los para o [Pandas](https://pandas.pydata.org/) e fazer a análise técnica e estatística
do resultado. Nesse estudo, foi utilizada somente a carga de dados do norte do país devido à grande massa de dados para serem
analisadas.
Para a execução do Pandas, é utilizado o framework [Jupyter Notebook](http://jupyter.org/) o qual fica responsável por gerar a 
análise aritimética do resultado, gerando estruturas estatísticas para melhor apresentação do escopo sugerido.
Para executar o Pandas com o Jupyter Notebook, execute no terminal a linha abaixo:
```
jupyter notebook
```
O serviço do Jupyter Notebook com o Pandas estará disponível através da URL [http://localhost:8888/notebooks/pandas.ipynb](http://localhost:8888/notebooks/pandas.ipynb).
