const widthInput = document.getElementById("width");
const stepsInput = document.getElementById("steps");
const cellSizeInput = document.getElementById("cellSize");
const seedSelect = document.getElementById("seed");
const drawBtn = document.getElementById("drawBtn");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

function clampInt(value, min, max, fallback) {
  const n = Number.parseInt(value, 10);
  if (Number.isNaN(n)) return fallback;
  return Math.min(max, Math.max(min, n));
}

function makeInitialRow(width, seedMode) {
  const row = new Uint8Array(width);
  if (seedMode === "random") {
    for (let i = 0; i < width; i += 1) row[i] = Math.random() < 0.5 ? 1 : 0;
    return row;
  }
  row[width - 1] = 1;
  return row;
}

function nextRule110Row(current) {
  const n = current.length;
  const next = new Uint8Array(n);

  for (let i = 0; i < n; i += 1) {
    const left = i === 0 ? 0 : current[i - 1];
    const center = current[i];
    const right = i === n - 1 ? 0 : current[i + 1];
    const pattern = (left << 2) | (center << 1) | right;
    next[i] = pattern === 7 || pattern === 4 || pattern === 0 ? 0 : 1;
  }

  return next;
}

function draw() {
  const width = clampInt(widthInput.value, 32, 1024, 256);
  const steps = clampInt(stepsInput.value, 32, 2048, 256);
  const cellSize = clampInt(cellSizeInput.value, 1, 8, 2);

  canvas.width = width * cellSize;
  canvas.height = steps * cellSize;

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  let row = makeInitialRow(width, seedSelect.value);

  for (let y = 0; y < steps; y += 1) {
    for (let x = 0; x < width; x += 1) {
      if (row[x] === 0) continue;
      ctx.fillStyle = "#111111";
      ctx.fillRect(x * cellSize, y * cellSize, cellSize, cellSize);
    }
    row = nextRule110Row(row);
  }
}

drawBtn.addEventListener("click", draw);
draw();
