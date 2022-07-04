<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    % include('seznam_operacij.tpl')
    <form action="/vpis_vrednosti/transponiranje" method="post">
        <label for="y">Število vrstic:</label>
        <input type="number" name="y" id="y"><br>
        <label for="x">Število stolpcev:</label>
        <input type="number" name="x" id="x"><br><br>
        <input type="submit" value="Izračunaj">
    </form>
</body>
</html>