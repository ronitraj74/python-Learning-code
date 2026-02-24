# f = open("myfile.txt")
# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))

# f.close()   
#---------------------------------------------------------------------
# f = open("myfile.txt")
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()

# f.close()
#---------------------------------------------------------------------
# f = open("myfile.txt", "a")
# f.write("This is nice")
# f.close()
#---------------------------------------------------------------------
#with statement
# with open("myfile.txt","r") as f:
#     text = f.read()
# print(text)