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
    return bare_list

def remove_countlist(line):
    import re
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
            i = remove_countlist(i)
            i = remove_template(i)
            dic[k].append(i)
        print k,
        for i in dic[k]:
            print i

def f_29():
    dic = f_27()
    filename = dic[u"国旗画像"]
    api_url = "http://en.wikipedia.org/w/api.php?action=query&titles=Image:" \
                + filename.replace(" ","%20") + "&prop=imageinfo&iiprop=url&format=json"
    
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
    morph_list = [[]]
    with open(MORPH_FILENAME, "r") as f:
        for line in f:
            if line.strip() == "EOS":
                if morph_list[-1] != []:
                    morph_list.append([])
                continue
            line = line.strip().split("\t")
            morph_list[-1].append({unicode(line[1],"utf-8"):unicode(line[0],"utf-8")})
    return morph_list

def f_30():
    for j in load_morpheme():
        for i in j:
            for k,v in i.items():
                print k, v

def f_31():
    # 一  名詞,数,*,*,*,*,一,イチ,イチ
    # 表層形 = 単語そのもの (= 辞書エントリ) 
    for j in load_morpheme():
        for i in j:
            for k,v in i.items():
                if u"動詞" == k.strip().split(",")[0]:
                    print v,k

def f_32():
    # つか    動詞,自立,*,*,五段・カ行イ音便,未然形,つく,ツカ,ツカ
    # v     k:0    1    2 3 4                5      6(原形)
    for j in load_morpheme():
        for i in j:
            key_list = k.strip().split(",")
            if u"動詞" == key_list[0]:
                print key_list[6],k

def f_33():
    # 装飾    名詞,サ変接続,*,*,*,*,装飾,ソウショク,ソーショク
    # v     k:0    1        2 3 4 5 6(原形)
    for j in load_morpheme():
        for i in j:
            k,v = i.items()[0]
            key_list = k.strip().split(",")
            if u"名詞" == key_list[0] and u"サ変接続" == key_list[1]:
                print key_list[6],k


def get_word_type(word_dic):
    return word_dic.items()[0][0].strip().split(",")[0]

def get_word(word_dic):
    return word_dic.items()[0][1]

def f_34():
    # example
    # 彼  名詞,代名詞,一般,*,*,*,彼,カレ,カレ
    # の  助詞,連体化,*,*,*,*,の,ノ,ノ
    # 掌  名詞,一般,*,*,*,*,掌,テノヒラ,テノヒラ
    # このやり方だと名詞(接尾)も含まれるので、日本語としてはおかしいものが混ざる
    for morph_list in load_morpheme():
        for idx in range(len(morph_list)-2):
            head = get_word_type(morph_list[idx])
            if u"名詞" != head[0]:
                continue

            mid = get_word_type(morph_list[idx+1])
            if not(u"助詞" == mid[0] and u"連体化" == mid[1]):
                continue

            tail = get_word_type(morph_list[idx+2])
            if u"名詞" != tail[0]:
                continue

            print "#########################"
            print morph_list[idx].items()[0][0]
            print morph_list[idx+1].items()[0][0]
            print morph_list[idx+2].items()[0][0]
            print "#########################"


def f_35():
    longest = []
    tmp = []
    for j in load_morpheme():
        for i in j:
            if u"名詞" == get_word_type(i):
                tmp.append(i)
            else:
                if len(tmp) > len(longest):
                    longest = tmp
                tmp = []

    for i in longest:
        print i.items()[0][1],



def get_counter():
    def get_origword(word_dic):
        return word_dic.items()[0][0].strip().split(",")[6]

    counter = {}
    for j in load_morpheme():
        for i in j:
            if get_word_type(i) == u"記号":
                continue
            origword = get_origword(i)
            if origword in counter:
                counter[origword] += 1
            else:
                counter[origword] = 1

    return counter



def f_36():
    for i in sorted(get_counter().items(),key=lambda x: -x[1]):
        print i[0],":",i[1]


