with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    starting_text = letter.read()

for name in names:
    stripped_name = name.strip()
    new_text = starting_text.replace("[name]", stripped_name)
    new_filename = (f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt")
    with open(new_filename, "w") as file:
        file.write(new_text)



