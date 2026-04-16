# CLAUDE.md

## Risk Management

Deploying code always carries risk. Employ proper version control and refactoring
strategies to mitigate risk.

### Version Control

- Make atomic commits: one commit per logical change (feature, fix, or
  refactor). Each commit should leave tests passing independently

### Refactoring Strategy

- Use the Strangler Fig pattern for incremental rewrites: replace pieces of
  the old system one at a time until the old code is fully gone.

## Style Guide

Enforce consistent style so that engineers and AI can parse code effectively
with less context cost.

### Formatting

- Functions and objects should follow vertical ordering: callers above callees,
  high-to-low within a module so that broad concepts are at the top and specific
  implementations are at the bottom.
