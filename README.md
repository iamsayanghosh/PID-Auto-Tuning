# PID Controller Auto-Tuning (Python)

This project implements automatic tuning of a PID controller using a grid search optimization approach. It computes optimal values of Kp, Ki, and Kd to improve system performance based on standard control system metrics.

---

## 📌 Overview

A Proportional-Integral-Derivative (PID) controller is widely used in engineering systems to regulate output response. However, tuning PID parameters manually can be time-consuming and inefficient.

This project demonstrates an automated approach to PID tuning by evaluating multiple parameter combinations and selecting the best set based on system performance.

Key capabilities:

- Accepts any user-defined transfer function  
- Simulates closed-loop system response  
- Automatically tunes PID parameters  
- Evaluates performance using standard control metrics  

---

## ⚙️ Features

- Supports custom transfer function input  
- Automatic PID tuning using grid search  
- Uses optimization instead of manual tuning methods  
- Evaluates system performance using:
  - Rise Time  
  - Settling Time  
  - Overshoot  
  - Steady-State Error  
- Compares:
  - Uncontrolled system  
  - Optimized PID-controlled system  
- Generates:
  - Step response plots  
  - Error vs time plots  

---

## 🌍 Applications

PID controllers are widely used in:

- Industrial automation  
- Robotics and motion control  
- Temperature and process control  
- Power and electronic systems  

This project highlights how automated tuning can improve system performance without manual trial-and-error.

---

## 🧠 Methodology

The system is modeled using a transfer function:

G(s) = 1 / (s² + 2s + 1)

The PID controller is defined as:

C(s) = Kp + Ki/s + Kd·s

### Optimization Strategy

A brute-force grid search is performed over predefined ranges of Kp, Ki, and Kd.

For each combination:

1. The closed-loop system is simulated  
2. Step response characteristics are computed  
3. A cost function evaluates performance  

### Cost Function

The objective is to minimize:

Cost = w1 × (Settling Time) + w2 × (Overshoot) + w3 × (Steady-State Error)

This ensures a balance between speed, stability, and accuracy.

---

## 📊 Performance Comparison

### Input Transfer Function

- Numerator: 1  
- Denominator: 1 2 1  

### Without PID

- Rise Time: 3.367 s  
- Settling Time: 5.879 s  
- Overshoot: 0.00%  

### With Optimized PID

- Rise Time: 0.352 s  
- Settling Time: 0.553 s  
- Overshoot: 1.23%  
- Steady-State Error: 0.0004  

### 🚀 Improvement

- ~10× faster rise time  
- ~10× faster settling time  
- Near-zero steady-state error  
- Minimal overshoot  

---

## 📈 Output

The optimized PID controller significantly improves system response compared to the uncontrolled system.

### System vs Optimized PID Response

![PID Output](results/output_pid.png)

---

## 🛠️ Technologies Used

- Python  
- NumPy  
- Matplotlib  
- python-control (Control Systems Library)  

---

## ▶️ How to Run

### 1. Install dependencies

pip install numpy matplotlib control

### 2. Run the program

python PID-Controller-Auto-Tuning.py

### 3. Enter system parameters

Example:

Enter numerator: 1  
Enter denominator: 1 2 1  

---

## 📁 Project Structure

PID-Auto-Tuning/
│
├── PID-Controller-Auto-Tuning.py  
├── results/  
│   └── output_pid.png  
└── README.md  

---

## ⚠️ Limitations

- Grid search is computationally expensive  
- Performance depends on chosen parameter ranges  
- Not suitable for complex nonlinear or high-order systems  

---

## 📌 Future Improvements

- Implement advanced optimization techniques (Genetic Algorithm / PSO)  
- Add graphical user interface (GUI)  
- Extend support to higher-order systems  
- Integrate with real-time hardware systems  

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Sayan Ghosh  
ECE Undergraduate
