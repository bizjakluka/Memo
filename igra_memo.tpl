% import model_memo
% rebase('base.tpl', title='Memo')

    <h1>Memo</h1>

    <blockquote>
     Vnešena kombinacija naj bo oblike štirih črk izmed YORGBV, npr. GYOR, pri čemer velikost črk (male, velike) ni pomembna.
     Po oddanem poskusu ti vrača na istoležečem mestu:
     črno ('B') – če si uganil barvo in lego, 
     belo ('W') – če si uganil le barvo, 
     nič (' ') – če nista pravi niti barva niti lega.
     Na voljo imaš zgolj 6 poskusov.
    </blockquote>

    <table>
     <tr>
        <td>

         <h2>{{igra.primerjava(None)}}</h2>

         Poskušane kombinacije: <b>{{igra.napacni_ugibi(None)}}</b>

        </td>

        <td>
         

        </td>
     </tr>
    </table>

    % if poskus == model_memo.ZMAGA:

    <h1> ZMAGA! <img src="/img/zmaga.gif" alt="slika manjka zaenkrat" /> </h1>

    <form action="/nova_igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>

    % elif poskus == model_memo.PORAZ:

    <h1> IZGUBILI STE! <img src="/img/poraz.gif" alt="slika manjka zaenkrat" /></h1>

    Pravilna kombinacija: <h4> {{igra.nakljucna_izbira}} </h4>

    <form action="/nova_igra/" method="post">
        
        <button type="sumbit">Nova igra</button>
    </form>

    % else:

    <form action="/igra/" method="POST">
        Kombinacija: <input type="text" name="kombinacija">
        <button type="submit">Pošlji ugib</button>
    </form>

    % end