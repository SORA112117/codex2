from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dreams.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Dream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    dreams = Dream.query.order_by(Dream.date.desc()).all()
    return render_template('index.html', dreams=dreams)

@app.route('/add', methods=['GET', 'POST'])
def add_dream():
    if request.method == 'POST':
        title = request.form['title']
        date_str = request.form['date']
        content = request.form['content']
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        dream = Dream(title=title, date=date, content=content)
        db.session.add(dream)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:dream_id>', methods=['GET', 'POST'])
def edit_dream(dream_id):
    dream = Dream.query.get_or_404(dream_id)
    if request.method == 'POST':
        dream.title = request.form['title']
        date_str = request.form['date']
        dream.date = datetime.strptime(date_str, '%Y-%m-%d').date()
        dream.content = request.form['content']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', dream=dream)

@app.route('/delete/<int:dream_id>', methods=['POST'])
def delete_dream(dream_id):
    dream = Dream.query.get_or_404(dream_id)
    db.session.delete(dream)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
