# A simple sentiment checker
text = input("How are you today?").lower()

if "happy" in text or "good" in text:
    print("Yay!")

elif "sad" in text or "bad" in text:
    print("Aw..")

else:
    print("I don't quite understand.")
