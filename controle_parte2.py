from PyQt6 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="uva",
    password="alunouva",
    database="cadastro_produtos"
)

if banco.is_connected():
    print("CONECTADO AO BANCO DE DADOS COM SUCESSO!")
        
def funcao_principal():
    linha01 = formulario.lineEdit.text()
    linha02 = formulario.lineEdit_2.text()
    linha03 = formulario.lineEdit_4.text()
    
    categoria = ""

    if formulario.radioButton.isChecked() :
        print("Categoria de Informatica foi selecionado")
        categoria = "Informatica"
        
    elif formulario.radioButton_2.isChecked() :
        print("Categoria de alimentos foi selecionado") 
        categoria = "Alimentos"
    else :
        print("Categoria de Eletronicos foi selecionado")
        categoria ="Eletronicos"

    print("Codigo:", linha01)
    print("Descricao:", linha02)
    print("Preco:", linha03)
    
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha01),str(linha02),str(linha03),categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    
app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()

banco.close()
#cursor.close()
