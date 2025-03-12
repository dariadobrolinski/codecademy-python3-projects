# In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Build point dictionary
letterToPoints = {key: value for key, value in zip(letters, points)}
letterToPoints[" "] = 0

# Score a word
def score_word(word):
    totalPoint = 0
    for letter in word:
      totalPoint += letterToPoints.get(letter.upper(), 0)
    return totalPoint
  
  # Score a game
playerToWords = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

playerToPoints = {}
for player, words in playerToWords.items():
  playerPoints = 0
  for word in words:
      playerPoints += score_word(word)
      playerToPoints[player] = playerPoints

print(playerToPoints)
