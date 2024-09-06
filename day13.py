print("Grade Calculator")
print()
print ("""Ready to find out your grade?
Enter your test score and we'll tell you your letter grade!""")
print()
testname = input("What is the name of the test? ")
print()
print("Let's see how you did on the", testname, "test!")
print()
maxscore = int(input("What is the maximum score you could receive? "))
yourscore = float(input("What score did you receive? "))
print()
print("Calculating...")
print()
percentage = yourscore / maxscore * 100
scorepercentage = round(percentage, 2)
if scorepercentage >= 90:
  print("\033[33mA score of", scorepercentage, "puts you at a letter grade of A+! Congratulations 🎊!")
elif scorepercentage <90 and  scorepercentage >=80:
  print(scorepercentage, "\033[32m\is a letter grade of A! Great job🎉! ")
elif scorepercentage <80 and scorepercentage >=70:
  print("\033[31mA score of", scorepercentage, "puts you at a letter grade of B! Congratulations👏!")
elif scorepercentage <70 and scorepercentage >=60:
  print("\033[34mYou got a score of", scorepercentage, "Which is a letter grade of C. You can do better!")
elif scorepercentage <60 and scorepercentage >=50:
  print("\033[35mWith", scorepercentage, "you have a letter grade of D. You need to study more!")
elif scorepercentage <50 and scorepercentage >=40:
  print("\033[36mYou got a letter grade of U with percentage of", scorepercentage, "You need to study more!")
else:
  print("""Unfortunately, you have failed the test base.
  There's room for improvement on this test.""")
