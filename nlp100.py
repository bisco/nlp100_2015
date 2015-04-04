# vim: fileencoding=utf-8

# http://www.cl.ecei.tohoku.ac.jp/nlp100/ より

##################
# Chapter 1.     #
##################
def f_00():
    print "stressed"[::-1]


def f_01():
    s = u"パタトクカシーー"
    print "".join([s[i] for i in range(len(s)) if i % 2 == 0])


def f_02():
    p = u"パトカー"
    t = u"タクシー"
    print "".join([p[i]+t[i] for i in range(len(p))])


def f_03():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print [len(i) for i in s.replace(".","").replace(",","").strip().split(" ")]


def f_04():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    onechar_set = set([1,5,6,7,8,9,15,16,19])
    s_list = s.replace(".","").replace(",","").strip().split(" ")
    dic = {}
    for i in range(len(s_list)):
        if (i+1) in onechar_set:
            dic[s_list[i][0]] = i
        else:
            dic[s_list[i][0:2]] = i

    for k, v in sorted(dic.items(), key=lambda x:x[1]):
        print k,":",v
    #print dic



def f_05():
    def word_bigram(words):
        word_list = words.strip().split(" ")
        return [(word_list[i],word_list[i+1]) for i in range(len(word_list)-1)]

    def char_bigram(words):
        return [words[i]+words[i+1] for i in range(len(words)-1)]

    sample = "I am an NLPer"
    print word_bigram(sample)
    print char_bigram(sample)


def f_06():
    para1 = "paraparaparadise"
    para2 = "paragraph"

    def char_bigram(words):
        return [words[i]+words[i+1] for i in range(len(words)-1)]

    X = set(char_bigram(para1))
    Y = set(char_bigram(para2))

    print "SUM:",X|Y
    print "MUL:",X&Y
    print "SUM:",X-Y
    print "'se' in X:",('se' in X)
    print "'se' in Y:",('se' in Y)


def f_07():
    def template(x,y,z):
        return u"%s時の%sは%s"%(x,y,z)
    print template(12,u"気温",22.4)


def f_08():
    def my_cipher(sentence):
        return "".join([str(219-int(ord(c))) if c.isalpha() and c.islower() else c for c in sentence])
    
    def my_decipher(sentence):
        decipher = []
        lower_bound = 219 - ord("z")
        upper_bound = 219 - ord("a")
        skip = 0
        for i in range(len(sentence)):
            if not sentence[i].isdigit():
                decipher.append(sentence[i])
                continue
            elif skip > 0:
                skip -= 1
                continue

            c = sentence[i:i+3]
            if c.isdigit() and (lower_bound <= int(c) <= upper_bound):
                decipher.append(chr(219-int(c)))
                skip = 2
            else:
                decipher.append(sentence[i])

        return "".join(decipher)
    
    base_sentence = "This is a test HELLO." 
    ciph_sentence = my_cipher(base_sentence)
    print base_sentence
    print ciph_sentence
    print my_decipher(ciph_sentence)


def f_09():
    def typoglycemia(sentence):
        word_list = sentence.strip().split(" ")
        head = word_list[0]
        mid  = word_list[1:-1]
        tail = word_list[-1]
        import random
        random.shuffle(mid)
        return " ".join([head]+mid+[tail])

    example = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print example
    print typoglycemia(example)


##################
# Chapter 2.     #
##################

import commands

def is_diff(my,sh):
    if len(my) != len(sh):
        return True
 
    for m,s in zip(my,sh):
        if m != s:
            return True
    return False

def f_10():
    my = str(sum([1 for i in open("hightemp.txt","r")]))+" hightemp.txt"
    sh = commands.getoutput("wc -l hightemp.txt")
    assert is_diff(my,sh) is False, "line count"


def f_11():
    my = ("".join([i.replace("\t"," ") for i in open("hightemp.txt","r")])).strip()
    sh =  commands.getoutput("cat hightemp.txt | sed -e 's/\t/ /g'")
    assert is_diff(my, sh) is False, "replace tab to space"


