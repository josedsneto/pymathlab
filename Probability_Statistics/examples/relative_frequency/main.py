'''This code tests the relative frequency of occurence of
   a choosen number in the range of 0 to 9. The results
   aims to show that the mean of relative frequency converges
   to a constant number in the order of 0.1'''

import matplotlib.pyplot as plt
import numpy as np

class RelativeFrequency:
    def __init__(self, Na):
        self.Na = Na

    def check_equals(self, number):
        return True if self.Na == number else False

    def calculate_frequency(self, corrects, trials):
        return corrects / trials

if __name__=='__main__':
    trials = 10000 
    freq_target = RelativeFrequency(Na=1)
    corrects = 0
    n_mean = []

    for n in range(trials):
        random_number = np.random.randint(10)
        
        if freq_target.check_equals(random_number):
            corrects += 1
        
        frequency = freq_target.calculate_frequency(corrects,n+1)
        n_mean.append(frequency)

    plt.plot(range(trials), n_mean)
    plt.title('Relative frequency through trials')
    #plt.figure(figsize=(10,5))
    plt.savefig('results.png')
