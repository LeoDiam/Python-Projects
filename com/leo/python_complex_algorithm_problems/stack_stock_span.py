
def read_quotes(filename):
    dates = []
    quotes = []
    with open(filename) as quotes_file:
        for line in quotes_file:
            if line.startswith('#'):
                continue
            parts = line.split(',')
            if len(parts) != 2:
                continue
            month, day, year = parts[0].split('/')
            date = '/'.join((year, month, day))
            dates.append(date)
            quotes.append(float(parts[-1]))
    return dates, quotes


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


dates, quotes = read_quotes("djia.csv")

spans_stack = stack_stock_span(quotes)
print(spans_stack)
