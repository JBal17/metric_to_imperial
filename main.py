from imp_dict import imperial_fractions

while True:
    metric_size = input("Please input a value (in mm) to convert to imperial: ")  # take input, check it is a number

    try:
        metric_size = float(metric_size)
    except:
        print('Please use digits for metric value')

    imperial_size = metric_size / 25.4  # convert metric to imperial

    imperial_int = int(imperial_size)

    imperial_decimal = imperial_size - imperial_int

    closest_decimal = ""
    closest_counter = 1
    for key in imperial_fractions.keys():
        diff = abs(imperial_decimal - float(key))
        if diff < closest_counter:
            closest_decimal = key
            closest_counter = diff

    converted_size_imperial = imperial_int + closest_decimal
    converted_size_metric = converted_size_imperial * 25.4

    converted_difference = round((converted_size_metric - metric_size),4)


    print(f"The converted value is {imperial_int} {imperial_fractions[closest_decimal]} in"
          f"\nThe difference between input value and converted value is {converted_difference}mm"
          f"\n")