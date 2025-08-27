import sys
sys.path.insert(0, '..')

import oqupy
import numpy as np
import matplotlib.pyplot as plt

# Operators and initial state
sigma_x = oqupy.operators.sigma("x")
sigma_y = oqupy.operators.sigma("y")
sigma_z = oqupy.operators.sigma("z")
initial_state = oqupy.operators.spin_dm("z-")

# Gaussian pulse shape
def gaussian_shape(t, area=1.0, tau=1.0, t_0=0.0):
    return area / (tau * np.sqrt(np.pi)) * np.exp(-(t - t_0)**2 / (tau**2))

# Time-dependent Hamiltonian
def hamiltonian_t(t):
    return gaussian_shape(t, area=np.pi/2.0, tau=0.245)/2.0 * sigma_x

system = oqupy.TimeDependentSystem(hamiltonian_t)

# Bath definition
bath = oqupy.Bath(
    sigma_z / 2.0,
    oqupy.PowerLawSD(
        alpha=0.126,
        zeta=3,
        cutoff=3.04,
        cutoff_type='gaussian',
        temperature=0.1309
    )
)

# Test memory cutoffs
tcut_values = [1.0, 2.0, 3.0]
results = []

for tcut in tcut_values:
    print(f"Running simulation with tcut = {tcut}")
    parameters = oqupy.TempoParameters(dt=0.1, tcut=tcut, epsrel=1e-4)
    process_tensor = oqupy.pt_tempo_compute(
        bath=bath,
        start_time=-2.0,
        end_time=3.0,
        parameters=parameters   
    )
    dynamics = oqupy.compute_dynamics(
        process_tensor=process_tensor,
        system=system,
        initial_state=initial_state,
        start_time=-2.0,
        progress_type="silent"
    )
    t_vals, s_x = dynamics.expectations(sigma_x, real=True)
    _, s_y = dynamics.expectations(sigma_y, real=True)
    s_xy = np.sqrt(s_x**2 + s_y**2)
    results.append((t_vals, s_xy, tcut))

# Plot results
for t_vals, s_xy, tcut in results:
    plt.plot(t_vals, s_xy, label=rf"$t_{{\mathrm{{cut}}}} = {tcut}$")

plt.xlabel(r'$t\,/\mathrm{ps}$')
plt.ylabel(r'$\langle \sigma_{xy} \rangle$')
plt.title("Parameter Convergence Test: Varying $t_{cut}$")
plt.ylim((0.0, 1.0))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()