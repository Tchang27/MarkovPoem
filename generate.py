from distutils.command.build_scripts import first_line_re
from scrape import Scraper
from graph import Graph, Vertex
import random
import nltk
from nltk.corpus import stopwords
import re
import string

STOP_WORDS = set(stopwords.words('english'))

#function if i need to grab words from a text document instead of scraping website
class Generator:
    def __init__(self):
        #for scraping
        # scraper = Scraper()
        # words = scraper.scrape_poems('https://www.gutenberg.org/files/12242/12242-h/12242-h.htm')

        #for text document
        self.words = []
        self.words = self.grab_words('dickinson_poems.txt')

        #make graph
        self.graph = self.generate_graph(self.words)

    def grab_words(self,path):
        with open(path, 'r') as f:
            text = f.read()

            #removes punctuation
            text = re.sub(r'\[(.+)\]', ' ', text)
            #removes roman numerals
            text = re.sub(r'(?=\b[MCDXLVI]{1,6}\b)M{0,4}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})(.)', ' ', text)
            #removes hyphens
            text = re.sub(r'[—]', ' ', text)
            text = ' '.join(text.split())
            text = text.lower()
            my_punctuation = string.punctuation.replace("'", "")
            text = text.translate(str.maketrans('','', my_punctuation))

        words = text.split()

        return words

    def generate_graph(self,words):
        g = Graph()
        words = nltk.pos_tag(words)

        previous_vertex = None
        previous_pos = None
        current_pos = None

        for word in words:
            word = list(word)
            word_vertex = g.get_vertex(word[0])
            current_pos = word[1]

            #change chain weighting based on previous part of speech
            if previous_vertex:
                    if previous_pos == current_pos:
                        if previous_pos == 'CC':
                            previous_vertex.increment_edge(word_vertex, 0.1)
                        elif previous_pos[0] == 'N':
                            previous_vertex.increment_edge(word_vertex, 0.3)
                        elif previous_pos == 'PRP' or previous_pos == 'PRP$':
                            previous_vertex.increment_edge(word_vertex, 0.1)
                        else:
                            previous_vertex.increment_edge(word_vertex)
                    else:
                        previous_vertex.increment_edge(word_vertex)

            previous_vertex = word_vertex
            previous_pos = current_pos

        #after every word is in the graph, generate probability mappings
        g.generate_probability_maps()

        return g

    def write_line(self, graph: Graph, words, count = 10):
        line = []

        #for the inputted number of words, generate a line using graph
        #try to follow grammatical rules - commas for clauses, ending on non-preposition or conjunction
        word = 'END'
        while word == 'END':
            word = graph.get_vertex(random.choice(words))
        
        prev_word = None
        for _ in range(count):
            while word.value == 'END' or word.value == prev_word:
                word = graph.get_next_word(word)
            line.append(word.value)
            prev_word = word.value
            word = graph.get_next_word(word)
        
        last_word = line[len(line)-1]
        word = graph.get_next_word(graph.vertices[last_word])
        while(last_word in STOP_WORDS):
            while word.value == 'END':
                word = graph.get_next_word(word)
            line.append(word.value)
            last_word = word.value
            word = graph.get_next_word(word)
        return line

    def clean_line(self, line):
        contains_verb = False
        contains_subject = False
        contains_object = False
        complete_clause = False
        determiner = False
        previous_pos = None

        line = nltk.pos_tag(line)

        for i in range(len(line)):
            item = list(line[i])

            if item[1] == 'DT' or item[1] == 'PRP$' or item[1] == 'PDT' :
                determiner = True
            elif item[1][0] == 'V':
                if not contains_verb:
                    contains_verb = True
            elif item[1][0] == 'N' or item[1] == 'PRP':
                if not contains_subject:
                    contains_subject = True
                elif not contains_object:
                    contains_object = True
                elif previous_pos != 'DETERMINER':
                    prev_item = list(line[i-1])
                    prev_item[0] = str(prev_item[0]) + ','
                    line[i-1] = (prev_item[0], prev_item[1])
                    contains_verb = False
                    contains_subject = False
                    contains_object = False
            if contains_verb and contains_subject and contains_object and previous_pos != 'DETERMINER' \
                and previous_pos != 'DT' and not determiner:
                complete_clause = True
                contains_verb = False
                contains_subject = False
                contains_object = False
            if complete_clause:
                item[0] = str(item[0]) + ','
                line[i] = (item[0], item[1])
                contains_verb = False
                contains_subject = False
                contains_object = False
                determiner = False
                complete_clause = False
            if determiner:
                previous_pos = 'DETERMINER' 
                determiner = False
            else:
                previous_pos = item[1] 
        
        corrected_line = []
        for item in line:
            if len(corrected_line) < 1:
                    first_word = item[0].capitalize()
                    corrected_line.append(first_word)
            else:
                corrected_line.append(item[0])

        return corrected_line


    def generate(self, length):
        #use graph to generate a line, input miminmum word count
        generated_line = self.write_line(self.graph, self.words, length)

        #this cleans the line using my own grammar rules - STILL INCOMPLETE/HAS BUGS
        punct_line = self.clean_line(generated_line)

        
        #print line
        return ' '.join(punct_line)

if __name__ == '__main__':
    generator = Generator()
    print(generator.generate(10))