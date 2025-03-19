"""
If the entries of a 3 by 3 matrix are chosen randomly between O and 1, what are the
most likely dimensions of the four subspaces?
"""

from tqdm import tqdm
import numpy as np
import time
import matplotlib.pyplot as plt


def check_full_rank_square_binary(m, num_of_instance):
    start_time = time.time()
    full_rank_count = 0
    for ii in tqdm(range(0, num_of_instance)):
        A = np.random.randint(2, size=(4, m))
        rank_A = np.linalg.matrix_rank(A)
        if rank_A == m:
            full_rank_count += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    return (full_rank_count / num_of_instance) * 100, elapsed_time, A


my_prop = []
master_start_time = time.time()
for i in range(1, 6):
    probability, my_elapsed_time, my_A = check_full_rank_square_binary(i, 100000)
    print()
    print("-" * 50)
    # print(f"Sample matrix A: {my_A}")
    print(f"probability of {i} by {i} matrix being full rank: {round(probability, 2)}%, elapsed time: {my_elapsed_time}")
    print("-" * 50)
    print()
    my_prop.append(probability)
master_end_time = time.time() - master_start_time
print(f"Calculation finished: total runtime:{master_end_time}")

my_prop_round = []
my_prop_round.extend(map(lambda x: round(x, 2), my_prop))
print(my_prop_round)

X = np.array(my_prop_round)
Y = np.arange(1, 6)
plt.bar(Y, X, width=0.6, align='center')
plt.xlabel('value of n')
plt.ylabel('Probability')
plt.title('Probability of Full column rank with fixed m and increasing n')
plt.show()






