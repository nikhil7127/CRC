class Inputs(object):
    def getMessage(self,val="message"):
        while 1:
            try:
                temp = int(input(f"Enter {val} Signal: "), 2)
                return bin(temp)[2:]
            except:
                print("Enter valid value")

    def getGenerator(self): 
        while 1:
            try:
                gen = int(input("Enter Generator Signal: "), 2)
                gen = bin(gen)[2:]
                if(gen[0] == "1" and gen[-1] == "1" and len(gen) > 2):
                    return gen
                else:
                    print("Genertor signal must start and end with 1")
            except:
                print("Enter valid value")


def XORSignal(a, b):
    send = len(b)-1
    if(str(a)[0] == "0"): 
        a = int(str(a), 2)
        return bin(a)[2:].rjust(send,"0")
    elif(str(a)[0] == "1"):
        send = len(b)-1
        a = int(str(a), 2)
        b = int(str(b), 2)
        return bin(a^b)[2:].rjust(send,"0")


if __name__ == "__main__":
    Inputs().getMessage()
    Inputs().getGenerator()


