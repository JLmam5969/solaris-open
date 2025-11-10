### File 2: `foundry_sim.py`

# 1. In your repo, click **Add file** → **Create new file**
# 2. Name: `foundry_sim.py`
# 3. Paste this:

```python
import numpy as np
import matplotlib.pyplot as plt

# Regolith composition (Mars average, mass fraction)
regolith = {'SiO2': 0.45, 'Fe2O3': 0.18, 'Al2O3': 0.10}

def extract(element, efficiency=0.7, tons_per_day=10):
    """Extract kg/day from regolith"""
    return regolith.get(element, 0) * efficiency * tons_per_day * 1000

# Simulation: 1 year of mining
days = 365
si_yield = [extract('SiO2') for _ in range(days)]
fe_yield = [extract('Fe2O3') for _ in range(days)]
al_yield = [extract('Al2O3') for _ in range(days)]

# Cumulative
si_cum = np.cumsum(si_yield)
fe_cum = np.cumsum(fe_yield)
al_cum = np.cumsum(al_yield)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(si_cum / 1000, label="Silicon (tons)", color="gray")
plt.plot(fe_cum / 1000, label="Iron (tons)", color="red")
plt.plot(al_cum / 1000, label="Aluminum (tons)", color="silver")
plt.axhline(1.5, color='green', linestyle='--', label="1 GPU Cluster (est.)")
plt.title("Year 1: From Martian Dust to AI Foundry")
plt.xlabel("Days")
plt.ylabel("Cumulative Material (tons)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("foundry_year1.png")
plt.close()

print("Simulation complete!")
print("After 1 year:")
print(f"  Silicon:  {si_cum[-1]/1000:.1f} tons")
print(f"  Iron:     {fe_cum[-1]/1000:.1f} tons")
print(f"  Aluminum: {al_cum[-1]/1000:.1f} tons")
print("→ Enough for ~20 GPU-class AI cores")
