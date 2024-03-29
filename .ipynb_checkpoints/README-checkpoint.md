# Evolution of Agriculture - Inputs, Environmental Impacts & Outputs

# Abstract
To answer the increasing demand for food, resulting from rising population and consumption, agriculture has evolved to employ modern industrial methods such as synthetic fertilizers, pesticides, and machinery in order to increase production.  However, these methods are also associated with increased environmental impacts, such as greenhouse gas emissions, land degradation and water pollution. Due to this, interest in alternative methods such as organic agriculture and permaculture is increasing – although these methods still represent a small fraction of global agriculture.
 
Considering the need to reduce the environmental impact of agriculture while maintaining and increasing production, we will establish the current level of global food production and analyze the evolution of modern agriculture in terms of the impact of increasing use of machinery, fertilizers and pesticides on production and yield as well as on environmental indicators. This information can be used to identify a baseline which alternatives much meet and improve upon. 


# Research questions
First Part: Production and Modern Industrial Methods
- What ‘current’ level of global food production is required? (as of 2013, the most recent year available in the dataset)
- How has food production and yield evolved? (within the timeframe of the dataset, from 1961-2013) 
- How has the use of modern/industrial agricultural methods (synthetic fertilizers, pesticides, machinery) evolved? 
- Can we identify some relationships between the evolution of production and yield, and the evolution of the use of synthetic fertilizers, pesticides and machinery? 
  - (For example, we expect that the use of these methods will increase production in general, but is there a point at which the relationship plateaus and there is no longer a significant increase? Is the change in yield for a given change in input such as fertilizers increasing or decreasing?) 
  
Second Part: Environmental Impact
- What is the current level of different environmental impact due to agriculture? (for example in terms CO2eq and land use area) 
- How has the level of environmental impact due to agriculture evolved? 
- Can we identify some relationships between the evolution of environmental impact and the evolutions studied in the previous section (evolution of production and yield, evolution of the use of synthetic fertilizers, pesticides and machinery). 
  - (For example, we can look at the increase in environmental impact for an increase in production → do we have more or less increase in environmental impact per increase in production now versus in the 1900’s? Further,  we have information regarding emissions due to energy use and synthetic fertilizers and can analyze the relationship between this and the use of machinery and fertilizers).


# Dataset
We will use the Global Food and Agriculture Statistics database from FAOStat: 
https://www.kaggle.com/unitednations/global-food-agriculture-statistics

1. To look at total production we will look at the worldwide production in terms of energy (ie. calories), using data from the food supply datasheet and summing for each country the energy supply associated to each crop.

2. From the country investment statistics data, we will look at the levels of investment in agriculture (for example investment in machinary), and will use this to analyze levels of 'development' or 'modernization' of agriculture between different years and countries 

3. To look at how yield has developed in relation to fertilizer and pesticide use, we will use the following datasets:
 - To look at pesticide use per country, we will use Pesticides data from Agri-environmental factors, which give us the amount of pesticides per ha of cropland for about 140 countries between 1990 and 2016. 
 - To look at fertilizers, we have also amount of fertilizers per ha of cropland but only from 2002.
 - To look at yield, in the “production/crops” sheet, we have yield for more than 40 crops from 1961 to 2017.

4. To look at CO2 emissions due to agriculture, we will use the “Emission-Agriculture/Agriculture total sheet” were we can have data of CO2 emitted between 1961 and 2017 for nearly 200 countries


# A list of internal milestones up until project milestone 2
Nov. 4th :
- Download the data and develop a strategy for how to handle the large dataset
- Prepare a Jupyter Notebook with a framework for the project
- Perform an initial analysis on the raw data to identify potential gaps/missing data, and find a methodology to deal with any issues found.
- Familiarize ourselves with the topic of industrial agriculture in order to understand the current situation, the history and the terms linked to it

Nov. 11th:
- Prepare the subsets of the data which we will require for our analysis 
- Write functions/scripts to analyze the data 
- Begin data visualization and discuss the most consistent way to visualize our data
- Perform any data cleaning found necessary during analysis and visualization 
  
Nov. 18th:
- Check the consistency between our analysis of different sections of data
- Finalize the visualization of the data
- Ensure that we have all the subsets of data and visualizations required to answer our research questions 

Nov. 25th (Deadline for Milestone 2):
- Comment and clean the presentation of the Notebook
- Debug our code 


# Questions for TAa
Is our topic either too ambitious or insufficient? 
It is not discussed above however we also considered looking into the distribution of production for different types of food in order to identify whether there are links between certain methods and certain foods. However, this may be too detailed. 

Is our topic (defining current levels for agricultural methods to meet and improve upon) appropriate within the context of “data science for social good”?

