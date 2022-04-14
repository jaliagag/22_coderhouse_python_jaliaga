#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ops = ["5", "2", "C", "D", "+"]
ops = ["5","-2","4","C","D","9","+","+"]
result = 0
record = []

for i in range(len(ops)):
    if ops[i] == "+":
        a = int(record[-1]) + int(record[-2])
        record.append(a)
    elif ops[i] == "C":
        record.pop()
    elif ops[i] == "D":
        a = int(record[-1])*2
        record.append(a)
    else:
        record.append(int(ops[i]))

for i in range(len(record)):
    result += record[i]
    #result += record[i]

print(result)
