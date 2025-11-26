from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Pet
from app import app, db
from sqlalchemy import or_
from PIL import Image
from werkzeug.utils import secure_filename
import uuid, os

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

@app.route('/')
def index():
    termo = request.args.get('q', '')  # pega o termo digitado na busca

    # começa pegando todos os pets
    query = Pet.query

    # se houver termo de pesquisa, filtra por nome ou descrição
    if termo:
        query = query.filter(
            or_(
                Pet.nome.ilike(f"%{termo}%"),
                Pet.descricao.ilike(f"%{termo}%")
            )
        )
    items_ = query.all()
    return render_template('index.html', items=items_)

from flask import jsonify

@app.route('/filter_pets', methods=['GET'])
def filter_pets():
    tipo = request.args.get('tipo')
    cor = request.args.get('cor')
    idade = request.args.get('idade')

    query = Pet.query.filter_by(status='adocao')  # apenas pets disponíveis para adoção, opcional

    if tipo and tipo != "todos":
        query = query.filter(Pet.tipo == tipo)
    if cor and cor != "todas":
        query = query.filter(Pet.cor == cor)
    if idade and idade != "todas":
        query = query.filter(Pet.idade == idade)

    pets = query.all()

    pets_data = [
        {
            "id": p.id,
            "nome": p.nome,
            "tipo": p.tipo,
            "cor": p.cor,
            "idade": p.idade,
            "descricao": p.descricao,
            "imagem": url_for('static', filename='uploads/' + p.imagem) if p.imagem else None,
            "contato": p.contato
        } for p in pets
    ]

    return jsonify(pets_data)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        estado = request.form['estado']
        telefone = request.form['telefone']
        cidade = request.form['cidade']

        # Verifica se já existe usuário com esse email
        existe_user = User.query.filter_by(email=email).first()
        if existe_user:
            flash("Já existe um usuário com esse email.")
            return redirect(url_for('register'))

        # Use pbkdf2:sha256 ou apenas padrão
        hashed_password = generate_password_hash(senha, method='pbkdf2:sha256')

        new_user = User(
            nome=nome,
            email=email,
              # salva o hash na coluna 'senha'
            estado=estado,
            telefone=telefone,
            cidade=cidade
        )
        new_user.set_password(senha) 
        db.session.add(new_user)
        db.session.commit()

        flash("Usuário cadastrado com sucesso! Faça login.")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(senha):
            login_user(user)
            return redirect(url_for('perfil'))
        else:
            flash("Email ou senha incorretos.")


    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Você saiu da sua conta.")
    return redirect(url_for('login'))

import uuid
import os
from flask import current_app

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        cor = request.form.get('cor')
        idade = request.form['idade']
        descricao = request.form['descricao']
        status = request.form['status']
        contato = request.form['contato']
        imagem = request.files['imagem'] if 'imagem' in request.files else None

        filename = None
        if imagem:
            filename = f"{uuid.uuid4().hex}_{imagem.filename}"
            upload_path = os.path.join(current_app.root_path, "static/uploads", filename)
            imagem.save(upload_path)

        new_pet = Pet(
            nome=nome,
            tipo=tipo,
            cor=cor,
            idade=idade,
            descricao=descricao,
            status=status,
            contato=contato,
            imagem=filename,
            user_id=current_user.id
        )

        db.session.add(new_pet)
        db.session.commit()
        flash("Pet cadastrado com sucesso!")

        return redirect(url_for('perfil'))

    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    item = Pet.query.get_or_404(id)
    if item.user_id != current_user.id:
        flash("Você não tem permissão para editar este pet.")
        return redirect(url_for('index'))
    if request.method == 'POST':
        item.nome = request.form['nome']
        item.tipo = request.form['tipo']
        item.idade = request.form['idade']
        item.descricao = request.form['descricao']
        item.status = request.form['status']
        item.contato = request.form['contato']

        imagem = request.files['imagem'] if 'imagem' in request.files else None
        if imagem and imagem.filename != '':
            imagem.save(f"app/static/uploads/{imagem.filename}")
            item.imagem = imagem.filename

        db.session.commit()
        flash("Pet atualizado com sucesso!")
        return redirect(url_for('index'))

    return render_template('update.html', pet=item)

@app.route('/delete/<int:id>', methods=['GET'])
@login_required
def delete(id):
    item = Pet.query.get_or_404(id)

    if item.user_id != current_user.id:
        flash("Você não tem permissão para excluir este pet.")
        return redirect(url_for('perfil'))

    db.session.delete(item)
    db.session.commit()
    flash("Pet removido com sucesso!")
    return redirect(url_for('perfil'))

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def is_real_image(file):
    try:
        img = Image.open(file)
        img.verify()
        return True
    except:
        return False


@app.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    imagem = request.files.get('foto_perfil')

    if not imagem or imagem.filename == "":
        flash("Nenhuma imagem selecionada.")
        return redirect(url_for('perfil'))

    # 1. Verifica extensão
    if not allowed_file(imagem.filename):
        flash("Envie apenas imagens PNG, JPG ou JPEG.")
        return redirect(url_for('perfil'))

    # 2. Verifica conteúdo real (protege contra arquivos renomeados)
    if not is_real_image(imagem.stream):
        flash("O arquivo enviado não é uma imagem válida.")
        return redirect(url_for('perfil'))

    # Resetar stream para o início antes de salvar
    imagem.stream.seek(0)

    # 3. Criar nome seguro
    filename = secure_filename(f"{uuid.uuid4().hex}_{imagem.filename}")
    upload_path = os.path.join(current_app.root_path, "static/uploads", filename)

    # 4. Salvar imagem
    imagem.save(upload_path)

    # 5. Atualizar no BD
    current_user.foto_perfil = filename
    db.session.commit()

    flash("Foto de perfil atualizada com sucesso!")
    return redirect(url_for('perfil'))


@app.route('/perfil')
@login_required
def perfil():
    termo = request.args.get('q', '')  # pega o termo digitado na barra de pesquisa

    # começa buscando apenas os pets do usuário logado
    query = Pet.query.filter_by(user_id=current_user.id)

    # se o usuário digitou algo, filtra por nome OU descrição
    if termo:
        query = query.filter(
            or_(
                Pet.nome.ilike(f"%{termo}%"),
                Pet.descricao.ilike(f"%{termo}%")
            )
        )

    meus_pets = query.all()

    return render_template('perfil.html', user=current_user, pets=meus_pets)
