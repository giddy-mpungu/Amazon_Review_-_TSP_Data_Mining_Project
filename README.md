# Amazon Beauty and Personal Care Reviews Analysis 🛍️✨

Welcome to the **Amazon Beauty and Personal Care Reviews Analysis** repository!

This repository contains code and instructions to analyze customer reviews for Beauty and Personal Care products using MapReduce jobs in Python.

Below is a comprehensive guide to help you understand the project and reproduce its results.

## 📚 Development Environment Setup

To ensure a consistent development environment and prevent conflicts with other Python projects on your system, we've set up a virtual environment using Python 3.11 within Visual Studio Code (VS Code).

### To set up your environment:
- Create a virtual environment using any preferred IDE (**This should not be a notebook**).
- Use the `venv` module to isolate project dependencies and prevent conflicts with other Python projects on your system.

Here's how to set it up:

1. Clone this repository to your local machine.
2. Navigate to the root directory of the repository.
3. Open the repository in Visual Studio Code.
4. In the terminal, run the following command to create the virtual environment:

```bash
python -m venv venv
```

5. Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```

- On macOS and Linux:
  ```bash
  source venv/bin/activate
  ```

6. Install the required libraries within the virtual environment using pip:
  ```bash
  pip install -r requirements.txt
  ```

## 📥 Data Acquisition

The Amazon Reviews dataset used in this project was downloaded from the official repository: [AmazonReviews2023](https://github.com/hyp1231/AmazonReviews2023). Specifically, we focused on the subset for Beauty and Personal Care products, but the code also wotks fro other categories. Follow these steps to acquire the dataset:

1. Download the dataset from the provided link.
2. Extract the dataset, which is available in compressed JSON format.
3. Place the extracted files in the `data` folder within the root directory of this repository.

## 📂 Folder Structure

The repository has the following folder structure:

```
root/
├── data/
│   └── dt_subset.jsonl  # Downloaded Amazon Reviews dataset (JSON)
└── results/
    ├── review_count_byproduct.csv
    ├── average_star_rating.csv
    ├── average_helpfulness.csv
    ├── sentiment_analysis_results.csv
    └── top_ten_most_reviewed.csv
├── average_helpfulness.py
├── average_star_rating.py
├── review_count.py
├── sentiment_analysis.py
└── top_ten_most_reviewed.py
├── requirements.txt
└── README.md  # (You are here!)
```

## 🏃‍♂️ Running MapReduce Jobs

To analyze the Amazon customer reviews for Beauty and Personal Care products, we've developed several MapReduce jobs. Here's how to run them:

- **Review Count by Product**:
  ```bash
  python review_count.py ./data/dt_subset.jsonl > ./results/review_count_byproduct.csv
  ```

- **Average Star Rating**:
  ```bash
  python average_star_rating.py ./data/dt_subset.jsonl > ./results/average_star_rating.csv
  ```

- **Average Helpfulness**:
  ```bash
  python average_helpfulness.py ./data/dt_subset.jsonl > ./results/average_helpfulness.csv
  ```

- **Sentiment Analysis**:
  ```bash
  python sentiment_analysis.py ./data/dt_subset.jsonl > ./results/sentiment_analysis.csv
  ```

- **Top Ten Most Reviewed Products**:
  ```bash
  python top_ten_most_reviewed.py ./data/dt_subset.jsonl > ./results/top_ten_most_reviewed.csv
  ```

## 🔄 Reproducing Results

To reproduce the results of this project, follow these steps:

1. Set up the development environment as described above.
2. Download the dataset and place it in the `data` folder.
3. Navigate to the root directory of the repository.
4. Run the desired MapReduce jobs using the commands provided.
5. The results will be stored in the `results` folder.

## ✨ Conclusion

This repository provides a basic framework for analyzing customer reviews for Beauty & Personal Care products on Amazon using MapReduce. 

You can extend this approach to implement additional analyses or modify the existing scripts for more specific needs.

If you have any questions or feedback, don't hesitate to reach out. Happy analyzing! 🎉
