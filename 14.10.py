


def cr(_size,_min,_max):
    _list=[]
    for i in range (_size):
        _list.append(random.randint(_min,_max))
    return _list
list1=cr(8,10,99)
for i in range(len(list1)):

    def adc(_list):
        _list = []
        a=50
        for i in range(len(_list)):
            if _list[i]==a:
                 _list.append(i)
        return _list
    print(list1)






