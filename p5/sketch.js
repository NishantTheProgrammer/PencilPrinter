let threshold, resolution, canvas, capture;

const minResolution = 20;
const maxResolution = 100;
let front = true; // Variable to keep track of camera selection

function setup() {
    threshold = createSlider(0, 255, 127).parent('threshold');
    resolution = createSlider(minResolution, maxResolution, 70).parent('resolution');
    canvas = createCanvas(400, 600).parent('canvas');

    initCapture();
    
    let switchCameraButton = document.getElementById('switchCamera');
    switchCameraButton.addEventListener('click', switchCamera);
}

function draw() {
    background(255);
    capture.loadPixels();

    let thresholdValue = threshold.value();
    let resolutionValue = round(map(resolution.value(), minResolution, maxResolution, width / minResolution, width / maxResolution));

    for (let y = 0; y < height; y += resolutionValue) {
        for (let x = 0; x < width; x += resolutionValue) {
            let loc = (x + y * width) * 4;
            let bright = (capture.pixels[loc] + capture.pixels[loc + 1] + capture.pixels[loc + 2]) / 3;

            if (bright > thresholdValue) {
                fill(255);
            } else {
                fill(0);
                noStroke();
            }
            ellipse(x, y, resolutionValue, resolutionValue);
        }
    }
}

function initCapture() {
    if (capture) {
        capture.stop();
        capture.remove();
    }
    capture = createCapture({
        video: {
            facingMode: front ? 'user' : 'environment'
        }
    }).parent('capture');
    capture.size(width, height);
    capture.hide();
}

function switchCamera() {
    front = !front;
    initCapture();
}
