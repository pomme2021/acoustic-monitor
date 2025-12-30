let audioData;
let amplitudes = [];
let sound;
let isPlaying = false;
let duration = 0;

function preload() {
  audioData = loadJSON("../processed/2025-12-13_15-32.json");
  sound = loadSound("../raw_audio/2025-12-13_15-32.wav");
}

function setup() {
  createCanvas(800, 300);
  background(255);

  if (!audioData || !audioData.amplitude) {
    text("JSON NOT LOADED", 20, 40);
    noLoop();
    return;
  }

  amplitudes = audioData.amplitude;

  // Button for audio unlock
  let btn = createButton("Play / Pause");
  btn.mousePressed(toggleAudio);
}

function toggleAudio() {
  userStartAudio();

  if (!isPlaying) {
    sound.play();
    isPlaying = true;
  } else {
    sound.pause();
    isPlaying = false;
  }
}

function draw() {
  background(255);
  stroke(0);
  noFill();

  beginShape();
  for (let i = 0; i < amplitudes.length; i += 200) {
    let x = map(i, 0, amplitudes.length, 0, width);
    let y = map(amplitudes[i], -1, 1, height, 0);
    vertex(x, y);
  }
  endShape();
}

// SCRUBBING LOGIC
function mousePressed() {
  if (!sound.isLoaded()) return;

  userStartAudio();

  // Clamp mouseX to canvas
  let x = constrain(mouseX, 0, width);

  // Convert x position to time
  let pct = x / width;
  let time = pct * sound.duration();

  sound.jump(time);
}

