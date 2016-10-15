import random
import string


class Genetic(object):
    def __init__(self, target_string, offsprings_number, required_fitness):
        self.target_string = target_string
        self.generations = 0
        self.initial_population = self.generate_string(len(self.target_string))
        self.offsprings = []
        self.offsprings_number = offsprings_number
        self.required_fitness = required_fitness

    def generate_string(self, length):
        return "".join(random.choice(string.lowercase) for i in xrange(length))

    def fitness(self, e_string):
        fitness = 0
        for i in xrange(len(self.target_string)):
            if self.target_string[i] == e_string[i]:
                fitness += 1
        return (100 / float(len(self.target_string))) * fitness

    def mutate(self, estring):
        """change random letter to a random value"""
        estring = list(estring)
        estring[random.randint(0, len(estring)) - 1] = random.choice(string.lowercase)
        return "".join(estring)

    def fill_offsprings(self, string):
        """fill self.offsprings with changed by 1 char strings"""
        for i in xrange(self.offsprings_number):
            self.offsprings.append(self.mutate(string))

    def evolve(self, olist):
        """returns the most fit element"""
        return max(olist, key=lambda x: self.fitness(x))

    def evolution(self):
        current_candidate = self.initial_population
        while current_candidate != self.target_string:
            self.fill_offsprings(current_candidate)
            current_candidate = self.evolve(self.offsprings)
            self.generations += 1
            print "{}: {}".format(self.generations, current_candidate)
        return self.generations


def main():
    sample_string = "lpsykongru"
    g = Genetic(sample_string, 10, 10.0)
    g.evolution()

if __name__ == "__main__":
    main()
