<?php
// decrypt.php
if(isset($_POST['text1']) && isset($_POST['text2'])){
    $text1 = $_POST['text1'];
    $text2 = $_POST['text2'];
    $encryption_key = $text2;
    $decrypted_text = openssl_decrypt($text1, "AES-256-CBC", $encryption_key, 0, "1234567890123456");
    if($text2 == $encryption_key){
        $response = array("decrypted_text" => $decrypted_text);
    }
    else{
        $response = array("decrypted_text" => "Invalid decryption key");
    }
    header("Content-Type: application/json");
    echo json_encode($response);
}
?>