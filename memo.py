import bottle
import model_memo

SKRIVNOST = 'moja skrivnost'
memo = model_memo.Memo()

@bottle.get("/")  
def index():
    return bottle.template('index.tpl')

@bottle.post("/nova_igra/") 
def nova_igra():
    id_igre = memo.nova_igra()
    bottle.response.set_cookie("idigre", "idigre{0}".format(id_igre), secret=SKRIVNOST, path='/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie("idigre", secret=SKRIVNOST).split('e')[1])
    igra, poskus = memo.igre[id_igre]
    return bottle.template('igra_memo.tpl', igra=igra, poskus=poskus)

@bottle.post("/igra/")
def ugibaj():
    id_igre = int(bottle.request.get_cookie("idigre", secret=SKRIVNOST).split('e')[1])
    kombinacija = bottle.request.forms.getunicode("kombinacija")
    memo.ugibaj(id_igre, kombinacija)
    bottle.redirect("/igra/")

@bottle.get("/img/<picture>")
def serve_pictures(picture):
    return bottle.static_file(picture, root="img")

bottle.run(reloader=True, debug=True)