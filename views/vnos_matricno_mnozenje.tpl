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
    <form action="/vpis_vrednosti/matricno_mnozenje" method="post">
        <label for="y">Število vrstic prve matrike:</label>
        <input type="number" name="y" id="y" required min="1" oninvalid="this.setCustomValidity('Vpišite pozitivno celo število!')" 
onchange="this.setCustomValidity('')"><br><br>
        <label for="x1">Število stolpcev prve matrike:</label>
        <input type="number" name="x1" id="x1" required min="1" oninvalid="this.setCustomValidity('Vpišite pozitivno celo število!')" 
onchange="this.setCustomValidity('')"><br><br><br>
        <label for="x2">Število stolpcev druge matrike:</label>
        <input type="number" name="x2" id="x2" required min="1" oninvalid="this.setCustomValidity('Vpišite pozitivno celo število!')" 
onchange="this.setCustomValidity('')"><br><br><br>
        <input type="submit" value="Naprej">
    </form>
</body>
</html>