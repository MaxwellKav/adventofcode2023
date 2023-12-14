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
        linematches = re.findall(r'(?:|one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)', line)
        print(linematches)
        for i in range(len(linematches)):
            for word, number in word_to_number.items():
                linematches[i] = linematches[i].replace(word, number)
        print(linematches)
        tal += str(int(linematches[0]))
        tal += str(int(linematches[-1]))
        print(tal)
        numbers.append(int(tal))
        '''
        for letter in line:
            if letter.isdigit():
                number += letter
                break
        for letter in line[::-1]:
            if letter.isdigit():
                number += letter
                break
        numbers.append(int(number))
        '''
    test = 0
    sum = 0
    for x in numbers:
        print(x)
        sum+=x
        test+=1
    print(test)
    print(sum)
hello()
