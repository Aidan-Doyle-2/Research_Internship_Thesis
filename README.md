# Comparing Markovian and Non-Markovian Dynamics in Quantum Gate Fidelity

This repository contains my MSc dissertation research, which investigates how memory effects in open quantum systems influence the performance of quantum gates. Using the **OQuPy** simulation framework, I modelled bosonic environments interacting with qubits through process tensors to study **Markovian** (memoryless) and **non-Markovian** (memory-retaining) dynamics.

## 🧠 Overview

Realistic quantum devices are inherently open systems that interact with their surroundings, causing **decoherence** and **noise**. While Markovian models assume information loss is irreversible, **non-Markovian dynamics** allow information to flow back into the system, potentially enhancing gate performance.

## 🧩 Research Focus

- Constructed **process tensors** to capture environmental memory  
- Coupled qubits to **bosonic harmonic baths**  
- Extracted **superoperators**, **Choi matrices**, and **Kraus operators**  
- Computed **average gate fidelities** with target unitary gates  
- Compared coherence retention and fidelity under Markovian vs non-Markovian dynamics  

## 🔬 Key Findings

- Memory-backflow in non-Markovian systems **slows decoherence** and **improves average gate fidelity**  
- Bloch vector components remain stable longer under memory effects  
- Excessive backflow or Lamb-shifts can offset benefits in more complex Hamiltonians  
- Demonstrates that non-Markovianity can be treated as a **useful resource** for realistic quantum gate design  

## 🧰 Tools and Methods

- **Python**, **OQuPy v0.5.0**, **NumPy**, **Matplotlib**  
- Process tensor construction using the **TEMPO algorithm**  
- Fidelity analysis via **Kraus decomposition** and **Choi matrices**

## 📄 Full Thesis

For complete details, equations, and simulation results, read the full dissertation:

[📘 Read the full thesis (PDF)](https://github.com/Aidan-Doyle-2/Research_Internship_Thesis/blob/master/Aidan_Doyle_Dissertation_Final_Final.pdf)
