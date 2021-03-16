def stack_stock_span(quotes):
    spans = [1]
    s = []
    for i in range(1, len(quotes)):
        while len(s) != 0 and quotes[s[-1]] <= quotes[i]:
            s.pop()
        if len(s) == 0:
            spans.append(i + 1)
        else:
            spans.append(i - s[-1])
        s.append(i)
    return spans

quote = [100, 80, 60, 70, 60, 75, 85, 105]
print(stack_stock_span(quote))
