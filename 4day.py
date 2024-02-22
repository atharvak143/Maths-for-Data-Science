# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:06:55 2023

@author: Pradip
"""

#write a Python program to draw a line with a suitable label
import matplotlib.pyplot as plt
X=range(1,50)
Y=[value*3 for value in X]
print("value of X:")
print(*range(1,50))

'''
this is equivalent to -
i in range(1,50):
    print(i,end="")
'''
print("Value of Y (thrice of X):")
print(Y)
#plot lines and/or markers to the Axes
plt.plot(X,Y)
#set the x-axis label of the current axis.
plt.xlabel('X-axis')
#set the y axis label of the current axis
plt.ylabel('Y-axis')
#set a title
plt.title('Draw a line.')
#display the figure
plt.show()

#######################################################

#using given axis values with suitable
#label in the x-axis , y axis and a title

import matplotlib.pyplot as plt
#x axis values
x=[1,2,3]
#y axis values
y=[2,4,1]
#plot lines and/or markers to the Axes
plt.plot(x,y)
#set the x-axis label of the current axis.
plt.xlabel('X-axis')
#set the y axis label of the current axis
plt.ylabel('Y-axis')
#set a title
plt.title('Sample graph.')
#display the figure
plt.show()

####################################################

#write python program to plot two or more lines 
#on same plot with suitable legends of each line
import matplotlib.pyplot as plt
#line no 1
x1=[10,20,30]
y1=[20,40,10]

#line no2
x2=[10,20,30]
y2=[40,10,30]

#plotting the line 1 points
plt.plot(x1,y1,label="Line1")
#plotting the line 2 points
plt.plot(x2,y2,label="Line2")
plt.xlabel('x-axis')
#set the y-axis label of the current axis
plt.ylabel('y-axis')
plt.title('two or more lines on same plot with suitable legends')
#show a legend on the plot
plt.legend()
#display a figure
plt.show()

###################################################

#write python program to plot two or more lines 
#lines with different legends, different width and colors
import matplotlib.pyplot as plt
#line no 1
x1=[10,20,30]
y1=[20,40,10]

#line no2
x2=[10,20,30]
y2=[40,10,30]

#set the x-axis label of the current axis.
plt.xlabel('X-axis')
#set the y axis label of the current axis
plt.ylabel('Y-axis')

# set a title
plt.title('two or more lines with differnt width and colours with legends ')
#display the figure
plt.plot(x1,y1, color='blue',linewidth=3,label='line1-width-3')
plt.plot(x2,y2, color='red',linewidth=5,label='line1-width-5')

plt.legend()
plt.show()

####################################################

#write python program to plot two or more lines 
#with different styles

import matplotlib.pyplot as plt
#line no 1
x1=[10,20,30]
y1=[20,40,10]

#line no2
x2=[10,20,30]
y2=[40,10,30]

#set the x-axis label of the current axis.
plt.xlabel('X-axis')
#set the y axis label of the current axis
plt.ylabel('Y-axis')

# set a title
plt.title('two or more lines with diff styles: ')
#display the figure
plt.plot(x1,y1, color='blue',linewidth=3,label='line1-width-3',linestyle='dotted')
plt.plot(x2,y2, color='red',linewidth=5,label='line1-width-5',linestyle='dashed')

plt.legend()
plt.show()

###########################################################

#set the lines markers
#x axis values
x=[1,4,5,6,7]
#y axis vales
y=[2,6,3,6,3]
#plotting the points
plt.plot(x,y, color='red',linewidth=3,label='line1-width-3',linestyle='dashdot',marker='o',markerfacecolor='blue',markersize=12)
plt.ylim(1,8)
plt.ylim(1,8)

#set the x-axis label of the current axis.
plt.xlabel('X-axis')
#set the y axis label of the current axis
plt.ylabel('Y-axis')

plt.legend()
plt.show()

##################################################

#write a python programming to display
#bar  charts of the popularity of programming languages
x=['java','python','PHP','Javascript','C#','c++']
popularity=[22.2,19.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("popularity of programming languages\n"+"Worldwide:")
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

##################################################

# horizontal graph
import matplotlib.pyplot as plt
x=['java','python','PHP','Javascript','C#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.barh(x_pos,popularity,color='green')
plt.ylabel('Languages')
plt.xlabel('Popularity')
plt.title("popularity of programming languages\n"+"Worldwide:")
plt.yticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

##################################################

#use unicorn color
import matplotlib.pyplot as plt
x=['java','python','PHP','Javascript','C#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]

plt.bar(x_pos,popularity,color=(0.4,0.6,0.8,1.0))
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("popularity of programming languages\n"+"Worldwide:")
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

###################################################

#use different cokors to each bar
import matplotlib.pyplot as plt
x=['java','python','PHP','Javascript','C#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color=('red','black','green','blue','orange','yellow'))
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("popularity of programming languages\n"+"Worldwide:")
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

###################################################

# 















