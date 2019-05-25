try:
    counter = 1
    while (counter >= 1):
        number = 2.0 ** counter
        counter = counter + 0.001

except OverflowError:
    print(counter, "to big to be stored in memory")

except KeyboardInterrupt:
    print("User stopped program when 'counter' was at", counter)

