
# Q4. Student Resource Portal

userId = input("Enter your username: ")
passKey = input("Enter your password: ")

if userId == "admin" and passKey == "ad123":
    print("Access Granted: Faculty Dashboard")

elif userId == "student" and passKey == "st2026":
    print("Access Granted: Notes and Practice Questions")

else:
    print("Invalid Credentials. Please try again")

# Q5. Traffic Light System

signal = {"red" : "Stop", "yellow" : "Slow Down", "green" : "Go"}

colorInput = input("Enter a traffic light color: ").lower()

if colorInput in signal:
    print(f"{signal[colorInput]}")

else:
    print("Invalid Color")

# Q6. Match Statement

seasonChoice = int(input("Enter a season number: "))

match seasonChoice:
    case 1:
            print("Spring")
        
    case 2:
        print("Summer")
        
    case 3:
        print("Autumn")

    case 4:
        print("Winter")

    case _:
        print("Unknown")

# Q7. Bank Loan Approval System

userAge = int(input("Enter your age: "))
monthlyIncome = int(input("Enter your monthly income: "))
creditPoint = int(input("Enter your credit score: "))

if 21 <= userAge <= 60:
    if monthlyIncome >= 30000:
        if creditPoint >= 700:
            print("Approved!")
        
        else:
            print("Disapproved! Credit Score is less than 700")
    else:
        print("Disapproved! Income is less than 30k")
else:
    print("Age is not between 21 and 60")


# Q8. Ticket booking System

personAge = int(input("Enter you age: "))
cardStatus = input("Do you have membership card? Yes or No: ").lower()
price = 200

if personAge < 12:
    print("Ticket is Free of Cost!")
    price = 0

elif 12 <= personAge <= 60 and cardStatus != 'yes':
    print(f"Ticket Cost = {price}")

elif 12 <= personAge <= 60 and cardStatus == 'yes':
    price = 150
    print(f"Ticket Cost = {price}")

else:
    price = 100
    print(f"You get a Senior citizen discount. Ticket Cost = {price}")


# Q9. Bonus for employees serving for more than 5 years

empSalary = int(input("Enter your salary: "))
workYear = float(input("Enter your year of service: "))

if workYear > 5:
    print(f"Net Bonus = {0.05 * empSalary}")

else:
    print("You don't have any bonus")


# Q10. Area of circle

circleRadius = float(input("Enter the radius of a circle: "))

print(f"Area of circle = {3.14 * circleRadius ** 2}")

# Q11. Wage per Day calculator

workerAge = int(input("Enter your age: "))
workerGender = input("Enter your gender, M or F: ").capitalize()

if 30 > workerAge >= 18:
    if workerGender == 'M':
        print("Your wage per day is 700")
    
    elif workerGender == 'F':
        print("Your wage per day is 750")

    else:
        print("Invalid Gender!")

elif 40 >= workerAge >= 30:
    if workerGender == 'M':
        print("Your wage per day is 800")
    
    elif workerGender == 'F':
        print("Your wage per day is 850")

    else:
        print("Invalid Age!")


# Q12. Fizz Buzz 

numberValue = int(input("Enter a number: "))

if numberValue % 3 == 0:
    if numberValue % 5 == 0:
        print("Fizz Buzz")
    else:
        print("Fizz")

else:
    if numberValue % 5 == 0:
        print("Buzz")
    
    else:
        print(numberValue)
    
# Q13. Electricity Bill

unitUsed = float(input("Enter your electricity usage in units: "))

if unitUsed < 100:
    print(f"Cost: Rs. {unitUsed * 5}")

elif unitUsed <= 300:
    print(f"Cost: Rs. {(100 * 5) + ((unitUsed - 100) * 8)}")

elif unitUsed > 300:
    print(f"Cost: Rs. {(100 * 5) + (200 * 8) + ((unitUsed - 300) * 10)}")

# Q14. Rock paper scissors game

firstPlayer = input("Enter your move, Rock, Paper or Scissors: ").lower()
secondPlayer = input("Enter your move, Rock, Paper or Scissors: ").lower()

gameMoves = ['rock', 'paper', 'scissors']

if firstPlayer not in gameMoves or secondPlayer not in gameMoves:
    print("Invalid Move")

