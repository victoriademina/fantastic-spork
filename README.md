# Fantastic Spork

A model project for learning the basics of [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming), inspired by [turn-based strategies](https://en.wikipedia.org/wiki/Turn-based_strategy).

## Game mechanics

### Map

Maps can be represented as a grid of N * M square **cells**.
Each cell can either be a sea or a land.

### Unit

Each unit has **health** and **experience**. Both characteristics are represented with non-negative integers.
Unit gains **experience** and looses **health** in fights. When unit's health reaches **0** the unit dies and is removed from the map.

### Movements

Units can only stand on land cells, and only one unit can stand on a cell.
Units move around a map in turns. In each turn unit can move to one of the neighbour cells in four directons: **North**, **South**, **East** or **West**.
Units can not move diagonally. Unit can make a move in a chosen direction only if the target cell lays within the map boundaries and is a land.
If a unit tries to move to a cell, which is taken by another unit, a fight happens.

### Fight

Fight can only happen if one unit moves to a cell, taken by another unit.
The moving unit is called **attacker** and the standing unit is called **defender**.
A unit wins a fight if it's opponent is dead.
If **attacker** wins, then it moves to the **defender**'s cell.
If **defender** wind, then it stays on it's cell.
If no one wins, then both units stay on their cells.