def f_12():
    f = open("hightemp.txt","r")
    col1 = open("col1.txt","w")
    col2 = open("col2.txt","w")
    for _line in f:
         line = _line.strip().split("\t")
         col1.write(line[0]+"\n")
         col2.write(line[1]+"\n")
    f.close()
    col1.close()
    col2.close()

    col1_read = ("".join(open("col1.txt","r").readlines())).strip()
    col1_result = commands.getoutput("cat hightemp.txt | cut -f 1")
    assert is_diff(col1_read, col1_result) is False,"col1.txt"

    col2_read = ("".join(open("col2.txt","r").readlines())).strip()
    col2_result = commands.getoutput("cat hightemp.txt | cut -f 2")
    assert is_diff(col2_read, col2_result) is False,"col2.txt"


def f_13():
    col1 = open("col1.txt","r")
    col2 = open("col2.txt","r")
    my = ("".join([c1.strip()+"\t"+c2 for c1,c2 in zip(col1,col2)])).strip()
    sh = commands.getoutput("paste col1.txt col2.txt")

    assert is_diff(my, sh) is False, "paste col1.txt col2.txt"


def f_14(filename, N):
    head = []
    count = 1
    for i in open(filename,"r"):
        head.append(i)
        if N <= count:
            break
        count += 1
    my = ("".join(head)).strip()
    sh = commands.getoutput("head -n %d %s"%(N,filename))

    assert is_diff(my, sh) is False, "head"


def f_15(filename, N):
    f = open(filename,"r")
    line_num = sum([1 for i in f])

    f.seek(0)
    tail = []
    count = line_num - N
    for line in f:
        if count > 0:
            count -= 1
            continue
        tail.append(line)

    my = ("".join(tail)).strip()
    sh = commands.getoutput("tail -n %d %s"%(N,filename))
    assert is_diff(my, sh) is False, "tail"


def f_16(filename, line_num):
    # by command "split": split -l line_num filename
    f = open(filename,"r")
    splited = []
    f.seek(0)
    counter = 0
    for line in f:
        if counter == 0:
            splited.append([])
        splited[-1].append(line)
        counter += 1
        if line_num <= counter:
            counter = 0

    # lazy check for code validation
    for i in splited:
        print len(i)


def f_17(filename):
    first_column = []
    for line in open("hightemp.txt","r"):
        first_column.append(line.strip().split("\t")[0])
    my = len(set(first_column))
    sh = int(commands.getoutput("cat hightemp.txt | cut -f 1 | sort | uniq | wc -l"))
    assert (my == sh), "Number of unique strings"


def f_18():
    hightemp_list = sorted([tuple(line.strip().split("\t"))  for line in open("hightemp.txt","r")],
                           key=lambda x:-float(x[2]))

    my = [i[2] for i in hightemp_list]
    sh = commands.getoutput("cat hightemp.txt | sort -n -k3 -r | cut -f3").split("\n")
    assert is_diff(my, sh) is False, "sort by temperature in reverse order"


def f_19():
    first_column = [line.strip().split("\t")[0] for line in open("hightemp.txt","r")]
    word_freq = {}
    for i in set(first_column):
        word_freq[i] = first_column.count(i)
    
    my = [str(v)+" "+k for k,v in sorted(word_freq.items(),key=lambda d:-d[1])]
    sh = [i.strip() for i in commands.getoutput("cat hightemp.txt | cut -f1 | sort | uniq -c | sort -r").split("\n")]
    #assert is_diff(my, sh) is False, "frequency count and sort"



##################
# Chapter 3.     #
##################
def get_uk_article():
    import json
    _JSON_FILENAME = "jawiki-country.json"
    with open(_JSON_FILENAME, "r") as f:
        # json.load cannot read multiple json object 
        for i in f:
            json_obj = json.loads(i)
            if json_obj["title"] == u"イギリス":
                break
    return json_obj["text"]


def f_20():
    print get_uk_article()


def get_category_line():
    return [i for i in get_uk_article().split("\n") if "Category" in i]


def f_21():
    for i in get_category_line():
        print i


def f_22():
    for line in get_category_line():
        print line.replace("[","").replace("]","").split(":")[1]


def f_23():
    for line in get_uk_article().split("\n"):
        if "==" in line:
            category_level = line.count("=") // 2 - 1
            print "LV:%d => %s"%(category_level,line)

def f_24():
    for line in get_uk_article().split("\n"):
        # [format] 
        # (File|ファイル):<media filename>|...
        # a line should be split by ":" and "|"
        if "File" in line or u"ファイル" in line:
            print line.split(":")[1].split("|")[0]

