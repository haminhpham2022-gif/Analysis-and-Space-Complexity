scores = [12, 25, 33, 41, 50, 67, 72, 85, 91, 98]
n = len(scores)
target = 98

print('===Quiz Score Finder===')
print(f"Score: {scores}\nTarget: {target}")
print()

# Linear Search
step = 0 
for i in range(n):
    step += 1
    if scores[i] == target:
        print(f"Linear Search: index = {i}\nsteps = {step}") 
        break
print()

# Binary Search
lo = 0
hi = n-1
step = 0
while lo <= hi:
    mid = (lo+hi)//2
    step += 1
    if scores[mid] == target:
        print(f"Binary Search: index = {mid}\nsteps = {step}") 
        break
    elif scores[mid]<target:
        lo = mid+1
    else:
        hi = mid-1
print()

# Recursive Binary Search
def recur_search(score, lo, hi, target, call=0):
    call += 1
    if lo < hi:
        return -1,call
    mid = (lo+hi)//2
    if scores[mid]==target:
        return mid,call
    elif score[mid]<target:
        return recur_search(score, mid+1, hi, target, call)
    else:
        return recur_search(score, lo, mid-1, target, call)
    
result,call = recur_search(scores, 0, n-1, target)
print(f"Recursive Binary Search: index = {result}\nsteps = {call}") 
print()