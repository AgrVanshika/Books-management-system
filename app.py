from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory database)
books = [
    {"id": 1, "title": "Harry Potter", "author": "J.K. Rowling", "genre": "Fantasy", "publication_date": "1997-06-26"},
    {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "publication_date": "1925-04-10"},
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book["id"] == id), None)
    return jsonify(book) if book else ("Book not found", 404)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book["id"] = len(books) + 1  # Generate a new ID
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        return ("Book not found", 404)
    
    updated_data = request.get_json()
    book.update(updated_data)
    return jsonify(book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book["id"] != id]
    return ("Book deleted", 204)

if __name__ == '__main__':
    app.run(debug=True)
