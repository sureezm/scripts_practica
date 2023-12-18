import os

#archives in directory, add a "/"  to the end of directory.
dir = 'src/refs/'
archives = os.listdir(dir)

refs = []

for archname in archives:
    #deleting nono numeral characters in the name
    number_archive = archname.replace('references','').replace('.txt','')

    #deleting initials ceros for number of publication
    while number_archive[0] == "0":
        number_archive = number_archive[1:]    
    route = dir + archname
    arch = open((route), encoding="utf8") 
    content = arch.readlines()[1:]
    nref = 0 #cont of lines = index of reference
    for i in content:
        nref += 1
        refs.append((int(number_archive),nref,i)) #(archive number, reference number, reference)
    arch.close()

for reference in refs:
    tup = list(reference) #convert into a list to be able to edit the reference
    tup[2] = tup[2].replace('\n','') #deleting the line break
    #numeration can be [x] or x., in both cases after the first space is where the reference begins 
    while tup[2][0] != ' ': #detecting the first space to delete all before it
        tup[2] = tup[2][1:]
    tup[2] = tup[2][1:] #delete the space
    reference = tuple(tup) #convert the list into a tuple