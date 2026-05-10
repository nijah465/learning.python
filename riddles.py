secret_word1 = "towel"
secret_word2 = "teapot"
secret_word3 = "cold"
guess_count = 0
guess_limit = 3
guess_count1 = 0
guess_limit1 = 3
response1 = ""
response2 = "" 
response3 = ""
correct = "Hurrah"
wrong = "oops"

while secret_word1 != response1 and guess_count < guess_limit :
      response1 = input(" What gets wet while drying?: ").lower()
      guess_count = guess_count + 1
      if secret_word1 == response1:
        print(correct)
      elif guess_count <= 2 :
          print(wrong + " Try again ")
if guess_count == guess_limit:
   print("The correct answer is TOWEL Go to the next")

while secret_word2 != response2 and guess_count1<guess_limit1:
    response2 = input("what begins with T ends with T and has T in it: ").lower()
    guess_count1 = guess_count1 + 1
    if secret_word2 == response2:
     print(correct)
    elif guess_count1 <= 2:
       print(wrong + "😜" )
if guess_count1 == guess_limit1:
   print("The correct anwer is Teapot")
print("game end")
    