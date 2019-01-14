'''

1 * 1 = 1
1 * 2 = 2   2 * 2 =  4
1 * 3 = 3   2 * 3 =  6   3 * 3 =  9
1 * 4 = 4   2 * 4 =  8   3 * 4 = 12   4 * 4 = 16
1 * 5 = 5   2 * 5 = 10   3 * 5 = 15   4 * 5 = 20   5 * 5 = 25
1 * 6 = 6   2 * 6 = 12   3 * 6 = 18   4 * 6 = 24   5 * 6 = 30   6 * 6 = 36
1 * 7 = 7   2 * 7 = 14   3 * 7 = 21   4 * 7 = 28   5 * 7 = 35   6 * 7 = 42   7 * 7 = 49
1 * 8 = 8   2 * 8 = 16   3 * 8 = 24   4 * 8 = 32   5 * 8 = 40   6 * 8 = 48   7 * 8 = 56   8 * 8 = 64
1 * 9 = 9   2 * 9 = 18   3 * 9 = 27   4 * 9 = 36   5 * 9 = 45   6 * 9 = 54   7 * 9 = 63   8 * 9 = 72  9 * 9 = 81

          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
     1 5 10 10 5 1
    1 6 15 20 15 6 1
   1 7 21 35 35 21 7 1
  1 8 28 56 70 56 28 8 1
 1 9 36 84 126 126 84 36 9 1

'''


def ninenine():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%s * %s = %s' % (i, j, i * j), end='\t')
        print()


def yanghui(n):
    nums = []
    for i in range(n):
        if not i:
            nums.append([1])
        else:
            new_list = [1]
            for k, v in enumerate(nums[i - 1]):
                if k < i - 1:
                    new_list.append(nums[i - 1][k] + nums[i - 1][k + 1])
                else:
                    new_list.append(v)
            nums.append(new_list)
    # print(nums)
    for i in range(n):
        for j in range(n - i - 1):
            print('\t', end='')
        for k in nums[i]:
            print(k, end='\t\t')
        print()
        print()


# yanghui(13)

def dengbian(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(' ', end='')
        for k in range(i):
            print('* ', end='')
        print()


# dengbian(10)

def dengbian2(n, ch):
    for i in range(1, n + 1):
        if i == n:
            print((ch + ' ') * n)
            break
        print(' ' * (n - i), end='')
        if i == 1:
            print(ch)
            continue
        print(ch, end='')
        print(' ' * (2 * i - 3), end='')
        print(ch)


def read_result():
    M = 5
    a = [1, 2, 3, 4, 5]
    i = 0
    j = M - 1
    while i < M:
        a[i], a[j] = a[j], a[i]
        print(a)
        i += 1
        j -= 1
    for i in range(5):
        print(a[i])


# dengbian2(10, '\\')
# dengbian2(15, '/')
read_result()
