import pandas as pd
import numpy as np
import gc
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv('input_train_2017.csv', parse_dates=["transactiondate"])
properties = pd.read_csv('input_properties_2017.csv')
test = pd.read_csv('input_sample_submission.csv')
test = test.rename(columns={'ParcelId': 'parcelid'})

for c, dtype in zip(properties.columns, properties.dtypes):
    if dtype == np.float64:
        properties[c] = properties[c].astype(np.float32)
    if dtype == np.int64:
        properties[c] = properties[c].astype(np.int32)

for column in test.columns:
    if test[column].dtype == int:
        test[column] = test[column].astype(np.int32)
    if test[column].dtype == float:
        test[column] = test[column].astype(np.float32)

#living area proportions
properties['living_area_prop'] = properties['calculatedfinishedsquarefeet'] / properties['lotsizesquarefeet']
#tax value ratio
properties['value_ratio'] = properties['taxvaluedollarcnt'] / properties['taxamount']
#tax value proportions
properties['value_prop'] = properties['structuretaxvaluedollarcnt'] / properties['landtaxvaluedollarcnt']

df_train = train.merge(properties, how='left', on='parcelid')
df_test = test.merge(properties, how='left', on='parcelid')

del properties, train
gc.collect()

df_train[['latitude', 'longitude']] /= 1e6
df_test[['latitude', 'longitude']] /= 1e6
df_train['censustractandblock'] /= 1e12
df_test['censustractandblock'] /= 1e12

### Label Encoding For Machine Learning & Filling Missing Values ###


# We are now label encoding our datasets.
#  All of the machine learning algorithms employed in scikit learn assume that t
# he data being fed to them is in numerical form. LabelEncoding ensures that all of our
# categorical variables are in numerical representation. Also note that we are filling the missing value
#  in our dataset with a zero before label encoding them. This is to ensure that label encoder function does not
#  experience any problems while carrying out its operation #

lbl = LabelEncoder()
for c in df_train.columns:
    df_train[c] = df_train[c].fillna(0)
    if df_train[c].dtype == 'object':
        lbl.fit(list(df_train[c].values))
        df_train[c] = lbl.transform(list(df_train[c].values))

for c in df_test.columns:
    df_test[c] = df_test[c].fillna(0)
    if df_test[c].dtype == 'object':
        lbl.fit(list(df_test[c].values))
        df_test[c] = lbl.transform(list(df_test[c].values))

### Rearranging the DataSets ###

# We will now drop the features that serve no useful purpose. We will also
# split our data and divide it into the representation to make it clear which features are to be treated as determinants
# in predicting the outcome for our target feature. Make sure to include the same features in the test set as were included
#  in the training set #


x_train = df_train.drop(['parcelid', 'logerror', 'transactiondate', 'propertyzoningdesc',
                         'propertycountylandusecode', ], axis=1)

x_test = df_test.drop(['parcelid', 'propertyzoningdesc',
                       'propertycountylandusecode', '201610', '201611',
                       '201612', '201710', '201711', '201712'], axis=1)

x_train = x_train.values
y_train = df_train['logerror'].values

### Cross Validation ###
# We are dividing our datasets into the training and validation sets so
# that we could monitor and the test the progress of our machine learning algorithm.
# This would let us know when our model might be over or under fitting on the dataset that we have employed. #

print(x_train)
from sklearn.model_selection import train_test_split
X = x_train
y = y_train
Xtrain, Xvalid, ytrain, yvalid = train_test_split(X, y, test_size=0.2, random_state=42)

###Implement the Xgboost###

# We can now select the parameters for Xgboost and monitor
#  the progress of results on our validation set. The explanation of the xgboost parameters
#  and what they do can be found on the following link http://xgboost.readthedocs.io/en/latest/parameter.html #

dtrain = xgb.DMatrix(Xtrain, label=ytrain)
dvalid = xgb.DMatrix(Xvalid, label=yvalid)
dtest = xgb.DMatrix(x_test.values)

# Try different parameters!

xgb_params = {'min_child_weight': 5, 'eta': 0.035, 'colsample_bytree': 0.5, 'max_depth': 4,
              'subsample': 0.85, 'lambda': 0.8, 'nthread': -1, 'booster': 'gbtree', 'silent': 1, 'gamma': 0,
              'eval_metric': 'rmse', 'objective': 'reg:linear'}

watchlist = [(dtrain, 'train'), (dvalid, 'valid')]
model_xgb = xgb.train(xgb_params, dtrain, 1000, watchlist, early_stopping_rounds=100,
                      maximize=False, verbose_eval=10)

###Predicting the results###


# Let us now predict the target variable for our test dataset.
# All we have to do now is just fit the already trained model on the test set
# that we had made merging the sample file with properties dataset #


Predicted_test_xgb = model_xgb.predict(dtest)

### Submitting the Results ###


# Once again load the file and start submitting the results in each column #

sample_file = pd.read_csv('input_sample_submission.csv')

for c in sample_file.columns[sample_file.columns != 'ParcelId']:
    sample_file[c] = Predicted_test_xgb

print('Preparing the csv file ...')
sample_file.to_csv('xgb_predicted_results.csv', index=False, float_format='%.4f')
print("Finished writing the file")
