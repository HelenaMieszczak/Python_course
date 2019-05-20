txt = "abcdef"

for letter in txt:
    print("-", letter)

print("***")

for i in range(5, 20, 2):  #(start, stop, krok)
    print(i)

print("***")

list = ["Ada", "Julia", "Ruby"]

for i in range(3):
    print(i, ":", list[i])

print("***")

pass_ = ""
magic = "hoksupokus"

for num in range(2, 10, 2):
    pass_ = pass_ + str(num) + magic[num]
    print(pass_)


