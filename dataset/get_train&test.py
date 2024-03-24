import random
import os
with open('rockyou_without_count',"r") as wordlist:
    lines = wordlist.readlines()
    random.shuffle(lines)
    half_len = len(lines) // 2
    first_half = lines[:half_len]
    second_half = lines[half_len:]
    target_directory = r"E:\markov实验复现\dataset"
    output_path = os.path.join(target_directory,"train.out")
    with open(output_path,"w") as output_file:
        for s in first_half:
            pd = s.strip()
            output_file.write(pd+'\n')
    output_path = os.path.join(target_directory,"test.out")
    with open(output_path,"w") as output_file:
        passwd = {}
        for s in second_half:
            if s in passwd:
                passwd[s] += 1
            else:
                passwd.setdefault(s,1)
        for s,count in passwd.items():
            pd = s.strip()
            output_file.write(pd + ' ' + str(count) + '\n')