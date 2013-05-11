import csv
with open('test.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    headers = reader.next()
    
    minlens = []
    maxlens = []
    # building the arrays with the correct length
    for cell in headers :
        minlens.append(len(cell))
        maxlens.append(len(cell))

    for row in reader:
        i = 0
        # give some output if it's a big file just to let keep you interested
        if reader.line_num % 100000 == 0 : print "processed " + str(reader.line_num) + " Lines"
        for cell in row :
            if len(cell) < minlens[i] :
                minlens[i] = len(cell)
            if (len(cell) > maxlens[i]) :
                maxlens[i] = len(cell)
            i = i + 1
    print headers
    print minlens
    print maxlens
    print "done"