import matplotlib.pyplot as plt
def f_37():
    label = []
    x = []
    y = []
    for i,v in enumerate(sorted(get_counter().items(), key=lambda x: -x[1])[:10]):
        label.append(v[0])
        x.append(i)
        y.append(v[1])
    plt.bar(x,y,align="center",width=0.5)
    plt.xticks(x,label)
    plt.xlim(-0.5,9.5)
    plt.xlabel(u"単語")
    plt.ylabel(u"出現頻度")
    plt.show()
   

def f_38(bins=30):
    label = []
    x = []
    y = []
    for i,v in enumerate(sorted(get_counter().items(), key=lambda x: -x[1])):
        label.append(v[0])
        x.append(i+1)
        y.append(v[1])

    plt.xlabel(u"出現頻度")
    plt.ylabel(u"単語の種類数")
    plt.title("Histogram")
    plt.hist(y,bins=bins)
    plt.show()


def f_39():
    label = []
    x = []
    y = []
    for i,v in enumerate(sorted(get_counter().items(), key=lambda x: -x[1])):
        label.append(v[0])
        x.append(i+1)
        y.append(v[1])

    plt.xlim(0.1,10e5)
    plt.xscale("log")
    plt.yscale("log")
    plt.title(u"Zipfの法則")
    plt.xlabel(u"出現頻度順位")
    plt.ylabel(u"出現頻度")
    plt.scatter(x,y)
    plt.show()
    

##################
# Chapter 5.     #
##################
"""
http://qiita.com/nezuq/items/f481f07fc0576b38e81d より
1行目

    *
    文節番号
    係り先の文節番号(係り先なし:-1)
    主辞の形態素番号/機能語の形態素番号
    係り関係のスコア(大きい方が係りやすい)

2行目

    表層形 （Tab区切り）
    品詞
    品詞細分類1
    品詞細分類2
    品詞細分類3
    活用形
    活用型
    原形
    読み
    発音
"""
class Morph():
    def __init__(self,morph_line):
        self.surface, morph_elems = morph_line.strip().split("\t")
        self.morph_elems = morph_elems.split(",")

        self.base = self.morph_elems[6]
        self.pos = self.morph_elems[0]
        self.pos1 = self.morph_elems[1]

    def elem_print(self):
        print self.base,

    def get_pos(self):
        return self.pos

    def get_surface(self):
        return self.surface

    def get_base(self):
        return self.base

    def is_noun(self):
        return  u"名詞" == unicode(self.pos, "utf-8")

    def is_verb(self):
        return  u"動詞" == unicode(self.pos, "utf-8")

    def is_joshi(self):
        return  u"助詞" == unicode(self.pos, "utf-8")

    def is_sahen_setsuzoku_noun(self):
        return  u"名詞" == unicode(self.pos, "utf-8") and \
                u"サ変接続" == unicode(self.pos1, "utf-8")

    def is_joshi_wo(self):
        return self.is_joshi() and u"を" == unicode(self.surface, "utf-8")

def f_40():
    morph_list = [[]]
    with open("neko.txt.cabocha","r") as f:
        for line in f:
            if line[0] == "*":
                continue
            if line.strip() == "EOS":
                if morph_list[-1] != []:
                    morph_list.append([])
                continue
            morph_list[-1].append(Morph(line))

    # 先頭は章番号なのでスキップする
    for i in morph_list[3]:
        i.elem_print()
    print ""

