def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        print(s)
#searchname()

#prints file contents without spaces
def searchname2():
    infile = open("names.txt", "r")
    for s in infile:
        print(s[: - 1])
#searchname2()

#print lines where names start with letter A
def searchname3():
    infile = open("names.txt", "r")
    for s in infile:
        if s.startswith("A"):
            print(s[ : -1])
#searchname3()

# print names based on user input
def searchname4():
    infile = open("names.txt", "r")
    letter = input("Enter letter ")
    for s in infile:
        if letter == s.startswith(""):
            print(s[: -1])
searchname4()