
stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 }
def fillable(stock, merch, n):
    # Your code goes here.
    if merch not in stock:
        return False
    if stock[merch] >= n and n >= 0:
        return True
    else:
        return False

print(fillable(stock,'football',1))