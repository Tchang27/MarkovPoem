from generate import Generator
import time
import language_tool_python

def write_lines_to_file(g, path, line_num, word_count):
    '''
    Writes generated lines to file along with grammatical accuracy

    Parameters:
    g: Markov Chain graph
    path: file path to text file to write to
    line_num: number of lines to be generated
    word_count: minimum number of words per generated line
    '''
    my_tool = language_tool_python.LanguageTool('en-US')  
    num_matches = 0
    f = open(path, 'w')

    for _ in range(line_num):
        line = g.generate(word_count)
        my_matches = my_tool.check(line) 
        if(len(my_matches) > 0):
            num_matches += 1 
        f.write(line + "\n")
    
    f.write('Precent grammatical accuracy according to LanguageTool: ' + str(((line_num-num_matches)/line_num)*100))

    f.close()

def sample_generations(g, num_samples, line_num, word_count):
    '''
    Function that averages grammatical accuracy of generated lines

    Parameters:
    g - Markov Chain
    num_smaples - number of samples of generated lines
    line_num - number of generated lines per sample
    word_count - number of minimum words per line
    '''
    my_tool = language_tool_python.LanguageTool('en-US')  
    accuracy = 0


    for _ in range(num_samples):
        num_matches = 0
        for _ in range(line_num):
            line = g.generate(word_count)
            my_matches = my_tool.check(line) 
            if(len(my_matches) > 0):
                num_matches += 1 
        accuracy += ((line_num-num_matches)/line_num)
        print(((line_num-num_matches)/line_num))

    accuracy = accuracy / num_samples
    print("Average accuracy: " + str(accuracy))
    
    
if __name__ == '__main__':
    start_time = time.time()
    generator = Generator()
    #write lines to file w/ accuracy show at the end
    write_lines_to_file(generator, 'generate_lines.txt', 100, 8)

    #gather 100 samples of 100 lines, and average accuracy
    # accuracy = 0
    # num_samples = 100
    # line_num = 100
    # sample_generations(generator, num_samples, line_num, word_count)
    
    end_time = time.time()
    print("Time to execute: " + str(end_time-start_time))

