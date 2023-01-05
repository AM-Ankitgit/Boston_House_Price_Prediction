from flask import Flask,render_template,jsonify,request
import config
from boston_project.utils import Boston_code
from flask_mysqldb import MySQL
import numpy as np

# write home api

app= Flask(__name__)


 
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Mysql@6776"
app.config["MYSQL_DB"] = "BOSTON_DATABASE"
mysql1 = MySQL(app)




@app.route("/")
def get_templates():
    return render_template('index1.html')

@app.route("/prediction_of_file",methods=["POST","GET"])
def get_boston_price():
    if request.method=="POST":
        print("we are in get method")
        data =request.form
        CRIM=eval(data['CRIM'])
        ZN  =eval(data['ZN'])
        INDUS=eval(data['INDUS'])
        CHAS=eval(data['CHAS'])
        NOX=eval(data['NOX'])
        RM=eval(data['RM'])
        AGE=eval(data['AGE'])
        DIS=eval(data['DIS'])
        RAD=eval(data['RAD'])
        TAX=eval(data['TAX'])
        PTRATIO=eval(data['PTRATIO'])
        B=eval(data['B'])
        LSTAT=eval(data['LSTAT'])
        boston_charges = Boston_code(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO,B,LSTAT)
        charges =boston_charges.get_predict_price()

        z1 = np.round(charges[0],2)
        cursor = mysql1.connection.cursor()
        query = 'CREATE TABLE IF NOT EXISTS Evening_batch_house(CRIM VARCHAR(20),ZN VARCHAR(20),INDUS VARCHAR(20),CHAS VARCHAR(20),NOX VARCHAR(20),RM VARCHAR(20),AGE VARCHAR(20),DIS VARCHAR(20),RAD VARCHAR(20),TAX VARCHAR(20),PTRATIO VARCHAR(20),B VARCHAR(20),LSTAT VARCHAR(20),PRICE VARCHAR(20))'
        cursor.execute(query)
        cursor.execute('INSERT INTO Evening_batch_house(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,PRICE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO,B,LSTAT,z1))
        mysql1.connection.commit()
        cursor.close()
        return render_template("index.html",z1=z1)

    else:
        print('we are running get method')

        CRIM=eval(request.args.get('CRIM'))
        ZN  =eval(request.args.get('ZN'))
        INDUS=eval(request.args.get('INDUS'))
        CHAS=eval(request.args.get('CHAS'))
        NOX=eval(request.args.get('NOX'))
        RM=eval(request.args.get('RM'))
        AGE=eval(request.args.get('AGE'))
        DIS=eval(request.args.get('DIS'))
        RAD=eval(request.args.get('RAD'))
        TAX=eval(request.args.get('TAX'))
        PTRATIO=eval(request.args.get('PTRATIO'))
        B=eval(request.args.get('B'))
        LSTAT=eval(request.args.get('LSTAT'))
        boston_charges = Boston_code(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO,B,LSTAT)
        charges =boston_charges.get_predict_price()

        z1 = np.round(charges[0],2)
        cursor = mysql1.connection.cursor()
        query = 'CREATE TABLE IF NOT EXISTS Evening_batch_house(CRIM VARCHAR(20),ZN VARCHAR(20),INDUS VARCHAR(20),CHAS VARCHAR(20),NOX VARCHAR(20),RM VARCHAR(20),AGE VARCHAR(20),DIS VARCHAR(20),RAD VARCHAR(20),TAX VARCHAR(20),PTRATIO VARCHAR(20),B VARCHAR(20),LSTAT VARCHAR(20),PRICE VARCHAR(20))'
        cursor.execute(query)
        cursor.execute('INSERT INTO Evening_batch_house(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,PRICE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO,B,LSTAT,z1))
        mysql.connection.commit()
        cursor.close()
        return render_template("index.html",z1=z1)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)