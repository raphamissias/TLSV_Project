# TLSV_Project
##### Apresentação
Programa para automação de conferência de contratos no Workforce Management da Oracle.
##### 👨‍💻 Tecnologias
• Python • Selenium
##### 🔧 Instalação
1. Clone o repositório:

`git clone https://github.com/raphamissias/TLSV_Project.git
cd TLSV_Project`


2. Instale as dependências:

`python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt`

##### 🚀 Executando o projeto
1. O arquivo .csv que servirá de consulta para o programa deve ser baixado diretamente pelo WFM na sessão de atendimentos técnicos e colocado na pasta csv_file.

1. Para iniciar o programa:

`python main.py`

##### 🎯 Fluxo Principal
1. O programa primeiramente irá iniciar o navegador Chrome em modo debug e se necessário, fará login no WFM.
2. Ele fará a leitura dos contratos do arquivo colocado na pasta “csv_file”.
2. Para cada contrato, é feito a busca no site e retornado o status e informações relevantes do contrato referente.
4. A nova planilha é atualizada com as informações a cada busca por contrato.
5. A planilha final é salva e o programa e navergador são finalizados.