from generate import Generator
import time
import language_tool_python

def write_lines_to_file(g, path, num):
    my_tool = language_tool_python.LanguageTool('en-US')  
    num_matches = 0
    f = open(path, 'w')

    for _ in range(num):
        line = g.generate(12)
        my_matches = my_tool.check(line) 
        if(len(my_matches) > 0):
            num_matches += 1 
        f.write(line + "\n")
        f.write(str(my_matches) + "\n")
    
    f.write('Precent grammar accuracy according to LanguageTool: ' + str(((num-num_matches)/num)*100))
    f.close()
    return (num_matches/num)*100

def write_paragraph(g, path, num):
    f = open(path, 'w')

    f.write(g.generate(num) + "\n")

    f.close()

def sample_generations(g, num_samples, line_num):
    my_tool = language_tool_python.LanguageTool('en-US')  
    accuracy = 0


    for _ in range(num_samples):
        num_matches = 0
        for _ in range(line_num):
            line = g.generate(12)
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
    write_lines_to_file(generator, 'generate_lines.txt', 100)

    #write a paragraph to file
    #write_paragraph(generator, 'generate_lines.txt', 100)

    #gather 100 samples of 100 lines, and average accuracy
    # accuracy = 0
    # num_samples = 100
    # line_num = 100
    # sample_generations(generator, num_samples, line_num)
    
    end_time = time.time()
    print("Time to execute: " + str(end_time-start_time))