# 1文をChunkオブジェクトのリストとする
# chunk = 文節
class Chunk():
    def __init__(self):
        self.chunk_idx = -1
        self.morphs = []
        self.dst = -1
        self.srcs = []
        self.score = 0

    def set_params(self, param_line):
        # * 0 5D 0/1 -0.620584
        #   0: *
        #   1: 文節番号
        #   2: 係り先の文節番号(係り先なし:-1)
        #   3: 主辞の形態素番号/機能語の形態素番号
        #   4: 係り関係のスコア(大きい方が係りやすい) 
        params = param_line.strip().split(" ")
        self.dst = int(params[2][:-1].strip())
        self.score = float(params[4])
        self.chunk_idx = int(params[1])
        
    def add_morph(self,morph):
        self.morphs.append(morph)

    def get_morphs(self):
        return self.morphs

    def get_dst_number(self):
        return self.dst

    def add_srcs(self,src_id):
        self.srcs.append(src_id)

    def get_srcs(self):
        return self.srcs

    def get_chunk_idx(self):
        return self.chunk_idx

    def get_morphs_surface_nomark(self):
        return [i.get_surface() for i in self.morphs if unicode(i.get_pos(), "utf-8") != u"記号"]

    def is_only_mark(self):
        if self.get_morphs_surface_nomark():
            return False
        else:
            return True

    def has_generic(self,checker):
        for morph in self.morphs:
            if checker(morph):
                return True
        return False

    def has_noun(self):
        return self.has_generic(lambda x:x.is_noun())

    def has_verb(self):
        return self.has_generic(lambda x:x.is_verb())

    def has_joshi(self):
        return self.has_generic(lambda x:x.is_joshi())

    def has_sahen_setsuzoku_noun(self):
        return self.has_generic(lambda x:x.is_sahen_setsuzoku_noun())

    def has_joshi_wo(self):
        return self.has_generic(lambda x:x.is_joshi_wo())

    def get_morphs_generic(self,checker):
        morph_list = []
        for morph in self.morphs:
            if checker(morph):
                morph_list.append(morph)
        return morph_list

    def get_joshi(self):
        return self.get_morphs_generic(lambda x:x.is_joshi())

    def get_verb(self):
        return self.get_morphs_generic(lambda x:x.is_verb())

    def get_bases_conv_first_noun(self,conv):
        str_list = []
        first = True
        for morph in self.morphs:
            if first and morph.is_noun():
                str_list.append(conv) 
                first = False
            else:
                str_list.append(morph.get_base())
        return str_list

    def elem_print(self):
        print "dst:",self.dst,
        print "src:",self.srcs,
        for morph in self.morphs:
            morph.elem_print()
        print


def make_chunk_lists():
    def set_dst_chunks(chunk_list):
        for i,chunk in enumerate(chunk_list):
            dst = chunk.get_dst_number()
            if dst >= 0:
                chunk_list[dst].add_srcs(i)

    chunk_list = [[]]
    
    with open("neko.txt.cabocha","r") as f:
        for line in f:
            if line[0] == "*":
                chunk = Chunk()
                chunk.set_params(line)
                chunk_list[-1].append(chunk)
                continue
            if line.strip() == "EOS":
                if chunk_list[-1] != []:
                    set_dst_chunks(chunk_list[-1])
                    chunk_list.append([])
                continue
            chunk_list[-1][-1].add_morph(Morph(line))

    return chunk_list

def f_41():
    chunk_lists = make_chunk_lists()
    for chunk in chunk_lists[8]:
        chunk.elem_print()


def f_42():
    for chunk_list in make_chunk_lists():
        for chunk in chunk_list:
            if chunk.is_only_mark():
                continue
            print "".join(chunk.get_morphs_surface_nomark()),
            print "\t",
            if chunk.get_dst_number() != -1:
                print "".join(chunk_list[chunk.get_dst_number()].get_morphs_surface_nomark())
            else:
                print "NO_DST"

def f_43():
    for chunk_list in make_chunk_lists():
        for chunk in chunk_list:
            if chunk.is_only_mark():
                continue
            if chunk.has_noun() and chunk_list[chunk.get_dst_number()].has_verb():
                print "".join(chunk.get_morphs_surface_nomark()),
                print "\t",
                print "".join(chunk_list[chunk.get_dst_number()].get_morphs_surface_nomark())
                

def make_node(src,dst):
    return src + " -> " + dst + ";\n"

def chunks_to_digraph(title,chunks):
    script = ["digraph " + title.strip().replace(" ","_") + "{ \n"]
    for chunk in chunks:
        dst = chunk.get_dst_number()
        if dst >= 0:
            script.append(make_node("".join(chunk.get_morphs_surface_nomark()),
                                    "".join(chunks[dst].get_morphs_surface_nomark())
                                    ))
    script.append("}\n")
    return "".join(script)

