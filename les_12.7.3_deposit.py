per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("введите сумму"))
TKB, SKB, VTB, SBR = per_cent.values()
deposit = list(map(int, [TKB * money / 100, SKB * money / 100, VTB * money / 100, SBR * money / 100]))
print(deposit)
deposit_max = max(deposit)
print("Максимальная сумма, которую вы можете заработать —", deposit_max)
