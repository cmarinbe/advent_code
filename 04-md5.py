# coding: utf-8
import md5
from itertools import count

input = "ckczppom"

def get_lowest_md5(input, zeros):
    m = md5.new()
    m.update(input)

    for val in count():
        ans = val+1 # we dont want the 0
        if ans%10000==0: print "Checking:", ans
        m_ans = m.copy()
        m_ans.update(str(ans))
        if (m_ans.hexdigest()).startswith(zeros):
            return ans, m_ans


def get_lowest_md5_5zeros(input):
    return get_lowest_md5(input, "00000")

def get_lowest_md5_6zeros(input):
    return get_lowest_md5(input, "000000")



# EOF