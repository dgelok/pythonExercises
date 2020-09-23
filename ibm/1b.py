def closest(s, queries):
    # Write your code here
    memoize = {}
    answers = []
    for i in queries:
        memoize[i] = {"letter": s[i]}
    
    for j in len(queries:
        letter = s[j]
        count = 0
        

string = "hackerrank"
query = [4, 1, 6, 8]

print(closest(string, query))
