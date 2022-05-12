#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i += 1;
    }
  }

  rotate () {
    const storage = this.height;
    this.height = this.width;
    this.width = storage;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
