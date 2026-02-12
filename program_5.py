'''Bank Balance/Budget Analysis Program
By Grace LeVoir
1 - 12 - 26'''


# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.


'''Pseudocode'''
    #Collect user budget
    #While there are expenses:
        #Input expense
        #Add expense to total
        #If expense is 0
            #Exit loop
    #If budget is greater than expenses
        #Difference is budget minus expenses
        #Display difference
    #If expenses are greater than budget
        #Difference is expenses minus budget
        #Display difference
    #If expenses equal budget
        #Display lack of difference
''''''


def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    # WRITE YOUR CODE HERE
    ######################

    budget = float(input('Enter budget: '))

    while True:

        spent = float(input('Enter expense or enter 0 for no more expenses: $ '))

        if spent == 0:
            break

        total += spent

    if budget > total:
        difference = budget - total
        print(f'You are ${difference:.2f} under budget.')

    if total > budget:
        difference = total - budget
        print(f'You are ${difference:.2f} over budget.')

    if budget == total:
        print('You are neither under or over budget; your expenses were exactly equal to your budget!')

if __name__ == '__main__':
    main()