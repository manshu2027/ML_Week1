// grading system

marks = int(input("enter your marks (0-100): "))

if marks >= 90:
  grade ="A"
  if marks >= 75:
  grade ="B"
  if marks >= 60:
  grade ="C"
  if marks >= 40:
  grade ="D"

  else:
  grade = "fail"
  print(f"you get: {grade}")
