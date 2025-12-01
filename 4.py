starting_number_of_organisms = int(input("Введите стартовое количество организмов"))
average_daily_percentage_increase = input("Введите среднесуточное увеличение в процентах")
number_of_days_for_breeding = int(input("Введите количество дней для размножения"))
population_size = starting_number_of_organisms
for i in range (1, number_of_days_for_breeding+1):
    population_size += population_size*float(f"0.{average_daily_percentage_increase}")
    print(f"номер дня {i} размер популяции {population_size}")
