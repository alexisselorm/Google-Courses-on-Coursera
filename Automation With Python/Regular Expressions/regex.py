import re


log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])
 
# use regex
regex = r"\[(\d+)\]"
result = re.search(regex,log)
print(result[1])
# Basic Matching with Grep
# Grep works by matching any lines that match a rule
# Grep is case sensitive so you might want to escape that by adding "-i" option
# Example: grep -i python /usr/share/dict/words

# Use the dot . character to match any letter in a word
print(re.search(r"p.ng","penguin"))
# TO find something with the first letter matching a rule, use the circumflex "^"
print(re.search(r"^x", "xylophone"))
# To find something with the last letter matching a rule, use the dollar sign $
# To ignore cases, pass in the re.IGNORECASE option
print(re.search(r"p.ng","Penguin", re.IGNORECASE))
# To use Character classes(eg: to allow for both upper and lowercase letters to match a string use [])
print(re.search(r"[Pp]ython","Python"))
print(re.search(r"cloud[a-zA-Z0-9]","CLOud9", re.IGNORECASE))
# Inside the square brackets, we can also define a range of characters using a dash. For example, we could use lowercase a to lowercase z to state any lowercase letter. 
print(re.search(r"[a-z]way","The end of the ampaswaygees"))
print(re.search(r"[a-z]way","What a way to go"))
# Sometimes we may want to match any characters that aren't in a group. To do that, we use a circumflex inside the square brackets. 
print(re.search(r"[^a-zA-Z]","This is a sentence with spaces")) #The pattern matches the first space in the sentence
print(re.search(r"[^a-zA-Z ]","This is a sentence with spaces.")) #Because of the space included in the pattern matching rule ,regex matches the period

# If we want to match either one expression or another, we can use the pipe symbol to do that. This lets us list alternative options that can get matched. For example, we could have an expression that matches either the word cat or the word dog, like this.
print(re.search(r"cat|dog", "I like cats"))
print(re.search(r"cat|dog", "I like dogs"))
print(re.search(r"cat|dog", "I like cats and dogs")) #This just finds the first matching pattern

# If we want to get all possible matches, we can do that using the findall function
print(re.findall(r"cat|dog", "I like cats and dogs"))

# Repitition qualifiers
# Use .* to repetitively match any letters that match a pattern
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))#Greedy
print(re.search(r"Py[a-z]*n", "Python Programming")) #Use character class to make the pattern match only letters. (This stops at the space)

result = re.search(r"aza", "razar")

print(result)


# Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
def check_aei (text):
      result = re.search(r"a.e.i.", text)
      return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

# Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.

def check_punctuation (text):
      result = re.search(r"[,.:;?!]", text)
      return result != None


print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

# The + symbol checks for one or more occurrence of the pattern
print(re.search(r"o+l+", "woolly"))

# The ? symbol checks for zero or one occurrence of the pattern.
print(re.search(r"p?each", "To each their own"))# The p wasn't in the text so it matched with each
# If p was present we would get peach like so
print(re.search(r"p?each", "I like peaches"))

# The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work. 
def repeating_letter_a(text):
      result = re.search(r"[aA].*[aA]", text)
      return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True