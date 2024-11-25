with open("movies.txt") as f:
    for line in f:
        l = line.rstrip()
        try:
            cleaned = l[:l.index('-')-1]
            print(cleaned)
        except:
            print("nothing to show here")