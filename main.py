__author__ = 'falkzach'

import bottle

@bottle.route('/recipes')
def index(name='List'):
    return '<html>' \
           '<head><title>Recipe\'s</title></head>' \
           '<body>' \
           '<div class=container>' \
           '<h1>Recipes</h1>' \
           '<p><a href="#" class="btn btn-primary btn-lg" role="button">Learn more &raquo;</a></p>' \
           '</div>' \
           '</body>' \
           '' \
           '<!-- Bootstrap CDN-->' \
           '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">' \
           '</html>'

bottle.run(host='localhost', port= 8080)
#open browser and brows to localhost:8080/recipes