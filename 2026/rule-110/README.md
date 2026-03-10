# Rule 110 Cellular Automata

Minimal browser project to draw Rule 110 evolution on a canvas.

## Run

1. Open `index.html` in a browser.
2. Change width, steps, cell size, seed.
3. Click **Draw**.

## Notes

- Automata is 1D; each row is the next generation.
- `single` seed starts from the rightmost cell.
- Boundary cells treat out-of-range neighbors as `0`.
- Rule 110 mapping used:
  - 111->0, 110->1, 101->1, 100->0
  - 011->1, 010->1, 001->1, 000->0
