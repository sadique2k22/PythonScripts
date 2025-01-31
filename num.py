def words_to_number(s):
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90
    }
    scale_map = {
        'hundred': 100,
        'thousand': 1_000,
        'million': 1_000_000,
        'billion': 1_000_000_000,
        'trillion': 1_000_000_000_000,
        'quadrillion': 1_000_000_000_000_000,
        'quintillion': 1_000_000_000_000_000_000,
        'sextillion': 1_000_000_000_000_000_000_000,
        'septillion': 1_000_000_000_000_000_000_000_000,
        'octillion': 1_000_000_000_000_000_000_000_000_000,
        'nonillion': 1_000_000_000_000_000_000_000_000_000_000,
        'decillion': 1_000_000_000_000_000_000_000_000_000_000_000,
        'undecillion': 10**36,
        'duodecillion': 10**39,
        'tredecillion': 10**42,
        'quattuordecillion': 10**45,
        'quindecillion': 10**48,
        'sexdecillion': 10**51,
        'septendecillion': 10**54,
        'octodecillion': 10**57,
        'novemdecillion': 10**60,
        'vigintillion': 10**63,
    }
    def parse_part(words):
        current = 0
        total_part = 0
        for word in words:
            if word == 'hundred':
                if current == 0:
                    current = 1
                total_part += current * 100
                current = 0
            else:
                current += number_map[word]
        total_part += current
        return total_part
    words = s.replace('-', ' ').lower().split()
    words = [word for word in words if word != 'and']
    total = 0
    current_group = []
    last_scale_value = 1 

    for word in words:
        if word in scale_map:
            scale_value = scale_map[word]
            if scale_value > last_scale_value:
                total += parse_part(current_group)
                total *= scale_value
                last_scale_value = scale_value
            else:
                total += parse_part(current_group) * scale_value
                last_scale_value = scale_value
            current_group = []
        else:
            current_group.append(word)
    total += parse_part(current_group)
    return total
while True:
    print(words_to_number(input("Enter a number name: ")))