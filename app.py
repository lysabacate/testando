from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compras')
def compras():
    #return '<ul><li>Arroz</li></ul>'
    return render_template('compras.html', item1 = 'Farinha', item2 = 'Cuscuz')

@app.route('/mercados')
def mercados():
    return render_template('mercados.html')

if __name__ == '__main__':
    app.run()

#@app.route('/gastos')
#def gastos():
    #mes = 'Fevereiro'
    #valor = 'R$ 843,00'
    #return render_template('gastos.html', a = mes, b = valor)

@app.route('/gastos', defaults= {'mes':'janeiro','valor':'0'})

@app.route('/gastos/<mes>/<valor>')
def gastos(mes, valor):
    return render_template('gastos.html', a = mes, b = valor)

@app.route('/dobro', defaults= {'n':0})
@app.route('/dobro/<int:n>')
@app.route('/dobro/<float:n>')
def dobro(n):
    resultado = 2*n
    return render_template('dobro.html', n=n, resultado = resultado)


@app.route('/perfil', defaults= {'nome':'anonimo'})
@app.route('/perfil/<nome>')
def perfil(nome):
    return render_template('perfil.html', nome = nome)