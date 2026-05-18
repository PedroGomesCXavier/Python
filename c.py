from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def diretorio():
    return ''' <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - Nome Sobrenome</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        header {
            text-align: center;
            border-bottom: 2px solid #35424a;
            padding-bottom: 20px;
            margin-bottom: 20px;
        }
        header h1 {
            margin: 0;
            color: #35424a;
        }
        .contact-info {
            color: #555;
            font-size: 0.9em;
        }
        h2 {
            color: #35424a;
            border-bottom: 1px solid #ccc;
            padding-bottom: 10px;
        }
        .experience-item, .education-item {
            margin-bottom: 20px;
        }
        .job-title {
            font-weight: bold;
            color: #000;
        }
        .company-date {
            font-style: italic;
            color: #666;
            display: flex;
            justify-content: space-between;
        }
        ul {
            padding-left: 20px;
        }
        .skills-list {
            list-style-type: none;
            padding: 0;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .skills-list li {
            background: #35424a;
            color: #fff;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Nome Sobrenome</h1>
            <p class="contact-info">
                São Paulo, SP | (11) 99999-9999 | email@exemplo.com<br>
                ://linkedin.com | ://github.com
            </p>
        </header>

        <section>
            <h2>Resumo Profissional</h2>
            <p>Profissional apaixonado com X anos de experiência em [Sua Área]. Especialista em [Habilidade 1] e [Habilidade 2], focado em trazer resultados e melhoria contínua.</p>
        </section>

        <section>
            <h2>Experiência Profissional</h2>
            
            <div class="experience-item">
                <div class="job-title">Cargo Atual</div>
                <div class="company-date">
                    <span>Nome da Empresa</span>
                    <span>Jan 2022 - Presente</span>
                </div>
                <ul>
                    <li>Responsável por desenvolver [projeto/funcionalidade].</li>
                    <li>Aumento de X% na produtividade utilizando [ferramenta].</li>
                </ul>
            </div>

            <div class="experience-item">
                <div class="job-title">Cargo Anterior</div>
                <div class="company-date">
                    <span>Nome da Empresa</span>
                    <span>Jan 2020 - Dez 2021</span>
                </div>
                <ul>
                    <li>Gerenciei [tarefa] e melhorei [processo].</li>
                </ul>
            </div>
        </section>

        <section>
            <h2>Educação</h2>
            <div class="education-item">
                <div class="job-title">Bacharelado em Área de Estudo</div>
                <div class="company-date">
                    <span>Nome da Universidade</span>
                    <span>2016 - 2020</span>
                </div>
            </div>
        </section>

        <section>
            <h2>Habilidades</h2>
            <ul class="skills-list">
                <li>HTML5</li>
                <li>CSS3</li>
                <li>JavaScript</li>
                <li>React</li>
                <li>Gerenciamento de Projetos</li>
                <li>Inglês Técnico</li>
            </ul>
        </section>
    </div>
</body>
</html>
  ''' # Isso é o que será retornado quando a rota '/' for acessada

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
