#1. make a dictionary variable with two keys and their values: fullName and reasonForAttendingAISaturday

dict = {
    'fullName': 'Oluwafunmito Odefemi', 'reasonForAttendingAISaturday':  'I hope to have improved greatly on my Python skillset and have learnt enough to be able to contribute to a team that will profer solutions to local challenges using Machine Learning and Artificial Intelligence'
}


#2. Make a print statement saying "My name is _ and at the end of this cohort I want to __"

print('My name is ' + dict['fullName'] + ' and by the end of this cohort, ' + dict['reasonForAttendingAISaturday'])


#3. Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = list(range(0,101)) #series of numbers

x = 0 #initialize counter for even numbers

y = 0 #initialize counter for odd numbers

#for loop to count even and odd numbers
for number in numbers: 
    if (number % 2 == 0):
        x = x + 1
    else :
        y = y + 1
        
        
#4. Print Number of even numbers and Number of odd numbers

print('Number of even numbers: ', x)
print('Number of odd numbers: ', y)