'''Average Rainfall Program
By Grace LeVoir
2 - 12 - 26'''


# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    # WRITE YOUR CODE HERE
    ######################    

    number_of_months = 0
    total_rainfall = 0

    years = int(input('How many years would you like? '))

    for year in range(1, years + 1):

        number_of_months += 12

        for month in range(1, 13):
            rainfall_inches = int(input(f'Enter rainfall in inches for year {year}, month {month}: '))
            total_rainfall += rainfall_inches

    average_rainfall = total_rainfall / number_of_months

    print(f'Number of months: {number_of_months}')
    print(f'Total rainfall: {total_rainfall} inches')
    print(f'Average rainfall: {average_rainfall:.2f} inches per month')



if __name__ == '__main__':
    main()