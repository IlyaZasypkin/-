# Законы де Моргана
def law_of_demorgan_1(A, B):
    return not (A and B) == (not A) or (not B)

def law_of_demorgan_2(A, B):
    return not (A or B) == (not A) and (not B)

# Проверка законов для всех возможных значений A и B
for A in [True, False]:
    for B in [True, False]:
        print(f"A={A}, B={B}:")
        print(f"Закон 1: {law_of_demorgan_1(A, B)}")
        print(f"Закон 2: {law_of_demorgan_2(A, B)}")
