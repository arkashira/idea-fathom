import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Idea:
    id: int
    title: str
    description: str
    anonymous: bool
    comments: list
    upvotes: int
    suggestions: list

@dataclass
class Comment:
    id: int
    idea_id: int
    text: str

@dataclass
class Suggestion:
    id: int
    idea_id: int
    text: str

class IdeaFathom:
    def __init__(self):
        self.ideas = []
        self.comments = []
        self.suggestions = []
        self.next_id = 1

    def publish_idea(self, title, description, anonymous=False):
        idea = Idea(
            id=self.next_id,
            title=title,
            description=description,
            anonymous=anonymous,
            comments=[],
            upvotes=0,
            suggestions=[],
        )
        self.ideas.append(idea)
        self.next_id += 1
        return idea

    def comment_on_idea(self, idea_id, text):
        comment = Comment(
            id=self.next_id,
            idea_id=idea_id,
            text=text,
        )
        self.comments.append(comment)
        for idea in self.ideas:
            if idea.id == idea_id:
                idea.comments.append(comment)
                break
        self.next_id += 1
        return comment

    def suggest_improvement(self, idea_id, text):
        suggestion = Suggestion(
            id=self.next_id,
            idea_id=idea_id,
            text=text,
        )
        self.suggestions.append(suggestion)
        for idea in self.ideas:
            if idea.id == idea_id:
                idea.suggestions.append(suggestion)
                break
        self.next_id += 1
        return suggestion

    def upvote_idea(self, idea_id):
        for idea in self.ideas:
            if idea.id == idea_id:
                idea.upvotes += 1
                break

    def get_idea(self, idea_id):
        for idea in self.ideas:
            if idea.id == idea_id:
                return idea
        return None

    def get_comments(self, idea_id):
        comments = []
        for comment in self.comments:
            if comment.idea_id == idea_id:
                comments.append(comment)
        return comments

    def get_suggestions(self, idea_id):
        suggestions = []
        for suggestion in self.suggestions:
            if suggestion.idea_id == idea_id:
                suggestions.append(suggestion)
        return suggestions
