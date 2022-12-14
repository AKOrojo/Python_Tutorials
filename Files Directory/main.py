# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f = open("Files Directory/Input/Names/invited_names.txt", "r")
y = f.readlines()


l = open("Files Directory/Input/Letters/starting_letter.txt")
letter_cont = l.read()
for name in y:
    s = name.strip()
    x = letter_cont.replace("[name]", s)
    with open(f"Files Directory/Output/ReadyToSend/letter_for_{s}.txt", "w") as cl:
        cl.write(x)
