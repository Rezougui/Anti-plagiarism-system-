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
            <form id="form" action="process.php" method="POST" enctype="multipart/form-data">
                <h1>Plagiat checker </h1>
                <div class=" form-floating">
                    <textarea name="user_text" class="form-control" placeholder="Your Text ..." id="user_text"
                        style="height: 200px"></textarea>
                    <label for="user_text">Your Text ...</label>
                </div>
                <h2>or Upload Your File </h2>
                <input name="user_file" class="form-control" type="file" id="user_file">
                <button type="submit" class="btn action-button">Send</button>

            </form>

        </div>
        <div class="circle1"></div>
        <div class="circle2"></div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous">
    </script>
    <script src="Js/app_index.js">
    </script>
</body>

</html>