# L33t H4x0r (Challenge from Real Python's Python Basics book)

# The code will turn the input text into leetspeak

text_input = input("Enter some text: ")

# Define a new text variable to store the changes

leetspeak = text_input # Empty string

# Introduce the replacement instances that will change the text

leetspeak = leetspeak.replace("a", "4")
leetspeak = leetspeak.replace("b", "8")
leetspeak = leetspeak.replace("e", "3")
leetspeak = leetspeak.replace("l", "1")
leetspeak = leetspeak.replace("o", "0")
leetspeak = leetspeak.replace("s", "5")
leetspeak = leetspeak.replace("t", "7")

print(leetspeak)