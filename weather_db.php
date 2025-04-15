<?php
error_reporting(0);
$db = mysqli_connect('localhost', 'root', '', 'weather');
$text = $_POST["text"] ?? '';
$sessionID = $_POST["sessionID"];
$serviceCode = $_POST["serviceCode"];
$phoneNumber = $_POST["phoneNumber"];

if (empty($text)) {
    $response = "CON SELECT YOUR CITY\n";
    $response .= "1. Kigali\n";
    $response .= "2. Musanze\n";
    $response .= "3. Huye\n";
} 
else {
    // Get the number user selected (1, 2, or 3)
    $city_number = (int)$text;
    
    // Look up weather in database
    $query = "SELECT * FROM district WHERE id = $city_number";
    $result = mysqli_query($db, $query);
    
    if ($row = mysqli_fetch_assoc($result)) {
        $response = "END Weather in {$row['district_name']}:\n";
        $response .= "Condition: {$row['weather_condition']}\n";
        $response .= "Temperature: {$row['temperature']}°C";
    } else {
        $response = "END Weather info not available";
    }
}
mysqli_close($db);
header('Content-type: text/plain');
echo $response;
?>