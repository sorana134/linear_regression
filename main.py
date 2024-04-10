import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
def main():
    data=pd.read_csv('real_estate_price_size (1).csv')
    result=data.describe()
    print(result)
    y=data['size']
    x1=data['price']
    plt.scatter(x1, y)
    plt.xlabel('price')
    plt.ylabel('size')

    x=sm.add_constant(x1)
    end=sm.OLS(y,x).fit()
    end=end.summary()
    print(end)
    yhat=0.0033*x1-122.3349
    fid=plt.plot(x1, yhat, lw=4, c='red')
    plt.show()



if __name__ == '__main__':
  main()