# Todo-App

## Aufgabe
Erstelle mit uv ein neues Projekt (uv init, siehe uv.pdf)
in dem projekt gibt es zwei dateien, main.py und todos.py

Erstelle ein Modul "todos". Lege dort eine Klasse Todo an.

## todos.py (Todo Klasse)
- Todos in einer Liste speichern
- 
class Todo:
- Attribute:
- name

zwei Methoden
- add_todo
- list_todos

## Aufruf
- todo_liste = Todo(name="Meine haushaltsliste")
- todo_liste.add_todo("Einkaufen")
- todo_liste.add_todo("Abspülen")
- todo_liste.list_todos()

## main.py
- importiere Todo-klasse
- und lege Todos an