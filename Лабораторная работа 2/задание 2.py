salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
needed_capital = spend - salary
for i in range(months-1):
    spend *= 1 + increase
    needed_capital += spend - salary

    if needed_capital > 0:
        money_capital += needed_capital
        needed_capital = 0

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
