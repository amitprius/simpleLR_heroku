
from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))
    
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    years = request.form['years']
       
    pred = model.predict(np.array([[int(years)]]))
    
    # predict = [i for i in request.form.values()]
    print(years, pred)
    return render_template('index.html', predict=str(pred))

#  if __name__ == '__main__':
#      app.run()

#=====================================

# from flask import Flask
# app = Flask(__name__)
  
# @app.route('/')


if __name__ == '__main__':
    app.run(debug=True)