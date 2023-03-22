from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import  QtWidgets as Qw
import sqlite3
import sys
import runpy
from datetime import datetime, date

# from insertion import insert

from En_Ui_window5 import Ui_MainWindow
from QUI_window4 import *
from blood_results import *
from Patient_register_test import Ui_Register_patient
from Patient_body import *

bodyyyy="alii"

class mainwindow :
    name=" "
    def __init__(self):
        self.main_win=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        ################ her musy creat connection
        self.ui.loadDB.clicked.connect(self.load_data)
        self.ui.edit.clicked.connect(self.edit_data)
        self.ui.new_win.clicked.connect(self.show_new_window)
        self.ui.register_butt.clicked.connect(self.register_window)
        # self.ui.name_patient.setText("1111")
        self.name = self.ui.name_patient.text()

    def show(self):
        self.main_win.show()

    def load_data(self):
        connection=sqlite3.connect("newdata.db")
        query=" select * from regsitration_info"
        cur=connection.cursor()
        results=cur.execute(query)
        self.ui.table111.setRowCount(0)
        self.ui.table111.setColumnCount(len(results.fetchone()))
        for row_num , row_data in enumerate(results):
            self.ui.table111.insertRow(row_num)
            for c_num, data in enumerate(row_data):
                curr_c=self.ui.table111.columnCount()
                self.ui.table111.setItem(row_num,c_num,Qw.QTableWidgetItem(str(data)))
        connection.close()
        # self.edit_data()

    def edit_data(self):
        row=self.ui.table111.rowCount();
        column=self.ui.table111.columnCount();
        # print(row, column)
        # data=self.ui.table111.item(0,0).text()
        # self.ui.table111.setItem(0,0,Qw.QTableWidgetItem(str(data)))
        row_list=list()
        edited=dict()
        # print(" has been changer to vale", data )
        for i in range(row):
            for j in range(column):
                 data=self.ui.table111.item(i,j).text()
                 # print(data, i , "  ", j)
                 # print(type(self.ui.table111.cellDoubleClicked(i,j)))
                 # print( "thats the netered cell " ,i,j)
                 self.ui.table111.setItem(i,j,Qw.QTableWidgetItem(str(data)))
                 row_list.append(data)
            edited[i]=row_list
            print(edited[i])
            row_list=[]

    def  show_new_window(self):
       # print( self.ui.name_patient.text())
       #  print(" pppppppppppp",name)
        self.w = AnotherWindow(self.ui.name_patient.text())
        self.w.show()

    def register_window(self):
        # print( self.ui.name_patient.text())
        #  print(" pppppppppppp",name)
        self.R = Register_win()
        self.R.show()

class AnotherWindow:
    name=""
    def __init__(self,num):
        self.name=num
        print(self.name ," thats me from the name window ")
        # super().__init__()
        self.sub_win=QMainWindow()
        self.sub_ui=UI_SHOW()
        # self.label = QLabel("Another Window")
        self.sub_ui.setupUi(self.sub_win)
        self.sub_ui.edit12.clicked.connect(self.on_edit_clicked)
        self.sub_ui.medical_info.clicked.connect(self.load_medical_data)
    def on_edit_clicked(self):
        self.sub_ui.label12.setText(self.name)
        self.edit_data_win2()




    def load_specifi_patient(self,name):
        connection = sqlite3.connect("newdata.db")
        query = " select * from regsitration_info where name =? "
        cur = connection.cursor()
        results = cur.execute(query, (name,))
        data = results.fetchone()

        # for i in data:
            # print(i, " ")
        # connection.close()
        return data
    def load_medical_data(self):
        id=self.sub_ui.table12.item(0,0).text()
        print(id, " id ------")
        connection = sqlite3.connect("newdata.db")
        cur = connection.cursor()
        query = ''' select * from body_char join blood_test
         on
         body_char.id=blood_test.Patient_id where id =?
        '''
        results = cur.execute(query, (id,))

        # print( " i am in load medical data ")
        print(type(int(id)))
        # print(" i am in load medical data 2222 ")
        med_data = results.fetchone()
        connection.close()
        count=0;
        for i in med_data:
            # print(i)
            self.sub_ui.table12_results.setItem(0,count,Qw.QTableWidgetItem(str(i)))
            count=count+1
        # print(med_data[12])
        self.sub_ui.label_diagnos.setText(med_data[11].upper())



    def edit_data_win2(self):
        name=self.name
        data=self.load_specifi_patient(name)
        print("from edit data win2-----------------")
        cn=1;

        for i in data :
            print(i," " ,cn)
            cn=cn+1

        row = self.sub_ui.table12.rowCount();
        self.sub_ui.table12.setColumnCount(len(data))
        column= self.sub_ui.table12.columnCount()
        count=0;
        count2=0
        for i in data:
            self.sub_ui.table12.setItem(0,count,Qw.QTableWidgetItem(str(i)))
            # current=self.sub_ui.table12.item(0,count).text()
            count=count+1



    def show(self):
        self.sub_win.show()

