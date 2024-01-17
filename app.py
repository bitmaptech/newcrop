from flask import Flask,request,jsonify
import numpy as np
import pickle


model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    N_SOIL = request.form.get('N_SOIL')
    P_SOIL = request.form.get('P_SOIL')
    K_SOIL = request.form.get('K_SOIL')
    # TEMPERATURE = request.form.get('TEMPERATURE')
    # HUMIDITY = request.form.get('HUMIDITY')
    # ph = request.form.get('ph')
    # RAINFALL = request.form.get('RAINFALL')
    

    input_query = np.array([[N_SOIL,P_SOIL,K_SOIL]])

    result = model.predict(input_query)[0]

    return jsonify({'CROP':str(result)})

    #result = {'cgpa': cgpa, 'iq':iq, 'profile_score':profile_score}
    #return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)