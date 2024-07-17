  moveTower: height from: fromPin to: toPin using: usingPin
  (height > 0) ifTrue: [
      self moveTower: (height-1) from: fromPin to: usingPin using: toPin.
      self moveDisk: fromPin to: toPin.
      self moveTower: (height-1) from: usingPin to: toPin using: fromPin]
  moveDisk: fromPin to: toPin
  Transcript cr.
  Transcript show: (fromPin printString,' - > ', toPin printString). 