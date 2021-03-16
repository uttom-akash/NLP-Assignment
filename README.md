# NLP-Assignment



#### Instructions

- `filepath` -  in respect to root folder.

  - If Root folder is `NLP-Assignment` and file is in  `NLP-Assignment\bangla.txt` then `filepath = bangla.txt`

  - If Root folder is `NLP-Assignment` and file is in  `NLP-Assignment\data\bangla.txt` then `filepath = data\bangla.txt`

    

1. `python 2-Assignment/nlp_sent_2016831034.py`  `-f`  `filepath`   Or  put file in `datasets` folder as `bangla.txt` and run  `python 2-Assignment/nlp_sent_2016831034.py`
2. `python 3-Assignment/nlp_tokenizer_2016831034.py`  `-f`  `filepath`   Or  put file in `datasets` folder as `bangla.txt` and run  `python 3-Assignment/nlp_tokenizer_2016831034.py`
3. `python 4-Assignment/nlp_histogram_2016831034.py`  `-fB`  `banglafilepath`  `-fE` `englishfilepath`  Or  put file in `datasets` folder as `bangla.txt` , `english.txt` and run  `python 4-Assignment/nlp_histogram_2016831034.py`



####	Files Descriptions in Output Folder

- `SplitedSentence.txt`  -  Contains list of splitted sentence. 
- `tokenizedWords.txt` -  Contains list of words tokens without punctuations.
- `tokenizeWithPunctuation.txt` -  Contains list of words tokens with punctuations.
- `uniqueTokenizedWords.txt` - Contains list of unique words tokens without punctuations.
- `histogram.json`  - Contains Statistics of parallel dataset in json format. 
- `histogram.txt`  - Contains Statistics of parallel dataset in table format.

