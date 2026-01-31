class flashcard:
    def __init__(self, word, meaning):
       self.word = word
       self.meaning = meaning
    def __str__(self):
      return self.word + " - " + self.meaning
    
flash=[]
while True:
   w= input("Enter a word: ")
   m= input("Enter a meaning: ")
   flash.append(flashcard(w,m))
   option=int(input("Enter 0 to add new flashcard and 1 to exit: "))
   if option==1:
      break
   

print("\nAll flashcards:")
for i in flash:
   print("->",i)
