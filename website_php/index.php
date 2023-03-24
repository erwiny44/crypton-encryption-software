<!DOCTYPE html>
<html>
<head>
    <title>Encryption/Decryption</title>
    <link rel="icon" href="icon.png">
</head>
<body>
<div class="container">
    <div class="card" ">
        <h1>Encryption</h1>
        <form id="encrypt-form">
            <div class="form-element">
                <label for="encrypt-input">Enter text to encrypt:</label>
                <input type="text" id="encrypt-input" name="encrypt-input">
                <br>
                <button type="submit" id="encrypt-button" class="form-button" style="margin-left: 200px;" >Encrypt</button>
            </div>
            <div class="form-content">
            <textarea id="encrypt-output" name="encrypt-output" placeholder="Encrypted text" rows="1" cols="60" readonly></textarea>
            <br>
            
            <textarea id="encryption-key-output" name="encryption-key-output" placeholder="Encryption key" rows="1" cols="60" readonly></textarea>
        </div>

        </form>
    </div>
    <div class="card" >
        <h1>Decryption</h1>
        <form id="decrypt-form">
            <div class="form-element">
                <label for="decrypt-input1">Enter encrypted text:</label>
                <input type="text" id="decrypt-input1" name="decrypt-input1" >
            </div>
            <div class="form-element">
                <label for="decrypt-input2">Enter decryption key:</label>
                <input type="text" id="decrypt-input2" name="decrypt-input2">
                <br>
                <button type="submit" id="decrypt-button" class="form-button" style="margin-left: 200px;" >Decrypt</button>
            </div>
            <div class="form-content">
                <textarea id="decrypt-output" name="decrypt-output" placeholder="Decrypted text" rows="2" cols="60" readonly></textarea>
            </div>
        </form>
    </div>
</div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    $(document).ready(function(){
        // Submit encrypt form
        $("#encrypt-form").submit(function(event){
            event.preventDefault();
            $.ajax({
                url: "encrypt.php",
                type: "POST",
                data: {text: $("#encrypt-input").val()},
                dataType: 'json',
                success: function(response){
                    $("#encrypt-output").val(response.encrypted_text);
                    $("#encryption-key-output").val(response.encryption_key);
                },
                error: function(xhr, status, error){
                    console.log("Error: " + error);
                }
            });
        });
        // Submit decrypt form
        $("#decrypt-form").submit(function(event){
            event.preventDefault();
            $.ajax({
                url: "decrypt.php",
                type: "POST",
                data: {text1: $("#decrypt-input1").val(), text2: $("#decrypt-input2").val()},
                dataType: 'json',
                success: function(response){
                    $("#decrypt-output").val(response.decrypted_text);
                },
                error: function(xhr, status, error){
                    console.log("Error: " + error);
                }
            });
        });
    });
</script>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow&display=swap');
    body {
        font-family: 'Barlow', sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #232323;
        color: white;
    }


    .card {
        
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: #171717;
        padding:  0 75px 75px 75px;
    }
    .form-element {
        padding-bottom: 10px;
    }
    .form-button {
        height: 35px;
        width: 80px;
        margin-top: 10px;
        margin-right: 50px;
    }

    input {
        width: 318px;
    }
</style>
</body>
</html>
