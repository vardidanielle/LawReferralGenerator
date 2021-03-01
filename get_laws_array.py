import json
import re

tikun_regex = "תיקון.*\d+"
if __name__ == '__main__':
    arr_of_laws = {}
    file = open('C:\\Users\\CPuser\\Desktop\\LawReferral\\LawReferralGenerator\\uriMap.json', 'r', encoding='utf-8', errors='ignore')
    f = file.read()
    file.close()
    json_file = json.loads(f)
    for element in json_file:
        official_name = element["OfficialName"].split(',')[0]
        official_name = official_name.replace("(", "\\(")
        official_name = official_name.replace(")", "\\)")
        official_name = official_name.replace("-", "(-| )")
        words_arr = official_name.split(' ')
        first_two_words = words_arr[0] + ' ' + words_arr[1]
        law_dict = {official_name: element["KnessetUrl"]}
        if first_two_words not in arr_of_laws:
            arr_of_laws[first_two_words] = law_dict
        else:
            arr_of_laws[first_two_words].update(law_dict)

    # file = open('C:\\Users\\CPuser\\Desktop\\LawReferral\\LawReferralGenerator\\lawsFile.txt', 'r', encoding='utf-8',
    #             errors='ignore')
    # line = file.readline()
    # while line:
    #     official_name = line.split(',')[0]
    #     official_name = official_name.replace("(", "\\(")
    #     official_name = official_name.replace(")", "\\)")
    #     official_name = official_name.replace("-", "(-| )")
    #     arr_of_laws[official_name] = ""
    #     line = file.readline()
    file = open('arr_of_laws.json', 'w')
    json.dump(arr_of_laws, file)
    file.close()
