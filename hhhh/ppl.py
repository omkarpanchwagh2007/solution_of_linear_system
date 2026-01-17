import numpy as np
import matplotlib.pyplot as plt

def simulate_projectile(v0, angle_deg, g=9.81):
    # Convert angle to radians
    theta = np.radians(angle_deg)
    
    # Calculate flight parameters
    t_flight = (2 * v0 * np.sin(theta)) / g
    t_max_height = t_flight / 2
    max_height = (v0 * np.sin(theta))**2 / (2 * g)
    max_range = (v0**2 * np.sin(2 * theta)) / g
    
    # Generate time points (100 points from start to finish)
    t = np.linspace(0, t_flight, 100)
    
    # Calculate X and Y positions
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    
    return {
        "x": x, "y": y,
        "t_flight": t_flight,
        "max_height": max_height,
        "max_range": max_range,
        "v0": v0,
        "angle": angle_deg
    }

def plot_trajectory(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data["x"], data["y"], label=f"{data['v0']} m/s at {data['angle']}°")
    plt.axhline(0, color='black', linestyle='--') # Ground line
    
    # Formatting
    plt.title("Projectile Motion Trajectory")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.ylim(bottom=0)
    plt.show()

# Execution
launch_velocity = int(input("Enter launch velocity (m/s): "))  # m/s
launch_angle = int(input("Enter launch angle (degrees): "))   # degrees

results = simulate_projectile(launch_velocity, launch_angle)

# Output Analysis
print(f"--- Analysis for {launch_angle}° at {launch_velocity} m/s ---")
print(f"Time of Flight: {results['t_flight']:.2f} s")
print(f"Max Height:     {results['max_height']:.2f} m")
print(f"Total Range:    {results['max_range']:.2f} m")

plot_trajectory(results)