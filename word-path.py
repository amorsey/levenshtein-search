from string import ascii_lowercase
from queue import PriorityQueue

class WordPath:
    def __init__(self):
        #Set with all words in dictionary. Lookup O(n).
        self.words = set()

        #Map with all common anagrams. Lookup O(n).
        self.anagrams = {}

        #Map of all words and neighboring words 1 opperation away. lookup O(n).
        self.graph = {}

    #Inputs from dictionary, and adds sorted.
    def build_lookup_tables(self):
        with open('20k.txt') as f: #Change '20k.txt' to your dictionary file.
            for line in f:
                word = line.strip('\n')
                self.words.add(word)
                sorted_word = ''.join(sorted(word))
                if sorted_word not in self.anagrams:
                    self.anagrams[sorted_word] = {word}
                else:
                    self.anagrams[sorted_word].add(word)

    #Updates graph with a new node and all word's one operation away.
    #Each neighbor word also has a token for the operation required to
    #change to it. This runs in O(m) time where m is the length of 'word'.
    def add_node(self, word):
        if word not in self.graph:
            self.graph[word] = {}
            for i in range(len(word)):
                self.check_guess(word, str(word[:i]+word[i+1:]), 'del')
                for c in ascii_lowercase:
                       self.check_guess(word, str(word[:i]+c+word[i+1:]), 'chg')
                       self.check_guess(word, str(word[:i]+c+word[i:]), 'add')
                for c in ascii_lowercase:
                    self.check_guess(word, str(word+c), 'add') #Add last letter
            anagram = ''.join(sorted(word))
            if anagram in self.anagrams: #Add any anagrams
                for w in self.anagrams[anagram]:
                    if w != word:
                        self.graph[word][w] = 'ang'

    #Simplifies add_node a little
    def check_guess(self, word, guess, operation):
        if guess in self.words and guess != word:
            self.graph[word][guess] = operation

    #Converts operation token into value
    def cost(self, add, delete, change, anagram, operation):
        return {
            'add': add,
            'del': delete,
            'chg': change,
            'ang': anagram
        }[operation]

    #Number of different letters. O(l1+l2) where l1 and l2 are word lengths
    def letter_dif(self, word1, word2):
        comp = {}
        for l in word1:
            if l not in comp:
                comp[l] = 1
            else:
                comp[l] += 1
        for l in word2:
            if l not in comp:
                comp[l] = -1
            else:
                comp[l] -= 1
        difference = 0
        for l in comp:
            difference += abs(comp[l])
        return difference

    #Searches through the 'graph' only adding nodes as needed
    def find_path(self, add, delete, change, anagram, word1, word2):
        frontier = PriorityQueue() #(weight, word)
        frontier.put((0,word1))
        word_costs = {word1:(0, "")} #word :(total cost, last word)
        while not frontier.empty():
            current_word = frontier.get()[1]
            if current_word == word2:
                break
            self.add_node(current_word)
            for neighbor in self.graph[current_word]:
                operation = self.graph[current_word][neighbor]
                step_cost = self.cost(add, delete, change, anagram, operation)
                new_cost = word_costs[current_word][0] + step_cost
                in_list = neighbor in word_costs
                if not in_list or new_cost < word_costs[neighbor][0]:
                    word_costs[neighbor] = (new_cost, current_word)
                if not in_list:
                    frontier.put((new_cost+self.letter_dif(word2,neighbor), neighbor))
        return word_costs

    #Runs a single search
    def path_runner(self):
        values = input().split()
        try:
            add = int(values[0])
            delete = int(values[1])
            change = int(values[2])
            anagram = int(values[3])
        except ValueError:
            raise ValueError('must enter four ints')
        except IndexError:
            raise ValueError('must enter four ints')
        word1 = input().lower()
        word2 = input().lower()
        if add < 0 or delete < 0 or change < 0 or anagram < 0:
            raise ValueError('edge weights can not be less than zero')
        if not word1.isalpha() or not word2.isalpha():
            raise ValueError('searched words must only contain letters')
        search = self.find_path(add, delete, change, anagram, word1, word2)
        if word2 in search:
            #Uncomment see searched path
            #print(self.word_path(search,word1, word2))
            return search[word2][0]
        return -1

    #Returns words in a searched path
    def word_path(self, w, start_word, end_word):
        word = end_word
        s = ")"
        while word != start_word:
            s =  " - " + word +":"+ str(w[word][0]) + s
            word = w[word][1]
        s = "(" + word +":"+ str(w[word][0]) + s
        return s


if __name__ == "__main__":
    my_search = WordPath()
    my_search.build_lookup_tables()
    #For multiple searches on an identical dictionary change range value
    for i in range(1):
        print(my_search.path_runner())
