<?php
// encrypt.php
if(isset($_POST['text'])){
    $text = $_POST['text'];
    $encryption_key = bin2hex(random_bytes(16)); // Generate a 128-bit (16-byte) random key and convert it to hex
    $encrypted_text = openssl_encrypt($text, "AES-256-CBC", $encryption_key, 0, "1234567890123456");
    $response = array("encryption_key" => $encryption_key, "encrypted_text" => $encrypted_text);
    header("Content-Type: application/json");
    echo json_encode($response);
}
?>
