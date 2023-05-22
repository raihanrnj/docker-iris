This section containers two model files


The model files 01.knn_with_iris_dataset.pkl and 02.iris_label_encoder.pkl are files saved using the joblib library in Python. These files contain the trained models that were previously trained and saved for later use.

01.knn_with_iris_dataset.pkl: This file contains the trained K-Nearest Neighbors classifier model. It was saved using the joblib.dump() function. The file can be loaded using joblib.load() to retrieve the trained classifier. Once loaded, you can use the classifier to make predictions on new data.

02.iris_label_encoder.pkl: This file contains the LabelEncoder object used to encode the target variable in the Iris dataset. The LabelEncoder is responsible for mapping the original class labels to integer values. It was also saved using the joblib.dump() function. The file can be loaded using joblib.load() to retrieve the LabelEncoder object. Once loaded, you can use the encoder to encode or decode class labels as needed.

By loading these saved model files, you can avoid retraining the models from scratch and directly use the trained models for predictions or further analysis.
