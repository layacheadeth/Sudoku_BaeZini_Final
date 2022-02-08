from dokusan import generators
import numpy as np

def generate_soduku():
    arr=np.array(list(str(generators.random_sudoku(avg_rank=150))))
    answer=arr.reshape(9,9)
    real_answer=answer.tolist()
    new_list = [[int(x) for x in lst] for lst in real_answer]

    print(new_list)
    return new_list

# generate_soduku()

