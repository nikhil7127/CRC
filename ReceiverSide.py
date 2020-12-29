from crc_Input import Inputs, XORSignal
from termcolor import colored

msg = Inputs().getMessage("received")
gen = Inputs().getGenerator()


if(len(msg) > len(gen)):
    temp = msg
    answer = temp[0:len(gen)-1]
    for d in range(len(gen)-1, len(temp)):
        answer = XORSignal(answer+temp[d], gen)

    not int(answer) and print(colored("No Error","green"))
    int(answer) and print(colored(f"Error\nremainder : {answer}","red"))
else:
    print("Length of message should be greater than generator signal")
