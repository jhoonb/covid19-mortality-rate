"""
HTML_INDEX_PAGE: str
uso:

Death Rate
Death Rate Brazil
Cases World
World Deaths
Cases Brazil
Deaths Brazil
Last updated

HTML_INDEX_PAGE.format(Death Rate, Death Rate Brazil, 
    Cases World, World Deaths, Cases Brazil, Deaths Brazil, Last updated)
"""


HTML_INDEX_PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <title>COVID-19 | World & Brazil</title>
</head>
<body>
    <div class="grid-2">
        
        <div class="section-1">
            <h1> Taxa de mortalidade global do Coronavírus </h1>
            <h4>(Global Death Rate for COVID-19)</h4>
            <i class="fas fa-skull-crossbones fa-5x white"> 4.17% </i>
            <br> <br>

            <h1> Taxa de mortalidade do Coronavírus no Brasil </h1>
            <h4>(Brazil Death Rate for COVID-19)</h4>
            <i class="fas fa-skull-crossbones fa-5x white"> 1.07% </i>
        </div>
        <div class="section-2">
            <h2>Mundo (World)</h2>
            <h3>Casos de Coronavirus (COVID-19 Cases): {}</h3>
            <h3>Mortes (Deaths): {}</h3>

            <h2>Brasil (Brazil)</h2>
            <h3>Casos de Coronavirus (COVID-19 Cases): {}</h3>
            <h3>Mortes (Deaths): {}</h3>
        </div>

        <h5>Última atualização em (Last updated): {}</h5>

        <div class="wrapper">
            <footer class="page-footer">
                @jhoonb: 
            <a href="https://www.twitter.com/jhoonb"> <i class="fab fa-twitter"> </i></a>
            
            <a href="https://www.github.com/jhoonb"> <i class="fab fa-github"></i></a>

            <a href="http://telegram.me/jhoonb"> <i class="fab fa-telegram"></i></a>

            <a href="https://discordapp.com/"> <i class="fab fa-discord"></i></a>

            <a href="https://medium.com/@jhoonb"> <i class="fab fa-medium"></i></a>

            <a href="https://dev.to/jhoonb"> <i class="fab fa-dev"></i></a>
        </footer>
        </div>
    </div>
</body>
</html>'''