<?php

$python_path = "C:/Users/ilias/AppData/Local/Programs/Python/Python39/";

$docx = "";
$type = $_GET['type'];
$file_name = $_GET['filename'];
$file_input_name = $_GET['file'];
$search = $_GET['search'];
if (!empty($_GET['docx']))
    $docx = $_GET['docx'];



if (empty($file_input_name))
    return;
$time = $file_input_name;
if (substr(PHP_OS, 0, 3) == 'WIN') {


    if (empty($_GET['docx']))
        shell_exec($python_path . "python.exe Python\main.py temp\input_$time temp\output_$time ");
    else
        shell_exec($python_path . "python.exe Python\main.py temp\input_$time.docx temp\output_$time");
} else {
    if (empty($_GET['docx']))
        shell_exec("python Python/main.py temp/input_$time temp/output_$time ");
    else
        shell_exec("python Python/main.py temp/input_$time.docx temp/output_$time ");
}