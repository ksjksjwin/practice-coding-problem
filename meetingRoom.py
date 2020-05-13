import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
time_list = []

for i in range(n):
     s, e = map(int, input().split())
     time_list.append((s,e))

time_list.sort(key = lambda x : (x[1],x[0])) #sort by a key

end_time = 0
count = 0

for s, e in time_list: #accessing the tuple value in time_list
    if s >= end_time:
        count += 1
        end_time = e

print(count)
