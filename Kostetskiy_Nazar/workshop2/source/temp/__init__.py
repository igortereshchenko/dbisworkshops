def f(x):
    x1, x2 = x
    print(x)
    return 2*((x1-11)**2) + x1*x2 + 6*x2**2

# x1 = (17.2, 17.2-15.8141)
# res = f(x1)
# print(res)
#
# print(-17.0348-8*2.4324)


if __name__ == '__main__':
    # interval = [-18.2475, -15.841]
    # eps = 0.2
    #
    # # while interval[0]-interval[1] < eps:
    # for i in range(10):
    #     medLabmda = (interval[0] + interval[1])/2
    #     print('MediumLambda: ', medLabmda)
    #     rightLambda = (interval[1] + medLabmda)/2
    #     print('rightLambda: ', rightLambda)
    #     leftLambda = (interval[0] + medLabmda)/2
    #     print('leftLambda: ', leftLambda)
    #     interval = leftLambda, rightLambda
    #     print('fl ', f((17.2, 17.2-leftLambda)))
    #     print('fr ', f((17.2,  17.2-rightLambda)))
    x1 = (17.2-5.98055, 0.1558)
    res = f(x1)
    print(res)

