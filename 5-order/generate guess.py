import os 
import numpy as np
def input_rule(path,order):
    passwd = {}
    with open(path,"r") as wordlist:
        now_word = None
        for s in wordlist:
            s = s.strip()
            if s == '\n':
                continue
            if len(s) == order:
                now_word = s
            else:
                wl = s.strip().split(' ')
                hz = wl[0]
                num = (float)(wl[1])
                if now_word in passwd:
                    passwd[now_word].setdefault(hz,num)
                else:
                    passwd.setdefault(now_word,{})
                    passwd[now_word].setdefault(hz,num)
    return passwd
now_guess = {}
#采取The threshold search algorithm生成口令，然后对生成的口令排序
path = 'rule.out'
passwd = input_rule(path,5)
threhold_d = (float)(1.0 / 1e7)
threhold_u = (float)(1.0)
target_directory = target_directory = r"E:\markov实验复现\5-order"
output_file_path = os.path.join(target_directory,'guess.out')
guesses = []
global total_guess
total_guess = 0
beg_symbol = '\x01'
def generate_passwd(depth,now_word,p,threhold_d,threhold_u):
    global total_guess
    if p <= threhold_d:
        return
    s = now_word[-5:]
    if s in passwd:
        for key,value in passwd[s].items():
            if key == '\0':
                if now_word + key not in now_guess:
                    now_guess.setdefault(now_word + key,p*value)
                    guesses.append([now_word+key,p*value])
                    #print(now_word + key,p*value)
                    total_guess += 1
            else:
                generate_passwd(depth+1,now_word+key,p*value,threhold_d,threhold_u)

while total_guess < 1e7 and (threhold_u != 0 and threhold_d != 0):#这里最后生成的密码次数与迭代次数有关不会是1e7
    generate_passwd(0,beg_symbol*5,1,threhold_d,threhold_u)
    threhold_u = threhold_d
    threhold_d = 1.0 * threhold_d / min(2.0,1.5 * 1e7 / total_guess)
    print(threhold_d,threhold_u)

print(total_guess)
guesses = sorted(guesses,key = lambda x:x[1],reverse=True)

with open(output_file_path,"w") as output_file:
    for i,item in enumerate(guesses):
        if i < 1e7:
            output_file.write(item[0])
            output_file.write('\n')
        else:
            break