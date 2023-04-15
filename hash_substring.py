# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
        text=input()
        text=text.upper()

        # input from keyboard
        
        if text.startswith("I"):
            pattern = input()
            text = input()
        if text.startswith("F"):
            file_name = open('./test/'+'06', 'r')
            dataLasa = file_name.read()
            splitedData=dataLasa.split()
            pattern = splitedData[0].rstrip()
            text =splitedData[1].rstrip()
        
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
        return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    d=256 #simbolu skaits ASCII tabulā
    q=13 #pirmskaitlis
    patLen=len(pattern)
    textLen=len(text)
    result=''
    g=0
    i=0
    patHashVal=0 #hash vērtība priekš paterna
    textHashVal=0 #hash vērtība priekš teksta
    h=1
    # and return an iterable variable
    for i in range(patLen-1):
         h=(h*d)%q
         #aprēķinās hash vērtību paternam un teksta pirmā loga vērtības
    for i in range(patLen):
         patHashVal=(d * patHashVal+ ord(pattern[i]))%q
         textHashVal=(d* textHashVal+ ord(text[i]))%q
    #iet cauri tekstam pārbaudot, kur paterns sakrīt ar tekstu
    for i in range(textLen-patLen+1):
        if patHashVal==textHashVal:
              for j in range(patLen):
                   if text[i+j] != pattern[j]:
                        break
              j+=1
              if j==patLen:
                 #print("hello1")
                 result=result+ str(i) 
        #aprēķina teksta nākamā loga vērtību + noņem pirmo simbolu un pievieno pēdējo 
        if i< textLen-patLen:
            textHashVal=(d*(textHashVal-ord(text[i])*h)+ord(text[i+patLen]))%q
        #ja gadījumā textHashVAl ir negatīva to pārveidoju uz pozitīvu
            if textHashVal<0:
                 textHashVal=textHashVal+q
    #print("result=",result)
    return (result)


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))