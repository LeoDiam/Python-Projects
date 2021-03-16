def simpleStockSpan(quotes):
    span = []
    for i in range(len(quotes)):
        k = 1
        span_end = False
        while i - k >= 0 and not span_end:
            if quotes[i - k] <= quotes[i]:
                k += 1
            else:
                span_end = True
        span.append(k)
    return span


quote = [100, 80, 60, 70, 60, 75, 85, 105]
print(simpleStockSpan(quote))