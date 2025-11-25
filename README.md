# TLSV_Project
## Presentation
Program for automating contract review in Oracle Workforce Management.
## 👨‍💻 Technologies
• Python • Selenium
## 🔧 Instalation
1. Clone the repository:

`git clone https://github.com/raphamissias/TLSV_Project.git
cd TLSV_Project`


2. Install the dependencies:

`python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt`

## 🚀 Running the project
1. The .csv file that will be used by program review must be downloaded in the technical support section on Oracle WFM and pasted in “csv_file” directory.

1. To run the program:

`python main.py`

## 🎯 Main Flow
1. The program firstly will run Chrome in debug mode and if necessary, will sing in on Oracle WFM.
2. The file in “csv_file” will be read and the contracts extracted.
2. For each contract, a search is performed and the status and relevant information about the current contract are returned.
4. The new spreadsheet is updated for each contract searched.
5. The final spreadsheet is saved, and the program and browser are closed.