def main():
    name = input("What is your name? ")
    name = name.capitalize()
    age = input("What is your age? ")
    age = int(age)
    fav_movie = input ("What is your favorite movie? ")
    fav_movie = fav_movie.capitalize()
    persons_theatre = [name, age, fav_movie]
    print(f"Hello {name}! You are {age} years old, and your favorite movie is {fav_movie}")
    movie_genre = input(f"Also, what is the genre of {fav_movie}? ")
    actor = input(f"What is the name of an actor from {fav_movie}? ")
    movie_info = [fav_movie, movie_genre, actor]
    persons_theatre.append(movie_info)
    print(f"So, {fav_movie} is a {movie_genre} movie, and it has {actor} in it? coo...")
main()

