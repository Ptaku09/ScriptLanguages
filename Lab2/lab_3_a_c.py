from lab_3_a import count_res_code_freq


def count_404s():
    frequency = count_res_code_freq(404)
    print(frequency)


if __name__ == '__main__':
    count_404s()
