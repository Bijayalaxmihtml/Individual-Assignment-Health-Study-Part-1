# Individual-Assignment-Health-Study-Part-1
# Health Study – Part 1: Statistics and Data Analysis

## 1. About the project

In this project I use Python to look at data from a health study with 800 people. The data has age, sex, height, weight, systolic blood pressure, cholesterol, smoking habits and disease status.

The main goal of this part is to practise working with health data: calculate simple statistics, make graphs, run simulations and use statistical methods to answer questions about the data.

In this part I:
- calculate simple statistics and make graphs,
- simulate the disease share with NumPy,
- make confidence intervals for the mean blood pressure with two methods,
- test if smokers have higher blood pressure than non-smokers,
- check how reliable my test is with a power simulation (VG),
- explain why I chose my methods, with their assumptions and limits (VG).

All the analysis code is written in the notebook. The `src/` folder has the same kind of functions as small reusable modules, with three tests. The notebook does not need them to run.

## 2. Project structure

```text
health_study_del1/
│
├── data/
│   └── health_study_dataset.csv
│
├── notebooks/
│   └── health_study_del1.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── statistics_analysis.py
│   └── visualizations.py
│
├── tests/
│   └── test_analysis.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

| Folder or file | What it is |
|---|---|
| `data/` | The dataset (CSV file) |
| `notebooks/health_study_del1.ipynb` | The notebook with all code, graphs and explanations |
| `src/data_processing.py` | Functions to load the data and calculate the disease share |
| `src/statistics_analysis.py` | Functions for descriptive statistics, confidence intervals and the smoker test |
| `src/visualizations.py` | Functions for graphs |
| `tests/test_analysis.py` | Three tests that check the functions |
| `requirements.txt` | The Python packages I use |
| `.gitignore` | Files that should not go to GitHub (for example `.venv`) |

## 3. Dataset

The dataset has 800 rows and 9 columns.

| Variable | Description |
|---|---|
| `id` | Number of the person |
| `age` | Age in years |
| `sex` | Sex (M or F) |
| `height` | Height in cm |
| `weight` | Weight in kg |
| `systolic_bp` | Systolic blood pressure in mmHg |
| `cholesterol` | Cholesterol in mmol/L |
| `smoker` | Smoker (Yes or No) |
| `disease` | Has the disease (1) or not (0) |

The assignment text calls the sex column `gender`, but in the CSV file it is called `sex`. I use the names from the file.

Before the analysis I checked the number of rows and columns, the data types, missing values and duplicates. There are no missing values and no duplicates, so I did not need to clean the data.

## 4. What is in the notebook

1. **Descriptive statistics:** mean, median, min and max for age, weight, height, systolic blood pressure and cholesterol (I also show the standard deviation).
2. **Graphs:** a histogram of blood pressure, a box plot of weight by sex, a bar chart of smokers and non-smokers, and a scatter plot of age and blood pressure. Each graph has a short explanation.
3. **Disease share and simulation:** 47 of 800 people (5.88%) have the disease. I simulate 1,000 people with the same probability (with a seed) and compare with the real share. I also repeat the simulation 10,000 times to see the normal random variation.
4. **Confidence intervals:** normal approximation, t distribution and bootstrap. I compare them and check them with SciPy (BCa bootstrap) and with a coverage simulation.
5. **Hypothesis test:** Welch's t-test (one-sided) to test if smokers have a higher mean blood pressure. I check the assumptions (Q–Q plots, Shapiro–Wilk, Levene), and I use a permutation test, effect size and a confidence interval for the difference as extra checks.
6. **Power simulation:** how often the test finds a real difference, how big a difference is needed for 80% power, and how the sample size changes the power.
7. **Method choices:** why I chose each method, what it assumes and what its limits are. I used the course material and the NumPy and SciPy documentation.

## 5. Main results

| Question | Result |
|---|---|
| Disease share | 5.88% (47 of 800). My simulation of 1,000 people gave 5.4%. This is normal random variation. |
| Mean systolic blood pressure | 149.2 mmHg. The 95% confidence interval is about 148.3 to 150.1 mmHg. All methods agree. |
| Smokers and non-smokers | Mean 149.5 and 149.1 mmHg. Difference 0.47 mmHg, one-sided p = 0.33. |
| Conclusion of the test | I do not reject H₀. There is not enough evidence that smokers have higher blood pressure. This does not prove that smoking has no effect. |
| Power | About 2.6 mmHg difference is needed for 80% power. A bigger sample would give more power. |

## 6. Python and tools

Python version: **3.13.6**

| Tool | Use |
|---|---|
| Pandas | Loading and handling the data |
| NumPy | Calculations and random simulations |
| Matplotlib | Graphs |
| SciPy | Statistical tests and confidence intervals |
| Jupyter Notebook | Writing and running the analysis |
| pytest | Running the tests |
| VS Code, Git and GitHub | Writing the project and storing it |

## 7. Automated tests

The file `tests/test_analysis.py` has three small tests. They use a tiny example table. They check that the disease share is counted correctly (2 cases out of 4 is 50%), that the confidence interval contains the sample mean, and that the smoker test gives a valid one-sided p-value between 0 and 1. I use pytest to run them. All 3 tests pass.

Run the tests from the main project folder (the one that has `src/` and `tests/`):
```bash
python -m pytest
```
To see each test by name:
```bash
python -m pytest tests/test_analysis.py -v
```

## 8. How to run the project

Open the main folder `health_study_del1` in VS Code and use the terminal in that folder.

**Step 1: make and activate a virtual environment**
```bash
python -m venv .venv
```
- Windows Git Bash: `source .venv/Scripts/activate`
- Windows PowerShell: `.venv\Scripts\activate`
- Mac or Linux: `source .venv/bin/activate`

**Step 2: install the packages**
```bash
python -m pip install -r requirements.txt
```

**Step 3: run the notebook**

Open `notebooks/health_study_del1.ipynb` in VS Code, choose the `.venv` Python environment and click **Restart Kernel and Run All Cells**. The notebook reads the data with a relative path (`../data/health_study_dataset.csv`), so it works on any computer.

**Step 4: run the tests**
```bash
python -m pytest
```

## 9. Reproducibility

- I set a random seed (42) at the start of the notebook. The extra simulations use their own seeds, so every result is the same each time.
- I use relative file paths.
- The packages are in `requirements.txt`.
- The `.venv` folder is in `.gitignore`, so it is not uploaded to GitHub.

## 10. Limits

- The data is observational, so I can see patterns but I cannot show that one thing causes another.
- Age is strongly linked to blood pressure and I did not adjust for it in this part.
- The results depend on the people in the dataset, so I interpret them with care.
- The simulation uses the real disease share. It is an exercise and not a prediction for real people.

## 11. Conclusion

In this part I used Python to explore a health dataset. I calculated statistics, made graphs, simulated the disease share, built confidence intervals with two methods and tested if smokers have higher blood pressure. I found no evidence of a difference, but my power simulation shows that only differences of about 2.6 mmHg or more could be found reliably with this sample. This part helped me understand statistical uncertainty and the limits of hypothesis tests.
