# this will produce a list of lists with exactly 1 of each integer in range 9

y = [[0 for i in range(9)] for i in range(9)]
iterations = 0
for row in y:
   for e in range(len(row)):
           row[e] = random.randint(1,9)
           while row.count(row[e]) != 1:
                   row[e] = random.randint(1,9)
                   iterations += 1
