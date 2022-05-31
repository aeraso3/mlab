from flask import Flask,render_template,request
import numpy as np
import pickle

model=pickle.load(open('antecedentes_hospitalizacion.pkl','rb'))

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def new():
    return render_template('new.html')

@app.route('/predict', methods=['POST','GET'] )
def predict():
    data1=float(request.form['a'])
    data2=float(request.form['b'])
    data3=float(request.form['c'])
    data4=float(request.form['d'])
    data5=float(request.form['e'])
    data6=float(request.form['f'])
    data7=float(request.form['g'])
    features=np.array([data1,data2,data3,data4,data5,data6,data7])
    pred = model.predict([features])
    
    def statement():
        if pred == 0:
            return 'Resultado:- El modelo ha pronosticado que no será hospitalizado pero debe cuidarse.'
        elif pred == 1:
            return 'Resultado:- Debe consultar con el médico, el modelo ha predicho que deberá ser hospitalizado.'
    
    return render_template('new.html',statement=statement())


if __name__=='__main__':
    app.run()