class Probe {
    constructor() {
      this.commands = [];
      this.position = { x: 0, y: 0 };
      this.minerals = 0;
    }
    move(x, y) { this.commands.push({x: x, y: y}); }
    gather() { this.commands.push(5) }
  }
  
  class MoveCommand {
    constructor(unit, x, y) {
    this.unit = unit;
    this.x = x;
    this.y = y;
    
    this.unit.move(this.x, this.y);
    
    }
    execute() {
      const command = this.unit.commands.pop();
      if(typeof(command) === "object") {
        this.unit.position = command || this.unit.position;
      }
    }
    canExecute() { return true; }
  }
  
  class GatherCommand {
    constructor(unit) {
      this.unit = unit;
      
      this.unit.gather();
      
      }
    execute() {
      const command = this.unit.commands.pop();
      if(typeof(command) === "number") {
          this.unit.minerals += command || 0;
        }
    this.unit.minerals += this.unit.commands.pop() || 0; }
    canExecute() { return unit.minerals === 0; }
  }