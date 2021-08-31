from tkinter import *
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

root =Tk()
root.title('Where Is My Money Going?')
root.iconbitmap('money.ico')
root.geometry('400x300')

# Set background color for the root
root.configure(background='#450b70')

# Create label with a input for income, bills, and savings rate
income_label = Label(root, text='Enter your income: ', justify= LEFT, bg='#450b70', fg='white', font='Raleway')
bill_label = Label(root, text='Enter your total bills amount: ', justify= LEFT, bg='#450b70', fg='white', font='Raleway')
savings_label = Label(root, text='Enter your savings rate: ', justify= LEFT, bg='#450b70', fg='white', font='Raleway')

# Position labels on top of each other in a grid
income_label.grid(row=0, column=0, padx=24)
bill_label.grid(row=1, column=0, padx=24)
savings_label.grid(row=2, column=0, padx=24)

# Create entry boxes to accept the values you type
income_entry = Entry(root)
bill_entry = Entry(root)
savings_entry = Entry(root)

# Position entry boxes on grid
income_entry.grid(row=0, column=1, pady=8)
bill_entry.grid(row=1, column=1, pady=8)
savings_entry.grid(row=2, column=1, pady=8)

# Create function for button action
def buttonClick():
	income = int(income_entry.get())
	bills = int(bill_entry.get())
	savings = float(savings_entry.get())

	net_savings = (income - bills)*savings
	total_spend = bills + net_savings
	left_over = income - total_spend

	if left_over > 0:
		### Convert everything to lists
		income_list = [income]
		bill_list = [bills]
		net_savings_list = [net_savings]
		left_over_list = [left_over]

		### Create a dictionary with the new list variables
		dictionary = {'income':income_list, 'bills':bill_list, 'savings':net_savings_list, 'left_over':left_over_list}

		### Create dataframe from dictionary
		df = pd.DataFrame.from_dict(dictionary)

		labels = df.columns

		### Create Sankey plot to show where my money is going

		data=[go.Sankey(
		    node = dict(
		      pad = 15,
		      thickness = 15,
		      line = dict(color = 'white', width = 0.5),
		      label = labels,
		      color = 'white'),
		    link = dict(
		      source = [0, 0, 0], 
		      target = [1, 2, 3],
		      value = [df['bills'], df['savings'], df['left_over']],
		      color = '#cf9fe5'
		  ))]

		layout = go.Layout(title='Where is my money going?',
							font= dict(size=20, color='white'),
							plot_bgcolor='#450b70',
							paper_bgcolor='#450b70')

		fig = go.Figure(data=data, layout=layout)

		pyo.plot(fig, filename='money.html')
		
	else:
		nomoney_label = Label(root, text='Enter your income: ', justify= LEFT, bg='#450b70', fg='white', font='Raleway')
		nomoney_label.grid(row=4, column=0, columnspan=2, pady=8)

# Create a button to submit the user input
myButton = Button(root, text='Submit', command= buttonClick)

# Position the button at the bottm of the gui
myButton.grid(row=3, column=0, columnspan=2, pady=8)




# Create mainloop
root.mainloop()



