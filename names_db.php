<?php
error_reporting(0);
$db = mysqli_connect('localhost', 'root', '', 'weather'); // Using a dedicated database
$text = $_POST["text"] ?? '';
$sessionID = $_POST["sessionID"];
$serviceCode = $_POST["serviceCode"];
$phoneNumber = $_POST["phoneNumber"];

// Split the user input into parts
$input = explode('*', $text);
$step = count($input);

if (empty($text)) {
    // Main menu
    $response = "CON What would you like to do?\n";
    $response .= "1. Register your name\n";
    $response .= "2. View your details\n";
} 
elseif ($input[0] == "1") { // Insert flow
    if ($step == 1) {
        $response = "CON Enter your first name:";
    }
    elseif ($step == 2) {
        $response = "CON Enter your last name:";
    }
    elseif ($step == 3) {
        // Save to database
        $firstName = mysqli_real_escape_string($db, $input[1]);
        $lastName = mysqli_real_escape_string($db, $input[2]);
        
        // Check if user already exists
        $check = mysqli_query($db, "SELECT * FROM users WHERE phone_number = '$phoneNumber'");
        
        if (mysqli_num_rows($check) > 0) {
            // Update existing record
            $query = "UPDATE users SET first_name = '$firstName', last_name = '$lastName' 
                      WHERE phone_number = '$phoneNumber'";
        } else {
            // Insert new record
            $query = "INSERT INTO users (phone_number, first_name, last_name) 
                      VALUES ('$phoneNumber', '$firstName', '$lastName')";
        }
        
        if (mysqli_query($db, $query)) {
            $response = "END Thank you! Your details have been saved.";
        } else {
            $response = "END Error: Could not save your details.";
        }
    }
}
elseif ($input[0] == "2") { // View flow
    $query = mysqli_query($db, "SELECT * FROM users WHERE phone_number = '$phoneNumber'");
    
    if (mysqli_num_rows($query) > 0) {
        $user = mysqli_fetch_assoc($query);
        $response = "END Your details:\nName: {$user['first_name']} {$user['last_name']}\n";
        $response .= "Phone: {$user['phone_number']}";
    } else {
        $response = "END You are not registered yet.\nSelect 1 to register.";
    }
}

mysqli_close($db);
header('Content-type: text/plain');
echo $response;
?>