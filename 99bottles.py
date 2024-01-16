def main():
    
    bottles = 99
    drinking_rate = 1

    def take_it_down(bottles, drinking_rate):
        
        if bottles>1: 
        
            print(f"{bottles} bottles of beer on the wall! {bottles} bottles of beer! You take one down, pass it around!")
            bottles = bottles-drinking_rate
            print(f"{bottles} bottles of beer on the wall!")

        else: 
            print(f"{bottles} bottle of beer on the wall!")
            print(f"{bottles} bottle of beer on the wall! {bottles} bottle of beer! You take it down, pass it around!")
            print("No more bottles of beer on the wall!")

    while bottles > 0:
        
        taking_one_down = input("Take one down? (y/n): ")
        if taking_one_down == 'y':
            take_it_down(bottles, drinking_rate)
            bottles = bottles-drinking_rate
        elif taking_one_down == 'n':
            print("Fair nuff.")
            break
main()
