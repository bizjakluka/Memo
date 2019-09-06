% import model_memo
% rebase('base.tpl', title='Vislice')





  <h1>Memo</h1>

  <blockquote>
    Memo je super igra.
    Računalnik izbere poljubno kombinacijo štirih barv od šestih.
    Barve so Y – rumena, O – oranžna, R – rdeča, B – modra, G – zelena, V - vijolična, pri čemer se barve ne ponavljajo, npr. YRGB.
    Tvoja naloga je, da poskušaš ugotoviti soigralčevo kombinacijo. 
    Po oddanem poskusu ti bo računalnik vrnil na istoležečem mestu:
    črno (B) – če si uganil barvo in lego, 
    belo (W) – če si uganil le barvo, 
    nič ( ) – če nista pravi niti barva niti lega.
    Na voljo imaš 6 poskusov.
    Vso srečo!
    
  </blockquote>

  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
