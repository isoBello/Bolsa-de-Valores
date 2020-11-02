# -*- coding: utf-8 -*-
dias = 0
taxa = 0
cotacoes = []
dp = [[]]


def bolsa():
    a = b = -1
    dp[dias][0] = dp[dias][1] = 0

    for i in range(dias-1, -1, -1):
        for j in range(len(dp[i])):
            if dp[i][j] == 1:
                x = cotacoes[i]
            else:
                x = -(cotacoes[i] + taxa)
            dp[i][j] = max((x + dp[i + 1][~j]), dp[i + 1][j])
    return dp[0][0]


def main():
    global dias, taxa, cotacoes, dp
    dias, taxa = map(int, input().split(" "))
    cotacoes = list(map(int, input().split(" ")))
    dp = [[-1 for i in range(2)] for j in range(dias + 1)]

    print(bolsa())


if __name__ == "__main__":
    main()
