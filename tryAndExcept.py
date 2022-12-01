elao = "5 degrees"
temp = 3

try:
    elao = int(elao)
    elao = elao * temp
except:
    elao = -1
    print("second way")

print(temp*elao)