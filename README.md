# sound-supporter
sound supporter for games.
from functions import speak
from functions import get_audio
#question 1
text = get_audio()
if "hello" in text or "hi" in text or "good morning" in text or "good afternoon" in text or "good night" in text or "good evening" in text or "it is a pleasure to meet you" in text or "it is nice to meet you" in text or "what is app" in text or "pleased to meet you" in text or "it is a pleaser" in text:
	speak("hello!it is a pleaser to meet you.")
	text = get_audio()
	if "but you are not near me" in text or "we just speaking" in text or "i can not see you and you cant see me" in text:
		speak("hahaha!it is a idiom")
		text = get_audio()
		if "Do you know other terms?" in text or "can you say me other idioms" in text:
			speak("i can say 5 idioms. say a number from 1 to 5 and listen to my idiom. if you want listen other idiom or your last idiom say a number again.if you want finish speaking about idioms,say finish.")
			while text!="finish":
				text = get_audio()
				if "one" in text or "1" in text:
					speak("The lights are on but nobody’s home – used to describe a stupid person.Example: She really has no clue- the lights are on but nobody’s home!")
				text = get_audio()
				if "two" in text or "2" in text:
					speak("When pigs fly – about something that will never happen.Example: Yea, right! You will get Taylor Swift to ask you on a date when pigs fly!")
				text = get_audio()
				if "three" in text or "3" in text:
					speak("To have Van Gogh’s ear for music – to be tone deaf |Van Gogh only had one ear!|Example: Xavi really shouldn’t play the piano- he has Van Gogh’s ear for music.")
				text = get_audio()
				if "four" in text or "4" in text:
					speak("To pig out – to eat a lot very quickly.Example: After the marathon, the runners pigged out at a dinner buffet.")
				text = get_audio()
				if "five" in text or "5" in text:
					speak("Everything but the kitchen sink – almost everything has been included.Example: Maria was trying so hard to get the question right, she was throwing out everything but the kitchen sink!")
if "how are you" in text or "how is it going" in text or "":
	speak("fine thanks what about you?")
	text = get_audio()
	if "not bad" in text or "well" in text or "not" not in text and "good" in text or "perfect" in text:
		speak("thats perfect!")
	else:
		speak("do you want to make you happy?")
		text = get_audio()
		while text!="finish":
			if "yes" in text or "yea" in text or "yeap" in text or "yeah" in text:
				speak("i dont have any jokes to tell you. ha. ha ha. ha.i was kiding! If you want a joke, say a number from 1 to 13. If you want a joke again, say another number. If you no longer want jokes, say finish")
			if "hello" in text:
	speak("hello best human in the world!how are you?")
	if "fine. and you?" in text:
		speak("not bad. thanks!")
if "hello how are you" in text:
	speak("hello best human in the world!fine thanks!and you?")

