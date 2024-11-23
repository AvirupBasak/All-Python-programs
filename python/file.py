"""
 create a new file "Practice.txt" using pyhton. Add this following data.
        Hi Everyone
        We are learning File i/o.
        Using Python.
        I like programming in c.
"""
import os
with open("Practice.txt","a") as f:
    f.write("\nHi Everyone We are learning File i/o.\nUsing Python.\nI like programming in c.")

with open("Practice.txt","r") as f:
    data = f.read()
    print(data)
os.remove("Practice.txt")