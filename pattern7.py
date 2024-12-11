# for row in range(5,0,-1):
#     for col in range(1,6):
#         if col % 2 == 0:
#             print(0,end =" ")
#         else:
#             print(1,end =" ")
#     print()

# second method to create this
for row in range(1,6):
 for col in range(5,0,-1):
  if col % 2 == 0:
   print(0,end = " ")
  else:
   print(1,end = " ")
 print()
 