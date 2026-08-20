# Supermarket Sales Analyzer

A Python-based data analysis project that explores supermarket sales data using **Pandas** and **Matplotlib**.

The project loads, preprocesses, analyzes, and visualizes supermarket sales data to identify patterns in revenue, customer behavior, payment methods, sales timing, and product performance.

## Features

* Data loading and preprocessing
* Revenue analysis
* Revenue comparison by branch
* Revenue analysis by product line
* Customer type analysis
* Gender-based revenue analysis
* Payment method analysis
* Monthly revenue analysis
* Day-of-week revenue analysis
* Hourly revenue analysis
* Average rating analysis by branch
* Average rating analysis by product line
* Data visualizations using Matplotlib
* Basic automated testing using Python `assert` statements

## Dataset

The project uses a supermarket sales dataset containing transaction-level information such as:

* Invoice details
* Branch
* Customer type
* Gender
* Product line
* Unit price
* Quantity
* Tax
* Total sales
* Date and time
* Payment method
* Customer rating

The dataset is used to analyze sales performance and identify patterns across different business dimensions.

## Technologies Used

* **Python**
* **Pandas** — data loading, preprocessing, grouping, and analysis
* **Matplotlib** — data visualization
* **Git & GitHub** — version control and project management

## Project Structure

```text
Supermarket-sales-analyzer/
│
├── data/
│   └── supermarket_sales.csv
│
├── images/
│   ├── revenue_by_branch.png
│   ├── revenue_by_product_line.png
│   ├── revenue_by_customer_type.png
│   ├── revenue_by_gender.png
│   ├── revenue_by_payment_method.png
│   ├── revenue_by_month.png
│   ├── revenue_by_day.png
│   ├── revenue_by_hour.png
│   ├── rating_by_branch.png
│   └── rating_by_product.png
│
├── notebooks/
│   └── ...
│
├── reports/
│   └── ...
│
├── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── analysis.py
│   └── visualization.py
│
├── visualize.py
├── test_analysis.py
├── requirements.txt
└── README.md
```

### File and Folder Description

| File / Folder          | Purpose                                                      |
| ---------------------- | ------------------------------------------------------------ |
| `data/`                | Contains the supermarket sales dataset                       |
| `images/`              | Stores the generated visualization images                    |
| `notebooks/`           | Contains notebooks used during data exploration and analysis |
| `reports/`             | Contains project reports and related documentation           |
| `src/data_loader.py`   | Loads the dataset                                            |
| `src/preprocess.py`    | Preprocesses and prepares the data                           |
| `src/analysis.py`      | Contains reusable functions for sales and rating analysis    |
| `src/visualization.py` | Contains reusable functions for creating visualizations      |
| `visualize.py`         | Runs the visualization functions                             |
| `test_analysis.py`     | Tests the analysis pipeline and verifies expected outputs    |
| `requirements.txt`     | Lists the Python dependencies required by the project        |
| `README.md`            | Contains project documentation                               |

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Supermarket-sales-analyzer
```

### 2. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analysis

```bash
python test_analysis.py
```

This loads the dataset, preprocesses the data, calculates revenue and rating metrics, and runs the analysis functions.

### 4. Generate visualizations

```bash
python visualize.py
```

The generated charts are saved in the `images/` directory.

## Testing

The project includes basic automated tests using Python `assert` statements.

Run:

```bash
python test_analysis.py
```

If all checks pass, the program displays:

```text
All tests passed!
```

## Analysis

The project performs the following analyses on the supermarket sales data:

### Revenue Analysis

* Total revenue
* Average revenue
* Revenue by branch
* Revenue by product line
* Revenue by customer type
* Revenue by gender
* Revenue by payment method
* Revenue by month
* Revenue by day of week
* Revenue by hour

### Rating Analysis

* Average customer rating by branch
* Average customer rating by product line

## Visualizations

The analysis results are visualized using **Matplotlib**.

The project generates bar charts for:

* Revenue by branch
* Revenue by product line
* Revenue by customer type
* Revenue by gender
* Revenue by payment method
* Revenue by month
* Revenue by day of week
* Revenue by hour
* Average rating by branch
* Average rating by product line

All generated visualizations are stored in the `images/` directory.

## Key Insights

The analysis of the supermarket sales data produced the following insights:

* **Total revenue:** The supermarket generated a total revenue of **322,966.75**, with an average revenue of **322.97 per transaction**.
* **Branch performance:** Branch **C** generated the highest revenue at **110,568.71**, followed closely by Branch A and Branch B.
* **Product line performance:** **Food and beverages** generated the highest revenue at **56,144.84**, while **Health and beauty** generated the lowest at **49,193.74**.
* **Customer type:** **Members** generated more revenue (**164,223.44**) than Normal customers (**158,743.31**).
* **Gender:** Female customers generated slightly more revenue (**167,882.93**) than male customers (**155,083.82**).
* **Payment methods:** **Cash** generated the highest revenue (**112,206.57**), followed by E-wallet and Credit card.
* **Monthly performance:** **January** recorded the highest revenue (**116,291.87**), while February recorded the lowest (**97,219.37**).
* **Day of week:** **Saturday** generated the highest revenue (**56,120.81**), while Monday generated the lowest (**37,899.08**).
* **Hourly performance:** **7 PM (19:00)** had the highest revenue (**39,699.51**), while **8 PM (20:00)** had the lowest (**22,969.53**).
* **Branch ratings:** Branch **C** had the highest average customer rating (**7.07**), while Branch B had the lowest (**6.82**).
* **Product line ratings:** **Food and beverages** had the highest average rating (**7.11**), while **Home and lifestyle** had the lowest (**6.84**).
