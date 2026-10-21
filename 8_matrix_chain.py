
def matrix_chain_order(dims):
    # Number of matrices
    n = len(dims) - 1

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for chain_len in range(2, n + 1):
        for i in range(1, n - chain_len + 2):
            j = i + chain_len - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j]
                        + dims[i - 1] * dims[k] * dims[j])

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]


if __name__ == "__main__":
    dims = [10, 30, 5, 60]

    min_cost = matrix_chain_order(dims)

    print("Matrix dimensions:", dims)
    print("Minimum multiplication cost:", min_cost)
