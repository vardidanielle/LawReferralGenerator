import json
import re

tikun_regex = "תיקון.*\d+"
if __name__ == '__main__':
    arr_of_laws = []
    file = open('C:\\Users\\CPuser\\Desktop\\LawReferral\\LawReferralGenerator\\uriMap.json', 'r', encoding='utf-8', errors='ignore')
    f = file.read()
    json_file = json.loads(f)
    for element in json_file:
        official_name = str(element["OfficialName"].split(',')[0])
        official_name = official_name.replace("(", "\\(")
        official_name = official_name.replace(")", "\\)")
        arr_of_laws.append(official_name)
    file.close()
    file = open('arr_of_laws.json', 'w')
    json.dump(arr_of_laws, file)
    file.close()
