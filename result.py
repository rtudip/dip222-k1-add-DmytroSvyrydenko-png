

#1
# country = 'Oman'
# year = 10000
# row = []
# with open("data.txt", "r") as f:
#     for line in f:
#         row = line.rstrip().split(",")

#         if row[4] == country:
#             if int(year) > int(row[6]):
#                 year = int(row[6])
#                 print(str(row[0]) + " " + row[4] + " " + str(row[6]))
# print(year)

#2
# country = 'Latvia'
# people_count = 0
# row = []
# with open("data.txt", "r") as f:
#     for line in f:
#         row = line.rstrip().split(",")

#         if row[4] == country:
#             people_count = people_count + int(row[8])
#             print(str(row[0]) + " " + row[4] + " " + str(row[8]))
# print(people_count)

#3
# country = 'Latvia'
# people_count = 0
# row = []
# with open("data.txt", "r") as f:
#     for line in f:
#         row = line.rstrip().split(",")

#         if row[4] == country and row[7] == 'Telecommunications':
#             people_count = people_count + int(row[8])
#             print(str(row[0]) + " " + row[4] + " " + str(row[8]))
# print(people_count)

#4
# country = 'Latvia'
# company_count = 0
# row = []
# with open("data.txt", "r") as f:
#     for line in f:
#         website = ''
#         row = line.rstrip().split(",")

#         if row[4] == country:
#             website = row[3]
#             if 'https://' in website:
#                 company_count = company_count + 1
#                 print(str(row[0]) + " " + row[4] + " " + str(row[3]))
# print(company_count)


#5
# country = 'Latvia'
# company_count = 0
# row = []
# with open("data.txt", "r") as f:
#     for line in f:
#         website = ''
#         row = line.rstrip().split(",")

#         if row[4] == country:
#             website = row[3]
#             if '.org' in website:
#                 company_count = company_count + 1
#                 print(str(row[0]) + " " + row[4] + " " + str(row[3]))
# print(company_count)