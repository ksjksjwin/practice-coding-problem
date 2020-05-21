import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

height_weight_list = []

for i in range(n):
    height , weight = map(int, input().split())
    height_weight_list.append((height, weight))

height_weight_list.sort(key = lambda x: (x[0],x[1]), reverse = True)

count = 0
weight = 0

for h, w in height_weight_list:
    if w > weight:
        count+=1
        weight = w

print(count)
