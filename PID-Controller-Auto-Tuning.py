import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
import os

def evaluate_system(closed, t_sim):
    """Return metrics + response; None if invalid/unstable."""
    try:
        t, y = ctrl.step_response(closed, T=t_sim)
        info = ctrl.step_info(closed, T=t_sim)

        if (
            np.isnan(info['SettlingTime']) or
            info['SettlingTime'] > 50 or
            np.isnan(y).any()
        ):
            return None

        sse = abs(1 - y[-1])

        score = (
            info['SettlingTime'] +
            0.5 * info['RiseTime'] +
            0.1 * info['Overshoot'] +
            5 * sse
        )

        return score, info, t, y

    except Exception:
        return None


def tune_pid(system, t_sim):
    best_score = float('inf')
    best_params = (0, 0, 0)

    for Kp in np.linspace(5, 15, 10):
        for Ki in np.linspace(1, 6, 10):
            for Kd in np.linspace(1, 5, 10):

                pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
                closed = ctrl.feedback(pid * system)

                result = evaluate_system(closed, t_sim)
                if result is None:
                    continue

                score, _, _, _ = result

                if score < best_score:
                    best_score = score
                    best_params = (Kp, Ki, Kd)

    return best_params


def main():
    num = list(map(float, input("Enter numerator: ").split()))
    den = list(map(float, input("Enter denominator: ").split()))

    system = ctrl.TransferFunction(num, den)
    t_sim = np.linspace(0, 10, 200)

    # 🔍 Tune PID
    Kp, Ki, Kd = tune_pid(system, t_sim)

    print("\nBest PID Parameters:")
    print(f"Kp = {Kp:.3f}, Ki = {Ki:.3f}, Kd = {Kd:.3f}")

    # Final system
    pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
    closed_loop = ctrl.feedback(pid * system)

    # Responses
    t1, y1 = ctrl.step_response(system, T=t_sim)
    t2, y2 = ctrl.step_response(closed_loop, T=t_sim)

    info_open = ctrl.step_info(system, T=t_sim)
    info_closed = ctrl.step_info(closed_loop, T=t_sim)

    print("\n--- WITHOUT PID ---")
    print(f"Rise Time       : {info_open['RiseTime']:.3f} s")
    print(f"Settling Time   : {info_open['SettlingTime']:.3f} s")
    print(f"Overshoot       : {info_open['Overshoot']:.2f} %")

    print("\n--- WITH OPTIMIZED PID ---")
    print(f"Rise Time       : {info_closed['RiseTime']:.3f} s")
    print(f"Settling Time   : {info_closed['SettlingTime']:.3f} s")
    print(f"Overshoot       : {info_closed['Overshoot']:.2f} %")
    print(f"Steady-state err: {abs(1 - y2[-1]):.4f}")

    # 📊 Combined Plot (professional)
    plt.figure(figsize=(10, 8))

    # System response
    plt.subplot(2, 1, 1)
    plt.plot(t1, y1, label="Without PID")
    plt.plot(t2, y2, label="Optimized PID")
    plt.axhline(1, linestyle='--', label='Reference')
    plt.title("System vs Optimized PID Response")
    plt.ylabel("Output")
    plt.legend()
    plt.grid()

    # Error plot
    plt.subplot(2, 1, 2)
    plt.plot(t2, 1 - y2)
    plt.title("Error vs Time (PID)")
    plt.xlabel("Time")
    plt.ylabel("Error")
    plt.grid()

    plt.tight_layout()

    # 💾 Save output (for GitHub)
    os.makedirs("results", exist_ok=True)
    plt.savefig("results/output_pid.png")

    plt.show()


if __name__ == "__main__":
    main()