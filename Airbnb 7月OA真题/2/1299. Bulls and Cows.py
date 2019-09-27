class Solution:
    def getHint(self, secret, guess):
        secretStore = {str(i): 0 for i in range(0, 10)}
        guessStore = {str(i): 0 for i in range(0, 10)}
        bullsStore = {str(i): 0 for i in range(0, 10)}

        for i in range(len(secret)):
            secretStore[secret[i]] += 1
            guessStore[guess[i]] += 1

            if guess[i] == secret[i]:
                bullsStore[guess[i]] += 1

        bulls, cows = 0, 0
        for num in bullsStore:
            bulls += bullsStore[num]
            cows += min(secretStore[num], guessStore[num]) - bullsStore[num]

        return str(bulls) + 'A' + str(cows) + 'B'
