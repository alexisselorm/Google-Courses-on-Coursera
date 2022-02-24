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
# TO find something with the first letter matching a rule, use the circumflex "^"
# To find something with the last letter matching a rule, use the dollar sign $
# To ignore cases, pass in the re.IGNORECASE option
result = re.search(r"aza", "razar")
print(re.search(r"^x", "xylophone"))
print(re.search(r"p.ng","penguin"))
print(re.search(r"p.ng","Penguin", re.IGNORECASE))
print(result)


# Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
def check_aei (text):
      result = re.search(r"a.e.i.", text)
      return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True