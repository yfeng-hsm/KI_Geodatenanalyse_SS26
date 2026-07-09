# GNN Visualization Teaching Plan

This plan separates the GNN material into two teaching modules.

## Module 1: Visual Demo

Purpose: make message passing visible before training a model.

The demo uses a small `river / street / mixed` node classification task. Each node has three evidence channels:

```text
water, road, urban/mixed context
```

Students should see:

- fixed graph edges: who can send messages to whom,
- node hidden/evidence values: the three lights on each node,
- current prediction: `river`, `street`, or `mixed`,
- selected target node: red boundary,
- direct message sources: yellow boundary,
- other nodes: black boundary,
- animated messages along fixed edges,
- one-hop and two-hop receptive field growth,
- over-smoothing risk when too much neighbour information is mixed.

The demo uses a residual GCN-style update:

```text
H_next = ReLU(0.25 * H_current + 0.75 * A_hat H_current W)
```

This is intentional. The residual term keeps local evidence visible so students can see a wider receptive field without immediately washing out boundary-node information.

## Module 2: Training Exercise

Purpose: show what is actually learned.

Students train and compare:

- feature-only MLP: uses node features only,
- GCN: uses node features and graph edges.

The exercise should make clear:

- `edge_index` is usually fixed in a standard GCN,
- normalized edge weights come from graph structure,
- neural weights `W` are learned from labels,
- hidden states change during forward passes,
- model parameters change during training,
- a GNN can outperform an MLP when connected nodes share useful context.

## Student Confusion Points

### 1. Are edge weights learned?

In the visual GCN demo, no. Edges and normalized adjacency weights are fixed.

What changes:

- hidden states,
- predictions,
- in a training exercise, neural weights.

What does not change in a standard GCN:

- graph connectivity,
- normalized adjacency weights.

Bridge concept:

```text
GCN: fixed adjacency weights
GAT: learned attention over neighbours
```

### 2. Why can classification get worse after more layers?

More layers mean a larger receptive field. That can help, but it can also mix different classes across boundaries. This is over-smoothing.

Teaching phrasing:

```text
More context is useful only if the model keeps the relevant local signal.
```

### 3. Are hidden lights the class?

No. Hidden lights are evidence channels. The predicted class is computed from these values.

Teaching phrasing:

```text
The lights are what the node currently knows.
The label is what the model predicts from that knowledge.
```

### 4. Is the visual demo trained?

No. It is hand-designed for explanation.

Teaching phrasing:

```text
Module 1 explains the mechanics.
Module 2 trains a model and tests whether the graph helps.
```

### 5. Why keep 25% of the old node state?

It prevents local evidence from being erased too quickly. This makes the demo more stable and introduces the idea behind residual connections.

## Suggested Classroom Flow

1. Start with the visual demo at layer 0.
2. Ask students to classify node 4 using only its three evidence lights.
3. Click one update and show how direct neighbours change node 4.
4. Click a second update and discuss the larger receptive field.
5. Pause to explain that edges did not update.
6. Discuss over-smoothing and why residual/self-retention helps.
7. Move to the training exercise.
8. Train MLP and GCN on Cora.
9. Compare test accuracy and inspect a node where graph context helps.
10. End with the GCN versus GAT distinction.

## Design Boundary

Keep the visual demo simple. It should not try to show backpropagation, gradient descent, train/test splits, and learned parameters at the same time.

Keep the training exercise real. It should not use hand-designed toy weights; it should train model parameters and evaluate held-out nodes.
