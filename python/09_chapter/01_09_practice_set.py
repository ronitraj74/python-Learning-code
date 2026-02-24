#------------------Write a program to read the text for a given file poem.txt and find out wheather it contain the given input word by the user-------------------

word = input("Enter the word to search in the file :")
f = open("poem.txt","r", encoding="utf-8")
content = f.read()
if word in content:
    print("yes")
else:
    print("Not")
f.close()
