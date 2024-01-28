def merge(arr, l, mid, h):
    left_half = arr[l:mid+1]
    right_half = arr[mid+1:h+1]

    i = j = 0
    k = l

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Copy the remaining elements of left_half, if any
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Copy the remaining elements of right_half, if any
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(arr, l, h):
    if l < h:
        mid = (l + h) // 2

        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, h)

        merge(arr, l, mid, h)


if __name__ == "__main__":
    # Example usage:
    array = [12, 11, 13, 5, 6, 7]
    print("Original array:", array)
    merge_sort(array, 0, len(array) - 1)
    print("Sorted array:", array)
