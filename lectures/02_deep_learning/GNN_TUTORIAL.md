# GNN Tutorial Notebook

This note links the Colab-ready tutorial for the graph neural network part of the deep learning lecture.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/lectures/02_deep_learning/notebooks/gnn_visual_message_passing_colab.ipynb)

## Notebook

- `notebooks/gnn_visual_message_passing_colab.ipynb`

## Teaching Structure

The notebook is designed for the third deep learning topic after neural networks/CNNs and transformers.

### Part A: Visual Message Passing

The first part uses a tiny graph and a hand-picked GCN-style update:

```text
H = ReLU(A_hat X W)
```

Students can inspect:

- an interactive widget app with `Update one layer` and `Reset` buttons,
- a single animated graph panel on the left and an operation explanation panel on the right,
- directed red arrows for incoming messages into the selected target node,
- animated message dots directly inside the same graph and a pulsing self-loop,
- compact hidden-state lights on each node instead of dense numeric node labels,
- boundary colors that mark the update role: red for the current target, yellow for neighbours, black for other nodes,
- node features before and after each update,
- normalized edge weights,
- the learnable weight matrix,
- per-neighbour messages for a selected target node,
- the result after stacking a second GNN layer.

The goal is to make message passing visible through an app-like workflow rather than a sequence of static images. Students follow red message arrows and animated dots inside the graph, click an update button, and watch hidden-state lights change in place. The right-hand panel visualizes how source hidden states, the weight matrix, edge weights, message vectors, summation, and ReLU produce the next target state.

### Part B: Real Graph Comparison

The second part uses the Cora citation network through PyTorch Geometric.

It compares:

- a feature-only MLP, which ignores graph edges,
- a GCN, which uses the same features plus neighbourhood structure.

The intended teaching point is that neighbourhood information can clearly improve node classification when connected observations are related. This is the bridge to geospatial AI examples where nearby cells, adjacent roads, linked images, or connected places often carry useful context.

## Colab Notes

The notebook installs `torch-geometric` in the first setup cell and keeps all execution outputs cleared in the repository. Students can open it in Colab and run from top to bottom.
