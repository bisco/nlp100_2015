# vim: fileencoding=utf-8

# http://www.cl.ecei.tohoku.ac.jp/nlp100/ より

##################
# Chapter 1.     #
##################
def f_00():
    print "".join([i for i in "stressed"][::-1])


def f_01():
    s = u"パタトクカシー"
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
    f_17("hightemp.txt")

if __name__ == "__main__":
    main()