class Register_win:
    personal_info=dict()
    def __init__(self):
        print(" Registeration has been done")
        # super().__init__()
        self.reg_win=QMainWindow()
        self.reg_ui=Ui_Register_patient()
        self.reg_ui.setupUi(self.reg_win)
        self.reg_ui.Save_button.clicked.connect(self.read_data)
        self.reg_ui.Charcteristics.clicked.connect(self.show_body_patien)
        self.reg_ui.results_blood.clicked.connect(self.read_data)
        self.reg_ui.send2DB.clicked.connect(self.send_patient_2database)
        self.reg_ui.results_blood.clicked.connect(self.show_blood_test)

    def read_data(self):

        print("Reading_Data")
        personal_info = dict()
        name =self.reg_ui.name.text();
        personal_info["name"]=name;

        surname =self.reg_ui.surname.text();
        personal_info["surname"] = surname ;

        father =self.reg_ui.father.text();
        personal_info["father"] = father;

        gender=self.reg_ui.gender.text()
        personal_info["gender"] = gender;

        telephone=self.reg_ui.telephone.text()
        personal_info["telephone"] = telephone;

        city =self.reg_ui.city.text();
        personal_info["city"] = city;

        street =self.reg_ui.street.text()
        personal_info["street"] = street;

        nationality=self.reg_ui.nationality.text()
        personal_info["nationality"] = nationality;

        passport_num =self.reg_ui.passport_num.text()
        personal_info["passport"] = passport_num;

        date=self.reg_ui.birthdate.date().toPyDate().strftime('%Y-%m-%d').split('-')
        date1=self.reg_ui.birthdate.date().toPyDate()
        dataccur=datetime.today().strftime('%Y-%m-%d').split('-')

        if (int(dataccur[1]) >= int(date[1])):
            m = 1
        else:
            m = 0
        age = (int(dataccur[0]) - int(date[0]) - 1) + m
        personal_info["age"] = age;

        # l=list()
        # l= [name, surname, father, street, city, nationality,date1,passport_num, age ]
        #
        #
        # ### list continues all personal data of patient personal info

        self.personal_info=personal_info

    def show_body_patien(self):
        self.B=Body_patient()
        self.B.show()
    def show_blood_test(self):
        self.B=Blood_Results()
        self.B.show_blood()

    def send_patient_2database(self):
        print("send 2 DB")

        personal_info=self.personal_info
        p=list()
        for k in personal_info:
            p.append(personal_info[k])
        print(p)

        conn = sqlite3.connect('newdata.db')
        cur = conn.cursor()
        maxx_id = ''' select  max(Patient_id) from regsitration_info '''
        maxx = cur.execute(maxx_id)
        maxx = maxx.fetchone()
        query = ''' insert into  regsitration_info values (?,?,?,?,?,?,?,?,?,?,?)'''
        print(" final step")
        print(maxx[0]+1,p)
        cur.execute(query,(maxx[0]+1,p[0],p[1],p[2],p[4],p[3],p[5],p[6],p[7],p[8],p[9]))
        print("check in reg ")
        cur.close()


    def show(self):
        self.reg_win.show()

class Body_patient:
    body=dict()

    def __init__(self):
        print("Body Charateristcs")
        self.body_win=QtWidgets.QMainWindow()
        self.body_ui=Ui_Dialog()
        self.body_ui.setupUi(self.body_win)
        self.body_ui.save_characteristcs.clicked.connect(self.get_characteristcis)
        # self.body_ui.



    def get_characteristcis(self):
        body_char = dict()

        weight=self.body_ui.weight.text()
        body_char["weight"]=(weight)

        height=self.body_ui.height.text()
        body_char["height"]=(height)

        waist=self.body_ui.waist.text()
        body_char["waist"]=(waist)

        hip=self.body_ui.hip.text()
        body_char["hip"]=(hip)

### dict continue body charateriscs

        b = list()
        for k in body_char:
            b.append(body_char[k])

        conn = sqlite3.connect('newdata.db')
        cur = conn.cursor()
        maxx_id = ''' select  max(id) from body_char '''
        maxx = cur.execute(maxx_id)
        maxx = maxx.fetchone()
        print(b, maxx[0]+1)
        query = ''' insert into  body_char values(?,?,?,?,?)'''
        cur.execute(query, (maxx[0] + 1, b[0], b[1], b[2], b[3]))
        print("check body char" )
        cur.close()

    def show(self):
        self.body_win.show()


class Blood_Results():
    def __init__(self):
        self.blood_win=QMainWindow()
        self.blood_ui=Ui_Blood()
        self.blood_ui.setupUi(self.blood_win)
        # self.blood.ui.save_results.clicked.connect(self.get_blood_results)
        self.blood_ui.save_results.clicked.connect(self.get_blood_results)

    def get_blood_results(self):
        blood_test = dict()

        cholestrol = self.blood_ui.cholestrol.text()
        blood_test["cholestrol"] = cholestrol

        glucose = self.blood_ui.glucose.text()
        blood_test["glucose"] = glucose

        HDL = self.blood_ui.hdl.text()
        blood_test["HDL"] = HDL

        SBP = self.blood_ui.sbp.text()
        blood_test["SBP"] = SBP

        BMI = self.blood_ui.bmi.text()
        blood_test["BMI"] = BMI


        DBP = self.blood_ui.dbp.text()
        blood_test["DBP"] = DBP

        Diabet = self.blood_ui.diabet.text()
        blood_test["diabet"] = Diabet

        bl=list()
        for k in blood_test:
            bl.append(blood_test[k])

        conn = sqlite3.connect('newdata.db')
        cur = conn.cursor()
        maxx_id = ''' select  max(id) from body_char '''
        maxx = cur.execute(maxx_id)
        maxx = maxx.fetchone()
        print(bl,maxx[0]+1)
        query = ''' insert into  blood_test values(?,?,?,?,?,?,?,?)'''
        cur.execute(query, ( bl[0], bl[1], bl[2], bl[3],bl[4],bl[5],bl[6], maxx[0] + 1,))
        print("check blodd test ")
        cur.close()



    def show_blood(self):
        self.blood_win.show()



def mainfun():
    app=QApplication(sys.argv)
    main_win=mainwindow()
    main_win.show()

    sys.exit=(app.exec_())

if __name__=='__main__':
    mainfun()


