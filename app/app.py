from flask import Flask, send_from_directory, render_template

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


if __name__ == '__main__':
    app.run(debug=True)