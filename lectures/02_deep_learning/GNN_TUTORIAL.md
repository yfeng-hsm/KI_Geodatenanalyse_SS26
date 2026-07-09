# GNN Tutorial Notebook

This note links the Colab-ready tutorial for the graph neural network part of the deep learning lecture.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/lectures/02_deep_learning/notebooks/gnn_visual_message_passing_colab.ipynb)

## Notebook

- `notebooks/gnn_visual_message_passing_colab.ipynb`

## Teaching Structure

The notebook is designed for the third deep learning topic after neural networks/CNNs and transformers.

### Part A: Visual Node Classification

The first part uses a tiny graph as a node classification task. Each node has three evidence features:

```text
water, road, urban/mixed context
```

The app predicts one of three classes:

```text
river, street, mixed
```

The GCN-style update is still:

```text
H_next = ReLU(0.25 * H_current + 0.75 * A_hat H_current W)
```

The residual/self-retention term is included for teaching stability: it keeps part of each node's own evidence while neighbourhood messages are mixed in. Without this, a second layer can over-smooth boundary nodes and make some classifications worse.

Students can inspect:

- an interactive widget app with `Update one layer` and `Reset` buttons,
- a single animated graph panel on the left and an operation explanation panel on the right,
- directed red arrows for incoming messages into the selected target node,
- animated message dots directly inside the same graph and a pulsing self-loop,
- compact hidden-state lights for the three evidence channels instead of dense numeric node labels,
- current node predictions shown as `river`, `street`, or `mixed`,
- boundary colors that mark the update role: red for the current target, yellow for neighbours, black for other nodes,
- one-hop and two-hop receptive field explanations,
- a note that wider receptive fields are useful only when they preserve relevant local evidence,
- node features before and after each update,
- normalized edge weights,
- the learnable weight matrix,
- per-neighbour messages for a selected target node,
- the result after stacking a second GNN layer.

The goal is to make message passing visible through an app-like workflow rather than a sequence of static images. Students follow red message arrows and animated dots inside the graph, click an update button, and watch hidden-state lights and class predictions change in place. The intentionally ambiguous crossing node starts closer to `mixed`; after it absorbs neighbourhood evidence, the `street` signal becomes stronger. The right-hand panel visualizes how source hidden states, the weight matrix, fixed edge weights, residual self-retention, message vectors, summation, and ReLU produce the next target state and prediction.

### Part B: Real Graph Comparison

The second part uses the Cora citation network through PyTorch Geometric.

It compares:

- a feature-only MLP, which ignores graph edges,
- a GCN, which uses the same features plus neighbourhood structure.

The intended teaching point is that neighbourhood information can clearly improve node classification when connected observations are related. This is the bridge to geospatial AI examples where nearby cells, adjacent roads, linked images, or connected places often carry useful context.

## Colab Notes

The notebook installs `torch-geometric` in the first setup cell and keeps all execution outputs cleared in the repository. Students can open it in Colab and run from top to bottom.
