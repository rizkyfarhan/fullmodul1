# def pascal (n):
#     mainlist = [1]
#     newlist = []
#     for i in range (n):
#         newlist.append(mainlist)
#         temp = []
#         temp.append(1)
#         if i == 0:
#             for j in range (len(mainlist)):
#                 temp.append(mainlist[j]+mainlist[j])
#         else:
#             for j in range (len(mainlist)-1):
#                 temp.append(mainlist[j]+mainlist[j+1])
#         temp.append(1)
#         mainlist = temp
#     print(newlist)
# pascal(5)