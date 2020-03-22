class MarioAdapter {
    
    constructor(legacyMario) {
      this.legacyMario = legacyMario;
    }
  
    attack(target) {
      target.health -= this.legacyMario.jumpAttack();
    }
  }