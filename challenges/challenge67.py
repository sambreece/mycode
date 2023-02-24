count = 0
vamp = open("vampytimes.txt","w")
with open("dracula.txt") as vampire_file:
    for line in vampire_file:
        if "vampire" in line.lower():
            print(line)
            vamp.write(line)
            count+=1
vamp.close()
print(f"Lines with the word vampire: {count}")
