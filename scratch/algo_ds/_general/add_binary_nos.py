"""

Add binary no represented in a string
"""


def compute(str1,str2):
    c=bin(int(str1,2)+int(str2,2))
    print(c)


if __name__=="__main__":
    compute("01","101")