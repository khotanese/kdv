import csv
import re

output = []
id_val = sem_id_val = 1
split_token = ";"

with open("input.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.reader(f, delimiter=",", quotechar='"')
    # skip the title row
    next(csv_reader)
    for row in csv_reader:
        dic_index_val = row[2]
        word_val = row[3]
        content_val = re.sub(r"【", "<i>", row[4])
        content_val = re.sub(r"】", "</i>", content_val)
        page_val = row[5]
        if split_token in dic_index_val:
            dic_index_list = dic_index_val.split(split_token)
            word_list = word_val.split(split_token)
            for index_val in range(len(word_list)):
                output.append([str(id_val), str(sem_id_val), dic_index_list[index_val], word_list[index_val], content_val, page_val])
                id_val += 1
            sem_id_val += 1
        else:
            output.append([str(id_val), str(sem_id_val), dic_index_val, word_val, content_val, page_val])
            id_val += 1
            sem_id_val += 1

with open("output.csv", "w", encoding="utf-8", newline='') as f:
    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in output:
        csv_writer.writerow(row)

print("Done!")
