from my_utils import is_line_valid
import re

def count_200s():
    counter = 0
    
    while True:
        try:
            line = input()
            
            if not is_line_valid(line):
                raise ValueError("Invalid line")
            elif re.search(" 200 .*$", line):
                counter += 1
            
        except EOFError:
            break
        
    print(counter)
    
    
if __name__ == '__main__':
    count_200s()