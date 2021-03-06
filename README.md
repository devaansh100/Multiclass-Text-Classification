# Multiclass Text Classifcation
The text classifier can handle large amounts of data with short training times. It can also handle a large number of output classes.

This code was used in the Amazon ML Challenge 2021(https://www.hackerearth.com/challenges/competitive/amazon-ml-challenge/), hosted by HackerEarth, to achieve a rank of 64 from 518 submitted models.

# FastText
FastText is a module provided by Facebook Research. More information about the module can be find in their GitHub repository(https://github.com/facebookresearch/fastText) and on their website(https://fasttext.cc). Our repository gives an upper level API that allows one to work with the fastText text classifcation model. We provide an API to generate the required files, train and infer from the model on your own data. 

# Installation and Setup

The following code should be run in order to initialise the different scripts.

```bash
cd fasttext_model
chmod +x init.sh
./init.sh
cd ..
pip install -r requirements.txt
```

# Data Preparation and Execution
Running ```python main.py``` will start the pipeline. Ensure that you have your equivalent of ```train.csv``` and ```test.csv``` in the dataset folder. The possible flags can be viewed by running ```python main.py --help``` or simply ```python main.py -h```. 

# Scripts
This section will discuss the function of all the scripts, their inputs and how to use them.

## scripts/build_fasttext.sh
This script is used to clone into the fastText repository and create all the executables. It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:

```bash
cd scripts
./build_fasttext.sh
```

It creates a ```fastText``` directory.

## init.sh
This script initialises all the other scripts and builds the fasttext module. This should be run at intialisation as mentioned above.

## scripts/train.sh
This script trains a fasttext model. It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:

```bash
cd scripts
./train.sh path_to_corpus.txt path_to_save_model
```

It creates two files - ```path_to_save_model.bin``` and ```path_to_save_model.vec```. ```path_to_save_model.bin``` is the trained model and ```path_to_save_model.vec``` are embeddings for all the words in the corpus.

More options will be soon added to the script.

## scripts/infer.sh
This script can be used to infer from a trained fasttext model. It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:

```bash
cd scripts
./infer.sh path_to_trained_model path_to_test_corpus.txt
```

It creates a ```predictions.csv``` with all the predictions for each input case along with a serial number. It also creates an intermediate file called```predictions.txt``` which is deleted once the csv file is created.

## create_corpus_fasttext.py
This script concatenates the label with input features in the format required by fasttext. It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:

```bash
python create_corpus_fasttext.py --csv path_to_csv_file --corpus path_to_corpus.txt --output path_to_output_file.txt
```

It creates a ```path_to_output_file.txt``` file which contains the corpus ready to be fed into fasttext.

Note: The aforementioned flags are optional. For more information, run ```python create_corpus_fasttext.py --help``` or simply ```python create_corpus_fasttext.py -h```.

## create_predictions.py
This script creates the ```predictions.csv``` from a ```predictions.txt``` . It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:

```bash
python create_predictions.py --header_first first_column_heading --header_second second_column_heading
```

It creates a ```predictions.csv``` with all the predictions for each input case along with a serial number.

Note: The aforementioned flags are optional. For more information, run ```python create_predictions.py --help``` or simply ```python create_predictions.py -h```.

## ensemble.sh
This script creates multiple predictions from multiple models that are passed into it. Multiple models are to be created by calling ```main.py``` multiple times. To use it, execute the following command:
```bash
cd scripts
./ensemble.sh path_to_test_corpus.txt 3 PRODUCT_NODE_ID BROWSE_NODE_ID trained_fasttext_model_1.bin trained_fasttext_model_2.bin trained_fasttext_model_3.bin
```

Any number of models can be passed as parameters. The second parameter is used to produce n-best predictions. In this case, 3 best predictions with their probabilities would be made. From all the predictions, the most confident prediction is chosen for the final prediction. The next two parameters are the headers, as explained in ```create_predictions.py```. Setting them to ```_``` will cause the program to use the default value.

Multiple intermediate files are created. These are ```predictions_1.txt```, ```predictions_2.txt``` etc.

Finally, a ```predictions.csv``` would be created with all the predictions for each input case along with a serial number.

## ensemble.py
This script combines all the prediction files created from the different models into one file. It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:
```bash
python ensemble.py --models 3
```

It creates a ```predictions.txt``` which contains each prediction seperated by ```\n```.

For more information, execute ```python ensemble.py --help``` or simply ```python ensemble.py -h```.

## Important Note
In ```train.sh```, ```infer.sh``` and ```ensemble.sh``` wherever path is mentioned, make sure that path is relative to the ```fasttext_model/fastText``` directory. Absolute paths will work as well.

## Preprocessing

The machine learning algorithms do not comprehend unstructured text data, and thus there is a need to clean and preprocess the data so that it can be used efficiently in various NLP algorithms. Sometimes unstructured text data contains noise that needs to be treated as well. This module standardizes the text data, thus making it ready for training. The module has been made flexible, keeping in mind the broad array of NLP tasks. 

## preprocess_text.py

This script removes noise from the data and preprocesses it, thus making it ready for training. It is automatically called in the pipeline however it can be customised according to your needs with the help of the given script 

```bash
python preprocess_text.py --input path_to_input_file --output path_to_output_file.txt --remove_html set_false_to_retain --remove_digit set_false_to_retain --remove_emoticon set_false_to_retain --remove_stopwords set_false_to_retain
```
It creates a ```path_to_output_file.txt``` file which contains preprocessed text

Note: The aforementioned flags are optional. For more information, run ```preprocess_text.py --help``` or simply ```python preprocess_text.py -h```.

