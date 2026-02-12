'''Movie Tix Program
By Grace LeVoir
2 - 12 - 26'''

# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    # WRITE YOUR CODE HERE
    ######################

    total = 0
    another_movie = True

    while another_movie == True:

        movie = input("Enter the movie name : ")
        tix = int(input(f"Enter the amount of tickets for {movie}: "))

        total += tix

        another = input("Do you want to add another movie ? [y/n] ")
        if another == "y":
            another_movie = True
        if another == "n":
            another_movie = False

    if another_movie == False:
        print()
        print(f"Your total amount of tickets is {total}")

if __name__ == '__main__':
    main()