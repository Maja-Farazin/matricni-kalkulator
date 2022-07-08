<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" href="/domaca.css" rel="stylesheet">
    <title>Document</title>
</head>
<body>
    % include('seznam_operacij.tpl')
    <form action="/vpis_vrednosti/determinanta" method="post">
        <label for="y">Velikost matrike:</label>
        <input type="number" name="y" id="y" required min="1" oninvalid="this.setCustomValidity('Vpišite pozitivno celo število!')" 
onchange="this.setCustomValidity('')"><br><br><br>
        <input type="submit" value="Naprej">
    </form>
</body>
</html>