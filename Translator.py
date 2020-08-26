from Functions import *

ende = input("To (M)orse or To (T)ext?~> ").upper()
inp = input("~> ")
if ende == "M":
    print(encrypt(inp.upper()))
else:
    print(decrypt(inp))
