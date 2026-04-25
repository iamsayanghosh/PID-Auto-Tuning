# PID Controller Auto-Tuning (Python)

This project implements automatic tuning of a PID controller using grid search optimization.
It finds optimal values of (K_p), (K_i), and (K_d) to improve system performance based on key control metrics.

---

## 📌 Overview

A Proportional-Integral-Derivative (PID) controller is widely used in control systems to regulate output response.

This project:

* Accepts any transfer function as input
* Simulates system response
* Searches for the best PID parameters
* Optimizes performance automatically

---

## ⚙️ Features

* Accepts custom transfer function input
* Automatic PID tuning using grid search
* Evaluates system using:

  * Rise Time
  * Settling Time
  * Overshoot
  * Steady-state error
* Compares system behavior:

  * Without PID
  * With optimized PID
* Generates response and error plots

---

## 🧠 Methodology

The system is modeled using a transfer function:

[
G(s) = \frac{1}{s^2 + 2s + 1}
]

A PID controller is defined as:

[
C(s) = K_p + \frac{K_i}{s} + K_d s
]

The algorithm:

1. Iterates over a range of (K_p, K_i, K_d)
2. Simulates closed-loop response
3. Calculates performance metrics
4. Uses a cost function to select optimal parameters

---

## 📊 Performance Comparison

### Input Transfer Function

Numerator: `1`
Denominator: `1 2 1`

### Without PID

* Rise Time: **3.367 s**
* Settling Time: **5.879 s**
* Overshoot: **0.00%**

### With Optimized PID

* Rise Time: **0.352 s**
* Settling Time: **0.553 s**
* Overshoot: **1.23%**
* Steady-state error: **0.0004**

### 🚀 Improvement

* ~10× faster rise time
* ~10× faster settling time
* Very low steady-state error
* Minimal overshoot

---

## 📈 Output

### System vs Optimized PID Response

---

## 🛠️ Technologies Used

* Python
* NumPy
* Matplotlib
* Control Systems Library (`python-control`)

---

## ▶️ How to Run

1. Install dependencies:

```
pip install numpy matplotlib control
```

2. Run the script:

```
python PID-Controller-Auto-Tuning.py
```

3. Enter transfer function:

```
Enter numerator: 1
Enter denominator: 1 2 1
```

---

## 📁 Project Structure

```
PID-Auto-Tuning/
│
├── PID-Controller-Auto-Tuning.py
├── results/
│   └── output_pid.png
└── README.md
```

---

## 📌 Future Improvements

* Implement advanced optimization (Genetic Algorithm / PSO)
* GUI for easier input/output
* Support for higher-order systems
* Real-time simulation integration

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Sayan Ghosh
ECE Undergraduate
