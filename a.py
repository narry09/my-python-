def old_macdonald(name):
    firstletter=name[0]
    inbetween=name[1:3]
    fourthletter=name[3]
    rest=name[4:]
    return firstletter.upper()+inbetween+fourthletter.upper()+rest
print(old_macdonald('narry'))