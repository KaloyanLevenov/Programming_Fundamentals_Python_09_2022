country_names = input().split(', ')
capital_names = input().split(', ')
my_dict = dict(zip(country_names,capital_names))
for country, capital in my_dict.items():
    print(f"{country} -> {capital}")