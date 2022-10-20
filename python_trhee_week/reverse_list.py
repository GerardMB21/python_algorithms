def reverse_list(arr:list) -> list:
  if arr == []:
    return []
  return reverse_list(arr[1:])+[arr[0]]

array = [1,2,3,4,5]

print(reverse_list(array))