from generate import Generator
import time

def write_lines_to_file(g, path, num):
    f = open(path, 'w')

    for _ in range(num):
        f.write(g.generate(12) + "\n")

    f.close()

def write_paragraph(g, path, num):
    f = open(path, 'w')

    f.write(g.generate(num) + "\n")

    f.close()

if __name__ == '__main__':
    start_time = time.time()
    generator = Generator()
    write_lines_to_file(generator, 'generate_lines.txt', 100)
    #write_paragraph(generator, 'generate_lines.txt', 100)
    end_time = time.time()
    print("Time to execute: " + str(end_time-start_time))

