# KI_Geodatenanalyse_SS26

Course repository for the Summer Semester 2026 module on AI for geospatial data analysis.

This repository is organized as a teaching workspace: each lecture has its own folder, and reusable project data loaders are kept separately from lecture material. Detailed content will be developed lecture by lecture.

## Course Structure

| Folder | Topic | Core focus |
| --- | --- | --- |
| `lectures/01_machine_learning/` | Machine learning basics | Simple ML workflows, interpretable models, tree models |
| `lectures/02_deep_learning/` | Deep learning | Neurons, optimization, CNNs, Transformers, GNNs |
| `lectures/03_llm_basics/` | LLM basics | Tokenization, embeddings, prompting, retrieval, geospatial use cases |
| `lectures/04_spatial_data_analysis/` | Spatial data analysis | Review of common spatial analysis concepts and tools |
| `lectures/05_ethics_bias/` | Ethics and bias | Fairness, bias, accountability, responsible use of geospatial AI |

Note: the course is planned as five lectures. The ethics and bias topic is placed as lecture 5, even though it may have been referred to as lecture 6 in early notes.

## Repository Layout

```text
.
├── lectures/
│   ├── 01_machine_learning/
│   ├── 02_deep_learning/
│   ├── 03_llm_basics/
│   ├── 04_spatial_data_analysis/
│   └── 05_ethics_bias/
└── data_loaders/
    ├── zensus/
    ├── airbnb/
    ├── mapillary/
    ├── osm_unfall_atlas/
    └── meinrad/
```

## Notebook Index

| Lecture | Notebook | Colab |
| --- | --- | --- |
| 01 Machine Learning | [Exercise 1.2: Supervised Learning with scikit-learn and PyTorch](lectures/01_machine_learning/notebooks/exercise_1_2_supervised_learning.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/lectures/01_machine_learning/notebooks/exercise_1_2_supervised_learning.ipynb) |
| 01 Machine Learning | [Exercise 1.3: Classification and Clustering on a Small Spatial Dataset](lectures/01_machine_learning/notebooks/exercise_1_3_classification_clustering.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/lectures/01_machine_learning/notebooks/exercise_1_3_classification_clustering.ipynb) |
| 02 Deep Learning | [Exercise 2.1: Basic Neural Network Training with PyTorch](lectures/02_deep_learning/notebooks/exercise_2_1_basic_neural_network_tabular.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/lectures/02_deep_learning/notebooks/exercise_2_1_basic_neural_network_tabular.ipynb) |
| 02 Deep Learning | [Exercise 2.2: A Small CNN for MNIST with PyTorch](lectures/02_deep_learning/notebooks/exercise_2_2_mnist_cnn_pytorch.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/lectures/02_deep_learning/notebooks/exercise_2_2_mnist_cnn_pytorch.ipynb) |
| 02 Deep Learning | [Graph Neural Networks: Visual Demo and Training Exercise](lectures/02_deep_learning/notebooks/gnn_visual_message_passing_colab.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/lectures/02_deep_learning/notebooks/gnn_visual_message_passing_colab.ipynb) |
| 03 LLM Basics | [Testing the Uni Mainz KI-Chat API](lectures/03_llm_basics/notebooks/uni_mainz_ki_chat_api_test.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/lectures/03_llm_basics/notebooks/uni_mainz_ki_chat_api_test.ipynb) |
| 03 LLM Basics | [Testing the AcademicCloud/GWDG SAIA Chat AI API](lectures/03_llm_basics/notebooks/academiccloud_saia_api_test.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/lectures/03_llm_basics/notebooks/academiccloud_saia_api_test.ipynb) |

## Teaching Design Principles

- Start from transparent and inspectable models before moving to more complex architectures.
- Keep geospatial examples central, instead of treating geodata as a generic tabular or image dataset.
- Use one or more shared project datasets across lectures so students can compare methods on familiar data.
- Separate conceptual material, practical notebooks, assignments, and reusable data access code.
- Make model limitations, uncertainty, bias, and ethical implications part of the technical workflow.

## Data Loader Area

The `data_loaders/` folder is reserved for reusable project data access code and dataset notes. The first planned datasets are:

1. Zensus 2022 grid-cell data
2. Airbnb data
3. Mapillary data
4. OSM Unfallatlas data
5. meinRad Mainz bike-sharing snapshots

Each dataset folder should eventually contain dataset documentation, setup instructions, preprocessing notes, and Python loader utilities.
