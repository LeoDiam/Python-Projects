x = 25
e = 0.01
guesses = 0
low = 0.0
high = max(1.0 , x)
ans = (high + low) / 2.0
while abs(ans**2 - x) >= e:
    print('low = ',low,' high = ',high,' ans ',ans)
    guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('num of guesses ',guesses)
print(ans,'is close to square root of ',x)