from flask import Flask, send_from_directory, render_template, jsonify, request
from .. import prediction

app = Flask(__name__, template_folder='standalone', static_folder='standalone/static')

@app.route('/ketcher')
def ketcher():
    return render_template('index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('standalone', path)

@app.route('/')
def iframe():
    return render_template("iframe_page.html")

@app.route('/api/predict', methods='[POST]')
def predict():
    try:
        data_json = request.get_json()
        if data_json is None:
            return jsonify({'error': 'erro'})
        
        molecule_smiles = data_json['smiles']
        prediction = prediction.prediction(molecule_smiles)
        
        return jsonify({'prediction': prediction})
    except:
        return jsonify({'error': 'erro'})


if __name__ == '__main__':
    app.run(debug=True)