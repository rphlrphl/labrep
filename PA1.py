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
test_scores.pop(1)
print(f"Average Score (two lowest dropped): {(sum(test_scores))/8}")
