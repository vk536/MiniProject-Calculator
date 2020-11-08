from Calculator.Square import square
from Calculator.Division import division
from Statistics.PopulationMean import populationmean


def samplevariance(num):
    try:
        pop_mean = populationmean(num)
        num_values = len(num)
        x = 0
        for i in num:
            x = x + square(i - pop_mean)
        return round(division(x, num_values), 7)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")
