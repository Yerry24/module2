first_ = input()
second_ = input()
third_ = input()
if first_ == second_ and first_ == third_:
    print(3)
elif first_ == second_ or first_ == third_ or second_ == third_:
    print(2)
else :
    print(0)