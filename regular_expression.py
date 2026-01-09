import re


def find_phrase_in_list(texte: str):
    phrases = re.split(r"[!?...]+", texte)

    phrases = [p.strip() for p in phrases if p.strip()]

    print(phrases)


def add_bla_in_html(html):
    modified_html = re.sub(r"<p>\s*</p>", "<p>bla</p>", html)
    print(modified_html)


def extract_email_address(texte):
    emails = re.findall(r"\b[\w.-]+@[\w.-]+\.[A-Za-z]{2,}\b", texte)

    print(emails)


def verify_password(password):
    return (
        len(password) >= 8
        and re.search(r"[A-Z]", password)
        and re.search(r"[a-z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    )
