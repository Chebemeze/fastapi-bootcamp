def export_books(library: list, filename: str = "library_export.csv"):
    if not library:
        print("You entered an empty library. Provide a valid library")
        return

    with open(filename, "w") as f:
        csv_list = ["title", "author", "year", "genre", "read", "rating"]
        f.write(','.join(csv_list) + "\n")

    for book in library:
        csv_list = [book["title"], book["author"], str(book["year"]), book["genre"], str(book["read"]), str(book["rating"])]

        with open(filename, "a") as f:
            f.write(','.join(csv_list) + "\n")

    print(f"📤 Successfully exported {len(library)} book(s) to {filename}!")

# Testing the function
if __name__ == "__main__":

    library = [
        {
        "title": "The great gatsby",
        "author": "f. scott fitzgerald",
        "year": 1925,
        "genre": "fiction",
        "read": False,
        "rating": 5
        },

        {
        "title": "Purple Hibiscus",
        "author": "Chimamanda Ngozi Adichie",
        "year": 2003,
        "genre": "fiction",
        "read": True,
        "rating": 4
        },

        {
        "title": "Understanding Purpose in Times of Perplexity: Seasons of Change",
        "author": "Myles Munroe",
        "year": 1998,
        "genre": "Christian and personal growth",
        "read": True,
        "rating": 8
        }
    ]
    export_books(library)