def f_25():
    base_info = False
    dic = {}
    for line in get_uk_article().split("\n"):
        if u"基礎情報" in line:
            base_info = True
            continue
        if "}}" == line:
            break
        if base_info:
            if line.find("|") == 0:
                line = line.replace("|","")
                left_equal_idx = line.find("=")
                key = line[:left_equal_idx]
                val = line[left_equal_idx+1:]
                dic[key] = val
            else:
                dic[key] += line

    for i in dic.keys():
        print i,dic[i]
    return dic


def remove_accent(line):
    line = line.replace("'''''","")
    line = line.replace("'''","")
    line = line.replace("''","")
    return line


def f_26():
    base_info = False
    dic = {}
    for line in get_uk_article().split("\n"):
        if u"基礎情報" in line:
            base_info = True
            continue
        if "}}" == line:
            break
        if base_info:
            line = remove_accent(line)
            if line.find("|") == 0:
                line = line.replace("|","")
                left_equal_idx = line.find("=")
                key = line[:left_equal_idx]
                dic[key] = line[left_equal_idx+1:]
            else:
                dic[key] += line

    for i in dic.keys():
        print i,dic[i]
    return dic
 

def remove_internal_link(line):
    if not (("[[" in line) and not (u"ファイル:" in line)):
        return line

    while "[[" in line:
        left_idx = line.find("[[")
        right_idx = line.find("]]")
        link = line[left_idx+2:right_idx]
        if "|" in link:
            if line.find("|") == 0:
                mid_idx = line[1:].find("|")
            else:
                mid_idx = line.find("|")
            display = line[mid_idx+2:right_idx]
        else:
            display = link
        line = line[:left_idx]+display+line[right_idx+2:]
    return line

def f_27():
    base_info = False
    dic = {}
    for line in get_uk_article().split("\n"):
        if u"基礎情報" in line:
            base_info = True
            continue
        if "}}" == line:
            break

        if base_info:
            # remove accent markup
            line = remove_accent(line)
            # remove internal link
            line = remove_internal_link(line)

            if line.find("|") == 0:
                line = line[1:]
                left_equal_idx = line.find("=")
                key = line[:left_equal_idx].strip()
                dic[key] = line[left_equal_idx+1:].strip()
            else:
                dic[key] += line

    #for i in dic.keys():
    #    print i,dic[i]
    return dic
 
def remove_file(line):
    if u"ファイル:" not in line:
        return line
    filename = line.replace("[[","").replace("]]","").replace(u"ファイル:","").strip()
    filename = filename.split("|")[0]
    return filename

def remove_category(line):
    if "Category:" not in line:
        return line
    category = line.replace("[[","").replace("]]","").replace("Category:","").split("|")[0].strip()
    return category

def remove_link(line):
    if "[" not in line:
        return line
    link_start = line.find("[")
    link_mid = line[link_start:].find(" ")+len(line[:link_start])+1
    link_end = line.find("]")
    return line[:link_start]+line[link_mid:link_end]+line[link_end+1:]

def remove_list(line):
    import re
    bare_list = re.sub("^\*+","",line)
    bare_list = re.sub("^#+","",line)
    return bare_list

def remove_template(line):
    line = line.replace("{{","").replace("}}","")
    if "|" in line:
        line = line.split("|")[-1].strip()
    return line

def f_28():
    dic = f_27()
    for k,v in dic.items():
        line = v.strip().split("\n")
        dic[k] = []
        for i in line:
            i = remove_file(i)
            i = remove_category(i)
            i = remove_link(i)
            i = remove_list(i)
            i = remove_template(i)
            dic[k].append(i)
        print k,
        for i in dic[k]:
            print i

def f_29():
    dic = f_27()
    filename = dic[u"国旗画像"]
    api_url = "http://en.wikipedia.org/w/api.php?action=query&titles=Image:"+filename.replace(" ","%20")+"&prop=imageinfo&iiprop=url&format=json"
    
    import urllib2
    resp = urllib2.urlopen(api_url)
    import json
    json_obj = json.loads(resp.read())
    for k,v in json_obj["query"]["pages"].items():
        print json_obj["query"]["pages"][k]["imageinfo"][0]["url"]

