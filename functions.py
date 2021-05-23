from imp_dict import imperial_fractions

def metric_to_imperial(metric_size):
    while True:
        try:
            metric_size = float(metric_size)
        except:
            return('Please use digits')

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

        converted_answer = (str(imperial_int) + " " + str(imperial_fractions[closest_decimal]))

        return converted_answer

def converted_difference(metric_size):
    while True:
        try:
            metric_size = float(metric_size)
        except:
            pass

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

        return str(converted_difference) + 'mm'