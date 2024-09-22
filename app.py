from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    original_language = db.Column(db.String(100))
    first_published_year = db.Column(db.Integer)
    sales = db.Column(db.Integer)
    genre = db.Column(db.String(100))

# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'original_language': book.original_language,
        'first_published_year': book.first_published_year,
        'sales': book.sales,
        'genre': book.genre
    } for book in books])


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)

