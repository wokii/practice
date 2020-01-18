def solution(input):
    l = 'a b c ch d dd e f ff g ng h i j l ll m n o p ph r rh s t th u w y'.split()
    
    s = set(l)
    
    input = input.lower()
    
    i = 0
    st = []
    
    while i < len(input):
        if i+1 < len(input) and input[i:i+2] in s:
            st.append(input[i:i+2])
            i += 2
        else:
            st.append(input[i])
            i += 1

    dic = {k:v for v, k in enumerate(l)}
    st.sort(key=lambda x: dic[x])
    
    return ''.join(st)
