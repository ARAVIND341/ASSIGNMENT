1)How to install dependencies?

First we clone the repository to create a python environment. Also we are creating a virtual environment for running PySpark

We can add the following command:
  git clone https://github.com/ARAVIND341/ASSIGNMENT.git
  cd ASSIGNMENT

For installing the venv(virtual environment)
  python -m venv spark-venv
  .\spark-venv\Scripts\activate

This will activate the virtual environment and shows (spark-venv) at the beginning of the command line

Then we can install the dependencies using the following command
  pip install -r requirements.txt

Some of the installed dependencies includes,
  PySpark,pandas,scikit-learn,numpy,seaborn,matplotlib etc

2)How to run the project?

  The command to run it is:
    dvc repro

  This will reproduce the pipeline and run various stages in it like preprocessing,feature engineering,regression,classification,evaluation.
  It will process the zomato dataset, helps to generate features, put in steps to train and test regression and classification models and helps to save evaluation metrics.

  

3)What are the expected results?


  In dvc.yaml, we are defining the stages for classification, regression etc.

  In regression, we are training the model to predict the rating_number where the results are stored in regression_model.pkl stored in the models folder and the metric is MSE

  In classification, restaurants are classified to be more known and less known ones, and the metrics is the accuracy.

  The results can be seen in the metrics.json file in reports
  
  
