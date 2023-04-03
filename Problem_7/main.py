def quicksort(a, i=0, j=1):
    n = len(a)
    if n == 0:
        return
    I_PIVOT = 0
    k = I_PIVOT
    for i in range(1, n):
        if a[i] < a[I_PIVOT]:
            k += 1
    # MC rethink logic because in this way it is inefficient and finds the position of the pivot in the ordered array, but without using it.

def main():
    a = [5, 2, 4, 7, 1, 3, 2, 6]
    print(f"Original: {a}")
    a = quicksort(a)
    print(f"Ordered: {a}")

main()
