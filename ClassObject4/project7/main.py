
from model.movie import Movie
n=int(input("Enter the number of movie:"))
movies=[]
for i in range(n):
    movie_id=int(input("Enter Movie ID:"))
    movie_name=input("Enter Movie name:")
    genre=input("Enter Genre:")
    rating=float(input("Enter Rating:"))
    ticket_price=int(input("Enter Ticket price:"))
    movie=Movie(movie_id,movie_name,genre,rating,ticket_price)
    movies.append(movie)

print("All Movies:")
for movie in movies:
    movie.display()

print("Movies with rating greater than 8:")
for movie in movies:
    if movie.rating>8.0:
        movie.display()

print("Action Movies:")
for movie in movies:
    if movie.genre.lower() == "action":
        movie.display()

print("Highest Rated Movie:")
highest_movie = movies[0]
for movie in movies:
    if movie.rating > highest_movie.rating:
        highest_movie = movie
highest_movie.display()

search_id = int(input("Enter Movie ID to search: "))
for movie in movies:
    if movie.movie_id == search_id:
        print("Movie Found:")
        movie.display()
        break
else:
    print("Movie not found")

total = 0
for movie in movies:
    total += movie.rating
average = total / len(movies)
print("Average Movie Rating:", round(average, 2))

print("Movies with ticket price greater than 300:")
for movie in movies:
    if movie.ticket_price > 300:
        movie.display()