#!/usr/bin/node
exports.logMe = function (item) {
  if (!this.nb){
    this.nb = 0;
  }
  this.nb += 1;
  console.log(`${this.nb - 1}: ${item}`);
}
