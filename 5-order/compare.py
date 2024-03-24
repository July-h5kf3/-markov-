import matplotlib.pyplot as plt
import numpy as np
beg_symbol = '\x01'
def input_testda(path):
    passwd = {}
    sum0 = 0
    with open(path,"r") as wordlist:
        for s in wordlist:
            wl = s.strip().split(' ')
            pd = beg_symbol * 5 + wl[0]+'\0'
            num = (int)(wl[1])
            if pd in passwd:
                passwd[pd] += num
                sum0 += num
            else:
                passwd.setdefault(pd,num)
                sum0 += num
    return passwd,sum0
import os
target_directory = r"E:\markov实验复现\5-order"
output_file_path = os.path.join(target_directory,"guess.out")
def comp(path,pas,sum0):
    now_guess = []
    suc_guess = []
    sum = 0
    sum1 = 0
    with open(path,"r") as wordlist:
        for s in wordlist:
            s = s.strip()
            if s in pas:
                sum += pas[s]
                sum1 += 1
            else:
                sum1 += 1
            now_guess.append(sum1)
            suc_guess.append((float)(1.0 * sum / sum0))
            #print(sum,len(now_guess))
    return now_guess,suc_guess
pas,Sum = input_testda(path='test.out')
path = 'guess.out'
x_value,y_value = comp(path,pas,Sum)
print(y_value[-1])
plt.plot(np.log10(x_value),y_value,marker='o')
plt.xlabel('Now Guess')
plt.ylabel('sucessful Guess')
plt.title('5-order Markov')
plt.show()