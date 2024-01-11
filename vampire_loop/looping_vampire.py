def main():
    with open("dracula.txt", "r") as drac:
        with open("vampytimes.txt", "w") as vampy:
            
            vamp_count = 0

            for line in drac:
                if "vampire" in line.lower():
                    print(line)
                    vamp_count += 1
                    print(vamp_count)
                    vampy.write(line)
                    
    drac.close()
main()
