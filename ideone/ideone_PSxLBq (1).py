#!/bin/python

import sys


S = raw_input()
no_of_messages=len(S)/3


total_S=S.count("S")
total_O=S.count("O")

print total_S
print total_O

total_s_eror=total_S-no_of_messages*2
total_o_eror=no_of_messages-total_O

y=total_s_eror+total_o_eror
print y