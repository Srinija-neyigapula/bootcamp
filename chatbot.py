a=input("enter your name?")
print("hi {} ,how are you?".format(a))
b=input()
if "not" in b:
    print("oh! sorry to know that {} .can i say a joke to make up your mood?".format(b))
    d=input()
    if "yes" in d:
        print("One joke, coming up! What is a sea monster’s favorite snack? Ships and dip.")
        e=input()
        if ("lol" or"haha" or "funny" )in e:
            print("i know,i'm pretty funny!!.Now can i help with anything else?")

    else:
        print("can i help you with something?")


elif ("good" or "fine") in b:
    print("good to know that. can i help you with anything?")

else:
    print("can i help you with something?")


c=input()

if ("food" or "hungry") in c:

    print("okay! here are some food delivery app and some recepies that you can cook")
elif "music" in c:
    print("here are some music videos")
elif ("read" or "study") in c:
    if "story" in c:
        print("here are some story reading websites that i recommend.")
    elif "book" in c:
        print("here are some books that i recommend")
    else:
        print("here is something that you learn")
elif "buy" in c:
    print("here are some websites for your shopping")
elif ("weather" or "climate") in c:
    print("these were the climate condition that i can recommend")
elif "no" in c:
    print("okay! have a good day")
else:
    print("sorry! i didn't get you")