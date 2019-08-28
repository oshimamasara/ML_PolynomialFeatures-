import numpy as np
from flask import Flask, request, jsonify
import pickle
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

poly_reg = PolynomialFeatures(degree = 6)

@app.route('/api', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    x = np.array(data['exp'])
    test_data = poly_reg.fit_transform([[x]])
    prediction = model.predict(test_data)
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555 ,debug = True)