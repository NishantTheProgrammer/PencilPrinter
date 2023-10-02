let threshold, resolution, canvas, capture, fileInput, uploadedImage;

const minResolution = 20;
const maxResolution = 100;
let front = true; // Variable to keep track of camera selection
let taken = false;
let data = [];

function handleFile(file) {

    console.log(file)
    if (file.type === 'image') {
        uploadedImage = loadImage(file.data);
    } else {
        console.error('Invalid file type. Please upload an image.');
    }
}



function setup() {
    threshold = createSlider(0, 255, 127).parent('threshold');
    resolution = createSlider(minResolution, maxResolution, 70).parent('resolution');
    canvas = createCanvas(400, 600).parent('canvas');
    fileInput = createFileInput(handleFile).parent('fileInput');
    fileInput.attribute('id', 'hiddenInputTag');

    initCapture();

    let switchCameraButton = document.getElementById('switchCamera');
    switchCameraButton.addEventListener('click', switchCamera);
}

function draw() {
    background(255);
    printBtn.disabled = !taken;


    let source;
    if (uploadedImage) {
        source = uploadedImage;
        source.resize(width, height);
    } else {
        source = capture;
        if(taken) {
            capture.stop();
        }
    }
    source.loadPixels();

    let thresholdValue = threshold.value();
    let resolutionValue = round(map(resolution.value(), minResolution, maxResolution, width / minResolution, width / maxResolution));

    data = [];
    for (let y = 0; y < height; y += resolutionValue) {
        const row = [];
        for (let x = 0; x < width; x += resolutionValue) {
            let loc = (x + y * width) * 4;
            let bright = (source.pixels[loc] + source.pixels[loc + 1] + capture.pixels[loc + 2]) / 3;

            if (bright > thresholdValue) {
                fill(255);
            } else {
                fill(0);
                noStroke();
            }
            ellipse(x, y, resolutionValue, resolutionValue);
            row.push(bright > thresholdValue)
        }
        data.push(row);
    }
    if (uploadedImage) { taken = true }
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

function onClear() {
    uploadedImage = null; 
    taken = false;
    initCapture();
}

function onPrint() {
    const stars = data.map(row => row.map(i => i ? '*' : ' ').join('')).join('\n');
    console.log(stars);
}