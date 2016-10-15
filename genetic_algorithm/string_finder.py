import random
import string


class Genetic(object):
    def __init__(self, target_string, offsprings_number, required_fitness):
        self.target_string = target_string
        self.generations = 0
        self.initial_population = generate_string(len(self.target_string))
        self.offsprings = []
        self.offsprings_number = offsprings_number
        self.required_fitness = required_fitness

    def mutate(self, estring):
        """change random letter to a random value"""
        estring = list(estring)
        estring[random.randint(0, len(estring)) - 1] = random.choice(string.lowercase)
        return "".join(estring)

    def fill_offsprings(self, string):
        for i in xrange(self.offsprings_number):
            self.offsprings.append(self.mutate(string))

    def evolve(self, olist):
        """remove elements not fit enough"""
        offsprings = filter(lambda i: fitness(i, self.target_string) >= self.required_fitness,
                            olist)
        return offsprings

    def evolution(self):
        self.fill_offsprings(self.initial_population)
        survivors = self.evolve(self.offsprings)
        while(self.target_string not in self.offsprings):
            self.offsprings = []
            self.generations += 1
            for i in survivors:
                self.fill_offsprings(i)
            survivors = self.evolve(self.offsprings)
            print survivors
        return self.generations


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
    g = Genetic(sample_string, 10, 10.0)
    print g.evolution()

if __name__ == "__main__":
    main()
