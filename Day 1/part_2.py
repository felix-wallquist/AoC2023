import re
digit_conversion_dict = {"one": "1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
digits_and_words = list(digit_conversion_dict.keys()) + ["1","2","3","4","5","6","7","8","9"]
sum = 0
with open("input.txt") as input:
    for line in input:
        extracted = re.findall(r"(?=("+'|'.join(digits_and_words)+r"))", line)
        for i in range(0, len(extracted)):
            if extracted[i] in list(digit_conversion_dict.keys()):
                extracted[i] = digit_conversion_dict.get(extracted[i])
        sum += int(''.join([[i for i in extracted][i] for i in (0, -1)]))
print(sum)