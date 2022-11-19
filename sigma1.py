##DNA BASE COUNT

#def baseCount(DNA: str):
#    print("A count => " ,DNA.count('A'))
#    print("C count => " ,DNA.count('C'))
#    print("G count => " ,DNA.count('G'))
#    print("T count => " ,DNA.count('T'))


#DNA = input("The input for DNA: ")

#baseCount(DNA)

def baseCount(DNA: str):

    countA = 0
    countC = 0
    countG = 0
    countT = 0

    for i in range(len(DNA)):

        if DNA[i] == 'A':
            countA += 1

        elif DNA[i] == 'C':
            countC += 1

        elif DNA[i] == 'G':
            countG += 1

        elif DNA[i] == 'T':
            countT += 1

        else:
            print('Invalid DNA code.')

    print("A count => " ,countA)
    print("C count => " ,countC)
    print("G count => " ,countG)
    print("T count => " ,countT)


DNA = input("The input for DNA: ")

baseCount(DNA)    

