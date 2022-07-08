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
    <br><br><br>
    % if operacija == "sled" or operacija == "determinanta":
        {{rezultat}}
    % else:
        <table>
            % for vrstica in rezultat:
            <tr>
                % for element in vrstica:
                    <td class="output">
                        {{element}}
                    </td>
                % end
            </tr>   
            % end
        </table>
    % end
    <br><br><br>
    <button onclick="window.location.href = '/';" class="domov">Domov</button>
</body>
</html>