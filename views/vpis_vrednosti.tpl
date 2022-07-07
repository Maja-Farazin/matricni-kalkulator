<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="/izracunaj" method="post">
        <input type="hidden" name="operacija" value="{{operacija}}">
        <input type="hidden" name="parameter" value="{{parameter}}">
        <input type="hidden" name="st_vrstic" value="{{st_vrstic}}">
        <input type="hidden" name="st_stolpcev" value="{{st_stolpcev}}">
        <input type="hidden" name="st_matrik" value="{{st_matrik}}">
        % for matrika in range(st_matrik):
            <table>
                % for vrstica in range(st_vrstic[matrika]):
                    <tr>
                        % for stolpec in range(st_stolpcev[matrika]):
                            <td>
                                <input type="number" name="polje:{{matrika}}-{{vrstica}}-{{stolpec}}" step="any" required style="width: 50px; height: 50px;">
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