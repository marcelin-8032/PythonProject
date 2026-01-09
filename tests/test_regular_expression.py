import random
from regular_expression import (
    add_bla_in_html,
    extract_email_address,
    find_phrase_in_list,
    verify_password,
)

import string

html = """
<!DOCTYPE html>
<html>
<head>
<title>Titre affiché dans la barre de titre du navigateur</title>
</head>
<body>
<p></p>
<p></p>
</body>
</html>
"""

texte = """Veuillez adresser toutes vos questions
Python à formation@numgrade.com. Pour les spams, envoyez-les directement à
spam.va_a-la-poubelle@numgrade.com 
qui ne manquera pas de les traiter rapidement !"""

# password = "Abc!&2345"


def generate_password():
    chars = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + '!@#$%^&*(),.?":{}|<>'
    )
    return "".join(random.choice(chars) for _ in range(10))


def test_regular_expression_ex1():
    find_phrase_in_list("Blabla! Blablabla... Bla?")


def test_regular_expression_ex2():
    add_bla_in_html(html)


def test_regular_expression_ex3():
    extract_email_address(texte)


def test_regular_expression_ex4():

    password = generate_password()
    print("generated_password: " + password)

    if verify_password(password):
        print("password is valid", password)
    else:
        print("password is Invalid", password)
