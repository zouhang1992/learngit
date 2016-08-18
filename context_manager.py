with open("new.txt", "r") as f:
    print (f.closed)
    for line in f:
        print line,

print "\n",(f.closed)
