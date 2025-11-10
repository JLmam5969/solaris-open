THRESHOLD_STRAIN = 0.02  # 2% deformation triggers repair
LASER_POWER = 1200       # °C
POWDER_FEED = 0.1        # mm per layer

def read_strain_gauge():
    import random
    return random.uniform(0, 0.05)  # Simulated

def heat_laser(temp):
    print(f"[REPAIR] Laser ON → {temp}°C")

def deposit_layer(thickness_mm):
    print(f"[REPAIR] Depositing {thickness_mm}mm Fe-Ni layer")

def anneal(temp, seconds):
    print(f"[REPAIR] Annealing at {temp}°C for {seconds}s")

# Main repair loop
while True:
    strain = read_strain_gauge()
    if strain > THRESHOLD_STRAIN:
        print(f"[ALERT] Strain {strain:.3f} > {THRESHOLD_STRAIN} → Repairing...")
        heat_laser(LASER_POWER)
        deposit_layer(POWDER_FEED)
        anneal(600, 30)
        print("[REPAIR] Complete. Rib restored.\n")
    else:
        print(f"[OK] Strain {strain:.3f} → No action.")
    
    import time
    time.sleep(2)  # Simulate 1-hour cycle
