<?php

$time = time();

if (isset($_POST['user_text']) && !empty($_POST['user_text'])) {

    $usertext = $_POST['user_text'];
    $usertext_to_file = fopen("temp/input_$time", "w");

    fwrite($usertext_to_file, $usertext);
    fclose($myfile);

    session_start();

    $_SESSION["load_time"] = floor(strlen($usertext) * 0.034);


    header("Location: result.php?type=user_text&filename=" . "input_$time" . "&file=$time&output=output_$time&search=1");
} else {

    if (!isset($_FILES['user_file']))
        header('Location: index.php');

    $docx = 0;



    $mimes = array('text/plain', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/pdf', 'application/msword');

    if (!in_array($_FILES['user_file']['type'], $mimes)) {
        echo "<h2> Only text / docx / pdf  files are supported.</h2>";
        echo "<p>This file has MIME type: " . $_FILES['user_file']['type'];
        exit();
    }


    // PDF
    if (strcmp($_FILES['user_file']['type'], 'application/pdf') == 0) {
        if (substr(PHP_OS, 0, 3) == 'WIN') {
            move_uploaded_file($_FILES['user_file']['tmp_name'], "temp/input_$time.pdf");
            shell_exec("scripts\pdftotext64 -enc UTF-8 temp\input_$time.pdf temp\input_$time");
        } else {
            move_uploaded_file($_FILES['user_file']['tmp_name'], "temp/input_$time.pdf");
            shell_exec("pdftotext temp/input_$time.pdf temp/input_$time");
        }
    } else {
        // DOCX
        if (strcmp($_FILES['user_file']['type'], 'application/vnd.openxmlformats-officedocument.wordprocessingml.document') == 0) {
            move_uploaded_file($_FILES['user_file']['tmp_name'], "temp/input_$time.docx");
            $docx = 1;
        }
        // DOC
        else if (strcmp($_FILES['user_file']['type'], 'application/msword') == 0) {
            move_uploaded_file($_FILES['user_file']['tmp_name'], "temp/input_$time.doc");
            if (substr(PHP_OS, 0, 3) == 'WIN')
                shell_exec("scripts\catdoc -d utf-8 temp/input_$time.doc > temp/input_$time");
            else
                shell_exec("catdoc -d utf-8 temp/input_$time.doc > temp/input_$time");
        }

        // TEXT
        else {
            move_uploaded_file($_FILES['user_file']['tmp_name'], "temp/input_$time");
            $docx = 0;
        }
    }


    if ($docx == 1)
        header("Location: result.php?type=user_file&filename=" . $_FILES['user_file']['name'] . "&file=$time&output=output_$time&search=1&docx=1");
    else
        header("Location:  result.php?type=user_file&filename=" . $_FILES['user_file']['name'] . "&file=$time&output=output_$time&search=1");
}