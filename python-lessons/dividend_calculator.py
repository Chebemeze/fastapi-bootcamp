# dividend_calculator.py
from multiprocessing import Pool

def sum_res(receipt):
    return sum(i*i for i in range(receipt))

if __name__== "__main__":
    thousand = [1000, 2000, 3000, 4000]
    with Pool(processes=4) as pool:
        results = pool.map(sum_res, thousand)
        print(results)
