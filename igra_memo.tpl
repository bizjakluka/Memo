% import model
% rebase('base.tpl', title='Memo')

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
     <small>Študentje</small>
    </blockquote>

    <table>
     <tr>
        <td>

         <h2>{{igra.primerjava()}}</h2>

         Nepravilne kombinacije: <b>{{igra.nepravilne_kombinacije()}}</b>
        </td>

        <td>
         <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje" />

        </td>
     </tr>
    </table>

    % if poskus == model.ZMAGA:

    <h1> ZMAGA! </h1>

    <form action="/nova_igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>

    % elif poskus == model.PORAZ:

    <h1> IZGUBILI STE! </h1>

    Pravilna kombinacija: <h4> {{igra.nakljucna_izbira}} </h4>

    <form action="/nova_igra/" method="post">
        
        <button type="sumbit">Nova igra</button>
    </form>

    % else:

    <form action="/igra/" method="POST">
        Črka: <input type="text" name="crka">
        <button type="submit">Pošlji ugib</button>
    </form>

    % end