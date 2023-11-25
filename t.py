import os
import json

output_file_s = 's.txt'
output_file_t = 't.txt'

folder_path = ''

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".json"):
            input_file = os.path.join(root, file)
            with open(input_file, 'r', encoding='utf-8-sig') as file:
                data = json.load(file)

            with open(output_file_s, 'a', encoding='utf-8') as file_s:
                for item in data['Words']:
                    english_word = item['EnglishWord']
                    file_s.write(english_word + '\n')

                    meanings = item['Meanings']
                    if meanings:
                        persian_meaning = meanings[0]
                        with open(output_file_t, 'a', encoding='utf-8') as file_t:
                            file_t.write(persian_meaning + '\n')
                    else:
                        print(f"file:{file} bug")
