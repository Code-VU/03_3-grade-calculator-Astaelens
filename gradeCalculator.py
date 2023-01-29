def calculateGrade():
    # Implement your solution in between the two comment blocks
    # print("Calculating Grade")
    # This first line is provided for you

    try:
        hrs = float(input("Enter score: "))
        if hrs>1:
            print("Bad score") 
        elif hrs>=.9:
            print("A")
        elif hrs >=.8:
            print("B")
        elif hrs>=.7:
            print("C")
        elif hrs>=.6:
            print("D")
        elif hrs>=0 and hrs<.6:
            print("F")
        else:
            print("Bad score")
    except:
        print("Bad score")
    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
