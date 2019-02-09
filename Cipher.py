##encrypts messages with a shift caeser cipher



alphaone={"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,        #maps numbers to letters
          "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19,
          "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
onealpha={}                                                                            #maps letters to numbers
for (letter,number) in alphaone.items():
    onealpha[number]=letter


def ask(question):
    "converts the answer to question to lowercase"
    response=str(input(question))
    return response.lower()


def ask_int(question):
    "only accepts positive or negative integers"
    response=input(question)
    done="not done"
    while done!="DONE":
        if response.isdigit():
            done="DONE"
        elif response[0]=="-":
            truncated=response[1:len(response)]
            if truncated.isdigit():
                    done="DONE"
            else:
                response=input(question)
        else:
            response = input(question)
    return (int(response))


def encrypt():
    "uses a shift cipher of x to convert a message to a new message"
    messagelist=[]
    newmessagelist=[]
    newmessage=''
    shift=(ask_int("How far would you like to shift?"))
    while shift >26:
            shift=shift-26
    while shift<0:
            shift=shift+26
    message=ask("What is your message?")
    alphax=alphaone.copy()
    for i in alphax:
        alphax[i]+=shift
        while alphax[i]>26:
            alphax[i]-=26
    for i in message:
        if i not in alphax:
            messagelist.append(i)
        elif i in alphax:
            messagelist.append(alphax[i])
    for i in messagelist:
        if i not in onealpha:
            newmessagelist.append(i)
        elif i in onealpha:
            newmessagelist.append(onealpha[i])
    for i in range(0,len(newmessagelist)):
        newmessage=newmessage+newmessagelist[i]
    return newmessage


print(encrypt())
