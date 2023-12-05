#!/usr/bin/python3
"""Dfns a clss MyInt tht inhrts frm int"""


class MyInt(int):
    """Invrt int oprtrs == nd !="""

    def __eq__(self, value):
        """Ovrrd == op wth != bhvr"""
        return self.real != value

    def __ne__(self, value):
        """ovrrd != oprtr with == bhvr"""
        return self.real == value
