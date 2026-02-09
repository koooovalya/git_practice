N_MAX = 15

def read_array():
    arr = list()
    n = int(input("Enter number of elements: "))
    if n > N_MAX:
        print("Error: too many elements")
        exit()
    print("Enter elements:")
    i = 0
    while (i < n):
        tmp = int(input(""))
        arr.append(tmp)
        i += 1
    return arr

def print_array(arr):
    print("Array:")
    i = 0
    while (i < len(arr)):
        print(arr[i], end = " ")
        i += 1
    print("")

# Основная программа
if __name__ == "__main__":
    a = read_array()
    print_array(a)
arr = list()
n = int(input("Enter number of elements: "))
N_MAX = 15
if n > N_MAX:
    print("Error: too many elements")
    exit()
print("Enter elements:")
i = 0
while (i < n):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1
print("Array:")
i = 0
while (i < n):
    print(arr[i], end = " ")
    i += 1
print("")

