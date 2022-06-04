README
Markov Chain - Emily Dickinson First Line Generator

Overview:
Using data scraped from Porject Gutenberg, the program builds
a Markov Chain using Emily Dickinson's poems - specificially, 
the first lines of every poem she has written. Using the chain,
it generates a line of poetry in the style of Emily Dickinson.

How to Run:
Run generate.py to generate phrases
Change the parameter in main to adjust minimum word count of the generated phrase
Note: Will need to install libraries in order to work

Known Issues/Bugs:
Grammar rules are still being ironed out, as the generated lines
usually output nonsensical words around half the time

Working on comma placement, still having issues with commas
in relation to independent/dependent clauses

Libraries Needed:
requests
bs4
lxml
nltk
