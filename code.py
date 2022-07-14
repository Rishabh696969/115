user_score = float(input("Enter Your Marks Here"))
chances = model(user_score* lr.coef_ + lr.intercept_).ravel()[]
if chances<=0.01:
    print("Student Will Not Get Accepted")
elif chances >= 1:
    print("Student Will Get Accepted")
elif chances <0.5:
    print("Student Might Not Get Accepted")
else:
    print("Student May Get Accepted")            