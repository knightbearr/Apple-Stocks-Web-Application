# Import Section:
# ---------------------------------------------------
# Import the module that important for this Analysis,
# streamlit module
# pandas library for preparing the data
# numpy for calculating some number or data
# and of course some modules for visualization
# ---------------------------------------------------

# Streamlit import
import streamlit as st

# Data and Computation Preparing
import pandas as pd
import numpy as np

# Visualization
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# Filter
import warnings
warnings.simplefilter('ignore')

# set up

# Streamlit Set Up
st.set_option('deprecation.showPyplotGlobalUse', False)

# Seaborn Set Up
sns.set_style('white')
sns.set_context('paper', font_scale=1.5)

# Matplotlib Set Up
plt.style.use('fivethirtyeight')

# Pandas Set Up
pd.set_option('display.width', 100)
pd.set_option('display.max_rows', 25)
pd.set_option('display.max_columns', 25)

# Container Section:
# ---------------------------------------------------
# Header Section:

# - Heading
# - Greetings
# - About

# Body Section:

# - Seeing Data
# - Visualization
# - Opinion

# Footer Section:

# - Conclusion
# - Prediction
# - Closing
# ---------------------------------------------------

HEADER = st.beta_container() # Header
BODY = st.beta_container() # Body
FOOTER = st.beta_container() # Footer

# Function Section

def plot_timeseries(data, label_1, label_2, col, title):

	"""
	Function That Returning Time Series Visualization
		
	Examples:

	data = put your data here
	label_1 = put your label or `label that you want to plot`
	label_2 = same like label_1
	col = column that we want to use for our Time Series
	title = 'Time Series for Data ....'

	"""
	  	
	# Figuring the size
	plt.figure(
		figsize=(20, 10)
		)
	    
	# Create a lineplot for data 1
	sns.lineplot(
		data=data,
	  	label=label_1,
	  	legend=False
	  	)
	    
	# Create a lineplot for data 2
	sns.lineplot(
		data=apple_data[col],
	  	label=label_2,
	  	legend=False
	  	)
	    
	# Create a title
	plt.title(title)
	    
	# Show the legend
	plt.legend()
	    
	# Show the plot
	plt.show()

def timeseries_lagplot(data):

	"""
	Function That Returning Time Series Lag Plot Visualization

	Examples:

	data = put your data here (data['Banana'])

	"""
	pd.plotting.lag_plot(data)

	plt.show()


def clustermap_visualization(data):

	"""
	Function that returning Clustermap Visualization

	Examples:

	data = data
	cmap = default
	standard_scale = default

	"""

	sns.clustermap(
		data,
		cmap='Blues',
		standard_scale=1
				)

	plt.show()

def subplots_visualization(data, subplots=True):

	"""
	Function that returning Subplots Visualization

	Examples:

	data = data
	subplots = False/True

	"""

	data.plot(
		subplots=True,
		figsize=(20, 12)
		)

	plt.show()

# Prepare the Data

# - Load the dataset and accomodate it to new
#   variable
# - Convert Date column to Timestamp
# - Del Adj Column
# - Set Date col into index
# - And Prepare the Date for Visualization

# Load the Data
apple_data = pd.read_csv('data/AAPL.csv')

# Convert Date Column into Timestamp
apple_data['Date'] = pd.to_datetime(apple_data['Date'])

# Delete Adj Close Column
del apple_data['Adj Close']

# Set the Date Col into Index
apple_data.set_index('Date', inplace=True)

# Data without Volume and Data with Volume
data_without_volume = apple_data.drop(columns=['Volume'])
volume = apple_data['Volume']

