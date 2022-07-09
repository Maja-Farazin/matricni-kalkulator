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
    <form action="/izracunaj" method="post">
        <input type="hidden" name="operacija" value="{{operacija}}">
        <input type="hidden" name="parameter" value="{{parameter}}">
        <input type="hidden" name="st_vrstic" value="{{st_vrstic}}">
        <input type="hidden" name="st_stolpcev" value="{{st_stolpcev}}">
        <input type="hidden" name="st_matrik" value="{{st_matrik}}">
        <br><br>
        % for matrika in range(st_matrik):
            <table>
                % for vrstica in range(st_vrstic[matrika]):
                    <tr>
                        % for stolpec in range(st_stolpcev[matrika]):
                            <td>
                                <input type="number" name="polje:{{matrika}}-{{vrstica}}-{{stolpec}}" step="any" required oninvalid="this.setCustomValidity('To polje ne sme ostati prazno!')" 
onchange="this.setCustomValidity('')" style="width: 75px; height: 50px; padding: 0;">
                            </td>
                        % end
                    </tr>
                % end
            </table><br><br>
        % end   
        <input type="submit" value="Izračunaj"> 
    </form>
</body>
</html>