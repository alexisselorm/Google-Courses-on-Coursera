
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

# Escape characters with \
print(re.search(r"\.com", "mydomain.com"))

#  \w matches any alphanumeric character including letters, numbers, and underscores
print(re.search(r"\w*","This is an example"))
print(re.search(r"\w*", "This_is_Another_example"))
# There's also \d for matching digits, \s for matching whitespace characters like space, tab or new line, \b for word boundaries and a few others


# # Question
# Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.
def check_character_groups(text):
  result = re.search(r"\w \w", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


# To match something but begins and ends with(more strictly), use the circumflex and $ sogns to make it more strict.
print(re.search(r"^A.*a$","Argentina"))
print(re.search(r"^A.*a$","Azerbaijan"))

# To construct a string that is a valid variable name in Python
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern,"_this_is_a_valid_variable"))
print(re.search(pattern,"is this valid or naa"))
print(re.search(pattern,"2what_about_This"))


# Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 
def check_sentence(text):
      result = re.search(r"^[A-Z].*[a-zA-Z ][.?!]$", text)
      return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

# The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.
def check_web_address(text):
      pattern = r"^[\w]*[\.\-\+][^/@]*$"
      result = re.search(pattern, text)
      return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

# Question 2
# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?
def check_time(text):
      pattern = r'(1[012]|[1-9]):[0-5][0-9][ ]{0,1}?(am|pm|AM|PM)'
      result = re.search(pattern, text)
      return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function: 
def contains_acronym(text):
      pattern = r"\(\w.*\w\)" 
      result = re.search(pattern, text)
      return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


# Question 6
# Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
def check_zip_code (text):
      result = re.search(r' \d{5}(?:-\d{4})?', text)
      return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False 