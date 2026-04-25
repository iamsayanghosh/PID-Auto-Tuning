# PID Controller Auto-Tuning (Python)

This project implements automatic tuning of a PID controller using grid search optimization.

## 🔧 Features

* Accepts custom transfer function input
* Automatically finds optimal Kp, Ki, Kd
* Optimizes:

  * Rise Time
  * Settling Time
  * Overshoot
  * Steady-state error
* Visual comparison of system response

## 📊 Output

![PID Response](results/output_pid.png)

## 📈 Example Performance

* Rise Time: ~0.35 s
* Settling Time: ~0.55 s
* Overshoot: ~1.2%
* Steady-state error: ~0

## ▶️ How to Run

```bash
pip install control numpy matplotlib
python PID-Controller-Auto-Tuning.py
```

## 🧠 Concepts Used

* PID Control Systems
* Grid Search Optimization
* Step Response Analysis

## 📌 Author

Sayan Ghosh
