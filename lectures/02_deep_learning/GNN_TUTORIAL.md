# GNN Tutorial Notebook

This note links the Colab-ready tutorial for the graph neural network part of the deep learning lecture.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/lectures/02_deep_learning/notebooks/gnn_visual_message_passing_colab.ipynb)

## Notebook

- `notebooks/gnn_visual_message_passing_colab.ipynb`

## Teaching Plan

- `GNN_VISUALIZATION_PLAN.md`

## Teaching Structure

The notebook is designed for the third deep learning topic after neural networks/CNNs and transformers.

### Module 1: Visual Node Classification Demo

This module is a teaching demo, not a trained model. It uses a tiny graph as a node classification task. Each node has three evidence features:

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

### Module 2: Train a Graph Neural Network

This module should be framed as the real modelling exercise. Here students should train model weights with labels and compare a graph-aware model against a feature-only baseline.

Recommended exercise flow:

1. Load a graph dataset such as Cora through PyTorch Geometric.
2. Train a feature-only MLP that ignores edges.
3. Train a GCN that uses the same features plus `edge_index`.
4. Compare validation/test accuracy and training curves.
5. Inspect one node where the GCN is correct and the MLP is wrong.
6. Discuss whether neighbourhood context helps or hurts.

The important contrast is:

```text
Visual demo:
fixed toy weights, designed for explanation

Training exercise:
learned model weights, evaluated on held-out nodes
```

In a standard GCN, the graph edges and normalized edge weights are usually fixed. The trainable part is the neural weight matrices. If students ask whether edge importance can be learned, use that as the bridge to GAT/attention:

```text
GCN: fixed adjacency weights, learned feature transformation W
GAT: learned attention score for each neighbour
```

### Current Real Graph Comparison

The current second part uses the Cora citation network through PyTorch Geometric.

It compares:

- a feature-only MLP, which ignores graph edges,
- a GCN, which uses the same features plus neighbourhood structure.

The intended teaching point is that neighbourhood information can clearly improve node classification when connected observations are related. This is the bridge to geospatial AI examples where nearby cells, adjacent roads, linked images, or connected places often carry useful context.

## Student Confusion Points

### Edge weights do not update in the demo

Students may read the animated red edges as learned edge weights. Make explicit that the grey graph structure is fixed. Red animation only means "this fixed edge is used for the selected target's current message passing step."

### Hidden states are not labels

The lights on each node are hidden/evidence values, not the final class itself. The class prediction is computed from those hidden values. This distinction matters because hidden states can become more road-like, water-like, or mixed before the visible label changes.

### More layers are not automatically better

A larger receptive field can help because a node can see more context. It can also hurt if different classes are mixed across boundaries. This is over-smoothing. The visual demo includes 25% self-retention so students can see wider context without immediately erasing local evidence.

### The visual demo is hand-designed

The demo uses fixed toy features and fixed toy weights to make message passing visible. It is not "training." The training exercise is where `W` is learned from labels and evaluated.

### GCN and GAT answer different questions

GCN answers: "Given this graph, how do neighbour features change node representations?"

GAT adds: "Which neighbours should matter more, and can the model learn that importance?"

## Colab Notes

The notebook installs `torch-geometric` in the first setup cell and keeps all execution outputs cleared in the repository. Students can open it in Colab and run from top to bottom.
