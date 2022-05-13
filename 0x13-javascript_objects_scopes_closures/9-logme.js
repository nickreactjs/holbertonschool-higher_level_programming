#!/usr/bin/node
exports.logMe = function (item) {
  if (!this.nb){
    this.nb = 0;
  }
  console.log(`${this.nb}: ${item}`);
  this.nb += 1;
}
