print("Day 13: Test Scores")
print()
test_name = input("What is the name of your test? ")
test_score = int(input("What was your test score? "))
max_score = int(input("What was the max score of the test? "))
print()

test_percentage = round(float((test_score / max_score) * 100), 2)


if test_percentage >= 95 and test_percentage <= 100:
  print(f"Your score: {test_percentage}%, which is an A+ 🙌🏻🏆")
elif test_percentage >= 90 and test_percentage < 95:
  print(f"Your score: {test_percentage}%, which is an A 🥇")
elif test_percentage >= 80 and test_percentage < 90:
  print(f"Your score: {test_percentage}%, which is a B 🥈")
elif test_percentage >= 70 and test_percentage < 80:
  print(f"Your score: {test_percentage}%, which is a C 🥉")
elif test_percentage >= 75 and test_percentage < 80:
  print(f"Your score: {test_percentage}%, which is a D 🫤")
else:
  print(f"Your score: {test_percentage}%, you failed the test 😢")