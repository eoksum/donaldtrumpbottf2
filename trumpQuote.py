from pynput.keyboard import Key, Controller
import keyboard as KeyPress
import time
import requests
import json
import random
import sys

kb = Controller()

tauntEveryTime = False
timespan = 10 # Default is 10 seconds.

print(10 * "=", "[Donald Trump Bot for TF2]", 10 * "=")

if "--taunt" in sys.argv:
    print("Taunting enabled")
    tauntEveryTime = True

for ind, argm in enumerate(sys.argv):
    if argm == "--time":
        timespan = int(sys.argv[ind + 1])
        print("Timespan set, not using defaults... Timespan is: ", timespan)

def getTrumpQuote():
	
	qts = ["Grab 'em by the p***y!","I WON THE ELECTION!","If you're going to keep cough like that, leave my room!","I had a meeting at Pentagon with lots of generals. It was like a movie, better looking than Tom Cruise and stronger.","I've just received a beautiful personal letter from Kim-Jong Un. It was a warm and beautiful letter.","I'm gonna be signing a national emergency. It's a great thing to do.","WALLS WORK 100%!!","Don't use the word smart with me Joe.","China has total respect to Donald Trump, and Donald Trump's very very large brain.","I'm a very stable genius.","This is one of the wettest Hurricane we have seen from the terms of water.","That's such a racist question!","You know what I am, I'm the biggest jackass on the planet"]
	
	if random.randint(1,2) < 2:
		out = random.choice(qts)
		print("Just got a random quote (from my local list. I have a beautiful local list, its one of the best!) => " + out)
		return out
	try:
		h = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random", timeout=5)
		out = h.text
		out = json.loads(out)
		out = out["message"]
		print("Just got a random quote => " + out)
	except:
		out = "I WON THE ELECT... (This claim about election fraud is disputed ~ Twitter, 2020)"
	return out

print("Im starting in 10 seconds...")
time.sleep(10)
print("Here I go...")

KeyPress.press_and_release("y")
oldmsg = ""
msg = ""
while KeyPress.is_pressed('ü') == False:
	
	while oldmsg == msg:
		print("I won't show the same message again!")
		msg = getTrumpQuote()
	if len(msg) > 127:
		msg = msg[:126]
	
	oldmsg = msg
	
	i = 0
	while i < 4:
		KeyPress.release("w")
		KeyPress.release("a")
		KeyPress.release("s")
		KeyPress.release("d")
		i += 1
	
	time.sleep(2)
	if tauntEveryTime:
		print("Taunt!")
		KeyPress.press_and_release("g")
		KeyPress.press_and_release("g")
		KeyPress.press_and_release("g")
		KeyPress.press_and_release("g")
		KeyPress.press_and_release("g")
		KeyPress.press_and_release("g")
	KeyPress.press_and_release("y")
	KeyPress.press_and_release('Ctrl + a, delete')
	time.sleep(1)
	kb.type(msg)
	kb.press(Key.enter)
	kb.release(Key.enter)
	
	time.sleep(timespan)