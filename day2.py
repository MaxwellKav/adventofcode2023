f = open("input2.txt", "r")
x = f.readlines()
sum=0
sum2=0
for line in x:
    splitline = line.split()
    game = splitline[1]
    splitline.pop(1)
    ran = 1
    efs = True
    cleaned_list = [word.replace(',', '').replace(';', '') for word in splitline]
    red = []
    blue = []
    green = []
    for n in cleaned_list:
        if n.isdigit():
            if int(n)>12 and cleaned_list[ran] == "red" or int(n)>13 and cleaned_list[ran] == "green" or int(n)>14 and cleaned_list[ran] == "blue":
                efs = False
            if cleaned_list[ran] == "red":
                red.append(int(n))
            if cleaned_list[ran] == "green":
                green.append(int(n))
            if cleaned_list[ran] == "blue":
                blue.append(int(n))
        ran+=1
    sum2 += max(red) * max(green) * max(blue)      
            
    if efs:
        sum += int(game.replace(':', ''))

print(sum)
print(sum2)
