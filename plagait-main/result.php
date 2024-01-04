<?php
session_start();
$load_time = 1;
if (isset($_SESSION["load_time"]))
    $load_time = $_SESSION["load_time"];

$docx = "";
$type = $_GET['type'];
$file_name = $_GET['filename'];
$file_input_name = $_GET['file'];
$file_output_name = $_GET["output"];
$search = $_GET['search'];
if (!empty($_GET['docx']))
    $docx = $_GET['docx'];


?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <link rel="stylesheet" href="CSS/style.css">

</head>

<body>

    <div class="plagait">
        <div class="plagait_body">
            <div class="result_processing">
                <h1>in processing <span id="timer_load"><?php echo $load_time ?></span> s...</h1>
                <h2>please wait a second </h2>

                <div class="loading">
                    <div class="spinner-grow text-primary" role="status"> </div>
                    <div class="spinner-grow text-secondary" role="status"> </div>
                    <div class="spinner-grow text-success" role="status"> </div>
                    <div class="spinner-grow text-danger" role="status"> </div>
                    <div class="spinner-grow text-warning" role="status"> </div>
                    <div class="spinner-grow text-info" role="status"> </div>
                    <div class="spinner-grow text-light" role="status"> </div>
                    <div class="spinner-grow text-dark" role="status"> </div>
                </div>
            </div>
            <div class="result">
                <h1>Plagiat Result</h1>

            </div>


        </div>

        <div class="circle1"></div>
        <div class="circle2"></div>
    </div>
    <p id="result_file" style="display: none;">
        <?php echo $file_output_name ?>
    </p>
    <p id="execute_file" style="display: none;">
        <?php
        if ($docx == "1")
            echo "execute.php?type=$type&filename=" . $file_name . "&file=$file_input_name&search=1&docx=1";
        else
            echo "execute.php?type=$type&filename=" . $file_name . "&file=$file_input_name&search=1";
        ?></p>



    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous">
    </script>
    <script src="Js/app_result.js"> </script>
</body>

</html>