from flask import Flask, render_template, request

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

#metodos get e post
#metodo get é padrão, se não definirmos algum método, vai ser automaticamente ele
@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['get'])
#@app.route('/recebedados', methods=['post'])
def recebedados():
    #nome = request.form['nome']
    #email = request.form['email']
    nome = request.args['nome']
    email = request.args ['email']
    estado = request.args ['estado']
    formacao = request.args ['formacao']
    modalidades = request.args.getlist('modalidades')
    #return nome+'-'+email
    return render_template('recebedados.html', nome=nome, email=email, estado=estado, formacao=formacao, modalidades = modalidades)

@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    if idade >= 18:
        return "Você é maior de idade"
    if idade < 18:
        return "Você é menor de idade"
    
@app.route('/situacaofinal/<float:nota>')
def situacaofinal(nota):
    if nota >= 60.0:
        return "Aprovado"
    elif nota >= 20.0:
        return "Recuperação"
    else:
        return "Reprovado"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificalogin', methods=['post'])
def verificalogin():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if usuario=="musbilus" and senha=="123":
        return render_template('arearestrita.html')
    else:
        return "Você tem permissão"

@app.route('/verificaidade2/<int:idade>')
def verificaidade2(idade):
    return render_template('verificaidade2.html', idade=idade)

@app.route('/usuario/<nome>')
def  usuario(nome):
    return render_template('usuario.html', nome=nome)