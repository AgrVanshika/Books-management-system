import pandas as pd
from app import db, Book  # Importing your existing database and Book model

# Load the CSV file
df = pd.read_csv('best-selling-books.csv')  # Replace with the actual path to your CSV file

# Loop through the CSV file and add each entry to the SQLite database
for index, row in df.iterrows():
    # Create a new book instance
    book = Book(
        title=row['title'],
        author=row['author'],
        original_language=row['original_language'],
        first_published_year=row['first_published_year'],
        sales=row['sales'],
        genre=row['genre']
    )
    
    # Add the book to the session
    db.session.add(book)

# Commit the changes to save all the entries to the database
db.session.commit()

print("Books have been successfully imported into the database!")
