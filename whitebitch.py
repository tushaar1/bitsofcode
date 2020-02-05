from PIL import Image

name = input("What is your name? ") # get your name
race = input("Hi {}, What is your race? ".format(name))  # get your race
openvm = open('voicemail.txt', 'r')   # open the voicemail file and read it
openout = open('out.txt', 'w')  # open the voicemail file as read and write

if race.lower() == 'white':
    for line in openvm:
        openout.write(line.replace('RACHEL', name.upper()))
    openout.close()
    with open('out.txt', 'r') as message:
        print(message.read())
elif race.lower() == 'black' or race.lower() == 'asian' or race.lower() == 'latino':
    print('Thank you for your service')
    im = Image.open(r'thanks.jpg')
    im.show()
else:
    print("ERROR 420: Race Not Found")
