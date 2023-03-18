import json

def ters_list(lst):
    cevrilmis_list = []
    for item in reversed(lst):
        if isinstance(item, list):
            cevrilmis_list.append(ters_list(item))
        else:
            cevrilmis_list.append(item)
    return cevrilmis_list
input_str = input("Liste Giriniz: ")
lst = json.loads(input_str)
cevrilmis_list = ters_list(lst)
print(cevrilmis_list)