# 2016 Election Modeling v2

## Introduction
My modeling goal was to build a regression model that could predict county level vote proportion for Donald Trump based upon demographic features, in order to determine the feature weights for predicting support for Donald Trump.  I downloaded county level 2016 election results data from Harvard Dataverse and county level demographic data from the US Census Bureau, both in csv form.  After dropping features with a large number of missing values as well as correlated features, and replacing the remaining missing values with the feature mean, I was left with 785 datapoints across 12 features.  The top performing regression model was SVR (RMSE: .092, MAE: .072, R2: .64), which outperformed the baseline Mean Dummy Regressor (RMSE: .154, MAE: .124, R2: .00). The top performing model with a linear kernel and accessible feature coefficients was linear regression (RMSE: .098, MAE: .079, R2: .60), which revealed that the greatest positive coefficients for Donald Trump vote proportion belonged to White Population Proportion (.045) and Veteran Population Proportion (.031) and the greatest negative coefficients were for Bachelor's Degree Proportion (-.035) and Per Capita Income (-.028).

## Obtain Data
I downloaded county level election results in csv form from Harvard Dataverse and csv form county level US Census Bureau demographic data available for the 800 largest counties in the US, representing 85% of the US population, from data.census.gov.  After merging csv files from the 2 sources together, the 2016 election dataset included 785 datapoints across 22 columns.

## Scrub Data

<a href="url"><img src="https://github.com/blantj/2016_election_modeling_v2/blob/main/Images/df_info.png" align="middle" height="225" width="175" ></a>

In order to scrub the 2016 election dataset, I first dropped descriptive variables that were not going to be included in the model, as well as the Non-English Speaker feature due to the large number of missing values. I also dropped all non-white racial groups because the combined values of all races would be heavily correlated since they added to one and I thought the white feature would be the most influential predictor of support for Donald Trump. I replaced missing values with the feature mean in order to avoid reducing sample size and updated the datatype for all features to float. I also divided all population count features, such as number of veterans, by county population in order to turn these into standardized variables that were comparable across counties. My final dataset included 785 datapoints across 12 features.

## Explore Data

<a href="url"><img src="https://github.com/blantj/2016_election_modeling_v2/blob/main/Images/trump_support_histogram.png" align="middle" height="200" width="300" ></a>

On average 52.7% of a county’s population voted for Donald Trump in the 2016 election with a standard deviation of 14.9%. Support for Donald Trump was normally distributed and had a leftward skew as the median of 54.5% exceeded the mean.

<a href="url"><img src="https://github.com/blantj/2016_election_modeling_v2/blob/main/Images/feature_corr_heatmap.png" align="middle" height="250" width="250" ></a>

The two most heavily correlated features in the dataset were the proportion of residents with a bachelors degree and per capita income, with a correlation of .81. While these features were heavily correlated, I decided to the leave them in because I thought they both still did have some explanatory contribution to the model. I would just have to keep this correlation in mind for the regression coefficients. In terms of feature engineering, some features had exponential relationships with Vote Proportion and required log transformations to make the relationship more linear.

## Model Data

<a href="url"><img src="https://github.com/blantj/2016_election_modeling_v2/blob/main/Images/model_performance.png" align="middle" height="200" width="400" ></a>

All non-baseline election models performed similarly with the exception of Support Vector Regression (RBF Kernel), which slightly outperformed the other models. SVR (RBF Kernel) performed strongly beating the baseline model in RMSE (.092 vs. 154) and MAE (.072 vs. .124). SVR (RBF Kernel)’s RMSE of .092 also compared favorably to Donald Trump’s vote proportion standard deviation of .149, which yielded an R-Squared of .64.

<a href="url"><img src="https://github.com/blantj/2016_election_modeling_v2/blob/main/Images/lr_feature_importance.png" align="middle" height="300" width="400" ></a>

Although, Support Vector Regression was the top performing model for predicting county level vote proportion for Donald Trump, this model included a non-linear kernel, which meant that I could not access feature coefficients. I instead pulled feature coefficients for the second best model, Linear Regression. The most impactful positive features were White Population Proportion (.045), Veteran Proportion (.031) and Mining Employment Per Capita (.030). The most important features negatively influencing support for Donald Trump were Bachelor’s Degree Proportion (-.035), Per Capita Income (-.028) and Latino Population Proportion (-.023).

<a href="url"><img src="https://github.com/blantj/2016_election_modeling_v2/blob/main/Images/lasso_feature_importance.png" align="middle" height="300" width="400" ></a>

I also pulled feature coefficients for Lasso, since Lasso performed similarly to Linear Regression in predictive ability with the added benefit of reducing or eliminating the importance of potentially overfit features. Lasso regularization did not have a major impact on the feature importances. Only one feature, Agricultural Employment Per Capita, was eliminated completely, while one other feature Disable Population Proportion, was nearly eliminated. Similarly there was only one pair of neighboring features , Latino Population Proportion and Per Capita Income, that traded places in being the second and third most impactful negative features. This confirmed the importance of all of the most impactful features from the Linear Regression model.

## Analyze Results
I was successfully able to build a regression model that could determine what demographic features were most important in influencing support for Donald Trump in the 2016 US presidential election. With an R-Squared of .6, the linear regression model was able to explain the majority of the county level variance in support for Donald Trump. The most important features upwardly impacting support for Donald Trump and their feature coefficients were White Population Proportion (.045), Veteran Proportion (.031) and Mining Employment Per Capita (.030). The most downwardly impactful features influencing support for Donald Trump were Bachelor’s Degree Proportion (-.035), Per Capita Income (-.028) and Latino Population Proportion (-.023).

## Next Steps
With more time, I would like to find new census features to include in my model to see if they could raise its ability to explain county level variation in support for Donald Trump even further.

# Github Files
[Modeling.ipynb](https://github.com/blantj/2016_election_modeling_v2/blob/main/Modeling.ipynb) :  2016 Election Modeling

# Sources
Harvard Dataverse: https://dataverse.harvard.edu/

Census Bureau: https://data.census.gov/

