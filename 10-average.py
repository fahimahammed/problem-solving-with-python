# 10. Write a python program to calculate total average of five subjects.

sub1 = float(input("Enter the sub1 marks: "))
sub2 = float(input("Enter the sub2 marks: "))
sub3 = float(input("Enter the sub3 marks: "))
sub4 = float(input("Enter the sub4 marks: "))
sub5 = float(input("Enter the sub5 marks: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
avg_marks = total_marks / 5 
print(f"Average marks of five subjects: {avg_marks}")