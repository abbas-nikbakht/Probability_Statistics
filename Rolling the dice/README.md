# 🎲 Rolling the Dice — Monte Carlo Simulation

An interactive **Monte Carlo simulation** that demonstrates how the **Expected Value** of a fair six-sided die can be estimated using repeated random sampling.

The project combines **Python, NumPy, SciPy, Plotly, and Dash** to create a simple interactive visualization of convergence toward the theoretical expected value.

---

## 📌 Overview

The expected value of a fair six-sided die is:

$$
E[X] = \sum_{x=1}^{6} xP(X=x)
$$

Since each outcome has a probability of :

$$
E[X] =
\frac{1+2+3+4+5+6}{6}
= 3.5
$$

In this project, the die is rolled repeatedly and the **sample mean** is calculated after every roll.

As the number of samples increases, the estimated expected value tends to converge toward **3.5**.

This provides a simple demonstration of the **Law of Large Numbers** and the fundamental idea behind Monte Carlo methods.

---

## ✨ Features

* 🎲 Interactive dice rolling
* 📊 Real-time Expected Value estimation
* 📈 Interactive Plotly visualization
* 🧮 Discrete probability distribution using `scipy.stats.rv_discrete`
* 🖼️ Dynamic dice images
* 🔄 Running average updated after every sample
* 🌐 Interactive web dashboard powered by Dash

---

## 🖥️ Demo

Click **Rolling the dice** to generate a new random outcome.

The application displays:

1. The current dice outcome
2. The corresponding dice image
3. The estimated Expected Value
4. A graph showing how the estimate changes as more samples are collected

> **Expected Value of a fair die: 3.5**

---

## 📈 Monte Carlo Estimation

For \(n\) observed samples \(X_1, X_2, ..., X_n\), the Monte Carlo estimate of the Expected Value is the sample mean:

$$
\hat{E}[X] = \frac{1}{n}\sum_{i=1}^{n} X_i
$$

For example:

```text
Rolls:
3, 6, 2, 4, 5

Estimated Expected Value:
4.0
```

With more rolls, the estimate generally moves closer to:

```text
3.5
```

---

## 🎯 Probability Distribution

The fair die is modeled as a discrete probability distribution:

```python
x = np.array([1, 2, 3, 4, 5, 6])

p_x = np.array([
    1/6,
    1/6,
    1/6,
    1/6,
    1/6,
    1/6
])
```

The distribution is created using SciPy:

```python
distribution_p_x = rv_discrete(
    values=(x, p_x)
)
```

A random sample is then generated from this distribution:

```python
sample_distribution_p_x = distribution_p_x.rvs(
    size=1
)[0]
```

---


## 🛠️ Technologies

| Technology | Purpose                           |
| ---------- | --------------------------------- |
| 🐍 Python  | Core programming language         |
| 🔢 NumPy   | Numerical computation             |
| 📐 SciPy   | Discrete probability distribution |
| 📊 Plotly  | Interactive visualization         |
| 🌐 Dash    | Interactive web application       |

---

## 📦 Installation



Install the required dependencies:

```bash
pip install dash numpy scipy plotly
```

---

## ▶️ Run the Application

Start the Dash application:

```bash
python app.py
```

The application runs on:

```text
http://127.0.0.1:8051/
```

Open the address in your browser and start rolling the dice.

---

## 📁 Project Structure

```text
Rolling/
│
├── Rolling_dice.py
│
├── assets/
│   ├── dice_1.png
│   ├── dice_2.png
│   ├── dice_3.png
│   ├── dice_4.png
│   ├── dice_5.png
│   └── dice_6.png
│
└── README.md
```

### `Rolling_dice.py`

Contains the Dash application, probability distribution, Monte Carlo sampling, Expected Value calculation, and Plotly visualization.

### `assets/`

Contains the dice images displayed by the Dash application.

### `README.md`

Project documentation and explanation of the underlying concepts.

---

## 🧠 Concepts Demonstrated

This project provides a practical introduction to several important concepts:

* **Expected Value**
* **Discrete Probability Distribution**
* **Random Sampling**
* **Sample Mean**
* **Monte Carlo Simulation**
* **Law of Large Numbers**
* **Data Visualization**
* **Interactive Dash Applications**

---

## 🔬 Connection to Reinforcement Learning

Monte Carlo simulation is also an important concept in **Reinforcement Learning**.

In Reinforcement Learning, Monte Carlo methods estimate value functions from sampled experiences and complete episodes.

The dice example provides a simple intuition:

```text
Random Samples
      ↓
Observed Outcomes
      ↓
Calculate Average
      ↓
Estimate Expected Value
      ↓
More Samples → Better Estimate
```

This simple experiment can therefore serve as an introduction to more advanced **Monte Carlo Prediction** methods used in Reinforcement Learning.

---

## 🚀 Future Improvements

Possible extensions of this project include:

* [ ] Add a configurable number of dice
* [ ] Add a reset button
* [ ] Display the number of rolls
* [ ] Display the theoretical Expected Value on the graph
* [ ] Compare theoretical and empirical distributions
* [ ] Add variance and standard deviation
* [ ] Add confidence intervals
* [ ] Add different probability distributions
* [ ] Extend the simulation to Monte Carlo methods in Reinforcement Learning

---

## 📚 Key Takeaway

> **The more samples we collect, the closer the sample average tends to get to the true Expected Value.**

For a fair six-sided die:

$$
\boxed{E[X] = 3.5}
$$

This project demonstrates this idea visually through an interactive Monte Carlo simulation.

---

## 👤 Author

**Abbas Nikbakht**

This project is part of a collection of practical examples for learning **Probability, Monte Carlo Methods, and Reinforcement Learning**.

