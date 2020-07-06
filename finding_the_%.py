from itertools import islice

# Practice reading text file into dictionary
d = {}
with open('dict_test.txt') as f:
    for line in f:
        (key, val) = line.split()
        d[int(key)] = val
print(d)

## Practice reading text file into dictionary
d1 = {}
with open('dict_test_2.txt') as f:
    for line in f:
        key = line.split()[0]
        num = line.split()[1:]
        d1[key] = list(map(int, num))
print(d1)

# exercise code - specific to reading in textfile rather than user input line by line
grades = {}
n = int(open('percent_input.txt').readline().rstrip())
print(n)
with open('percent_input.txt') as f:
    for line in islice(f, 1, n+1): # read rest of lines
        key = line.split()[0]
        num = line.split()[1:]
        grades[key] = list(map(float, num))
    for query in f:
        pass
print(grades)
print(query)
print(sum(grades[query])/len(grades[query]))

# exercise code - for user input line by line
'''
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
'''