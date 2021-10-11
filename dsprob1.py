wordict = {
    "scale":"nap",
    "hair":"bal",
    "shirt":"kapda",
}
a = input("enter the hindi word:\n")
#("english name is:",wordict[a])
print("the meaning of your name is:", wordict.get(a))