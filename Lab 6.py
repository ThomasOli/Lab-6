
def encode(passcode):
    pas = " "
    for i in passcode:
        pas += str((int(i)+3) % 10)
    return pas
        

