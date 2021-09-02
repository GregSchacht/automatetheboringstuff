import re
strongword = "b1ggl3Sd"
nocap="b1ggl3sd"
nolow="B1GGL3SD"
nonum="Bigglesd"
noalph="81661354"
tooshort="bleah"
specials="!nsalsdm"

characterRegex=re.compile(r'''\w*[A-Z]\w*[a-z]\w*\d\w*|  #Cap lower digit
                   \w*[A-Z]\w*\d\w*[a-z]\w*|  #cap digit lower
                   \w*[a-z]\w*[A-Z]\w*\d\w*| #lower cap digit
                   \w*[a-z]\w*\d\w*[A-Z]\w*| #lower digit cap
                   \w*\d\w*[A-Z]\w*[a-z]\w*| #digit cap lower
                   \w*\d\w*[a-z]\w*[A-Z]\w* #digit lower cap
                   ''', re.VERBOSE)

specialsRegex = re.compile(r"\W+")
upperRegex = re.compile(r".*[A-Z].*")
lowerRegex = re.compile(r".*[a-z].*")
digitRegex = re.compile(r".*\d.*")
lengthRegex = re.compile(r"\w{8,}")


def deepCheck(testword):
    if characterRegex.search(str(testword)) != None and lengthRegex.search(str(testword)) != None:
        print ("Looks strong to me!")
    elif specialsRegex.search(str(testword)) != None: print ("Try not using specials, moron. It's not that fancy.")
    elif lengthRegex.search(str(testword)) == None: print("That's too short, you dingus!")
    elif upperRegex.search(str(testword)) == None: print("You need an UPPERCASE letter!")
    elif lowerRegex.search(str(testword)) == None: print("You need a lowercase letter!")
    elif digitRegex.search(str(testword)) == None: print("You need a digit!")

deepCheck(tooshort)