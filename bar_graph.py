import matplotlib.pyplot as plt
state=['panjab','haryana','up','mp','bihar','keral']
area=[220,120,100,40,80,30]
cl=['red','green','blue','brown','yellow','orange']
plt.bar(state , area , color=cl,edgecolor='yellow')
plt.xlabel('state')
plt.ylabel('area')
plt.title('Area of wheat cultivation')
plt.show()
