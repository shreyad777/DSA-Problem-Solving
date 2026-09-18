class StockSpanner:
    def __init__(self):
        self.stack = []
    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            previous_price, previous_span = self.stack.pop()
            span += previous_span
        self.stack.append((price, span))
        return span


prices = list(
    map(int, input("Enter stock prices: ").split())
)

spanner = StockSpanner()

result = []

for price in prices:
    result.append(spanner.next(price))

print("Stock Spans:", result)