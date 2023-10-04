def cesar_shifting(letter, key):
    """
    Cette fonction effectue un décalage dans l'alphabet d'une lettre
    param letter: la lettre à décaler
    param key: la valeur de décalage
    return: la lettre décalée
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    if letter.islower() and letter.lower() in alphabet:
        return alphabet[(alphabet.index(letter.lower()) + key) % 26]
    if letter.isupper() and letter.lower() in alphabet:
        return alphabet[(alphabet.index(letter.lower()) + key) % 26].upper()
    else:
        return letter


def cesar(message, key):
    """
    Cette fonction effectue un décalage dans l'alphabet de toutes les lettres du message
    Elle utilise la fonction cesar_shifting.
    param message: message dont les lettres doivent être décalées
    param key: la valeur du décalage
    return: message (de)chiffré par le décalage
    """
    data = []

    for i in message:
        data.append(cesar_shifting(i, key))
    output = ''.join(data)
    return output


def build_cesar_key(cryptogramme):
    """
    Cette fonction calcul la valeur du décalage sur base du cryptogramme.
    Elle identifie la lettre la plus fréquente du cryptogramme et l'associe à la lettre 'e'.
    La différence entre les deux lettres permet d'obtenir la clé de chiffrement
    param cryptogramme: le cryptogramme à décrypter
    return: la valeur du décalage
    """
    frequencies = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                   'm': 0,
                   'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
                   'z': 0}
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    cryptogramme_mod = cryptogramme.lower()
    for letter in cryptogramme_mod:
        if letter in frequencies:
            frequencies[letter] = cryptogramme_mod.count(letter)
        else:
            pass
    most_frequent = max(frequencies, key=frequencies.get)

    key = alphabet.index(most_frequent) - alphabet.index('e')
    return key


def crypto_cesar(cryptogramme):
    """
    Cette fonction réalise une cryptanalyse d'un message chiffré par la méthode de César.
    Elle utilise la fonction build_cesar_key pour déterminer la clé de chiffrement.
    Le décryptage est effectué à l'aide de la méthode cesar
    param cryptogramme: cryptogramme à cryptanalyser
    return: message en clair
    """
    key = -(build_cesar_key(cryptogramme))
    message = cesar(cryptogramme, key)
    return message