if "how are you" in text:
	speak("fine thanks what about you?")
	text = get_audio()
	if "not bad" in text or "well" in text or "not" not in text and "good" in text or "perfect" in text:
		speak("thats perfect!")
	else:
		speak("do you want to make you happy?")
		text = get_audio()
		while text!="finish":
			text = get_audio()
			if "yes" in text or "yea" in text or "yeap" in text or "yeah" in text:
				speak("i dont have any jokes to tell you. ha. ha ha. ha. i i have many jokes. say a numbeer from  to 63 and listen my joke!")
			text = get_audio()
			if "one" in text or "1" in text:
				speak("Two hunters are out in the woods when one of them collapses. He’s not breathing and his eyes are glazed. The other guy whips out his cell phone and calls 911.“I think my friend is dead!” he yells. “What can I do?”The operator says, “Calm down. First, let’s make sure he’s dead.”There’s a silence, then a shot. Back on the phone, the guy says, “OK, now what?”ha ha ha ha")
			text = get_audio()
			if "two" in text or "2" in text:
				speak("A turtle is crossing the road when he’s mugged by two snails. When the police show up, they ask him what happened. The shaken turtle replies, “I don’t know. It all happened so fast.”ha ha ha ha ")		
			text = get_audio()
			if "three" in text or "3" in text:
				speak("A priest, a minister, and a rabbi want to see who’s best at his job. So they each go into the woods, find a bear, and attempt to convert it. Later they get together. The priest begins: “When I found the bear, I read to him from the Catechism and sprinkled him with holy water. Next week is his First Communion.”“I found a bear by the stream,” says the minister, “and preached God’s holy word. The bear was so mesmerized that he let me baptize him.”They both look down at the rabbi, who is lying on a gurney in a body cast. “Looking back,” he says, “maybe I shouldn’t have started with the circumcision.”ha ha ha ha")
			text = get_audio()
			if "four" in text or "4" in text:
				speak("“Why do they lock gas station bathrooms? Are they afraid someone will clean them?”ha ha ha ha")
			text = get_audio()
			if "five" in text or "5" in text:
				speak("A guy spots a sign outside a house that reads “Talking Dog for Sale.” Intrigued, he walks in.“So what have you done with your life?” he asks the dog.“I’ve led a very full life,” says the dog. “I lived in the Alps rescuing avalanche victims. Then I served my country in Iraq. And now I spend my days reading to the residents of a retirement home.”The guy is flabbergasted. He asks the dog’s owner, “Why on earth would you want to get rid of an incredible dog like that?”The owner says, “Because he’s a liar! He never did any of that!”ha ha ha ha")
			text = get_audio()
			if "six" in text or "6" in text:
				speak("In surgery for a heart attack, a middle-aged woman has a vision of God by her bedside. “Will I die?” she asks.God says, “No. You have 30 more years to live.”With 30 years to look forward to, she decides to make the best of it. So since she’s in the hospital, she gets breast implants, liposuction, a tummy tuck, hair transplants, and collagen injections in her lips. She looks great! The day she’s discharged, she exits the hospital with a swagger, crosses the street, and is immediately hit by an ambulance and killed. Up in heaven, she sees God. “You said I had 30 more years to live,” she complains.“That’s true,” says God.“So what happened?” she asks.God shrugs. “I didn’t recognize you.”ha ha ha ha")
			text = get_audio()
			if "seven" in text or "7" in text:
				speak("A car hit an elderly man. The paramedic says, “Are you comfortable?”The man says, “I make a good living.”")
			text = get_audio()
			if "eight" in text or "8" in text:
				speak("A poodle and a collie are walking together when the poodle suddenly unloads on his friend. “My life is a mess,” he says. “My owner is mean, my girlfriend ran away with a schnauzer, and I’m as jittery as a cat.”“Why don’t you go see a psychiatrist?” suggests the collie.“I can’t,” says the poodle. “I’m not allowed on the couch.”ha ha ha ha")
			text = get_audio()
			if "nine" in text or "9" in text:
				speak("A man, shocked by how his buddy is dressed, asks him, “How long have you been wearing that bra?” The friend replies, “Ever since my wife found it in the glove compartment.”ha ha ha ha")
			text = get_audio()
			if "ten" in text or "10" in text:
				speak("“The easiest time to add insult to injury is when you’re signing somebody’s cast.”ha ha ha ha")
			text = get_audio()
			if "eleven" in text or "11" in text:
				speak("A ventriloquist is performing with his dummy on his lap. He’s telling a dumb-blonde joke when a young platinum-haired beauty jumps to her feet. “What gives you the right to stereotype blondes that way?” she demands. “What does hair color have to do with my worth as a human being?”Flustered, the ventriloquist begins to stammer out an apology.“You keep out of this!” she yells. “I’m talking to that little jerk on your knee!”ha ha ha ha")
			text = get_audio()
			if "twelve" in text or "12" in text:
				speak("Once I saw this guy on a bridge about to jump. I said, “Don’t do it!”He said, “Nobody loves me.” I said, “God loves you. Do you believe in God?”He said, “Yes.”I said, “Are you a Christian or a Jew?”He said, “A Christian.”I said, “Me, too! Protestant or Catholic?”He said, “Protestant.”I said, “Me, too! What franchise?”He said, “Baptist.”I said, “Me, too! Northern Baptist or Southern Baptist?”He said, “Northern Baptist.”I said, “Me, too! Northern Conservative Baptist or Northern Liberal Baptist?”He said, “Northern Conservative Baptist.”I said, “Me, too! Northern Conservative Baptist Great Lakes Region, or Northern Conservative Baptist Eastern Region?”He said, “Northern Conservative Baptist Great Lakes Region.”I said, “Me, too! Northern Conservative†Baptist Great Lakes Region Council of 1879, or Northern Conservative Baptist Great Lakes Region Council of 1912?”He said, “Northern Conservative Baptist Great Lakes Region Council of 1912.”I said, “Die, heretic!” And I pushed him over.ha ha ha ha")
			text = get_audio()
			if "thirteen" in text or "13" in text:
				speak("The doctor says, “Larry, everything looks great. How are you doing mentally and emotionally? Are you at peace with God?”Larry replies, “God and I are tight. He knows I have poor eyesight, so He’s fixed it so when I get up in the middle of the night to go to the bathroom, poof! The light goes on. When I’m done, poof! The light goes off.”“Wow, that’s incredible,” the doctor says.A little later in the day, the doctor calls Larry’s wife.“Bonnie,” he says, “Larry is doing fine! But I had to call you because I’m in awe of his relationship with God. Is it true that he gets up during the night, and poof, the light goes on in the bathroom, and when he’s done, poof, the light goes off?”“Oh, no,” exclaims Bonnie. “He’s peeing in the refrigerator again!”")

elif text == "what's my name" or text == "do you know my name" or text == "what is my name" or "what's my name" in text:
	speak("dont know do you want to tell that?")
	text = get_audio()
	if "yes" in text or "yea" in text or "yeap" in text or "yeah" in text:
		speak("so tell that")
		text = get_audio()
		if "my name is" in text or "its" in text:
			speak("i cant uderstand that please just tell your name")
		text = get_audio()
		speak("hello")
		speak(text)
	elif "no" in text:
		speak("hahaha")
	else: 
		speak("please ask 1 question and answer my question")

