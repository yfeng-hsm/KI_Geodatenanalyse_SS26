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
- a PyVis graph panel on the left and an operation explanation panel on the right,
- directed red arrows for incoming messages into the selected target node,
- an animated message-flow strip that shows messages moving along the graph and a pulsing self-loop,
- node fill colors that preserve the current state value and boundary colors that mark the update role,
- node features before and after each update,
- normalized edge weights,
- the learnable weight matrix,
- per-neighbour messages for a selected target node,
- the result after stacking a second GNN layer.

The goal is to make message passing visible through an app-like workflow rather than a sequence of static images. Students can drag, zoom, and hover over the PyVis graph, follow red message arrows and the animated message-flow strip, click an update button, and watch node values and state colors change in place while boundary colors identify the current target, message-source neighbours, and nodes not used in the selected update.

### Part B: Real Graph Comparison

The second part uses the Cora citation network through PyTorch Geometric.

It compares:

- a feature-only MLP, which ignores graph edges,
- a GCN, which uses the same features plus neighbourhood structure.

The intended teaching point is that neighbourhood information can clearly improve node classification when connected observations are related. This is the bridge to geospatial AI examples where nearby cells, adjacent roads, linked images, or connected places often carry useful context.

## Colab Notes

The notebook installs `torch-geometric` in the first setup cell and keeps all execution outputs cleared in the repository. Students can open it in Colab and run from top to bottom.
