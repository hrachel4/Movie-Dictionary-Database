# Movie Database Management System
# Create a dictionary to store movie information

import json

movie_database = {
    "The Dark Knight": {
        "year": 2008,
        "genre": "Action",
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    },
    "Inception": {
        "year": 2010,
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    },
    "Pulp Fiction": {
        "year": 1994,
        "genre": "Crime",
        "director": "Quentin Tarantino",
        "actors": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"]
    }
}


def add_movie():
    title = input("Enter the movie title: ")
    genre = input("Enter the movie genre: ")
    director = input("Enter the name of the director: ")
    release_date = input("Enter the release date of the movie (YYYY): ")
    actors = input("Enter the names of the actors (separated by commas): ")
    actors_list = actors.split(", ")

    movie_database[title] = {
        "genre": genre,
        "director": director,
        "release_date": release_date,
        "actors": actors_list
    }

    print(f"{title} has been added to the database.")


# Edit movie information
def edit_movie():
    title = input("Enter the movie title you want to edit: ")
    if title in movie_database:
        print("What information do you want to edit?")
        print("1. Genre")
        print("2. Director")
        print("3. Release Date")
        print("4. Actors")
        choice = input("Enter your choice (1-4): ")
# Update the selected information based on user choice
        if choice == "1":
            new_genre = input("Enter the new genre: ")
            movie_database[title]["genre"] = new_genre
            print(f"{title}'s genre has been updated.")
        elif choice == "2":
            new_director = input("Enter the new director: ")
            movie_database[title]["director"] = new_director
            print(f"{title}'s director has been updated.")
        elif choice == "3":
            new_release_date = input("Enter the new release date (YYYY-MM-DD): ")
            movie_database[title]["release_date"] = new_release_date
            print(f"{title}'s release date has been updated.")
        elif choice == "4":
            new_actors = input("Enter the new actors (separated by commas): ")
            movie_database[title]["actors"] = new_actors.split(", ")
            print(f"{title}'s actors have been updated.")
        else:
            print("Invalid choice.")
    else:
        print(f"{title} is not in the database.")   

#  Delete a movie from the database
def delete_movie():
    title = input("Enter the movie title you want to delete: ")
    if title in movie_database:
        del movie_database[title]
        print(f"{title} has been deleted from the database.")
    else:
        print(f"{title} is not in the database.")

# View all movies in the database
def view_movies():
    title = input("Enter movie title to view details (or press Enter to view all): ")
    if title == "":
        if not movie_database:
            print("The database is currently empty.")
        else:
            print("\n--- Viewing All Movies ---")
            for movie_name, details in movie_database.items():
                print(f"Title: {movie_name}")
                print(f"  Genre: {details['genre']}")
                print(f"  Director: {details['director']}")
                print(f"  Actors: {', '.join(details['actors'])}")
                print("-" * 20)
                
    elif title in movie_database:
        details = movie_database[title]
        print(f"\nTitle: {title}")
        print(f"Genre: {details['genre']}")
        print(f"Director: {details['director']}")
        print(f"Release Date: {details['release_date']}")
        print(f"Actors: {', '.join(details['actors'])}")
        print("-" * 20)
        
    else:
        print(f"Sorry, '{title}' was not found in the database.")

# Search for a movie by an criteria
def search_movie():
    search_criteria = input("Enter the search criteria (title, genre, director, release_date, actors): ")
    search_value = input("Enter the search value: ")

    found_movies = []
    for title, details in movie_database.items():
        if search_criteria in details and search_value.lower() in details[search_criteria].lower():
            found_movies.append(title)

    if found_movies:
        print("Movies found:")
        for movie in found_movies:
            print(movie)
    else:
        print("No movies found matching the criteria.")

# Save and load data to and from a file to ensure that movie data is not lost between program sessions
def save_data():
    filename = input("Enter the filename to save the data (default: movie_database.json): ")
    if not filename:
        filename = "movie_database.json"
    with open(filename, "w") as file:
        json.dump(movie_database, file, indent=4)
    print(f"Data has been saved to {filename}.")

def load_data():
    filename = input("Enter the filename to load the data from (default: movie_database.json): ")
    if not filename:        filename = "movie_database.json"
    global movie_database
    try:
        with open(filename, "r") as file:
            movie_database = json.load(file)
        print(f"Data has been loaded from {filename}.")
    except FileNotFoundError:
        print("No existing data found. Starting with an empty database.")

# Graphical user interface that enables users to perform all the required actions with ease
def main():
    load_data()
    while True:
        print("\nMovie Database Management System\n")
        print("1. Add Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. View Movies")
        print("5. Search Movie")
        print("6. Save Data")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            edit_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            view_movies()
        elif choice == "5":
            search_movie()
        elif choice == "6":
            save_data()
        elif choice == "7":
            save_data()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

