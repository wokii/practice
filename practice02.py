

#int TransChineseToInt(string input)

dic = {
    "零" : 0,
    "一" : 1,
    "二" : 2,
    "两" : 2,
    "三" : 3,
    "四" : 4,
    "五" : 5,
    "六" : 6,
    "七" : 7,
    "八" : 8,
    "九" : 9,
    "十" : 10

}

def solution(input):
    if len(input) != 1 and input[0] == '零':
        raise Exception("invalid input")
    input = input.replace('零', '')


    split1 = input.split('亿')
    # split1 is a list
    if len(split1) > 2:
        raise Exception("invalid input")
    elif len(split1) == 2:
        pre_yi, past_yi = split1
    else:
        pre_yi, past_yi = '', split1[0]

    split2 = past_yi.split('万')

    if len(split2) > 2:
        raise Exception("invalid input")
    elif len(split2) == 2:
        pre_wan, past_wan = split2
    else:
        pre_wan, past_wan = '', split2[0]
    # pre_yi, pre_wan, past_wan
    res = 0
    res += belowOneWan(past_wan)
    res += belowOneWan(pre_wan) * 10000
    res += belowOneWan(pre_yi) * 100000000

    return res


def checkValid(digitName, string):
    if digitName in string:
        pre, past = string.split(digitName)
        
        #print(pre, past)
        if len(pre) != 1:
            raise Exception("invalid input")
        elif pre not in dic:
            raise Exception("invalid input")
        elif dic[pre] == 10:
            raise Exception("invalid input")


def belowOneWan(string):
    if len(string) == 2 and string[0] == '十':
        if string[1] not in dic:
            raise Exception("invalid input")
        res = dic[string[1]] + 10
        return res
    if len(string) == 0:
        return 0
    if len(string) == 1:
        return dic[string]
    
    s = string
    for digitName in "千百十":
        
        
        try:
            #print("s", s)
            checkValid(digitName, s)
            split = s.split(digitName)
            if len(split) == 1:
                s = split[0]
            else:
                s = split[1]
        except:
            raise Exception("invalid input, error before: ", digitName)

    res = 0


    for i,c in enumerate(string):
        if c == '千':
            thousands = string[i-1]
            res += 1000*dic[thousands]
        elif c == '百':
            hundreds = string[i-1]
            res += 100*dic[hundreds]
        elif c == '十':
            tens = string[i-1]
            res += 10* dic[tens]
    lastdigit = string[-1]
    if lastdigit in dic and dic[lastdigit] < 10:
        res += dic[lastdigit]
    return res
