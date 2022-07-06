<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    % for matrika in seznam_matrik:
    <table>
        % for vrstica in matrika:
        <tr>
            % for element in vrstica:
                <td style="border: 1px solid black; width: 50px; height: 50px;">
                    {{element}}
                </td>
            % end
        </tr>   
        % end
    </table><br>
    % end
    <br><br><br>
    <table>
        % for vrstica in rezultat:
        <tr>
            % for element in vrstica:
                <td style="border: 1px solid black; width: 50px; height: 50px;">
                    {{element}}
                </td>
            % end
        </tr>   
        % end
    </table>
    <br><br><br>
    <button onclick="window.location.href = '/';">Domov</button>
</body>
</html>