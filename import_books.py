import pandas as pd
from app import db, Book, app  # Importing your existing database and Book model

# Load the CSV file
df = pd.read_csv('data/best-selling-books.csv')  # Replace with the actual path to your CSV file

with app.app_context():
    # Loop through the CSV file and add each entry to the SQLite database
    for index, row in df.iterrows():
        # Create a new book instance
        book = Book(
            title=row['Title'],
            author=row['Author(s)'],
            original_language=row['Original language'],
            first_published_year=row['First published'],
            sales=row['Approximate sales in millions'],
            genre=row['Genre']
        )
        
        # Add the book to the session
        db.session.add(book)

    # Commit the changes to save all the entries to the database
    db.session.commit()

print("Books have been successfully imported into the database!")
