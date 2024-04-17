import xml.etree.ElementTree as ET
import datetime as dt
import os


def main():
    data_orders = []
    data_payment_mehods = []

    root = ET.Element('root')

    date = ET.SubElement(root, 'date')
    caissier = ET.SubElement(root, 'caissier')
    ticket = ET.SubElement(root, 'ticket')
    heure = ET.SubElement(root, 'heure')

    orders = ET.SubElement(root, 'order')
    for order in data_orders:
        code = ET.SubElement(orders, 'code')
        article = ET.SubElement(orders, 'article')
        qty = ET.SubElement(orders, 'qty')
        pu = ET.SubElement(orders, 'pu')
        pt = ET.SubElement(orders, 'pt')

    payment_mehods = ET.SubElement(root, 'payment_method')

    total = ET.SubElement(root, 'total')
    percu = ET.SubElement(root, 'percu')
    rendu = ET.SubElement(root, 'rendu')
    taxe = ET.SubElement(root, 'taxe')


if __name__ == '__main__':
    from bs4 import BeautifulSoup
    import re

    # compil = re.compile('TOTAL HT')
    #
    # with open('doc.html', 'r') as file:
    #     template = BeautifulSoup(file.read(), 'html.parser')
    #     company = "".join([p.text for p in template.find_all('div', {"class": "company_name"})]).replace('\n', '').replace(' ', '')
    #     data = "".join([p.text for p in template.find_all('table', {"class": "liste_article"})]).replace('\n\n\n', '\n').split('\n\n\n')
    #     payment = "".join([p.text for p in template.find_all('div', {"class": "company_paiement"})]).strip().split('\n\n\n\n')
    #
    #     payment_m = list()
    #     footer = list()
    #     for element in payment:
    #         data1 = element.replace('\n\n\n', ':').replace('\n\n', '')
    #         if data1 != '':
    #             payment_m.append(data1.split(':'))
    #         else:
    #             break
    #
    #     use = list()
    #     data_head, data_boby = list(), list()
    #
    #     for element in data:
    #         use.append(element.strip().split('\n'))
    #
    #     root = ET.Element('root')
    #
    #     date = ET.SubElement(root, 'date')
    #     date.text = (use[0][-2])
    #     # print(use[0])
    #
    #     caissier = ET.SubElement(root, 'caissier')
    #     caissier.text = use[0][-3]
    #
    #     ticket = ET.SubElement(root, 'ticket')
    #     ticket.text = use[0][-5]
    #
    #     heure = ET.SubElement(root, 'heure')
    #     heure.text = use[0][-1]
    #
    #     orders = ET.SubElement(root, 'order')
    #     for order in use[1:]:
    #         numero = ET.SubElement(orders, 'ligne')
    #
    #         code = ET.SubElement(numero, 'code')
    #         code.text = order[-6]
    #
    #         article = ET.SubElement(numero, 'article')
    #         article.text = order[-5]
    #
    #         qty = ET.SubElement(numero, 'qty')
    #         qty.text = order[-4]
    #         condi = ET.SubElement(numero, 'conditionnement')
    #         condi.text = order[-3]
    #
    #         pu = ET.SubElement(numero, 'pu')
    #         pu.text = order[-2]
    #
    #         pt = ET.SubElement(numero, 'pt')
    #         pt.text = order[-1].strip()
    #
    #     payment_mehods = ET.SubElement(root, 'payment_method')
    #     for method in payment_m[:-1]:
    #         name = ET.SubElement(payment_mehods, 'payment_name')
    #         name.text = method[0]
    #
    #         montant = ET.SubElement(payment_mehods, 'montant')
    #         montant.text = method[1]
    #
    #     total = ET.SubElement(root, 'total')
    #     total.text = payment[-1].strip()
    #
    #     taxe = ET.SubElement(root, 'taxe')
    #     print(payment[-3].split(':'))
    #     taxe.text = payment[-3].split(':')[1].strip()
    #
    #     # print(template.find_all('td', {"id": "caissiere"}))
    #
    #     xml_data_read = ET.parse('Catalog.xml')
    #
    #     # getting the parent tag of
    #     # the xml document
    #     root_read = xml_data_read.getroot()
    #     print('====', root_read)
    with open('Order26_09_23.html', 'r') as file:
        template = BeautifulSoup(file.read(), 'html.parser')
        root = ET.Element('root')

        root_order = template.find_all('div', {"key": "POS"})

        for record in root_order:
            date_ = "".join([p.text for p in record.find_all('td', {"key": "date"})])
            caissier_ = "".join([p.text for p in record.find_all('td', {"key": "caissier"})])
            ticket_ = "".join([p.text for p in record.find_all('td', {"key": "ticket"})])
            heure_ = "".join([p.text for p in record.find_all('td', {"key": "heure"})])
            total_paid_ = "".join([p.text for p in record.find_all('td', {"key": "total_paid"})])
            numero_ = "".join([p.text for p in record.find_all('td', {"key": "number"})])
            code_ = "$".join([p.text for p in record.find_all('td', {"key": "code"})])
            designation_ = "$".join([p.text for p in record.find_all('td', {"key": "designation"})])
            qty_ = "$".join([p.text for p in record.find_all('td', {"key": "qty"})])
            condi_ = "$".join([p.text for p in record.find_all('td', {"key": "condi"})])
            pu_ = "$".join([p.text for p in record.find_all('td', {"key": "pu"})])
            pt_ = "$".join([p.text for p in record.find_all('td', {"key": "pt"})])
            payment_method_ = " ".join([p.text for p in record.find_all('td', {"key": "payment_name"})])
            payment_price_ = " ".join([p.text for p in record.find_all('td', {"key": "payment_price"})])
            taxe_ = "".join([p.text for p in record.find_all('td', {"key": "taxe"})])

            commande = ET.SubElement(root, 'commande')

            date = ET.SubElement(commande, 'date')
            date.text = date_

            caissier = ET.SubElement(commande, 'caissier')
            caissier.text = caissier_

            ticket = ET.SubElement(commande, 'ticket')
            ticket.text = ticket_

            heure = ET.SubElement(commande, 'heure')
            heure.text = heure_

            orders = ET.SubElement(commande, 'order')
            for i in range(len(designation_.split('$'))):
                numero = ET.SubElement(orders, 'ligne')

                code = ET.SubElement(numero, 'code')
                code.text = code_.strip().split('$')[i]

                article = ET.SubElement(numero, 'article')
                article.text = designation_.strip().split('$')[i]

                qty = ET.SubElement(numero, 'qty')
                qty.text = qty_.strip().split('$')[i]

                condi = ET.SubElement(numero, 'conditionnement')
                condi.text = condi_.strip().split('$')[i]

                pu = ET.SubElement(numero, 'pu')
                pu.text = pu_.strip().split('$')[i]

                pt = ET.SubElement(numero, 'pt')
                pt.text = pt_.strip().split('$')[i]

            payment_mehods = ET.SubElement(commande, 'payment_method')
            for method in range(len(payment_price_.split(' '))):
                name = ET.SubElement(payment_mehods, 'payment_name')
                name.text = payment_method_.split(' ')[method]

                montant = ET.SubElement(payment_mehods, 'montant')
                montant.text = payment_price_.split(' ')[method]

            total = ET.SubElement(commande, 'total')
            total.text = total_paid_

            taxe = ET.SubElement(commande, 'taxe')
            taxe.text = taxe_

        tree = ET.ElementTree(root)
        print(tree)

        # os.chdir("/home/gh/Desktop/XmlFile")
        xml_file = "Order{0}.xml".format(dt.date.today().strftime('%d_%m_%y'))
        html_file = "Order{0}.html".format(dt.date.today().strftime('%d_%m_%y'))

        tree.write(xml_file, encoding="utf8", xml_declaration=True)

        # xml_data_read = ET.parse('Catalog.xml')

        # # getting the parent tag of
        # # the xml document
        # root_read = xml_data_read.getroot()
        #
        # tree = ET.ElementTree(root_read)
        # tree.write('Catalog.xml', encoding="utf8", xml_declaration=True)


