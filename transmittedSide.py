from crc_Input import Inputs, XORSignal
from termcolor import colored

msg = Inputs().getMessage()
gen = Inputs().getGenerator()

if(len(msg) > len(gen)):
    temp = msg + (len(gen)-1)*"0"
    answer = temp[0:len(gen)-1]
    for d in range(len(gen)-1, len(temp)):
        answer = XORSignal(answer+temp[d], gen)
    msg += answer

    #normal
    # print(f"Transmitted Signal: {' '.join(msg)}")
    
    #colored
    print("Transmitted signal: ",end="")
    for index,val in enumerate(msg):
        if(len(msg)-index>len(gen)-1):
            print(val,end=" ")
        else:
            print(colored(val,"yellow"),end=" ")



else:
    print("Length of message should be greater than generator signal")


