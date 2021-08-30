## wheres-my-money-going.py
A python project that visualizes income against bills, savings, and free cash.

Inspiration for this tool:
I do this often in excel. 
I wanted a quicker way to calculate how much free cash I will have for a pay period to help me plan purchases in between paychecks.

Packages required:
tkinter,
pandas,
plotly.graph_objs

I wanted to visualize where my money was going by aggregating cash outflows into three buckets: Bills, Savings, and Free Cash

When running this program a GUI window will pop-up with three input fields:

Enter income: (Enter your income)
Enter total bills amount: (Enter the total of all your bills for the period)
Enter savings rate: (Enter the amount of post-bill savings you would like to save as a float between 0-1)

Hitting Submit will take in your variables and generate a Sankey graph with Plotly.

The graph will visualize the where your money is going this period.
