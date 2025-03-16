"""CHAPTER 5 no. 10"""
test_scores = []
counter = 0

# this block takes test scores input
while counter < 10:
    try:
        score = float(input(f"{[counter+1]} Enter test score: "))
        if score > 100:
            print("Score greater than 100 is entered. Try again.")
            raise ValueError("Score greater than 100 is entered.") # raises an error whenever a score greater than 100 is entered
        else:
            test_scores.append(score)
            counter += 1
    except Exception as e:
        print(f"ERROR: {e}")
        
test_scores.sort() # sorts out test_scores variable in an ascending order

print(f"""Highest score: {test_scores[9]}
Lowset score: {test_scores[0]}
Average: {(sum(test_scores))/10}
Second Largest Score: {test_scores[8]}""")

# pops out the two lowest scores, then computes the new average
test_scores.pop(0)
test_scores.pop(0)
print(f"Average Score (two lowest dropped): {(sum(test_scores))/8}")

"""CHAPTER 8 no. 15"""
lst = [1 if j==0 else 0 for i in range(12) for j in range(i)]
print(lst)

"""CHAPTER 10 no. 26"""
solutions = []
while True:
    try:
        test = float(input("Enter a number: ")) # this still accepts numbers with decimals. however, it will still print out nothing.
        break
    except Exception as e:
        continue

for i in range(1,1001):
    for j in range(1,i):
        if i**2 - j**2 == test: # appends if match
            solutions.append((i, j))
            
if solutions:
    print(f"The following differences leads to this number -> {test}")
    for x, y in solutions:
        print(f"{x}**2 - {y}**2 = {test}")

else:
    print("No solutions found within the range.")
