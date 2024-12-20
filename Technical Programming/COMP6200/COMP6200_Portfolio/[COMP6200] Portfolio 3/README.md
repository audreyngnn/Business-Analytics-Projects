# Portfolio 3: Mobile Price Analytics (MQ) .☘︎ ݁˖

## Brief
In this Portfolio task, I'll be working with a new dataset called 'Mobile Price Data.' It contains details about mobile phone hardware, specifications, and prices. My main goal is to create classification models to predict phone prices (labeled as 'price range' in the dataset) and evaluate their performance.

--> **Analysis Summary**
1. The KNN model with hyperparameter tuning achieved a slightly higher accuracy of 0.93 compared to 0.92 obtained without hyperparameter tuning. This suggests that optimizing the hyperparameter (the number of neighbors, k) led to an improvement in model performance.
2. The optimal value of k found through hyperparameter tuning was 13. This suggests that considering a larger number of neighbors for classification yielded the best results for this dataset.
3. Although hyperparameter tuning led to improved accuracy, it also required additional computational resources. GridSearchCV exhaustively searches through the specified parameter grid, which can be computationally intensive, especially for larger datasets or when the parameter space is large.
4. While hyperparameter tuning improved accuracy, it's important to consider the trade-offs between model performance and computational cost. In some cases, the marginal improvement in accuracy may not justify the increased computational overhead associated with hyperparameter tuning.

## Objectives ✧ ̟
1. Investigate the dataset
2. Clean and Transform the data (if necessary)
3. Examine feature correlations
4. Implement Logistic Regression Model
5. Apply KNN Model.
6. Optimize the hyper-parameter K in KNN.

## Technical Proficiency  ๋࣭⭑
*  Classification Model Development
