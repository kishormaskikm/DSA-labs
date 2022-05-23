file1 = open("myfile.txt")
print(file1.read())
file1.close()


file1 = open("myfile.txt", "a")
file1.write("\nWriting to file :) hey good moring ")
file1.close()






with open("myfile.txt", "r") as f:
    data = f.readlines()

with open("myfile.txt", "w") as f:
    f.truncate()
    # b = int(input("enter age : "))
    # for line in data :
    #
    #     if line.strip("\n") != "Age : 20" :
    #         f.write(line)

