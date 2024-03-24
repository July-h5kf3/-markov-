import random
import os
target_directory = r"E:\markov实验复现\dataset"
output_path_file = os.path.join(target_directory,'train_without_count')
path = 'rockyou.out'
with open(path) as wordlist:
    with open(output_path_file,"w") as output_file:
        for s in wordlist:
            wl = s.strip().split(' ')
            pd = wl[0]
            num = (int)(wl[1])
            for i in range(0,num):
                output_file.write(pd+'\n')
            
    