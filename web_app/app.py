from flask import Flask, render_template, request
from validation.code_validator import HSNValidator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    code = ""
    result = None
    error = None
    if request.method == 'POST':
        code = request.form.get('hsn_code', '')
        valid, message = HSNValidator().validate(code)
        if valid:
            result = message
        else:
            error = message
    return render_template('index.html', code=code, result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)