else:
    if firstPlayer == secondPlayer:
        print("It is a draw")
    
    elif firstPlayer == 'rock' and secondPlayer == 'scissors':
        print("Player 1 wins")
    
    elif firstPlayer == 'paper' and secondPlayer == 'rock':
        print("Player 1 wins")

    elif firstPlayer == 'scissors' and secondPlayer == 'paper':
        print("Player 1 wins")

    else:
        print("Player 2 wins")

# Q15. positive -> odd or even

checkNum = int(input("Enter a number: "))

if checkNum >= 0:
    if checkNum % 2 == 0:
        print(f"{checkNum} is positive and even")
    
    else:
        print(f"{checkNum} is positive and odd")

else:
    print(f"{checkNum} is negative")

# Q16. Sales Handler

billAmount = float(input("Enter the total amount: "))
memberStatus = input("Are you a member? Yes or No: ").lower()

if billAmount > 1000:
    if memberStatus == 'yes':
        print(f"Final Amount: {billAmount - (billAmount * 0.2)}")

    else:
        print(f"Final Amount: {billAmount - (billAmount * 0.1)}")

else:
    print(f"Final Amount: {billAmount}")


# Q17. Weight in other planets

earthWeight = float(input("Enter your Earth Weight: "))
planetChoice = int(input("Enter a planet number, 1 to 7: "))

gravityRate = {1 : 0.38, 2 : 0.91, 3 : 0.38, 4 : 2.53, 5 : 1.07, 6 : 0.89, 7 : 1.14}

if planetChoice not in gravityRate:
    print("invalid Planet Number")

else:
    print(f"Your weight on planet {planetChoice} is {earthWeight * gravityRate[planetChoice]} kg")


# Q18. Grade Calculator

sub1 = int(input("Enter the marks of the first subject: "))
sub2 = int(input("Enter the marks of the second subject: "))
sub3 = int(input("Enter the marks of the third subject: "))
sub4 = int(input("Enter the marks of the fourth subject: "))

grandTotal = sub1 + sub2 + sub3 + sub4
percentValue = (grandTotal/400) * 100

print(f"Total Marks: {grandTotal}")
print(f"Percentage: {percentValue}")

if percentValue <= 40:
    print("Grade: Fail")

elif percentValue > 70:
    print("Grade: Distinction")

elif percentValue > 60:
    print("Grade: First Division")

elif percentValue > 40:
    print("Grade: Pass")

    # Q19. ATM logic

accountBalance = 5000

pin = input("Enter your pin: ")

if pin == '123':
    option = input("Select the appropriate option: 1. Withdraw  2. Check Balance  3. Exit: ")

    if option == 1:
        amount = int(input("Enter the amount to withdraw: "))
        
        if amount > accountBalance:
            print("Insufficient Funds!")

        else:
            accountBalance -= amount
            print(f"Successfully withdrawn Rs. {amount}! New balance is Rs. {accountBalance}")
    
    elif option == 2:
        print(f"Current balance: {accountBalance}")

    elif option == 3:
        print("Thank you for Visitng!")

    else:
        print("Invalid option!")

else:
    print("Invalid pin! Access Denied!")


# Q20. Magic Forest Game

print("Welcome to the Magic Forest!")

direction = input("Where do you want to go? North or South?: ").lower()

if direction == 'north':
    choice = input("Cross the River or follow the path? Cross or follow?: ").lower()

    if choice == 'cross':
        print("Game Over!")
    
    elif choice == 'follow':
        choice = input("Choose from Fairy, Ogre or Elf: ").lower()
        if choice == 'fairy' or choice == 'ogre':
            print("Game Over!")
        
        elif choice == 'elf':
            print("You Win!")

        else:
            print("Invalid Option!")

    else:
        print("Invalid Option!")

elif direction == 'south':
    print("Game Over!")

else:
    print("Invalid Option! Please choose the right direction")


# Q21. Smart Elevator

floorNum = int(input("Enter the floor number: "))

isDoorClosed = True
isRunning = False

if floorNum <= 10 and floorNum >= 0:
    weight = float(input("Enter the total weight: "))
    if weight <= 500:
        
        if isDoorClosed:
            isRunning = True
        else:
            print("Close the door!")
    
    else:
        print("Overweight! Lift Cannot Move!")

else:
    print("Invalid Floor Number!")