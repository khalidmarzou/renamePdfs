import re
text = """
            Reçu d’opération de virement
            Imprimé le 28/04/2024 16:28:48
            EMETTEUR A DEBITER
            Compte 4585909211032000
            Nom d'émetteur ZAKARIA SIDQUI
            BENEFICIAIRE A CREDITER
            Compte 230791490798721103120014
            Nom du bénéficiaire mohssin
            Banque du bénéficiaire CIH Bank
            DETAIL DU VIREMENT
            Montant 20.00
            Type Virement CIH
            Date 28/04/2024 16:28:48
            Motif de l'opération UABAH
            ETAT Executé
            
            
            
            
            
            
            *Ce virement est exécuté selon les conditions tarifaires habituelles  
            
            C.I.H siège social: Casablanca-187 Avenue Hassan Il -www.cih.co.ma- Tél: 05 22 47 90 00 - 05 22 47 91 11 Fax : 05 22 47 
            91 63 S.A au Capital de 3.051.978.400Dh RC: 203 Casa CNSS: 1027805 IF: 01084033, Patente: 34200588, ICE 
            001542240000068

        """

pattern = r"Motif de l'opération (\w+)"

matches = re.search(pattern, text)
if matches:
    invoice_number = matches.group(1)
    print("Invoice Number:", invoice_number)
else:
    print("Invoice number not found.")