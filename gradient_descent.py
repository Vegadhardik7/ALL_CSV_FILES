import numpy as np
def gradient_descent(x,y):
    m_curr = 0                                                   # m in y = m*x+b
    b_curr = 0                                                   # b in y = m*x+b
    iterations = 10000
    n = len(x)
    learning_rate = 0.08
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr                        # y=m*x+b
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])  # formula 1

        md = -(2/n)*sum(x*(y-y_predicted))                       # formula 2
        bd = -(2/n)*sum(y-y_predicted)                           # formula 3

        m_curr = m_curr - learning_rate * md                     # formula 4(for steps)
        b_curr = b_curr - learning_rate * bd                     # formula 5(for steps)

        print("m{},b{},cost{} iteration{}".format(m_curr,b_curr,cost,i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)
