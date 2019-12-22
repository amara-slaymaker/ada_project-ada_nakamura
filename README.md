# Evolution of Agriculture - Inputs, Environmental Impacts & Outputs

# How to read the Milestone 3
The notebook is in the branch master and is called `Milestone_3.ipynb`. The data story is available at http://165.22.123.74/

# Abstract
To answer the increasing demand for food, resulting from rising population and consumption, agriculture has evolved to employ modern industrial methods such as synthetic fertilizers, pesticides, and machinery in order to increase production.  However, these methods are also associated with increased environmental impacts, such as greenhouse gas emissions, land degradation and water pollution. Due to this, interest in alternative methods such as organic agriculture and permaculture is increasing – although these methods still represent a small fraction of global agriculture.
 
Considering the need to reduce the environmental impact of agriculture while maintaining and increasing production, we will establish the current level of global food production and analyze the evolution of modern agriculture in terms of the impact of increasing use of machinery, fertilizers and pesticides on production and yield as well as on environmental indicators. This information can be used to identify a baseline which alternatives much meet and improve upon. 

# Research questions
First Part: Production and Modern Industrial Methods
- How has food yield evolved in time all over the world? (within the timeframe of the dataset, from 1961-2013)

Second Part : Correlation between fertilizers use and surfacic yields using PCA
- How has the use of synthetic fertilizers evolved? 
- Can we identify some relationships between the evolution of production and yield, and the evolution of the use of synthetic fertilizers? 
  
Third Part: Correlation between fertilizers use and surfacic yields using UMAP
- Same questions than for Part 2
- Is this more complex tool more appropriated for this study?

Fourth Part: Environmental Impact
- What is the current level of different environmental impact due to agriculture? (for example in terms CO2eq and land use area) 
- How has the level of environmental impact due to agriculture evolved? 
- Can we identify some relationships between the evolution of environmental impact and the evolutions studied in the previous section (evolution of production and yield, evolution of the use of synthetic fertilizers, pesticides and machinery). 
  - (For example, we can look at the increase in environmental impact for an increase in production → do we have more or less increase in environmental impact per increase in production now versus in the 1900’s? Further,  we have information regarding emissions due to energy use and synthetic fertilizers and can analyze the relationship between this and the use of machinery and fertilizers).


# Dataset
We will use the Global Food and Agriculture Statistics database from FAOStat: 
https://www.kaggle.com/unitednations/global-food-agriculture-statistics

1. To look at total production we will look at the worldwide production in terms of production (in tonnes) and of surfacic yields (in hg/ha). The production will be studied into different subsets : the meat production, the eggs, the milk, the crops, the cereals, the coarse grains.

2-3. To look at how yield has developed in relation to fertilizer and pesticide use, we will use the following datasets:
 - To look at fertilizers, we have also amount of fertilizers per ha of cropland but only from 2002.
 - To look at yield, in the “production/crops” sheet, we have yield for more than 40 crops from 1961 to 2017.

4. To look at CO2 emissions due to agriculture, we will use the “Emission-Agriculture/Agriculture total sheet” were we can have data of CO2 emitted between 1961 and 2017 for nearly 200 countries.

# Group organisation
We worked together on each step, from the preliminary data analysis to the preparation of the final presentation. 


