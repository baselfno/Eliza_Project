from condition_map import is_it_about_other_teams
from escaper import *
from synonym import search

def get_escape_answers(question):
    question = [search(q) for q in question]
    if 'nassr' in question:
        return update_counter("nassr_escape")
    if 'itihad' in question:
        return update_counter("itihad_escape")
    if 'ahli' in question:
        return update_counter("ahli_escape")
    if 'khaleej' in question:
        return update_counter("khaleej_escape")
    if 'nishimura' in question:
        return update_counter("nishimura_escape")
    if 'injury' in question or 'injuries' in question:
        return update_counter("injuries_escape")
    if is_it_about_other_teams(question):
        return update_counter("other_teams_escape")
    return "I dont want to talk about this, leave if you don't have other questions"

def get_yesno_answers(question):
    if question[0] in ['can', 'could', 'may', 'would']:
        return f'yes I {question[0]}'
    return " I am not sure"

def get_other_matches_answers(question):
    return update_counter('matches_escape')