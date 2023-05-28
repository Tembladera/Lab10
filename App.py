from flask import Flask, render_template, request,redirect,url_for
from calcular import calcular
app = Flask(__name__)

@app.route('/')
def Index():
    operation = request.args.get('operation')
    resultado = request.args.get('resultado')
    return render_template('index.html', operation=operation,resultado=resultado)

@app.route('/calculadora', methods=['POST'])
def Calculadora():
    if request.method == 'POST':
        operation = request.form['operation']
        resultado = calcular(operation)

        # Calculamos
        calcular(operation)


    return redirect(url_for('Index', operation=operation ,resultado=resultado))

if __name__ == '__main__':
    app.run(port=3000,debug=True)
    