# Network programming lab 10 - Regular expressions
# created by Osman Said 08-12-2021

import re

def extract_email():
    mtxt ="jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."
    print("\n\nThe text: ", mtxt)
    emails = re.findall(r"\s\w+(?:\.\w+)*@\w+\.\w+(?:\.\w+)?",mtxt)
    print('The correct email addresses:', emails)


def get_header():
    htmltxt = """ bla bla bla 
            <h1> My Rubric </h1> 
            bla bla bla. """
    print('\n\n',re.findall(r"<h1>\s*(.*?)\s*</h1>",htmltxt))


def get_simpsons():

    tabla = open("tabla.html",encoding="utf-8")
    txt = tabla.read()
    result = re.findall(r'<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>\s*(?:<div.*?>\s*)*<p.*?>\s*.*?(Säsong)\s(\d+).*?(\d+).*?(\d+)\.\s(.*?)\..*?\s*(Regi.*?)?\..*?\s*</p>', txt )
    print("\n\n")

    for i in result:

        print('_____________________')
        print(' Tid: {}'.format(i[0]))
        print(' Säsong: {}'.format(i[2])) 
        print(' Avsnitt: {}/{}'.format(i[3], i[4]))
        print(' Handlingar: {}'.format(i[5])) 


extract_email()
get_header()
get_simpsons()
