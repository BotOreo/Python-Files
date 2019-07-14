import matplotlib.pyplot as plt

x=[15,5,5,8,11,15,19,22,25,25,15]
y=[3,15,20,22,22,20,22,22,20,15,3]
plt.plot (x,y, label='Mine, Python')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('You are')
plt.legend()
plt.show()