# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
        
    def wasExpensive(self):
        movie_budget = self.budget
        if movie_budget > 100000000:
            return True
            print(f"The movie {self.title} was expencive - budget is {self.budget} USD")
        else:
            return False
            print(f"The movie {self.title} was cheap - budget is {self.budget} USD")

movie1 = Movie("Avatar 2", "James Cameron", 370000000)
movie2 = Movie("Harry Potter and the Philosopher Stone", "Chris Columbus", 125000000)
movie3 = Movie("Juno", "Jason Reitman", 7500000)

movie1.wasExpensive()
movie2.wasExpensive()
movie3.wasExpensive()
