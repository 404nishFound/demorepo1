import random
class slots:
 def rand(self):
   n=random.randint(1,5)
   if(n == 1):
     r = "💀 | "
   elif(n ==2):
     r = "🪙 | "
   elif(n ==3):
     r = "🍒 | "
   elif(n ==4):
     r = "💎 | "
   else:
     r = "7️⃣ | "
   return r
credits = int(input("Insert credit(s)"))
while(credits >= 0):
 choice = input("Do you want to play? (y/n): ").lower()
 if(choice == "n"):
   print("Thank you for playing")
   print("you get:", credits)
   break
 else:
  if(credits < 3):
       print("insufficient balance")
       print("you get:", credits)
       break

  else:
      print("playing")
      obj = slots()
      a = obj.rand()
      b = obj.rand()
      c = obj.rand()
      print(a,b,c)
  if( a == b and b == c and c == "7️⃣ | "):
   credits *= 5
  elif(a == b and b == c and c == "💎 | "):
   credits *= 2
  elif(a == b and b == c and c == "🪙 | "):
   credits += 10
  elif(a == b and b == c and c == "🍒 | "):
   credits += 3
  elif(a == b and b == c and c == "💀 | "):
   credits = credits - credits
  elif(a == b or b == c or c == a):

    if(a == b):
        pair = a
    elif(b == c):
        pair = b
    else:
        pair = c

    if(pair == "7️⃣ | "):
        credits += 10
    elif(pair == "💎 | "):
        credits += 5
    elif(pair == "🪙 | "):
        credits += 2
    elif(pair == "🍒 | "):
        credits += 0
    elif(pair == "💀 | "):
        credits -= 5
  else:
   credits = credits - 3
  print("remaining balance:", credits)



