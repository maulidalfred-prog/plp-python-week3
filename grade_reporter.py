scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0

for score in scores:
    if score >= 80:
        print(score, "A")
    elif score >= 70:
        print(score, "B")
    elif score >= 50:
        print(score, "C")
    else:
        print(score, "F")
    if score >= 50:
        passed += 1
    else:
        failed += 1

total = sum(scores)
average = total / len(scores)

print("Passed:", passed)
print("Failed:", failed)
print("Average:", round(average, 1))