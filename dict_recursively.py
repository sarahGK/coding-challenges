# print all the values of a dictionary of dictionaries
def list_of_values(json_dict):
    list = []
    for k in json_dict:
        get_value(list,json_dict[k])

    return list
# recursively get all the values
def get_value(list,item):
    if isinstance(item,dict):
        for k,v in item.items():
            get_value(list,v)
    else:
        list.append(item)


if __name__ == '__main__':
    d = { "A": 1,
          "B": {
              "C":{"F":2,
                   "D":3
                 },
              "G":4
              },
           "E": None
         }
    print(d)
    l = list_of_values(d)
    print(l)