# Header Section:
with HEADER:

	#============================================================ |Set the title|
	st.title('**Apple Stock Analysis - Knightbearr**')

	#============================================================ |Set the Image|
	st.image('picture/apple_logo.jpg')

	#============================================================ |Text Greeting|
	st.subheader("**Hi! Welcome!**")

	#============================================================ |About|
	st.markdown("In this project, I'll make **Apple Stock Analysis \
				 with Visualization**, hopefully you guys like it! \
				 owh yes, sorry if my English is bad, hopefully you can \
				 understand what I'm explained to you! and, if you \
				 want to get the **Data** or the **Source Code**, you can check it \
				 out in my Github Repositories, Thanks in Advance!")

	#============================================================ |Explanation| 
	st.markdown("And, before we move on to Analysis and Visualization, I'll \
				 give you guys a quick Explanation about, what is Open Stock, \
				 High Stock, Low Stock, etc.")

	#============================================================ |Open|
	st.markdown("* **Open:** \
				     The Open is the starting period \
					 of trading on a securities exchange \
					 or organized over-the-counter market. ")

	#============================================================ |High|
	st.markdown("* **High:** \
				     The High is the highest price at which \
					 a stock traded during the course of the \
					 trading day and is typically higher than \
					 the closing or equal to the opening price. ")

	#============================================================ |Low| 
	st.markdown("* **Low:** \
				     The Low is typically lower than the opening  \
					 or closing price, as it is unusual that the \
					 lowest price of the day would happen to occur \
					 at those particular moments.")

	#============================================================ |Close| 
	st.markdown("* **Close:** \
				     The Close is the closing price generally \
					 refers to the last price at which a stock \
					 trades during a regular trading session.")

	#============================================================ |Volume| 
	st.markdown("* **Volume:** \
				     The Volume can be an indicator of market \
					 strength, as rising markets on increasing \
					 volume are typically viewed as strong and \
					 healthy.")

