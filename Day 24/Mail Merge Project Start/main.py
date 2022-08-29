PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    content = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in content:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)





