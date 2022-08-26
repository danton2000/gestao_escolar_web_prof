from flask import Flask, render_template, redirect, url_for, request

import sqlite3

app = Flask(__name__)

@app.route('/')
def index():

    return redirect(url_for('alunos'))

@app.route('/alunos/')
def alunos():

    con = sqlite3.connect("gestao_escolar.db")

    cur = con.cursor()

    sql = """
        SELECT matricula, nome FROM Alunos
    """

    cur.execute(sql)

    alunos = cur.fetchall()

    con.close()

    return render_template('alunos.html', alunos=alunos)

@app.route('/alunos/<matricula>/editar', methods=('GET', 'POST'))
def alunos_editar(matricula):

    con = sqlite3.connect("gestao_escolar.db")

    cur = con.cursor()

    if request.method == 'POST':

        matricula = request.form['txt_matricula']

        nome = request.form['txt_nome']

        cur.execute("UPDATE Alunos set nome = ? WHERE matricula = ?",
        (nome, matricula))

        con.commit()

        con.close()

        return redirect(url_for("alunos"))

    cur.execute("SELECT matricula, nome FROM Alunos WHERE matricula = ?",
        (matricula,))

    aluno = cur.fetchone()
    
    con.close()

    return render_template('aluno-editar.html', aluno=aluno)