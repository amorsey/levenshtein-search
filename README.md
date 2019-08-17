# levenshtein-search

## Problem
You’ve probably heard of the Levenshtein distance between strings (if you haven’t, no problem! Check it out on Wikipedia).  Your task is to transform one word into another, with four operations: add a letter, delete a letter, change a letter, and take an anagram of the existing word.  Additionally, you have to obey the following rules:

Every interim step between the first and the last word must also be a word
No interim step can be less than three letters
The first line of input will contain the “cost” of each operation in the order above
The second line of input will contain the starting word
The third line of input will contain the ending word

Your goal is to find the lowest possible “cost” of transforming the starting word into the ending word.  You can use any word list you like -- feel free to include your word list or a link to it as part of your solution. (Depending on your word list, your answer might not be exactly the same as ours below.)

Your solution should detect and handle invalid input, and return -1 if there is no solution.

Example input:

1 3 1 5
HEALTH
HANDS
(output: 7) (HEALTH - HEATH - HEATS - HENTS - HENDS - HANDS)
(If your dictionary doesn’t have a couple of these words in there, don’t worry -- you’re scored on your code, not your word list.)

1 9 1 3
TEAM
MATE
(output: 3) (TEAM - MATE)

7 1 5 2
OPHTHALMOLOGY
GLASSES
(output: -1)


## Solution
To run the program make sure you have Python3 and pip3 install on your machine. I suggest running the program in a enviroment using virtualenv.

### Setup
Creaing an enviroment (optional):
'''virtualenv ENV -p python3 #optional
source ENV/bin/activate #optional'''
Installing libraries:
'''pip install 
'''
###

## Explanation
You can imagine each word as a node on a graph, where words with a Levenshtein of 1 (L1) are connected by an edge.

When looking at the problem this way there are two main tasks:
1. Create the graph.
2. Search the graph for the shortest path between any given words.

For finding a word's neighbors we can compare it to every other word in the dictionary for an O(n) time, where n is the size of the dictionary. However if we iterate through all variations of a word and check in a hashmap it takes O(n) time once to create the hashmap, and O(m) for each subsequent check. Assuming n >> m, or in other words, that our dictionary size will be much larger than our word lengths, than this is a good tradoff. If we are doing multiple searches through the same dictionary we can further save time by reusing the graph we create.

#To search the graph I used standard A* pathfinding with number of differing
#letters as my heuristic. I could have used Levenshtein distance, but that
#does not account for anagrams, so I choose the more general option. In the
#worst case it searches all words, all words are connected to eachother, and
#it has to find all neighbors each time. That gives, O(n^2m).