# Body Section
with BODY:

	#============================================================ |Set the Sub Header|
	st.subheader("**Let's see the Data**")

	#============================================================ |Seeing Data|
	st.markdown("*Data Without Volume:*")
	st.write(data_without_volume)

	st.markdown("*Data Volume:*")
	st.write(volume)

	st.markdown("As we can see above, the data is ready to \
				 Visualize and the Date Column is now in the **Index** \
				 and the type is **Timestamp**.")

	st.subheader("Let's see the Max and Min Value in every columns")

	st.markdown("* **Open:**")
	st.markdown(f"Max Value of Open: `{apple_data['Open'].max()}`")
	st.markdown(f"Min Value of Open: `{apple_data['Open'].min()}`")

	st.markdown("* **High:**")
	st.markdown(f"Max Value of High: `{apple_data['High'].max()}`")
	st.markdown(f"Min Value of High: `{apple_data['High'].min()}`")

	st.markdown("* **Low:**")
	st.markdown(f"Max Value of Low: `{apple_data['Low'].max()}`")
	st.markdown(f"Min Value of Low: `{apple_data['Low'].min()}`")

	st.markdown("* **Close:**")
	st.markdown(f"Max Value of Close: `{apple_data['Close'].max()}`")
	st.markdown(f"Min Value of Close: `{apple_data['Close'].min()}`")

	st.markdown("* **Volume:**")
	st.markdown(f"Max Value of Volume: `{apple_data['Volume'].max()}`")
	st.markdown(f"Min Value of Volume: `{apple_data['Volume'].min()}`")

	#============================================================ |Set the Title|
	st.title("**And now, Let's Visualize the Data!**")

	#============================================================ |Cluster Map Visualization|
	st.subheader("**Cluster Map Visualization**")
	st.pyplot(clustermap_visualization(apple_data))

	#============================================================ |Subplots Visualization|
	st.subheader("**Subplots Visualization**")
	st.pyplot(subplots_visualization(apple_data))

	st.markdown("> **Conclusion:**")
	st.markdown("Okay great, Every Open, High, Low, and Close in 2020 to 2021 stock \
				 are Have the most increasing, but volume are decreasing.")

	#============================================================ |Set the Title|
	st.title("**Analysis on Open, High, Low, and Close from 1980 - Current Year**")

	#============================================================ |Apple Stock in 1980 - 2000|
	st.subheader("**1. Apple Stock in 1980 - 2000**")
	st.line_chart(data_without_volume.loc['1980-12-12':'2000-12-31'])
	st.markdown("> **Conclusion:**")
	st.markdown("Stocks up and down are clearly visible here, where there \
				 is a good increase in 1983 to 1986, and ups and down in \
				 1988 to 1996 and there is a very drastic increase in the \
				 year of 1998 to 2000 but there's very drastic decline \
				 to, in the middle of 2000.")

	#============================================================ |Apple Stock in 2001 - 2010|
	st.subheader("**2. Apple Stock in 2001 - 2010**")
	st.line_chart(data_without_volume.loc['2001-01-01':'2010-12-31'])
	st.markdown("> **Conclusion:**")
	st.markdown("Okay, as we can see in the visualization above, there's \
				 no significant increase or decreasing stocks in 2001 - 2004, \
				 and there we can see in 2005 start to increase stock until 2011.")

	#============================================================ |Apple Stock in 2010 - Current Year|
	st.subheader("**3. Apple Stock in 2010 - Current Year**")
	st.line_chart(data_without_volume.loc['2011-01-01':])
	st.markdown("> **Conclusion:**")
	st.markdown("Okay, it looks like there are a few similarities between the increase \
				 and decrease in stock in the year 2010 - 2011, as we can see in \
				 the visualization above, there's no significant increase or decreasing \
				 stocks in 2012 - 2016, and there we can see in the 2017 start to \
				 increase stock until now.")

	#============================================================ |Overall Apple Stocks|
	st.subheader("**4. Overall Apple Stock Data**")
	st.line_chart(data_without_volume)
	st.markdown("> **Conclusion:**")
	st.markdown("Okay, as we can see in the visualization above, there's no significant \
				 increase or decreasing stocks in 1980 - 2005, and there we can see in the \
				 2006 start to increase stock until now,  \
				 Good Job Steve Jobs, but. Let's see the Volume.")

	#============================================================ |Set the Title|
	st.title("**Analysis on Volume 1980 - Current Year**") 

	#============================================================ |Apple Volume in 1980 - 2000|
	st.subheader("**1. Apple Volume in 1980 - 2000**")
	st.line_chart(volume.loc['1980-12-12':'2000-12-31'])
	st.markdown("> **Conclusion:**")
	st.markdown("There are various increases and decreases from the volume data above.")

	#============================================================ |Apple Volume in 2001 - 2010|
	st.subheader("**2. Apple Volume in 2001 - 2010**")
	st.line_chart(volume.loc['2001-01-01':'2010-12-31'])
	st.markdown("> **Conclusion:**")
	st.markdown("Volume ups and downs are clearly visible here, where there is a good increase \
				 in months 2001 to 2009, and there is a very drastic decline in the last month of 2011.")

	#============================================================ |Apple Volume in 2010 - Current Year|
	st.subheader("**3. Apple Volume in 2011 - Current Year**")
	st.line_chart(volume.loc['2011-01-01':])
	st.markdown("> **Conclusion:**")
	st.markdown("Wow, what's happened Mr Apple? the Volume reduction is \
				 very significant from 2014 - Now.")

	#============================================================ |Apple Volume in 2010 - Current Year|
	st.subheader("**4. Okay Let's see Apple Volume Overall Data**")
	st.line_chart(volume)
	st.markdown("> **Conclusion:**")
	st.markdown("There was a modest increase in Volume from 1980 to 1998 and a large \
				 increase in Volume from 1999 to early 2011 and a decline in 2012 until now.")

	#============================================================ |Set the Title|
	st.title("**Let's Try the Area Plots**")

	#============================================================ |Area Plots 1|
	st.subheader("**Apple Stock (Open and High) with Area Plot Visualization 1980 - 2010**")

	st.area_chart(data_without_volume.loc['1980-12-12':'2010-01-01', ['Open', 'High']])

	#============================================================ |Area Plots 2|
	st.subheader("**Apple Stock (Low and Close) with Area Plot Visualization 1980 - 2010**")

	st.area_chart(data_without_volume.loc['1980-12-12':'2010-01-01', ['Low', 'Close']])

	#============================================================ |Area Plots 3|
	st.subheader("**Apple Stock (Open and High) with Area Plot Visualization 2011 - Current Year**")

	st.area_chart(data_without_volume.loc['2011-01-01':, ['Open', 'High']])

	#============================================================ |Area Plots 4|
	st.subheader("**Apple Stock (Low and Close) with Area Plot Visualization 2011 - Current Year**")

	st.area_chart(data_without_volume.loc['2011-01-01':, ['Low', 'Close']])

	#============================================================ |Area Plots 5|
	st.subheader("**Apple Volume Stock with Area Plot Visualization 1980 - 2010**")

	st.area_chart(volume.loc['1980-12-12':'2010-01-01'])

	#============================================================ |Area Plots 6|
	st.subheader("**Apple Volume Stock with Area Plot Visualization 1980 - 2010**")

	st.area_chart(volume.loc['2011-01-01':])

	#============================================================ |Set the Title|
	st.title("**Time Series Analysis on Open, Closing, and Volume Stock**")

	#============================================================ |Preparing the Data|
	open_stock = apple_data[['Open']]
	close_stock = apple_data[['Close']]
	volume_stock = apple_data[['Volume']]

	#============================================================ |Simple Moving Average|
	st.markdown("> **Simple Moving Average**")
	st.markdown("A Simple Moving Average (SMA) is an arithmetic moving calculated by \
				 adding recent prices and then dividing that figure by the number of time \
				 periods in the calculation average.")

	#============================================================ |Open Stock|
	st.subheader("**1. Open Stock**")

	# Prepare the data
	simple_moving_average_open_stock = open_stock.rolling(window=30).mean()

	st.pyplot(plot_timeseries(
			simple_moving_average_open_stock,
			'Moving Average',
			'Actual',
			'Open',
			'Open Stock Moving Average'			
		))

	#============================================================ |Close Stock|
	st.subheader("**2. Close Stock**")

	# Prepare the data
	simple_moving_average_close_stock = close_stock.rolling(window=30).mean()

	st.pyplot(plot_timeseries(
			simple_moving_average_close_stock,
			'Moving Average',
			'Actual',
			'Close',
			'Close Stock Moving Average'			
		))

	#============================================================ |Volume Stock|
	st.subheader("**3. Volume Stock**")

	# Prepare the data
	simple_moving_average_volume_stock = volume.rolling(window=30).mean()

	st.pyplot(plot_timeseries(
			simple_moving_average_volume_stock,
			'Moving Average',
			'Actual',
			'Volume',
			'Volume Stock Moving Average'			
		))

	#============================================================ |Weighted Moving Average|
	st.markdown("> **Weighted Moving Average**")
	st.markdown("A Weighted Moving Average puts more weight on recent data and \
				 less on past data. This is done by multiplying each bar's price \
				 by a weighting factor. Because of its unique calculation, WMA will \
				 follow prices more closely than a crresponding Simple Moving Average.")

	#============================================================ |Prepare the Data|
	weights = np.arange(1, 51)
	
	#============================================================ |Open Stock|
	st.subheader("**1. Open Stock**")

	# Prepare the data
	open_MV = apple_data['Open'].rolling(50).apply(lambda close: np.dot(close, weights)/weights.sum(),
		      raw=True)

	st.pyplot(plot_timeseries(
			open_MV,
			'Weighted Moving Average',
			'Actual',
			'Open',
			'Open Stock Weighted Moving Average'			
		))

	#============================================================ |Close Stock|
	st.subheader("**2. Close Stock**")

	# Prepare the data
	close_MV = apple_data['Close'].rolling(50).apply(lambda close: np.dot(close, weights)/weights.sum(),
		       raw=True)

	st.pyplot(plot_timeseries(
			close_MV,
			'Weighted Moving Average',
			'Actual',
			'Close',
			'Close Stock Weighted Moving Average'			
		))
	
	#============================================================ |Volume Stock|
	st.subheader("**3. Volume Stock**")

	# Prepare the data
	volume_MV = apple_data['Volume'].rolling(50).apply(lambda close: np.dot(close, weights)/weights.sum(),
		      	raw=True)

	st.pyplot(plot_timeseries(
			volume_MV,
			'Weighted Moving Average',
			'Actual',
			'Volume',
			'Volume Stock Weighted Moving Average'			
		))
	
	#============================================================ |Exponential Moving Average|
	st.markdown("> **Exponential Moving Average**")
	st.markdown("The Exponential Moving Average (EMA) is a technical chart that tracks \
		         the price of an investment (like a stock or commodity) over time. \
		         The EMA is a type of Weighted Moving Average (WMA) that gives more \
		         weighting or importance to recent price data.")

	#============================================================ |Open Stock|
	st.subheader("**1. Open Stock**")

	# Prepare the data
	expo_mv_open = apple_data['Open'].ewm(
										span=50,
										adjust=False).mean()

	st.pyplot(plot_timeseries(
			expo_mv_open,
			'Exponential Moving Average',
			'Actual',
			'Open',
			'Open Stock Exponential Moving Average'			
		))

	#============================================================ |Open Stock|
	st.subheader("**2. Close Stock**")

	# Prepare the data
	expo_mv_close = apple_data['Close'].ewm(
										span=50,
										adjust=False).mean()

	st.pyplot(plot_timeseries(
			expo_mv_close,
			'Exponential Moving Average',
			'Actual',
			'Close',
			'Close Stock Exponential Moving Average'			
		))

	#============================================================ |Open Stock|
	st.subheader("**3. Volume Stock**")

	# Prepare the data
	expo_mv_volume = apple_data['Volume'].ewm(
										span=50,
										adjust=False).mean()

	st.pyplot(plot_timeseries(
			expo_mv_volume,
			'Exponential Moving Average',
			'Actual',
			'Volume',
			'Volume Stock Exponential Moving Average'			
		))

	#============================================================ |Time Series Lag Plot|
	st.markdown("> **Time Series Lag Plot**")
	st.markdown("A Lag Plot helps to check if a time series data set random or not. \
				 A random data will be evenly spread whereas a shape or trend \
				 indicates the data is not random.")

	#============================================================ |Open Stock|
	st.subheader("**1. Open Stock**")

	st.pyplot(timeseries_lagplot(apple_data['Open']))

	#============================================================ |Close Stock|
	st.subheader("**2. Close Stock**")

	st.pyplot(timeseries_lagplot(apple_data['Close']))

	#============================================================ |Volume Stock|
	st.subheader("**3. Volume Stock**")

	st.pyplot(timeseries_lagplot(apple_data['Volume']))

	st.markdown("**Conclusion:**")
	st.markdown("If we see the visualization above.")

	#============================================================ |Conclusion|

	st.markdown("* **Open:** \
				 Open, Have very good increase from `0.1283` in `1980-12-12`-`156.9800` in `2021-09-08`")

	st.markdown("* **High:** \
				 High, Have a good increase from `0.1289` in `1980-12-12`-`157.0400` in `2021-09-08`")

	st.markdown("* **Low:** \
		 	  	 Low, Have a good increase too from `0.1283` in `1980-12-12`-`153.9800` in `2021-09-08`")

	st.markdown("* **Close:** \
			     Close, have a very good increase from `0.1283` in `1980-12-12`-`155.1100` in `2021-09-08`")

	st.markdown("* **Volume:** \
				 But, Volume start from `469033600` in `1980-12-12` and Decreasing, `2012` until now.")

	st.title("Thanks for Visiting my Web Application!")

	st.markdown("You can get the Data and the Source Code [Here](https://github.com/knightbearr/Apple-Stocks-Web-Application)")