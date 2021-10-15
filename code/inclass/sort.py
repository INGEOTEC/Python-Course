def bubble(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp
    return numbers

if __name__ == '__main__':
    print(bubble([4, 3]))    