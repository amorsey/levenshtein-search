# levenshtein-search

## Problem
You’ve probably heard of the Levenshtein distance between strings (if you haven’t, no problem! Check it out on [https://en.wikipedia.org/wiki/Levenshtein_distance](Wikipedia).  Your task is to transform one word into another, with four operations: add a letter, delete a letter, change a letter, and take an anagram of the existing word.  Additionally, you have to obey the following rules:

Every interim step between the first and the last word must also be a word
No interim step can be less than three letters
The first line of input will contain the “cost” of each operation in the order above
The second line of input will contain the starting word
The third line of input will contain the ending word

Your goal is to find the lowest possible “cost” of transforming the starting word into the ending word.  You can use any word list you like -- feel free to include your word list or a link to it as part of your solution. (Depending on your word list, your answer might not be exactly the same as ours below.)

Your solution should detect and handle invalid input, and return -1 if there is no solution.


## Example inputs:

1 3 1 5\
HEALTH\
HANDS\
(output: 7) (HEALTH - HEATH - HEATS - HENTS - HENDS - HANDS)

1 9 1 3\
TEAM\
MATE\
(output: 3) (TEAM - MATE)

7 1 5 2\
OPHTHALMOLOGY\
GLASSES\
(output: -1)


## Solution
### Running Program
1. Make sure you have Python3 installed on your machine.
1. Download the 20k.txt and LevSearch.py files, and make sure they are both in the same directory.
2. Run LevSearch.py with Python3.

### Explanation
You can imagine each word as a node on a graph, where words with a Levenshtein of 1 are connected by an edge.

Once you convert the problem into a graph you can use a standard graph search algorithm to find the shortest distance.

1. Read in data and create lookup tables for each word and the anagrams of each word.
2. Starting with the first word:
   1. Sort its letters and check that against the anagram table.
   2. Go through each letter variation and check those against the word table.
   3. Add any matching words to a list of neighbor words.
   4. Choose a word from the list of seen words with the smallest change cost and repeat.
3. Continue this process until one of two things happen:
   1. You run out of seen words. Then return -1.
   2. You have found the destination word, and your remaining seen words would all create longer paths than your current shortest path.

### Runtime
#### Creating the tables
Creating the lookup tables will take O(nm) time where n is the number of words in the dictionary and m is the length of the longest word. Since m much smaller than n we can simplify this to O(n).

#### Checking for a word's neighbors
Checking each variation of a word will take O(m).

#### Traversing the graph
The traversal of a graph has a runtime of O(elog(v)) where e is the number of edges and v is the number of vertices. In our case that is O(n^2log(n)) because at most each word is connected to each other word once.

#### Combining everything
Adding everything we get O(n + mn^2log(n)). This simplifies to O(n^2log(n)).

Since we choose the shortest cost node for each step our average time will end up being much better than this.
