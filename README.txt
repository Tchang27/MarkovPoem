README
Markov Chain - Emily Dickinson First Line Generator

Overview:
    Using data scraped from Project Gutenberg, the program builds
    a Markov Chain using Emily Dickinson's poems. Using the chain,
    it generates a line of poetry in the style of Emily Dickinson.
    An example of generated lines is found in generate_lines.txt

How to Run:
    Run generate.py to generate phrases
        Can either scrape from website, or use text document
        In the constructor, uncomment lines 17/18 to use scraper; else, the Markov chain 
        will be built using the text document of emily dickinson's poems
    Run writer.py to generate phrases and write them to a text file
        Can measure accuracy of line generator by running sample_generations()

    Libraries Needed:
    requests
    bs4
    lxml
    nltk
    language_tool_python

Known Issues/Bugs:
    Grammar rules are still being ironed out, as the generated lines
    usually output nonsensical words around half the time

    Working on comma placement, still having issues with commas
    in relation to independent/dependent clauses


Acknowledgments:
Markov Chain data structure representation inspired by Kylie Ying, https://www.youtube.com/watch?v=8ext9G7xspg