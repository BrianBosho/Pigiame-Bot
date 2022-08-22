import random
import os

title_list = []
description_list = []
images_list = []

images_path = "C:\\Users\\Blade\\Desktop\\Web Automation\\pillow_editor\\saved_wmk\\"
my_pics = os.listdir(images_path)

title_file = open("titles adjectives.txt", "r")
description_file = open("features.txt", "r")
for line in title_file:
    title_list.append(line.strip())

for line in description_file:
    description_list.append(line.strip())

for pic in my_pics:
    full_path = images_path + pic
    images_list.append(full_path)

random.shuffle(description_list)
random.shuffle(images_list)

old_titles = []
description = random.choice(description_list) + "\n" + random.choice(description_list) + "\n" + random.choice(
    description_list)

for i in range(20):
    title = random.choice(title_list) + " " + random.choice(title_list) + " " + random.choice(title_list) + " curtains"
    repeat = title in old_titles
    while repeat:
        title = random.choice(title_list) + " " + random.choice(title_list) + " " + random.choice(
            title_list) + " curtains"
        repeat = title in old_titles

    print(title)
    old_titles.append(title)



