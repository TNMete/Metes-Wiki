dictionary = {
    "Pull": "Holt Änderungen aus einem Remote-Repository (z. B. GitHub) und integriert sie in dein lokales Repository.",
    "Merge": "Kombiniert Änderungen aus verschiedenen Branches. Wird oft verwendet, um Änderungen von einem Feature-Branch in den Haupt-Branch (z. B. main) zu integrieren.",
    "Repository": "Ein Projektordner auf GitHub, der den gesamten Code und die Versionsgeschichte eines Projekts enthält.",
    "Clone": "Erstellt eine Kopie eines Repositories auf deinem lokalen Computer, um daran zu arbeiten.",
    "Pull Request": "Eine Anfrage, um Änderungen, die in einem Branch vorgenommen wurden, in einen anderen Branch zu integrieren (oft in den Haupt-Branch eines Repositories).",
    "Push": "Überträgt Änderungen von deinem lokalen Repository zu einem Remote-Repository, z. B. auf GitHub.",
    "GitHub": "Eine Plattform für die Versionskontrolle und Zusammenarbeit an Codeprojekten, die Git verwendet.",
    "Branch": "Ein paralleler Arbeitsbereich innerhalb eines Repositories, in dem du Änderungen vornehmen kannst, ohne den Haupt-Branch zu beeinflussen.",
    "Commit": "Eine Momentaufnahme von Änderungen in deinem Code, die zu einem Repository hinzugefügt werden. Jeder Commit enthält eine Nachricht, die beschreibt, was geändert wurde.",
}


def extend_dictionary():
    print(
        "Erweiterung des Wörterbuchs. Geben Sie 'exit' ein, um die Erweiterung zu beenden."
    )

    git_command = input("Gib ein Git-Wort ein: ").strip().capitalize()
    if git_command.lower() == "exit":
        return
    command_description = input(
        f"Geben Sie die Beschreibung für '{git_command}' ein: "
    ).strip()
    dictionary[git_command] = command_description
    print(
        f"'{git_command}' wurde mit der Beschreibung '{command_description}' hinzugefügt."
    )


while True:
    user_input = input("Welche Beschreibung soll ausgegeben werden? ").strip()
    if user_input.lower() == "exit":
        break
    if user_input.capitalize() in dictionary:
        print(
            f"Der Begriff '{user_input}' hat folgende Funktion: '{dictionary[user_input.capitalize()]}'."
        )
    else:
        print(f"Das Wort '{user_input}' ist nicht im Wörterbuch enthalten.")
        extend = (
            input("Möchten Sie das Wörterbuch erweitern? (ja/nein): ").strip().lower()
        )
        if extend == "ja":
            extend_dictionary()
