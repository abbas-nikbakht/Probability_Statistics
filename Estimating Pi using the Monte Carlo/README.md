# Estimating π Using the Monte Carlo Method

This project demonstrates how the value of **π (Pi)** can be estimated using the **Monte Carlo Method** and randomly generated points.

The method is based on generating random points inside a square and determining how many of those points fall inside an inscribed circle. The ratio of points inside the circle to the total number of points can then be used to estimate π.

---

## 📌 Overview

The **Monte Carlo Method** is a computational technique that uses random sampling to approximate numerical results.

In this project, a circle with radius 1 is placed inside a square with side length 2. Random points are generated uniformly within the square.

For each generated point `(x, y)`, the following condition is used to determine whether the point lies inside the circle:

$$
x^2 + y^2 \leq 1
$$

The ratio between the number of points inside the circle and the total number of generated points approximates the ratio between the areas of the circle and the square:

$$
\frac{N_{\text{inside}}}{N_{\text{total}}}
\approx
\frac{\pi r^2}{(2r)^2}
=
\frac{\pi}{4}
$$

Therefore:

$$
\pi \approx 4
\frac{N_{\text{inside}}}{N_{\text{total}}}
$$

As the number of randomly generated points increases, the estimated value generally approaches the actual value of π.

---

## Features

* 🎲 Random point generation
* 🔵 Visualization of the circle and square
* 📍 Visualization of randomly generated points
* 🧮 Monte Carlo estimation of π
* 📊 Comparison between estimated π and the actual value
* 🔢 Configurable number of samples
* 📈 Visualization of the simulation process
* 🖥️ Interactive Plotly visualization
* ⚡ Dynamic point generation
* 📐 Equal x and y coordinate scales

---

## Technologies

| **Technology**        | **Purpose**                                         |
| --------------------- | --------------------------------------------------- |
| 🐍 Python             | Core programming language                           |
| 🔢 NumPy              | Random number generation and numerical calculations |
| 📊 Plotly             | Interactive visualization                           |
| 🎯 Monte Carlo Method | Estimation of π                                     |

---

## Installation

Install the required dependencies:

```bash
pip install numpy plotly
```

---

## Run the Application

Run the Python script:

```bash
python estimating_pi_monte_carlo.py
```

The application generates random points inside a square and determines whether each point is located inside or outside the circle.

The estimated value of π is calculated from the generated samples.

---

## 🧠 Concepts Demonstrated

This project provides a practical introduction to several important concepts:

* **Monte Carlo Simulation**
* **Random Sampling**
* **Uniform Distribution**
* **Numerical Estimation**
* **Probability**
* **Geometric Probability**
* **Area Ratios**
* **Circle and Square Geometry**
* **Convergence**
* **Statistical Approximation**
* **Data Visualization**

---

## 🚀 Future Improvements

Possible extensions of this project include:

* ✅ interactive input for the number of samples
* ✅ Add real-time point generation
* ✅ Display the current π estimate during the simulation
* Plot the estimation error as the number of samples increases
* ✅ Improve the interactive visualization
* ✅ Color-coding the data to understand this point
---

## 👤 Author

**Abbas Nikbakht**

This project was developed to demonstrate the **Monte Carlo Method** and understand how random sampling can be used to estimate mathematical quantities such as π.
