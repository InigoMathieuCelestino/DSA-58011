n = int(input("Enter number of elements: "))
test_scores = [0]*n
odd = 0

for i in range(n):
    test_scores[i] = int(input("Enter test score: "))

print("Scores in the list are: ", test_scores)

for i in range(n):

    if test_scores[i] % 2 == 1:

        odd = odd+test_scores[i]

print("The sum of all odd score are: ", odd)
