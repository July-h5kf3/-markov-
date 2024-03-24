path = 'train_3order.out'

def inp(path,beg_symbol,end_symbol):
    passwd = {}
    with open(path,encoding="ISO-8859-1") as wordlist:
        for s in wordlist:
            wl = s.strip().split(' ')
            pd = beg_symbol * 3 + wl[0] + end_symbol
            num = (int)(wl[1])
            if pd in passwd:
                passwd[pd] += num
            else:
                passwd.setdefault(pd,num)
    return passwd

def js(passwd,order):
    base = {}
    for key,value in passwd.items():
        l = len(key)
        for i in range(l - order):
            qz = key[i:i + order]
            hz = key[i + order]
            if qz in base :
                if hz in base[qz]:
                    base[qz][hz] += value
                else:
                    base[qz].setdefault(hz,value)
            else:
                base.setdefault(qz,{})
                base[qz].setdefault(hz,value)
    return base

# test 5 : 输出以及进行laplace平滑 

import os
target_directory = r"E:\markov实验复现\3-order"
output_file_path4 = os.path.join(target_directory,"rule.out")

def laplace_4(base):
    for key,value in base.items():
        num = sum(value.values())
        for k,v in value.items():
            base[key][k] = (v * 1.0 + 0.01) / (num + 0.96)
    for key,value in base.items():
        base[key] = sorted(value.items(), key=lambda t: t[1], reverse=True)                       
    with open(output_file_path4, "w") as output_file:
        for key, value in base.items():
            output_file.write(f"{key}\n")
            for sub_key, sub_value in value:
                output_file.write(f"{sub_key} {sub_value}\n")

beg_symbol = '\x01'
end_symbol = '\0'
passwd = inp(path,beg_symbol,end_symbol)
order = 3
base = js(passwd,order)
laplace_4(base)
