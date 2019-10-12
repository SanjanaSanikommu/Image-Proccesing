from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['file']
    return projectpath

if __name__ == '__main__':
    app.run()

