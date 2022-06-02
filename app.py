from flask import Flask,render_template, request
import numpy as np
import pickle

model2=pickle.load(open('rl_vive.pkl','rb'))

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def new():
    return render_template('new.html')

@app.route('/predict', methods=['POST','GET'] )
def predict():
    data1=int(request.form['a'])
    data2=int(request.form['b'])
    data3=int(request.form['c'])
    data4=int(request.form['d'])
    data5=int(request.form['e'])
    data6=int(request.form['f'])
    data7=int(request.form['g'])
    features=np.array([data1,data2,data3,data4,data5,data6,data7])
    pred = model2.predict([features])
    
    def statement():
        if pred == 0:
            return 'Result:- The model has predicted that you will not suffer from any cardic arresst but you should take care of your self.'
        elif pred == 1:
            return 'Result:- You should consult with doctor, The model has predicted that you will suffer form cardic arrest.'
    
    return render_template('new.html',statement=statement())


if __name__=='__main__':
    app.run()