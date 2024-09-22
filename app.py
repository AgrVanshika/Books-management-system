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

# Endpoint to get book by its id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'original_language': book.original_language,
            'first_published_year': book.first_published_year,
            'sales': book.sales,
            'genre': book.genre
    }), 200
    else:
        return jsonify({'error': 'Book not found!'}), 404
    
# Endpoint to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        title=data['title'],
        author=data['author'],
        original_language=data.get('original_language', ''),
        first_published_year=data.get('first_published_year', ''),
        sales=data.get('sales', ''),
        genre=data.get('genre', '')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'New book added!', "book_id": new_book.id}), 201

# Endpoint to update a new book by its id
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book=Book.query.get(book_id)
    if not book:
        return jsonify({'message':'Book not found!'}), 404
    data = request.json
    book.title=data.get('title', book.title)
    book.author=data.get('author', book.author)
    book.original_language=data.get('original_language', book.original_language)
    book.first_published_year=data.get('first_published_year', book.first_published_year)
    book.sales=data.get('sales', book.sales)
    book.genre=data.get('genre', book.genre)

    db.session.commit()
    return jsonify({'message': 'Book updated successfully'}), 200

# Endpoint to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message':'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully!'}), 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)

