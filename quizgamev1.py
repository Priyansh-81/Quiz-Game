print("Welcome to the Computer Quiz Game!")


response=input("Do you want to play? ");

marks=0

if response.lower()!="yes":
    print("Okay, see ya later.")
    quit()

#question 1
print("What is the full form for CPU: ")
ans=input("Enter your response: ")

if ans.lower()=="central processing unit" :
    print("Correct!")
    marks+=1;
else:
    print("Incorrect Answer!")

#question 2
print("What is the full form for GPU: ")
ans=input("Enter your response: ")

if ans.lower()=="graphics processing unit" :
    print("Correct!")
    marks+=1;
else:
    print("Incorrect Answer!")

#question 3
print("What is the full form for PSU: ")
ans=input("Enter your response: ")

if ans.lower()=="power supply unit" :
    print("Correct!")
    marks+=1;
else:
    print("Incorrect Answer!")

#question 4
print("What is the full form for PROM: ")
ans=input("Enter your response: ")

if ans.lower()=="programmable read only memory" :
    print("Correct!")
    marks+=1;
else:
    print("Incorrect Answer!")

print("\nYour Score: " + str(marks)+ "\nPercentage: "+str(marks/4*100)+ "%.\nThank you for playing!")