def f_44():
    chunk_lists = make_chunk_lists()
    chunk_list = chunk_lists[8]
    script = chunks_to_digraph("section 44",chunk_list)

    import sys
    sys.stdout.write(script)


# get_kaku_pattern => (動詞のリスト: [class Morph], 助詞のリスト: [class Morph], 動詞のかかり元:[class Chunk])
# 動詞も助詞も複数あるパターンがある(複合辞をぶった切るから？)
def get_kaku_patterns():
    kaku_patterns = []
    for chunk_list in make_chunk_lists():
        for chunk in chunk_list:
            if not chunk.has_verb():
                continue
            srcs = chunk.get_srcs()

            joshi = []
            chunks = []
            for i in srcs:
                joshi_cand = chunk_list[i].get_joshi()
                for j in joshi_cand:
                    joshi.append(j)
                if joshi_cand:
                    chunks.append(chunk_list[i])

            if not joshi:
                continue

            kaku_patterns.append((chunk.get_verb(),sorted(joshi),chunks))
    return kaku_patterns           


def f_45():
    for i in get_kaku_patterns():
        print i[0][0].get_base()+"\t"+" ".join([j.get_base() for j in i[1]])


def chunk_to_str(ck):
    return "".join(ck.get_morphs_surface_nomark())

def f_46():
    for i in get_kaku_patterns():
        print "".join([
                        i[0][0].get_base(),
                        "\t",
                        " ".join([j.get_base() for j in i[1]]),
                        "\t",
                        "".join([chunk_to_str(k) for k in i[2]])
                       ])


# get_kaku_pattern => (動詞のリスト: [class Morph], 助詞のリスト: [class Morph], 動詞のかかり元:[class Chunk])
#
# 参考資料：http://pj.ninjal.ac.jp/corpus_center/csj/manu-f/bunsetsu.pdf
# (辞書の問題か、cabochaの使い方の問題だと思うが)
# cabochaでは複合辞をうまく扱えないので、
# 以下のとおり勝手に条件を付ける(自然言語処理的に正しいのだろうか？)
# ・Chunkを構成する助詞が複数ある場合、最後に出現した助詞をChunkの助詞とする
# ・出現順が最後ではない助詞は、複合辞を構成するものとして、助詞扱いしない
#
# また、簡単のため、動詞に直接係るもののみ扱う(サ変接続名詞+を格の文節に係るものは考えない)
#
def f_47():
    lastjoshi_to_str = lambda x: x.get_joshi()[-1].get_surface()
    jutsugo_and_chunks = []
    for kaku_patterns in get_kaku_patterns():
        morph_verbs = kaku_patterns[0]
        chunk_srcs = kaku_patterns[2]

        jutsugo = [morph_verbs[0].get_base()]
        chunks = []
        NO_JUTSUGO = True
        for ck in chunk_srcs:
            if NO_JUTSUGO and ck.has_sahen_setsuzoku_noun() and ck.has_joshi_wo():
                #述語は複数ないものとする  
                jutsugo = [i.get_base() for i in ck.get_morphs()] + jutsugo
                NO_JUTSUGO = False
            else:
                chunks.append(ck)
        jutsugo_and_chunks.append((jutsugo,sorted(chunks,key=lastjoshi_to_str)))  

    for i in jutsugo_and_chunks:
        print "".join([
                        "".join(i[0]),
                        "\t",
                        " ".join([lastjoshi_to_str(j) for j in i[1]]),
                        "\t",
                        " ".join([chunk_to_str(k) for k in i[1]])
                      ])
                        

 
# get_all_kakari_path => [ [chunk内のpathリスト], [chunk内のpathリスト], ... ,]
# chunk内のpathリスト => [ [chunk,chunk,chunk, ... ,], [chunk,chunk,chunk, ... ,], ... ,]
def get_all_kakari_path_list():
    kakari_path = []
    for chunk_list in make_chunk_lists():
        kakari_path.append([])
        for chunk in chunk_list:
            if not chunk.has_noun():
                continue
            dst = chunk.get_dst_number()
            chunk_root = []
            while dst != -1:
                chunk_root.append(chunk_list[dst])
                dst = chunk_list[dst].get_dst_number()

            if chunk_root:
                chunk_root.insert(0,chunk)
                kakari_path[-1].append(chunk_root)

    return kakari_path


