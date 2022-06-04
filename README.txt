README
Markov Chain - Emily Dickinson First Line Generator

Overview:
    Using data scraped from Porject Gutenberg, the program builds
    a Markov Chain using Emily Dickinson's poems. Using the chain,
    it generates a line of poetry in the style of Emily Dickinson.
    An example of generated lines is found in generate_lines.txt

How to Run:
    Run generate.py to generate phrases
        Can either scrape from website, or use text document
    Run writer.py to generate phrases and write them to a text file

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
