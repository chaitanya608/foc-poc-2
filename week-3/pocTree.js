"use strict";
/**
 * JavaScript definition for basic Tree class
 */

class Tree {
  constructor(value, children) {
    this.value = value;
    this.children = children;
  }

  toString() {
    let ans = "[";
    ans += this.value.toString();

    this.children.forEach((child) => {
      ans += ", ";
      ans += child.toString();
    });

    return ans + "]";
  }

  get value() {
    // Getter for node's value
    return this.value;
  }

  set value(item) {
    // this.value = item;
  }

  *children() {
    // Generator to return children
    for (let i = 0; i < this.children.length; i++) {
      yield children[i];
    }
  }

  numNodes() {
    // Compute number of nodes in a tree
    let nodes = 1;
    this.children.forEach((child) => {
      nodes += child.numNodes();
    });

    return nodes;
  }

  numLeaves() {
    // Compute number of leaves in the tree.
    let leaves = 1;
    this.children.forEach((child) => {
      if (!child.numNodes()) {
        leaves += 1;
      }
    });

    return leaves;
  }

  height() {
    // Compute the height of a tree rooted by itself
    let height = 0;
    this.children.forEach((child) => {
      if (!!child.numNodes()) {
        height = Math.max(height, child.height() + 1);
      }
    });

    return height;
  }
}

function runExamples() {
  // Create some trees and apply various methods to these trees.
  const treeA = new Tree("a", []);
  const treeB = new Tree("b", []);
  console.log(
    "Tree consisting of single leaf node labelled 'a'",
    treeA.toString()
  );
  console.log(
    "Tree consisting of single leaf node labelled 'b'",
    treeB.toString()
  );

  const treeCAB = new Tree("c", [treeA, treeB]);
  console.log("Tree consisting of three nodes.", treeCAB);
}

runExamples();
