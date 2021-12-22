import csv
import re

output = []
id_val = sem_id_val = 1
split_token = ";"
dic_dks = "DKS"
dic_svk = "SVK"
dic_sgs = "SGS"
dic_krnd = "KRND"
dic_krnd_texts = "KRND_TEXT"
dic_kbm_mbhp = "KBM_MBhP"
dic_kbm_texts = "KBM_MBhP_TEXT"
dic_xjm = "XJM"
dic_xjm_texts = "XJM_TEXT"
dic_notes = "Notes"

def clean_content_val(data):
    data = re.sub(r"<", "&lt;", data)
    data = re.sub(r">", "&gt;", data)
    data = re.sub(r"【", "<i>", data)
    data = re.sub(r"】", "</i>", data)
    data = re.sub(r"《", "<sup>", data)
    data = re.sub(r"》", "</sup>", data)
    data = re.sub(r"{", "<sub>", data)
    data = re.sub(r"}", "</sub>", data)
    data = re.sub(r"；", ";", data)
    data = re.sub(chr(11), "", data)
    data = re.sub(r"\|\|\|", "</br>", data)
    data = re.sub(r"\|\|\|", "</br>", data)
    # data = re.sub(r"^%([\d\.]+ ?\;?)", "<font color='red'> \g<1></font>", data)
    data = re.sub(r"%([\d\.;]+ ?)", "</br><font color='red'> \g<1></font>", data)
    while "</br></br>" in data:
        data = data.replace("</br></br>", "</br>")    
    return data

def combine_dics(dic_1, dic_2, dic_3, dic_d, dic_dt, dic_km, dic_kmt, dic_dxjm, dic_dxjmt, dic_n):
    output = ""
    if dic_1!="":
        output = f"<b>[{dic_dks}]</b> {dic_1}</br>"
    if dic_2!="":
        output += f"<b>[{dic_svk}]</b> {dic_2}</br>"
    if dic_3!="":
        output += f"<b>[{dic_sgs}]</b> {dic_3}</br>"
    if dic_d!="":
        output += f"<b>[{dic_krnd}]</b> {dic_d}</br>"
    if dic_dt!="":
        output += f"<b>[{dic_krnd_texts}]</b></br> {dic_dt}</br>"
    if dic_km!="":
        output += f"<b>[{dic_kbm_mbhp}]</b></br> {dic_km}</br>"
    if dic_kmt!="":
        output += f"<b>[{dic_kbm_texts}]</b></br> {dic_kmt}</br>"
    if dic_dxjm!="":
        output += f"<b>[{dic_xjm}]</b></br> {dic_dxjm}</br>"
    if dic_dxjmt!="":
        output += f"<b>[{dic_xjm_texts}]</b></br> {dic_dxjmt}</br>"
    if dic_n!="":
        output += f"<b>[{dic_notes}]</b> {dic_n}<br/>"
    while "</br> </br>" in output:
        output = output.replace("</br> </br>", "</br>")
    return output


with open("input.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.reader(f, delimiter=",", quotechar='"')
    # skip the title row
    next(csv_reader)
    for row in csv_reader:
        dic_index_val = row[2]
        word_val = row[3]
        content_val = combine_dics(clean_content_val(row[4]), clean_content_val(row[6]), clean_content_val(row[7]), clean_content_val(row[8]), clean_content_val(row[10]), clean_content_val(row[11]), clean_content_val(row[13]), clean_content_val(row[14]), clean_content_val(row[16]), clean_content_val(row[17]))
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
