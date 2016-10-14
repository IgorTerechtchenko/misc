import random
import string


class Genetic(object):
    def __init__(self, string, offsprings_number, required_fitness):
        self.string = string
        self.generations = 0
        self.initial_population = generate_string(len(string))
        self.offsprings = []
        self.offsprings_number = offsprings_number
        self.required_fitness = required_fitness

    def mutate(self, string):
        """change random letter to a random value"""
        string = list(string)
        string[random.randint(0, len(string))] = random.choice(string.lowercase)
        return "".join(string)

    def fill_offsprings(self, string):
        for i in self.offsprings_number:
            self.offsprings.append(self.mutate(string))

    def evolve(self):
        self.offsprings = filter(lambda i: fitness(i) >= self.required_fitness,
                                 self.offsprings)

    def evolution(self):
        self.fill_offsprings(self.initial_population)
        self.evolve()
        buf = []
        while(string not in self.offsprings):
            self.generations += 1
            self.fill_offsprings()
            self.evolve()

def fitness(s1, s2):
    fitness = 0
    for i in xrange(len(s1)):
        if s1[i] == s2[i]:
            fitness += 1
    return (100 / float(len(s1))) * fitness


def generate_string(length):
    return "".join(random.choice(string.lowercase) for i in xrange(length))


def main():
    sample_string = "lpsykongru"
    print len(sample_string)

if __name__ == "__main__":
    main()
