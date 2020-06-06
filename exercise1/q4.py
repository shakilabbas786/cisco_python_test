import matplotlib.pyplot as plt 
  
x1 = [5,3,7,5]  #triangle 1 
y1 = [5,3,3,5] 


x2 = [4,0.5]    #left line
y2 = [3,0.5]

x3 = [6, 9.5]  #right line
y3 = [3, 0.5]

x4 = [0, 2, -2, 0]     #triange 2
y4 = [1, -1, -1, 1]

x5 = [10, 12, 8, 10]     #triange 3
y5 = [1, -1, -1, 1]

x6 = [1.5, 8.5]  #bottom line
y6 = [-0.5, -0.5]

plt.plot(x1, y1, "k") 
plt.plot(x2, y2, "k") 
plt.plot(x3, y3, "k") 
plt.plot(x4, y4, "k") 
plt.plot(x5, y5, "k") 
plt.plot(x6, y6, "k") 


plt.title('My first graph!') 
  
plt.show()
