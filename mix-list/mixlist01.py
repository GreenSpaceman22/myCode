#!/usr/bin/env python3
import random

def main():
    # making a list contain 3 things
    my_list = [ "192.168.0.5", 5060, "UP" ]
    # display first item
    print("The first item of the list (IP): " + my_list[0])
    # display second item
    print("The second item of the list (port): " + str(my_list[1]))
    # display second item 
    print("The third item of the list (state): " + my_list[2])
    wordbank= ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    wordbank.append(4)
    num = int(input(f"pick a random number between 1 and {len(tlgstudents)-1}: "))-1
    student_name = tlgstudents[num]
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent")
main()
