import pandas as pd
import numpy as np
from scipy.stats import permutation_test


chat_id = 230790372 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05

    def statistic(x, y, axis):
        return np.mean(x, axis=axis) - np.mean(y, axis=axis)

    pvalue = permutation_test([x, y], statistic, alternative='less').pvalue

    if pvalue <= alpha:
        is_rejected = True
    else:
        is_rejected = False

    return is_rejected
