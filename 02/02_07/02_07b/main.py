# Linear Search

my_list = [8, 5, 0, 3, 9, 7, 3, 5]
ITEM = 300
found = 0

for i, search in enumerate(my_list):
  if ITEM==search:
    # print(f"We found {ITEM} at idx {i} :)")
    found=1
    break

if not found:
  print(f"We didn't find {ITEM} anywhere :(")
  


print(my_list.index(ITEM))