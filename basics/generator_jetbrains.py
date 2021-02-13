n = int(input())


def even(n):
    for i in range(n+1):
        if not i%2:
            yield i

for i in even(n):
	print(i)


# Don't forget to print out the first n numbers one by one here

