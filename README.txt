README
Markov Chain - Text Generator

Overview:
    Using data scraped from Project Gutenberg, the program builds
    a Markov Chain using Emily Dickinson's poems. Using the chain,
    it generates a line of poetry in the style of Emily Dickinson.
    An example of generated lines is found in generate_lines.txt.
    This program can be applied to other texts with varyng results.

Program Structure:
graph.py - data structure for the Markov Chain
scrape.py - optional Object that scrapes text from website. Depending on the website
            the scraper needs t0 be modified
generate.py - reads in text data, creates a Markov Chain using the words from the data,
              generates a line using the Markov Chain, adds commas/cleans grammar, then
              returns the line
writer.py - writes generated lines to a file
text_files - holds example text files to build the markov chain

How to Run:
    Run generate.py to generate phrases
        The Markov chain will be built using the text document of emily dickinson's 
        poems which was prescraped from the website
        Note: the scraper can be used but has limited functionality as of now
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
    usually output nonsensical words

    Working on comma placement, still having issues with commas
    in relation to independent/dependent clauses, such as when to add 
    commas after leading dependent clauses


Acknowledgments:
Markov Chain data structure representation inspired by Kylie Ying, https://www.youtube.com/watch?v=8ext9G7xspg