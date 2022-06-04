from generate import main
import time

def write_lines_to_file(path, num):
    f = open(path, 'w')

    for _ in range(num):
        f.write(main(12) + "\n")

    f.close()

if __name__ == '__main__':
    start_time = time.time()
    write_lines_to_file('generate_lines.txt', 100)
    end_time = time.time()
    print("Time to execute: " + str(end_time-start_time))