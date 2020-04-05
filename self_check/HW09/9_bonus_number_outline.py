#format_list_0 = []
#format_list_1 = []
#format_list_2 = []

def default(level = 0):
    return []

def number_outline(L, plugin = default, prefix = ()):
    #global format_list_0 
    format_list_0 = plugin(0)
    #global format_list_1 
    format_list_1 = plugin(1)
    #global format_list_2 
    format_list_2 = plugin(2)
    if type(L) in {list, tuple}:
        i = 0
        for v in L:
            if type(v) not in {list, tuple}:
                i += 1
            number_outline(v, plugin, prefix + (i,))
    else:
        if format_list_0 == []:
            s = ' ' * 4 * (len(prefix) - 1)
            s += '.'.join(map(str, prefix))
            s += '. ' + L
            print(s)
        elif format_list_0 == ():
            s = ' ' * 4 * (len(prefix) - 1)
            if len(prefix) == 1:
                s += 'Chapter '
                s += '.'.join(map(str, prefix))
            elif len(prefix) == 2:
                s += 'Section '
                s += '.'.join(map(str, prefix))
            elif len(prefix) == 3:
                s += '.'.join(map(str, prefix))
            else:
                s += '.'.join(map(str, prefix))
            s += '. ' + L
            print(s)

        else:
            s = ' ' * 4 * (len(prefix) - 1)
            if len(prefix) == 1:
                s += format_list_0[prefix[0] - 1]
            elif len(prefix) == 2:
                s += format_list_1[prefix[1] - 1]
            elif len(prefix) == 3:
                s += format_list_2[prefix[2] - 1]
            else:
                prefix = list(prefix)
                prefix.pop(0)
                prefix.pop(0)
                prefix = tuple(prefix)
                s += '.'.join(map(str, prefix))
            s += '. ' + L
            print(s)
  

def my_outline_format_function(level = 0):
    if level == 0:
        return ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    elif level == 1:
        return [chr(i) for i in range(65, 75)]
    else:
        return [str(i) for i in range(1, 11)]

def my_thesis_format_function(level = 0):
    return ()


