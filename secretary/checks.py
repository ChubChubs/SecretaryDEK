__author__ = 'masterbob'
"""
This module is for checking the DB for conflicting data.
Generally, it's meant to provide messages with all tricky things that can occur
in one of the DB tables.
But in further intellectualizing all this stuff, a can't say what will be at the end)
"""
from .models import *
from docgen.models import *


def check_model(for_what):
    """

    :param for_what:
     A string that specifies a target for checking.
    :return:
    A list of messages with all found collisions.
    """
    if for_what == 'reviewers':
        # TODO: Make reviewers examination
        return ["MSG: Nothing to alert. All seems to be fine"]

    elif for_what == 'restrictions':
        # TODO: Check for restrictions
        return ["MSG: Nothing to alert. All seems to be fine"]

    elif for_what == 'diplomas':
        # TODO: Check diplomas
        return ["MSG: Nothing to alert. All seems to be fine"]

    elif for_what == 'overflows':
        # TODO: Check for overflows. Exceeding restrictions or etc.
        return ["MSG: Nothing to alert. All seems to be fine"]

    elif for_what == 'time_paradoxes':
        # TODO: Check that time milestones are properly set.
        return ["MSG: Nothing to alert. All seems to be fine"]

    elif for_what == 'user_profiles':
        # TODO: Check that all users have their profiles.
        return ["MSG: Nothing to alert. All seems to be fine"]

    elif for_what == 'users':
        # TODO: Cheock users for convenient data.
        return ["MSG: Nothing to alert. All seems to be fine"]

def check_reviewers(who=None):
    """
    This function does a lookup for Reviewers model
    Firstly - get the true reviewers.
    Second - look for all fields. If someone is null, or improperly initialized.
    :return:
    """
    Reviewer.objects.get(redundant_dude=False)


