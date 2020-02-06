
print("Hi, welcome to the meat show!")
print("This is a quiz about the best rapper, Blueface")
print("Try to get many of these correct as possible: "
      "the questions consist of true facts and complete the lyrics")

print("1. Complete the lyric: Bust down, ______.")
ans1 = input("").lower()
print("2. Blueface is a famous what?")
ans2 = input("").lower()
print("3. What does Blueface do when he pulls up on your block")
ans3 = input("").lower()
print("4. Blueface, an opponent of a Hanggun bought what in?")
ans4 = input("").lower()
print("5. What is Blueface's Instagram account? ")
ans5 = input("").lower()

result = 0
num_correct = 0


if ans1 == "thotiana":
    print("Correct !")
    num_correct += 1
else:
    print("Incorrect")

if ans2 == "crip":
    print("Correct !")
    num_correct += 1
else:
    print("Incorrect")

if ans3 == "bleed it":
    print("Correct !")
    num_correct += 1
else:
    print("Incorrect")

if ans4 == "mac":
    print("Correct !")
    num_correct += 1
else:
    print("Incorrect")

if ans5 == "bluefacebleedem":
    print("Correct !")
    num_correct += 1
else:
    print("Incorrect")


if num_correct / 5 == 1:
    print("100% "
          "You are a true blueface fan !!!")
elif num_correct / 5 == 0.8:
    print("You got {} correct, almost there !!".format(num_correct))
elif num_correct / 5 == 0.6:
    print("Step it up sis !! you got {} correct".format(num_correct))
elif num_correct / 5 == 0.4:
    print("You got {} correct, fake fan".format(num_correct))
elif num_correct / 5 == 0.2:
    print("You got {} correct, you probably only have heard Thotiana, fake fan".format(num_correct))
else:
    print("FUCK OUTTA HERE BLOOD!!")

