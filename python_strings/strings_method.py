s="Hello World"

print(len(s)) # find length of string ->string index start with 0
print(s.capitalize()) #capital first latter of string
print(s.upper()) # upper every letter of string
print(s.lower()) # lower every letter
print(s.center(18,"^")) #first find length of string and it's center through
print(s.endswith("ld")) # in string any letter end with patricular letter it give true or false
print(s.startswith("H")) # in string any letter start with patricular letter it give true or false
print(s.find("e"))#find e and give its index value
print(s.isalnum()) #this method means its string value or numeric value than give true or false in python speace consider as nothing that why give false
print(s.isalpha()) #this method means its string value  than give true or false in python speace consider as nothing
print(s.swapcase()) # swap upper into lower case,lower into upper case
print(s.count("l")) #count how many time string repeat
print(s.replace("l","p")) # swap string
print(s.title()) #make as title first word make upper case and after speace word make upper case

