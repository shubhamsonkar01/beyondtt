# Beyond the Teacher: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning

Project page and supplementary material for the ICRA 2026 paper: **Beyond the Teacher: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning**.

[![Website](https://img.shields.io/badge/Project-Page-blue.svg)](https://focaslab.com/) *(Coming soon)*
[![Paper](https://img.shields.io/badge/arXiv-Coming%20Soon-b31b1b.svg)](#)
[![Video](https://img.shields.io/badge/Video-YouTube-FF0000.svg)](https://youtu.be/sEGpXu0vF7Q)

### Authors
S. Saharsh\*, Shubham Sonkar\*, Pushpak Jagtap, Ravi Prakash  
*\*Equal contribution*  

**Cyber Physical Systems, Indian Institute of Science (IISc), Bengaluru, India**  
[HiRO Lab](https://hiro.cps.iisc.ac.in/) | [FoCAS Lab](https://www.focaslab.com/)

---

## Abstract

Imitation learning (IL) provides a powerful mechanism for robots to acquire complex skills from human demonstrations. However, standard IL approaches are highly sensitive to the quality of training data, heavily relying on expert demonstrations to learn effective policies. In practice, collecting purely expert data is expensive, time-consuming, and prone to human error, resulting in datasets that often exhibit large variations in skill level. 

To address this challenge, we present a novel IL pipeline that robustly learns from mixed-quality—or even predominantly naive—demonstrations. Our method extends Periodic Dynamic Movement Primitives (DMPs) to model cyclic robot motions and introduces an LSTM-based trajectory scoring and refinement mechanism. By estimating the expertise level of individual demonstrations, our network learns to dynamically adjust the trajectory parameters, bringing sub-optimal execution closer to expert-like behavior. 

We evaluate our proposed framework on a real-world Franka Emika Panda robotic manipulator across three distinct dynamic object manipulation tasks: Wiping, Pick-and-Place, and Weaving. Our experimental results demonstrate that the proposed method significantly outperforms baseline approaches (such as standard BC, Traj-BC, ILEED, and Neural-ODE) when trained on noisy datasets, consistently generating smooth, goal-directed, and stable trajectories that approach true expert performance.

---

## Code Structure

This repository contains the source code for the interactive project website.

```text
research-paper-website/
├── index.html              # Main project page (HTML/JS)
├── static/                 
│   └── css/
│       └── style.css       # Styling and layout
├── fig8/                   # Rollout plots for Wiping task
├── fig9/                   # Rollout plots for Pick-and-Place
├── fig10/                  # Rollout plots for Weaving
├── pnpdata/                # Pick-and-Place trajectory data
├── weavingdata/            # Weaving trajectory data
├── wipingdata/             # Wiping trajectory data
├── trajectory_data.json    # Processed demonstration trajectories
├── rollout_data.json       # Processed rollout trajectories
└── README.md
```

## Running the Website Locally

To view the interactive 3D Plotly plots locally, you'll need to serve the directory using a local web server (opening the HTML file directly in the browser restricts loading local JSON files).

1. Open your terminal in this repository.
2. Run a simple Python HTTP server:
   ```bash
   python3 -m http.server 8080
   ```
3. Open `http://localhost:8080` in your web browser.

## BibTeX

If you find our work useful, please consider citing:

```bibtex
@inproceedings{saharsh2026beyond,
  title     = {Beyond the Teacher: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning},
  author    = {Saharsh, S. and Sonkar, Shubham and Jagtap, Pushpak and Prakash, Ravi},
  booktitle = {Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
  year      = {2026},
  address   = {Bengaluru, India}
}
```

## Acknowledgments

This research was conducted at the [HiRO Lab](https://hiro.cps.iisc.ac.in/) and [FoCAS Lab](https://www.focaslab.com/) at the Cyber Physical Systems department, Indian Institute of Science (IISc). The website template is lightly adapted from Nerfies.
