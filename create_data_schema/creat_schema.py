import csv

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
        content_val = row[4]
        page_val = row[5]
        if split_token in dic_index_val:
            for each_dic_index_val in dic_index_val.split(split_token):
                output.append([str(id_val), str(sem_id_val), each_dic_index_val, word_val, content_val, page_val])
                id_val += 1
            sem_id_val += 1
        else:
            output.append([str(id_val), str(sem_id_val), dic_index_val, word_val, content_val, page_val])
            id_val += 1
            sem_id_val += 1

with open("output.csv", "w", encoding="utf-8") as f:
    output_str = ""
    for row in output:
        output_str += "\t".join(row) + "\n"
    f.write(output_str)

print("Done!")
