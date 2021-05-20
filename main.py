#1 ---------------------------------------------------

#Code asks user to give a temp in fahrenheit
temperatureF = int(input("Type a fahrenheit temperature: "))

#Convert the fahrenheit temperature to celcius 
temperatureC = (temperatureF - 32) * ( 5 / 9 )

#prints the message "Your temperature in celsius is" followed by the temp in celcius
print("Your temp in celsius is " , temperatureC)

#2 --------------------------------------------------

#Check if the user wants to convert from F to C or C to F by assigning each pathway a number (1 or 2)
conversion = input("Type 1 to convert Fahrenheit to Celcius or type 2 to convert Celcius to Fahrenheit: ")
#Get the temperature that the user is trying to change
temperature = input("type the temperature you are looking to convert: ")

#if the user wants to convert F to C, preform the proper conversion and print the results with the message ("The temperature you typed in celcius is: %s." %temp)
if float(conversion)== 1:

  #preform F to C conversion
  temperature = (float(temperature) - 32) * 5 / 9
  print("The temperature you typed in celcius is: %s." %temperature)

#if the user wants to convert C to F, preform the proper conversion and print the results with the message ("The temperature you typed in fahrenheit is: %s." %temp)
elif float(conversion) == 2: 

  #preform C to F conversion
  temperature = float(temperature) * 9 / 5 + 32
  print("The temperature you typed in fahrenheit is: %s." %temperature) 

#if the user did not make their choice 1 or 2, let them know with this message "Your answer has to be a 1 or a 2. Nothing else."
else:
  print("The answer for your conversion choices has to be a 1 or a 2. Nothing else.")

#3---------------------------------------------------

#Set the number of words at the beginning to 0
num = 0

#while the word is not = to x keep repeating the program asking for a new word
while True:
    W = input("Enter one word (Click x to end the program): ")

    #Print the word chosen by the user
    print (W)       

    #if the word typed is equal to x, print the amount of words typed and end the while loop as to stop the program
    if W == "x":
        print ("%s words have been entered." %num)
        break #x does not count as a word

    #if something other than x is typed, add 1 to the number counter
    else:
        #Increases the count each time a word is typed that isn't "x"
        num = num + 1 

#4----------------------------------------------------

#set password to "hello"
pword = ("hello")

#print the message "Enter the password" and set the variable "answer" to the answer given by the user
answer = input("Type the password: ")

#while the answer given by the user is not equal to the actual password, repeat the loop
while answer != pword:
    #if the answer given is wrong, print "Wrong answer"
    print ("Wrong Answer")
    #repeat the question as to continue the loop
    answer = input("Enter the password: ")

    #if the answer given by the user is correct, print the phrase "Correct. You have cracked the password!"
    if answer == pword:
      print ("Correct. You have cracked the password!")

#5-------------------------------------------------------

#set number of numbers typed = to 0 at the start because no numbers have been typed yet
numL = 0

#set L equal to square brackets to tell the code that with the lettters being entered you are creating a list
L = []

#while the number of numbers is less than 9, keep repeating the while loop
while numL <= 9: #because lists start counting from 0

    #set numb = to a number that the user inputs when asked "Enter a number: "
    numb = input("Enter one number: ")

    #Increase numL by one each time a number is entered until the amount of numbers exceeds 9 
    numL = numL + 1

    #with the append function, add each number being typed to the list "L"
    L.append(numb)

#Print "The numbers you entered were:"
print ("The numbers typed were: ")
#following "The numbers you entered were: " \n.joinL joins all of the numbers added to the L list. Finaly these numbers are printed in order
print ("\n".join(L))