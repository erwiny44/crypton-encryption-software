const express = require('express');
const { spawn } = require('child_process');

const app = express();
const port = 3000;

// Set up middleware to parse JSON request bodies
app.use(express.json());

// Serve the index.html file when a GET request is made to the root path
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Handle POST requests to /encrypt
app.post('/encrypt', (req, res) => {
  const plaintext = req.body.plaintext;
  
  // spawn new child process to call the python script
  const python = spawn('python3', ['encryption.py', plaintext]);

  // Collect data from script
  let encryptedData;
  python.stdout.on('data', (data) => {
    console.log('Pipe data from python script');
    encryptedData = data.toString();
  });

  // In close event we are sure that stream from child process is closed
  python.on('close', (code) => {
    console.log(`Child process closed with code ${code}`);
    const encryptedDataArr = encryptedData.split('\n');
    const output = {
      ciphertext: encryptedDataArr[0],
      key: encryptedDataArr[1],
    };
    res.send(output);
  });
});

// Handle POST requests to /decrypt
app.post('/decrypt', (req, res) => {
  const ciphertext = req.body.ciphertext;
  const key = req.body.key;

  // spawn new child process to call the python script
  const python = spawn('python3', ['decryption.py', ciphertext, key]);

  // Collect data from script
  let decryptedData;
  python.stdout.on('data', (data) => {
    console.log('Pipe data from python script');
    decryptedData = data.toString();
  });

  // In close event we are sure that stream from child process is closed
  python.on('close', (code) => {
    console.log(`Child process closed with code ${code}`);
    const output = {
      plaintext: decryptedData,
    };
    res.send(output);
  });
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
