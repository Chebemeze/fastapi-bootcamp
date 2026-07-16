def export_books(library: dict, filename: str = "library_export.csv"):
    if library is None:
        return
    try:
        with open(filename, "r"):
            pass
    except Exception:
        user_reply = input("The file name you entered doesn't exist, do you want to create it? y/n\n")
        if user_reply == "n" or user_reply == "N":
            return

    csv_list = ["title", "author", "year", "genre", "status", "rating"]
    with open(filename, "w") as f:
        each_line = ','.join(csv_list)
        f.write(each_line + "\n")

    count = 0
    for title in library:
        author = library[title]["author"]
        year = library[title]["year"]
        genre = library[title]["genre"]
        status = library[title]["status"] # asks them to change the read to status instead
        rating = library[title]["rating"]

        csv_list = [title, author, str(year), genre, status, str(rating)]


        each_line = ','.join(csv_list)

        if count < len(library)-1:
            with open(filename, "a") as f:
                f.write(each_line + "\n")
        else:
            with open(filename, "a") as f:
                f.write(each_line)
        count += 1

    print(f"📤 Successfully exported {len(library)} book(s) to {filename}!")

if __name__ == "__main__":

    # I am using nested dict instead of list because I dont want repeated books inside the dictionary
    library = {
        "The great gatsby" : {
        "author": "f. scott fitzgerald",
        "year": 1925,
        "genre": "fiction",
        "status": "read",
        "rating": 5
        },

        "Purple Hibiscus" : {
        "author": "Chimamanda Ngozi Adichie",
        "year": 2003,
        "genre": "fiction",
        "status": "No",
        "rating": 4
        },

        "Understanding Purpose in Times of Perplexity: Seasons of Change" : {
        "author": "Myles Munroe",
        "year": 1998,
        "genre": "Christian and personal growth",
        "status": "No",
        "rating": 8
        }
    }
    export_books(library)