def f_48():       
    for kakari_path_list in get_all_kakari_path_list():
        for kakari_path in kakari_path_list:
            print " -> ".join([chunk_to_str(chunk) for chunk in kakari_path])
        print


   
# 名詞のみを置き換えていたり、名詞+助詞を置き換えていたりでルールがよくわからないので、
# 出力例から勝手に類推する。
# 
# [出力例]
# Xは | Yで -> 始めて -> 人間という -> ものを | 見た
# Xは | Yという -> ものを | 見た
# Xは | Yを | 見た
# Xで -> 始めて -> Y
# Xで -> 始めて -> 人間という -> Y
# Xという -> Y
# 
# ルール1：係り受けパスの先頭の文節については、置き換え対象を名詞とする。
#          => 文節 i については、最初に出現した名詞を含む文節の名詞を
#             X と置き換える。
#             文節 j については、文節 j からスタートする係り受けパスが、
#             文節 i からスタートする係り受けパスのサブセットでない場合は、
#             最初に出現した名詞を含む文節の名詞を Y と置き換える。
#
# ルール2：係り受けパスの先頭でない文節については、置き換え対象を分節全体とする。
#          => 文節 j が、文節 i からスタートする係り受けパスのサブセットの場合は、
#             最初に出現した名詞を含む文節全てをYと置き換える。
#
# ルール3: (多分ないと思うが) 共通部分を持たない2つのパスに関しては、処理対象としない
# 
def f_49():
    import itertools
    def intersection_kakari_path(path_x, path_y):
        return list(set(path_x) & set(path_y))

    def diff_kakari_path(path_x, path_y):
        return list(set(path_x) - set(path_y))
    
    noun_phrases_paths = []
    for kakari_path_list in get_all_kakari_path_list():
        noun_phrases_paths.append([])
        for path_x, path_y in itertools.combinations(kakari_path_list,2):
            intersect = intersection_kakari_path(path_x, path_y)
            if not intersect:
                continue
            path_x_diff = diff_kakari_path(path_x, intersect)
            path_y_diff = diff_kakari_path(path_y, intersect)
            
            noun_phrases_paths[-1].append({"path_x_diff": path_x_diff, 
                                           "intersection": intersect, 
                                           "path_y_diff": path_y_diff,
                                           })

    for dics in noun_phrases_paths:
        for dic in dics:
            path_x_diff = dic["path_x_diff"]
            path_y_diff = dic["path_y_diff"]
            intersect = dic["intersection"]
        
            if path_x_diff[1:]:
                print " -> ".join([
                                    "".join(path_x_diff[0].get_bases_conv_first_noun("X")),
                                    " -> ".join([chunk_to_str(chunk) for chunk in path_x_diff[1:]])
                                  ]),
            else:
                print " -> ".join([
                                    "".join(path_x_diff[0].get_bases_conv_first_noun("X")),
                                  ]),

            # path_y が path_x のサブセット
            #   => path_y_diff == [] 
            if not path_y_diff:
                print "-> Y"
            else:
                print "|",
                if path_y_diff[1:]:
                    print " -> ".join([
                                        "".join(path_y_diff[0].get_bases_conv_first_noun("Y")),
                                        " -> ".join([chunk_to_str(chunk) for chunk in path_y_diff[1:]])
                                      ]),
                else:
                    print " -> ".join([
                                        "".join(path_y_diff[0].get_bases_conv_first_noun("Y")),
                                      ]),

                print "|", 
                print " -> ".join([chunk_to_str(chunk) for chunk in intersect])
        print


                

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
    #f_36()
    #f_37()
    #f_38()
    #f_39()
    #f_40()
    #f_41()
    #f_42()
    #f_43()
    #f_44()
    #f_45()
    #f_46()
    #f_47()
    #f_48()
    f_49()

if __name__ == "__main__":
    main()
