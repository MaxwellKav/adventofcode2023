import re

def hello():
    numbers = []
    #check = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    f = open("input.txt", "r")
    x = f.readlines()
    for line in x:
        tal = ""
        word_to_number = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'ten': '10'
        }
        linematches = re.findall(r'(?:one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)', line)
        for i in range(len(linematches)):
            for word, number in word_to_number.items():
                linematches[i] = linematches[i].replace(word, number)
        tal += linematches[0]
        tal += linematches[-1]
        numbers.append(int(tal))
    sum = 0
    for x in numbers:
        sum+=x
    print(sum)
hello()
