#!/usr/bin/python

import argparse

# PLAN
# Store 3 values
# FIRST:
# The price to hold (starting at index 0)
# SECOND:
# The 2nd price that will be compared to price 1 to see if it's going to yield a profit
# Third:
# The profit, initialized to 0 

# loop through array first time looking at initial price (i)
# loop through array again looking at subsequent prices to see the maximum profit (j)
# Once maximum profit is found, set that number to profit
# MUST BUY BEFORE YOU CAN SELL


def find_max_profit(prices):
  profit = 0
  for i in range(len(prices) -1 ):  # giving us indices in prices array 
    print(f'THIS IS I',i)
     # j is iterating through the array to 
    for j in range(i + 1, len(prices)):
      if prices[j] >= prices[i]:
        profit = prices[j] - prices[i]
        # set a max profit variable and compare it to profit if max profit is < then set profit to max profit
        print(f'Profit: ',profit)

    return profit

prices = [1050, 270, 1540, 3800, 2, 5000]
print(F"Max profit: ",find_max_profit(prices))



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))