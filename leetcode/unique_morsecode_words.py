morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
morse_dict = {key : value for key, value in zip([chr(x) for x in range(97, 123)], morse)}

def uniqueMorseRepresentations(words) -> int:
    morse_set = set()
    for word in words:
        morse_word = ''
        for x in word:
            morse_word += morse_dict[x]
        morse_set.add(morse_word)
    
    return len(morse_set)

print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))