import random
import os
target_directory = r"E:\markov实验复现\dataset"
output_path = os.path.join(target_directory,"train_3order.out")
with open('train.out',"r") as wordlist:
    lines = wordlist.readlines()
    len  = 1000000
    random.shuffle(lines)
    first = lines[:len]
    second = lines[len:2*len]
    third = lines[len*2:len*3]
    with open(output_path,"w") as output_file:
        passwd = {}
        for s in first:
            if s in passwd:
                passwd[s] += 1
            else:
                passwd.setdefault(s,1)
        for key,count in passwd.items():
            pd = key.strip()
            output_file.write(pd + ' ' + str(count) + '\n')
    output_path = os.path.join(target_directory,"train_4order.out")
    with open(output_path,"w") as output_file:
        passwd = {}
        for s in second:
            if s in passwd:
                passwd[s] += 1
            else:
                passwd.setdefault(s,1)
        for key,count in passwd.items():
            pd = key.strip()
            output_file.write(pd + ' ' + str(count) + '\n')
    output_path = os.path.join(target_directory,"train_5order.out")
    with open(output_path,"w") as output_file:
        passwd = {}
        for s in third:
            if s in passwd:
                passwd[s] += 1
            else:
                passwd.setdefault(s,1)
        for key,count in passwd.items():
            pd = key.strip()
            output_file.write(pd + ' ' + str(count) + '\n')
