import random

def generate_yes_no():
    return "yes" if random.random() < 0.95 else "no"

# Generate a list of 10 random "yes" or "no" values
#change the 10 inside the bracets with the number of outputs you want
random_yes_no_list = [generate_yes_no() for _ in range(10)]

# Print each result
for result in random_yes_no_list:
    print(result)

#print the output to a different .txt file
with open("random_yes_no_output.txt", "w") as file:
    for result in random_yes_no_list:
        file.write(result + "\n")