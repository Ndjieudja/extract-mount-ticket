# --*-- coding: utf8 --*--

def head(company, niu, rc, tck, client, caissier, date, heure):
    return '''
    <table style="width: 100%; font-family: Franklin Gothic;">
        <tr>
            <td style="width: 25%;"></td>
            <td style="width: 25%;">
                <div>
                    <div class="company_name" style="font-size: 1.2em!important; font-weight: bold;">{0}
                    </div>
                </div>
            </td>
            <td style="width: 25%;">
                <div style="font-size: 0.7em !important;font-weight: bold;"> NIU : {1}, RC :{2}</div>
            </td>
            <td style="width: 25%;"></td>
        </tr>
    </table>
    <br><br>
    <table class="liste_article" width="100%" align="center" style="font-family: Franklin Gothic;">
        <tr>
            <td width="20%"> Ticket N°</td>
            <td width="20%"> Client</td>
            <td width="20%"> Caissier(e)</td>
            <td width="20%"> Date</td>
            <td width="20%"> Heure</td>
        </tr>
        <tr>
            <td key="ticket" width="20%"><span style="padding-right:3px">{3}</span></td>
            <td key="client" width="20%"><span>{4}</span></td>
            <td key="caissier" width="20%"><span>{5}</span></td>
            <td key="date" width="20%"><span>{6}</span></td>
            <td key="heure" width="20%"><span>{7}</span></td>
        </tr>
    </table>
    <br/>

'''.format(company, niu, rc, tck, client, caissier, date, heure)


def body(data_line):
    complete = ''
    for line in data_line:
        complete += order_line(line.n, line.code, line.desi, line.qty, line.condi, line.pu, line.pt)

    return '''
    <table class="liste_article" align="center" width="95%" style="font-family: Franklin Gothic;">
        <tr>
            <th width="2%" style="border: 1px solid gray;padding:8px">N°</th>
            <th width="8%" style="border: 1px solid gray;padding:8px">Code</th>
            <th width="57%" style="border: 1px solid gray;padding:8px;text-align:center"> Designation</th>
            <th width="5%" style="border: 1px solid gray;padding:8px;text-align:center"> Qte</th>
            <th width="16%" style="border: 1px solid gray;padding:8px;text-align:center"> Cond</th>
            <th width="6%" style="border: 1px solid gray;padding:8px;text-align:center"> PU</th>
            <th width="8%" style="border: 1px solid gray;padding:8px;text-align:center">P TTC</th>
        </tr>
        {0}
    </table>
    <br/>
    
'''.format(complete)


def footer(ht, tax, ttc, payment_data, rendu):

    data = ''
    for payment in payment_data:
        data += order_payment(payment.p_name, payment.ref, payment.amount)

    return '''
    <div class="company_paiement">
        <div class="reglement" style="font-size:0.8em; font-family: Franklin Gothic;">
            <table class="orderReceipt_table" style="font-family: Franklin Gothic;">
                <tbody>
                    {0}
                    <tr>
                        <td style="padding-left: 0px;"> Rendu Espèce</td>
                        <td align="center"></td>
                        <td align="right"><span align="right">{1}</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="mode_paiement" style="font-size:0.8em; font-family: Franklin Gothic;">
            <table class="orderReceipt_table" style="font-family: Franklin Gothic;">
                <tbody>
                <tr>
                    <td class="pos-receipt-right-align" style="padding-bottom:4px"> TOTAL HT :</td>
                    <td align="right"><span class="pos-receipt-right-align" style="padding-left:4px">{2}</span></td>
                </tr>
                <tr>
                    <td class="pos-receipt-right-align" style="padding-bottom:4px"> TAXES :</td>
                    <td key="taxe" align="right"><span class="pos-receipt-right-align" style="padding-left:4px">{3}</span>
                    </td>
                </tr>
                <tr>
                    <td class="pos-receipt-right-align" style="padding-bottom:4px"> NET A PAYER :</td>
                    <td key="total_paid" align="right"><strong><span class="pos-receipt-right-align"
                                    tyle="font-size:1.4em;padding-left:4px;font-weight: bold;">{4}</span></strong>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
    <br>

'''.format(data, ht, tax, ttc, rendu)


def note(obs):
    footer_note = '''
    <div style="font-family: Franklin Gothic;">
        <div style="text-align: center; font-size: 12px;">{0}</div>
    </div>
'''.format(obs)


def order_payment(p_name,  ref, amount):
    text = '''
        <tr>
            <td key="payment_name" style="padding-left: 0px;">{0}</td>
            <td align="center"><span>{1}</span></td>
            <td key="payment_price" align="right"><span align="right">{2}</span></td>
        </tr>
    '''.format(p_name, ref, amount)


def order_line(n, code, desi, qty, condi, pu, pt):
    return '''
        <tr style="border-bottom: 1px solid gray;padding:3px;text-align:center">
            <td key="number" style="border: 1px solid gray;text-align:left;padding:3px;"><span>{0}</span></td>
            <td key="code" style="border: 1px solid gray;text-align:left;padding:3px;">
                <div>{1}</div>
            </td>
            <td key="designation" style="border: 1px solid gray;text-align:left;padding:3px;">
                <div>{2}</div>
            </td>
            <td key="qty" style="border: 1px solid gray;text-align:right;padding:3px;">
                <div>{3}</div>
            </td>
            <td key="condi" style="border: 1px solid gray;text-align:left;padding:3px;">
                <div>{4}</div>
            </td>
            <td key="pu" style="border: 1px solid gray;text-align:right;padding:3px;">
                <div>{5}</div>
            </td>
            <td key="pt" style="border: 1px solid gray;text-align:right;padding:3px;">
                <div>{6}</div>
            </td>
        </tr>
    
    '''.format(n, code, desi, qty, condi, pu, pt)


if __name__ == '__main__':
    bill = '''
        <!DOCTYPE>
        <html>
            {0}
            {1}
            {2}
            {3}
        </html>
        
    '''.format(
        head('company', 'niu', 'rc', 'tck', 'client', 'caissier', 'date', 'heure'),
        body('data_line'),
        footer('ht', 'tax', 'ttc'),
        note('obs')
    )