from flask import Flask, send_from_directory, render_template

app = Flask(__name__, template_folder='standalone', static_folder='standalone/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('standalone', path)

if __name__ == '__main__':
    app.run(debug=True)