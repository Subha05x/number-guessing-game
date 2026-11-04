import random 
n = random.randint(1, 10)
attempt = 3
while attempt > 0 :
    p = int(input("Guess The Number between (1-10): "))
    attempt -= 1
    print("Chances :", attempt)

    if n == p:
        print("YOU WON🎊")
        break
    elif n < p:
        print("GO Lower:⬇️")
    elif n > p:
        print("GO Higher:⬆️")

    if attempt == 0 and p != n :
        print("YOU LOSS 😂\n The number was",n)
        break
