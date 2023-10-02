let threshold, resolution, canvas, capture;


const minResolution = 20;
const maxResolution = 100;
function setup() {
    threshold = createSlider(0, 255, 127).parent('threshold'); // Corrected range from 0-255
    resolution = createSlider(minResolution, maxResolution, 70).parent('resolution'); // Adjusted range and default value
    canvas = createCanvas(400, 600).parent('canvas');
    capture = createCapture(VIDEO).parent('capture');
    capture.size(width, height);
    capture.hide();
}

function draw() {
    background(255); // Set background to white
    capture.loadPixels(); // Load pixels from the video capture

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