##################
# Chapter 4.     #
##################
def load_morpheme():
    MORPH_FILENAME = "neko.txt.mecab"
    morph_list = []
    with open(MORPH_FILENAME, "r") as f:
        for line in f:
            if line.strip() == "EOS":
                continue
            line = line.strip().split("\t")
            morph_list.append({unicode(line[1],"utf-8"):unicode(line[0],"utf-8")})
    return morph_list

def f_30():
    for i in load_morpheme():
        for k,v in i.items():
            print k, v

def f_31():
    # 一  名詞,数,*,*,*,*,一,イチ,イチ
    # 表層形 = 単語そのもの (= 辞書エントリ) 
    for i in load_morpheme():
        for k,v in i.items():
            if u"動詞" == k.strip().split(",")[0]:
                print v

def f_32():
    # つか    動詞,自立,*,*,五段・カ行イ音便,未然形,つく,ツカ,ツカ
    # v     k:0    1    2 3 4                5      6(原形)
    for i in load_morpheme():
        for k,v in i.items():
          key_list = k.strip().split(",")
          if u"動詞" == key_list[0]:
              print key_list[6],k

def f_33():
    # 装飾    名詞,サ変接続,*,*,*,*,装飾,ソウショク,ソーショク
    # v     k:0    1        2 3 4 5 6(原形)
    for i in load_morpheme():
        for k,v in i.items():
            key_list = k.strip().split(",")
            if u"名詞" == key_list[0] and u"サ変接続" == key_list[1]:
                print key_list[6],k

def f_34():
    # example
    # 彼  名詞,代名詞,一般,*,*,*,彼,カレ,カレ
    # の  助詞,連体化,*,*,*,*,の,ノ,ノ
    # 掌  名詞,一般,*,*,*,*,掌,テノヒラ,テノヒラ
    # このやり方だと名詞(接尾)も含まれるので、日本語としてはおかしいものが混ざる
    morph_list = load_morpheme()
    for idx in range(len(morph_list)-2):
        head = morph_list[idx].items()[0][0].strip().split(",")
        if u"名詞" != head[0]:
            continue

        mid = morph_list[idx+1].items()[0][0].strip().split(",")
        if not(u"助詞" == mid[0] and u"連体化" == mid[1]):
            continue

        tail = morph_list[idx+2].items()[0][0].strip().split(",")
        if u"名詞" != tail[0]:
            continue

        print "#########################"
        print morph_list[idx].items()[0][0]
        print morph_list[idx+1].items()[0][0]
        print morph_list[idx+2].items()[0][0]
        print "#########################"


def f_35():
    def get_word_type(word_dic):
        return word_dic.items()[0][0].strip().split(",")[0]

    def get_word(word_dic):
        return word_dic.items()[0][1]

    longest = []
    tmp = []
    for i in load_morpheme():
        if u"名詞" == get_word_type(i):
            tmp.append(i)
        else:
            if len(tmp) > len(longest):
                longest = tmp
            tmp = []

    for i in longest:
        print i.items()[0][1],


def get_counter():
    counter = {}
    for i in load_morpheme():
        origword = get_origword(i)
        if origword in counter:
            counter[origword] += 1
        else:
            counter[origword] = 1

    return counter

def f_36():
    def get_origword(word_dic):
        return word_dic.items()[0][0].strip().split(",")[6]

    for i in sorted(get_counter().items(),key=lambda x: -x[1]):
        print i[0],":",i[1]



def main():
    #f_00()
    #f_01()
    #f_02()
    #f_03()
    #f_04()
    #f_05()
    #f_06()
    #f_07()
    #f_08()
    #f_09()
    #f_10()
    #f_11()
    #f_12()
    #f_13()
    #f_14("hightemp.txt",10)
    #f_15("hightemp.txt",10)
    #f_16("hightemp.txt",9)
    #f_17("hightemp.txt")
    #f_18()
    #f_19()
    #f_20()
    #f_21()
    #f_22()
    #f_23()
    #f_24()
    #f_25()
    #f_26()
    #f_27()
    #f_28()
    #f_29()
    #f_30()
    #f_31()
    #f_32()
    #f_33()
    #f_34()
    #f_35()
    f_36()

if __name__ == "__main__":
    main()
