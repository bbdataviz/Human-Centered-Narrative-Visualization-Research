# Human-Centered-Narrative-Visualization-Research

This repository documents the research and design process that led to the development of the **HG Story**. It contains the original narrative visualization prototypes, data processing pipeline, design iterations, and supplementary material associated with my Master's thesis and the subsequent IEEE VIS publication.

The project began in 2023 at the University of Bergen as the visualization research project *"Visualizing Untold Stories through a Human Lens"*. It evolved through several research phases, including iterative prototype development, user studies, and empirical evaluation, before culminating in the modern React-based **HG Story** web application.

The research explores how narrative visualization and human-centered design can communicate the personal experiences behind medical data. As a case study, it focuses on **Hyperemesis gravidarum (HG)**, a severe pregnancy condition, using data from the **Norwegian Mother, Father and Child Cohort Study (MoBa)**.

The original prototypes were developed using **HTML5, CSS3, JavaScript, and D3.js**, combining interactive visualizations, illustration, animation, and storytelling techniques to create accessible and emotionally engaging data stories.

---


## 🔭 Project Evolution

🌱 [Research prototypes (2023–2024)](https://github.com/bbdataviz/Human-Centered-Narrative-Visualization-Research)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓ <br>
🧪 [Master's thesis (2025)](https://github.com/bbdataviz/Emotional-Engagement-in-Narrative-Medical-Visualization)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓ <br>
📄 IEEE VIS publication (2026)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓ <br>
🚀 [HG Story (React application)](https://github.com/bbdataviz/hg-story)


| Goals (2025) | Status | 
|---|---|
| Refactor into a React architecture | ✅ Completed | 
| Create reusable visualization components | ✅ Completed | 
| Reduce code redundancy | ✅ Completed | 
| Improve maintainability | ✅ Completed | 
| Improve accessibility	| ✅ Completed | 
| Improve desktop responsiveness | 🚧 In test mode | 
| Mobile responsiveness	| 🚧 In progress | 

---

## 💡 Motivation

This project explores how interactive visualization and storytelling can communicate personal experiences behind medical data.

Through this project, I had the opportunity to experiment with data visualization metaphors and raise awareness of a disease that is often overlooked or mistaken for normal pregnancy nausea.

--- 

## 🔬 Research and Data Exploration

As part of the project, exploratory analysis was conducted on subsets of MoBa data to investigate whether selected side symptoms differed between women affected by nausea and vomiting during pregnancy and those without symptoms.

The project development involved regular discussions with a bioinformatics researcher to better understand the medical and analytical context of the data.

The exploratory work and visualization concepts contributed to ideas that later became part of a multi-year research grant related to Hyperemesis gravidarum research.

---

## ✨ Features

- interactive D3.js-based data visualizations
- incremental chart construction and guided narrative flow
- animated focus transitions for small-scale data patterns
- illustration-driven UI with interactive quote elements
- dual narrative perspectives:
 - an individual story centered around a human protagonist
 - a neutral, generalized data-driven perspective
- iceberg metaphor for communicating visible and hidden aspects of disease experiences
- responsive visual hierarchy and typography integration

---

## 📸 Narrative Comparison

### Narrative Introduction

| Individual Perspective | Collective Perspective |
|---|---|
| ![Protagonist illustration](./screenshots/img1-1.png) | ![Infographic showing prevalence](./screenshots/img2-1.png) |
| Personal narrative introduction | Statistical introduction to HG prevalence |

### Conflict and Disease Experience

| Individual Perspective | Collective Perspective |
|---|---|
| ![Protagonist drowning in the ocean](./screenshots/img1-2.png) | ![Ambulance emergency](./screenshots/img2-2.png) |
| Emotional burden visualized through metaphor | Clinical emergency framing |

### Data Visualization

| Individual Perspective | Collective Perspective |
|---|---|
| ![Personalized data visualization with quotes from the protagonist](./screenshots/img1-3.png) | ![Data visualization with quotes from multiple women](./screenshots/img2-3.png) |
| Visualization combined with an individual voice | Visualization using collective patient experiences |

### Resolution

| Individual Perspective | Collective Perspective |
|---|---|
| ![Protagonist reflecting on motherhood](./screenshots/img1-4.png) | ![Illustrated reflection and summary](./screenshots/img2-4.png) |
| Personal reflection and resolution | Collective reflection and summary |

---

## 🧬 MoBa Data Availability

Data from the Norwegian Mother, Father and Child Cohort Study (MoBa) are managed by the Norwegian Institute of Public Health and are subject to ethical approval and GDPR regulations.

Due to participant privacy restrictions, the dataset cannot be publicly redistributed. Researchers seeking access must apply through the Norwegian health data services platform and obtain approval from the appropriate ethics committees and data owners.


Link: [MoBa – Norwegian Mother, Father and Child Cohort Study](https://www.fhi.no/en/ch/studies/moba/)

---

## 🛠 Tech Stack

- D3.js
- JavaScript
- HTML5
- CSS3

---

## 📊 Repository Contents
```
archive/
├── individual-story/     Original individualized narrative visualization prototype
└── general-story/        Original generalized narrative visualization prototype

data-processing/
├── data/                 Source datasets
├── processed/            Processed datasets used for the prototypes
└── documentation/        Data processing scripts and documentation

screenshots/              Figures illustrating the research prototypes
```
---

## 🎨 Design Notes

The UI combines data visualization with vector illustration to increase emotional engagement.

The project emphasizes:

- accessible visualization design
- readability and visual hierarchy
- harmonious color palettes

---

🧠 What I Learned

This project gave me practical experience with:

- designing interactive visualization flows
- structuring frontend-heavy applications
- translating sensitive medical topics into accessible visual communication
- balancing aesthetics, readability, and usability
- iterative design refinement through user feedback

---

## 📄 License

This project is licensed under the MIT License.
Copyright (c) 2026 Beatrice Budich
