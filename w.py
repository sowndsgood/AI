w1 = w2 = 10
x=[1,2,3,4,5,6,7]
y=[2,3,4,5,6,7,8]
for i in range(25):
    Err_w1 = Err_w2 = []
   
    for a in range(len(x)):
        Err_w1.append(2*x[a]*(w1*x[a]+w2-y[a]))
        Err_w2.append(2*(w1*x[a]+w2-y[a]))
    w1 = w1 - (0.1*sum(Err_w1)/len(Err_w1))
    w2 = w2 - (0.1*sum(Err_w2)/len(Err_w2))

print(w1,w2)

