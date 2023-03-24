import re, sys
from collections import Counter

def tg_in_file(xmlFile):
    with open(xmlFile) as fobj:
        xml = fobj.read()
    pattern = r"<\w{1,}" 
    how_many_tags = Counter(re.findall(pattern, xml))
    fin = {}
    for i in how_many_tags:
        key = i
        fin[key] = how_many_tags[i]
    return fin
    
def tag_counter(inpt, text):
    op_tag, cl_tag = '<'+inpt, '/'+inpt
    idxs_op = [index for index in range(len(text)) if text.startswith(op_tag, index)]
    idxs_cl = [index for index in range(len(text)) if text.startswith(cl_tag, index)]
    pairs = []
    while idxs_op and idxs_cl:
        min_diff = sys.maxsize
        pair = None
        for x in idxs_op:
            for y in idxs_cl:
                diff = y - x
                if diff > 0 and diff < min_diff:
                    min_diff = diff
                    pair = (x, y)
        if pair:
            pairs.append(pair)
        idxs_op.remove(pair[0])
        idxs_cl.remove(pair[1])
    ans = []
    for pair in pairs:
        ans.append(pair)
    return op_tag, cl_tag, sorted(ans)

def replace_tag(text, new_tag, op_tag, flag):
    inpt = op_tag[1:]
    a,b,pos=tag_counter(inpt,text)
    while pos != []:
        if flag == 1:
            ntext = text[:pos[0][0]+1] + new_tag + text[pos[0][0]+len(op_tag):pos[0][1]] + '/' + new_tag + text[pos[0][1]+len(op_tag):]
            text = ntext
            a,b,pos=tag_counter(inpt,text)
            return text
        elif flag == 0:
            del pos[0]
            return text