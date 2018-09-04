#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  print () {
    let prompt = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(prompt.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
